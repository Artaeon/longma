"""
Learning modes: Learn, Flashcards, Quiz, Review.
"""

from __future__ import annotations

import random
import time
from typing import TYPE_CHECKING

import questionary
from rich.columns import Columns
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from chinese_cli.pronunciation import get_pronunciation_guide
from chinese_cli.srs import ProgressTracker
from chinese_cli.vocab_data import (
    ALL_VOCAB,
    CATEGORIES,
    CATEGORY_KEYS,
    VocabEntry,
    get_vocab_by_category,
)

if TYPE_CHECKING:
    pass

console = Console()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

LANG_MODE = "both"  # global, set by CLI


def _display_name(lang: str) -> str:
    return {"de": "Deutsch", "en": "English", "both": "Deutsch + English"}[lang]


def _translation(entry: VocabEntry, lang: str) -> str:
    """Get translation string based on language mode."""
    if lang == "de":
        return entry.german
    elif lang == "en":
        return entry.english
    else:
        return f"{entry.german}  •  {entry.english}"


def _example_translation(entry: VocabEntry, lang: str) -> str:
    if lang == "de":
        return entry.example_de
    elif lang == "en":
        return entry.example_en
    else:
        return f"{entry.example_de}  •  {entry.example_en}"


def _quality_prompt() -> int:
    """Ask user to rate their recall quality (0–5)."""
    choices = [
        questionary.Choice("0 — Complete blackout 🔴", value=0),
        questionary.Choice("1 — Wrong, but recognized after 🟠", value=1),
        questionary.Choice("2 — Wrong, felt familiar 🟡", value=2),
        questionary.Choice("3 — Correct, difficult 🟢", value=3),
        questionary.Choice("4 — Correct, some hesitation 🔵", value=4),
        questionary.Choice("5 — Perfect recall ⭐", value=5),
    ]
    result = questionary.select(
        "How well did you recall?",
        choices=choices,
        style=questionary.Style([
            ("highlighted", "fg:cyan bold"),
            ("pointer", "fg:cyan bold"),
            ("answer", "fg:green bold"),
        ]),
    ).ask()
    return result if result is not None else 3


def _category_select() -> str | None:
    """Ask user which category to study."""
    choices = [
        questionary.Choice(f"  {desc}", value=key)
        for key, desc in CATEGORIES.items()
    ] + [questionary.Choice("  🔀 All categories", value="all")]

    result = questionary.select(
        "Choose a category:",
        choices=choices,
        style=questionary.Style([
            ("highlighted", "fg:cyan bold"),
            ("pointer", "fg:cyan bold"),
        ]),
    ).ask()
    return result


# ---------------------------------------------------------------------------
# MODE 1: Learn — Browse vocabulary
# ---------------------------------------------------------------------------

def mode_learn(lang: str) -> None:
    """Browse vocabulary by category in a pretty table."""
    console.print()
    cat = _category_select()
    if cat is None:
        return

    if cat == "all":
        vocab = list(ALL_VOCAB)
    else:
        vocab = get_vocab_by_category(cat)

    if not vocab:
        console.print("[yellow]No vocabulary found.[/yellow]")
        return

    # Paginate — show 10 at a time
    page_size = 10
    total_pages = (len(vocab) + page_size - 1) // page_size

    for page in range(total_pages):
        start = page * page_size
        end = min(start + page_size, len(vocab))
        page_vocab = vocab[start:end]

        table = Table(
            title=f"📖  Vocabulary  ({start + 1}–{end} of {len(vocab)})",
            show_header=True,
            header_style="bold cyan",
            border_style="dim",
            title_style="bold white",
            expand=True,
        )
        table.add_column("汉字", style="bold yellow", justify="center", width=12)
        table.add_column("Pinyin", style="green", width=16)
        if lang in ("de", "both"):
            table.add_column("Deutsch", style="white", width=22)
        if lang in ("en", "both"):
            table.add_column("English", style="white", width=22)
        table.add_column("HSK", style="dim cyan", justify="center", width=5)

        for v in page_vocab:
            row = [v.hanzi, v.pinyin]
            if lang in ("de", "both"):
                row.append(v.german)
            if lang in ("en", "both"):
                row.append(v.english)
            row.append(str(v.hsk_level))
            table.add_row(*row)

        console.print()
        console.print(table)

        # Show example + pronunciation for the first word on the page
        sample = page_vocab[0]
        if sample.example_hanzi:
            pron_hint = get_pronunciation_guide(sample.pinyin)
            pron_line = f"\n[magenta]🔊 {pron_hint}[/magenta]" if pron_hint else ""
            console.print()
            console.print(
                Panel(
                    f"[bold yellow]{sample.example_hanzi}[/bold yellow]\n"
                    f"[green]{sample.example_pinyin}[/green]\n"
                    f"[dim]{_example_translation(sample, lang)}[/dim]"
                    f"{pron_line}",
                    title=f"💡 Example: {sample.hanzi}",
                    border_style="cyan",
                    width=60,
                )
            )

        if page < total_pages - 1:
            result = questionary.confirm(
                "Next page?",
                default=True,
                style=questionary.Style([("answer", "fg:cyan")]),
            ).ask()
            if not result:
                break

    console.print("\n[dim cyan]End of vocabulary list.[/dim cyan]\n")


# ---------------------------------------------------------------------------
# MODE 2: Flashcards
# ---------------------------------------------------------------------------

def mode_flashcards(lang: str, tracker: ProgressTracker) -> None:
    """Interactive flashcard mode with SRS rating."""
    console.print()
    cat = _category_select()
    if cat is None:
        return

    if cat == "all":
        vocab = list(ALL_VOCAB)
    else:
        vocab = get_vocab_by_category(cat)

    if not vocab:
        console.print("[yellow]No vocabulary found.[/yellow]")
        return

    random.shuffle(vocab)

    # Limit session to 15 cards
    session_size = min(15, len(vocab))
    vocab = vocab[:session_size]
    correct = 0
    total = 0

    console.print(
        Panel(
            f"[bold]🃏 Flashcard Session[/bold]\n"
            f"[dim]{session_size} cards • Press Ctrl+C to quit early[/dim]",
            border_style="magenta",
            width=50,
        )
    )

    try:
        for i, v in enumerate(vocab, 1):
            console.print(f"\n[dim]Card {i}/{session_size}[/dim]")

            # Show the hanzi
            console.print(
                Panel(
                    f"[bold yellow on default] {v.hanzi} [/bold yellow on default]",
                    title="❓ What does this mean?",
                    border_style="yellow",
                    width=40,
                    padding=(1, 4),
                )
            )

            questionary.press_any_key_to_continue(
                "Press any key to reveal...",
            ).ask()

            # Reveal
            pron_hint = get_pronunciation_guide(v.pinyin)
            pron_line = f"\n[magenta]🔊 {pron_hint}[/magenta]" if pron_hint else ""
            console.print(
                Panel(
                    f"[bold yellow]{v.hanzi}[/bold yellow]\n"
                    f"[green]{v.pinyin}[/green]\n"
                    f"{pron_line}\n"
                    f"[bold white]{_translation(v, lang)}[/bold white]\n\n"
                    f"[dim]{v.example_hanzi}[/dim]\n"
                    f"[dim green]{v.example_pinyin}[/dim green]\n"
                    f"[dim]{_example_translation(v, lang)}[/dim]",
                    title="✅ Answer",
                    border_style="green",
                    width=55,
                    padding=(1, 2),
                )
            )

            quality = _quality_prompt()
            card = tracker.review(v.hanzi, quality)
            total += 1
            if quality >= 3:
                correct += 1

            # Brief feedback
            level_colors = {
                "new": "dim", "learning": "yellow",
                "reviewing": "cyan", "mastered": "green",
            }
            color = level_colors.get(card.mastery_level, "white")
            console.print(
                f"  [{color}]Level: {card.mastery_level.upper()}[/{color}] · "
                f"Next review in {card.interval} day(s)"
            )

    except KeyboardInterrupt:
        console.print("\n[dim]Session interrupted.[/dim]")

    # Session summary
    acc = (correct / total * 100) if total > 0 else 0
    console.print(
        Panel(
            f"[bold]Session Complete![/bold]\n\n"
            f"Cards reviewed: [cyan]{total}[/cyan]\n"
            f"Correct: [green]{correct}[/green] / {total}\n"
            f"Accuracy: [{'green' if acc >= 70 else 'yellow' if acc >= 50 else 'red'}]{acc:.0f}%[/{'green' if acc >= 70 else 'yellow' if acc >= 50 else 'red'}]",
            title="📊 Summary",
            border_style="cyan",
            width=40,
        )
    )


# ---------------------------------------------------------------------------
# MODE 3: Quiz (Multiple Choice)
# ---------------------------------------------------------------------------

def mode_quiz(lang: str, tracker: ProgressTracker) -> None:
    """Multiple choice quiz: given hanzi, pick translation."""
    console.print()
    cat = _category_select()
    if cat is None:
        return

    if cat == "all":
        vocab = list(ALL_VOCAB)
    else:
        vocab = get_vocab_by_category(cat)

    if len(vocab) < 4:
        console.print("[yellow]Need at least 4 words for a quiz.[/yellow]")
        return

    random.shuffle(vocab)
    session_size = min(10, len(vocab))
    quiz_words = vocab[:session_size]
    correct = 0

    console.print(
        Panel(
            f"[bold]📝 Quiz Mode[/bold]\n"
            f"[dim]{session_size} questions • Choose the correct translation[/dim]",
            border_style="blue",
            width=50,
        )
    )

    for i, word in enumerate(quiz_words, 1):
        console.print(f"\n[dim]Question {i}/{session_size}[/dim]")
        console.print(f"  [bold yellow]{word.hanzi}[/bold yellow]  [green]({word.pinyin})[/green]\n")

        # Build choices: 1 correct + 3 distractors
        distractors = [v for v in ALL_VOCAB if v.hanzi != word.hanzi]
        random.shuffle(distractors)
        options = [word] + distractors[:3]
        random.shuffle(options)

        choices = [
            questionary.Choice(
                f"  {_translation(opt, lang)}",
                value=opt.hanzi,
            )
            for opt in options
        ]

        answer = questionary.select(
            "Which translation is correct?",
            choices=choices,
            style=questionary.Style([
                ("highlighted", "fg:cyan bold"),
                ("pointer", "fg:cyan bold"),
                ("answer", "fg:green bold"),
            ]),
        ).ask()

        if answer == word.hanzi:
            console.print("  [bold green]✓ Correct![/bold green]")
            correct += 1
            tracker.review(word.hanzi, 4)
        else:
            pron_hint = get_pronunciation_guide(word.pinyin)
            console.print(f"  [bold red]✗ Wrong![/bold red]  Correct: [yellow]{_translation(word, lang)}[/yellow]")
            if pron_hint:
                console.print(f"  [magenta]🔊 {pron_hint}[/magenta]")
            tracker.review(word.hanzi, 1)

    # Summary
    acc = (correct / session_size * 100)
    console.print(
        Panel(
            f"[bold]Quiz Complete![/bold]\n\n"
            f"Score: [cyan]{correct}[/cyan] / {session_size}\n"
            f"Accuracy: [{'green' if acc >= 70 else 'yellow' if acc >= 50 else 'red'}]{acc:.0f}%[/{'green' if acc >= 70 else 'yellow' if acc >= 50 else 'red'}]",
            title="📊 Results",
            border_style="blue",
            width=40,
        )
    )


# ---------------------------------------------------------------------------
# MODE 4: Review (Spaced Repetition)
# ---------------------------------------------------------------------------

def mode_review(lang: str, tracker: ProgressTracker) -> None:
    """Review cards that are due based on spaced repetition schedule."""
    due_hanzi = tracker.get_due_cards()

    if not due_hanzi:
        console.print(
            Panel(
                "[bold green]🎉 All caught up![/bold green]\n\n"
                "[dim]No cards are due for review right now.\n"
                "Try learning new words or come back later![/dim]",
                border_style="green",
                width=50,
            )
        )
        return

    # Map hanzi to vocab entries
    hanzi_map = {v.hanzi: v for v in ALL_VOCAB}
    due_vocab = [hanzi_map[h] for h in due_hanzi if h in hanzi_map]

    if not due_vocab:
        console.print("[yellow]No matching vocabulary found for due cards.[/yellow]")
        return

    # Sort by urgency (most overdue first)
    due_vocab.sort(key=lambda v: tracker.get_card(v.hanzi).next_review)

    session_size = min(20, len(due_vocab))
    review_words = due_vocab[:session_size]
    correct = 0
    total = 0

    console.print(
        Panel(
            f"[bold]🔄 Review Session[/bold]\n\n"
            f"[dim]{session_size} cards due for review[/dim]",
            border_style="magenta",
            width=50,
        )
    )

    try:
        for i, v in enumerate(review_words, 1):
            card = tracker.get_card(v.hanzi)
            console.print(f"\n[dim]Review {i}/{session_size} · Level: {card.mastery_level}[/dim]")

            console.print(
                Panel(
                    f"[bold yellow] {v.hanzi} [/bold yellow]",
                    title="❓ Recall this word",
                    border_style="yellow",
                    width=40,
                    padding=(1, 4),
                )
            )

            questionary.press_any_key_to_continue("Press any key to reveal...").ask()

            pron_hint = get_pronunciation_guide(v.pinyin)
            pron_line = f"\n[magenta]🔊 {pron_hint}[/magenta]" if pron_hint else ""
            console.print(
                Panel(
                    f"[bold yellow]{v.hanzi}[/bold yellow]\n"
                    f"[green]{v.pinyin}[/green]\n"
                    f"{pron_line}\n"
                    f"[bold white]{_translation(v, lang)}[/bold white]",
                    title="✅ Answer",
                    border_style="green",
                    width=55,
                    padding=(1, 2),
                )
            )

            quality = _quality_prompt()
            updated = tracker.review(v.hanzi, quality)
            total += 1
            if quality >= 3:
                correct += 1

            console.print(
                f"  [cyan]→ {updated.mastery_level.upper()}[/cyan] · "
                f"Next in {updated.interval} day(s) · "
                f"Accuracy: {updated.accuracy:.0f}%"
            )

    except KeyboardInterrupt:
        console.print("\n[dim]Review interrupted. Progress saved.[/dim]")

    acc = (correct / total * 100) if total > 0 else 0
    console.print(
        Panel(
            f"[bold]Review Complete![/bold]\n\n"
            f"Reviewed: [cyan]{total}[/cyan]\n"
            f"Correct: [green]{correct}[/green] / {total}\n"
            f"Accuracy: [{'green' if acc >= 70 else 'yellow' if acc >= 50 else 'red'}]{acc:.0f}%[/{'green' if acc >= 70 else 'yellow' if acc >= 50 else 'red'}]",
            title="📊 Review Summary",
            border_style="magenta",
            width=40,
        )
    )
