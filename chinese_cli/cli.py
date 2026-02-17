"""
汉语学习工具 — Chinese Learning CLI

A beautiful terminal-based tool for learning Mandarin Chinese,
designed for German / Austrian native speakers in tech.
"""

from __future__ import annotations

import sys
import time

import questionary
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

from chinese_cli import __version__
from chinese_cli.modes import mode_learn, mode_flashcards, mode_quiz, mode_review
from chinese_cli.pronunciation import (
    show_tone_guide,
    show_initials_guide,
    show_finals_guide,
    show_advantages,
    render_word_pronunciation,
)
from chinese_cli.srs import ProgressTracker
from chinese_cli.stats import show_stats
from chinese_cli.vocab_data import ALL_VOCAB

console = Console()


# ---------------------------------------------------------------------------
# Welcome banner
# ---------------------------------------------------------------------------

BANNER = r"""
[bold cyan]
  ╔══════════════════════════════════════════════════╗
  ║                                                  ║
  ║     汉 语 学 习 工 具                              ║
  ║     ─────────────────                             ║
  ║     Chinese Learning CLI                         ║
  ║                                                  ║
  ║     [yellow]学中文，走向世界[/yellow]                           ║
  ║     [dim]Learn Chinese, reach the world[/dim]               ║
  ║                                                  ║
  ╚══════════════════════════════════════════════════╝
[/bold cyan]"""

TAGLINE = (
    "[dim]Designed for [bold]German/Austrian[/bold] tech professionals "
    f"· {len(ALL_VOCAB)} words · v{__version__}[/dim]"
)


def _show_banner() -> None:
    """Display the animated welcome banner."""
    console.print(BANNER)
    console.print(f"  {TAGLINE}\n")


# ---------------------------------------------------------------------------
# Language selection
# ---------------------------------------------------------------------------

def _select_language() -> str:
    """Let user choose their base language for translations."""
    result = questionary.select(
        "Translation language:",
        choices=[
            questionary.Choice("🇩🇪  Deutsch", value="de"),
            questionary.Choice("🇬🇧  English", value="en"),
            questionary.Choice("🇩🇪🇬🇧  Both (Deutsch + English)", value="both"),
        ],
        default="both",
        style=questionary.Style([
            ("highlighted", "fg:cyan bold"),
            ("pointer", "fg:cyan bold"),
            ("answer", "fg:green bold"),
        ]),
    ).ask()
    return result or "both"


# ---------------------------------------------------------------------------
# Main menu
# ---------------------------------------------------------------------------

MENU_CHOICES = [
    questionary.Choice("📖  Learn — Browse vocabulary", value="learn"),
    questionary.Choice("🃏  Flashcards — Study with cards", value="flashcards"),
    questionary.Choice("📝  Quiz — Multiple choice test", value="quiz"),
    questionary.Choice("🔄  Review — Spaced repetition", value="review"),
    questionary.Choice("🔊  Pronunciation — How to say it", value="pronunciation"),
    questionary.Choice("📈  Stats — View your progress", value="stats"),
    questionary.Choice("🔍  Search — Find a word", value="search"),
    questionary.Choice("⚙️   Language — Change language", value="language"),
    questionary.Choice("👋  Quit — 再见！", value="quit"),
]

MENU_STYLE = questionary.Style([
    ("highlighted", "fg:cyan bold"),
    ("pointer", "fg:cyan bold"),
    ("answer", "fg:green bold"),
    ("question", "fg:white bold"),
])


def _search_mode(lang: str) -> None:
    """Search vocabulary by keyword."""
    console.print()
    query = questionary.text(
        "Search (hanzi, pinyin, english, or german):",
        style=MENU_STYLE,
    ).ask()
    if not query:
        return

    from chinese_cli.vocab_data import search_vocab

    results = search_vocab(query)
    if not results:
        console.print(f"[yellow]  No results for '{query}'[/yellow]")
        return

    table = Table(
        title=f"🔍 Results for '{query}'",
        show_header=True,
        header_style="bold cyan",
        border_style="dim",
    )
    table.add_column("汉字", style="bold yellow", justify="center", width=12)
    table.add_column("Pinyin", style="green", width=16)
    if lang in ("de", "both"):
        table.add_column("Deutsch", style="white", width=22)
    if lang in ("en", "both"):
        table.add_column("English", style="white", width=22)
    table.add_column("Category", style="dim cyan", width=10)

    for v in results[:20]:
        row = [v.hanzi, v.pinyin]
        if lang in ("de", "both"):
            row.append(v.german)
        if lang in ("en", "both"):
            row.append(v.english)
        row.append(v.category)
        table.add_row(*row)

    console.print()
    console.print(table)
    console.print()


def _pronunciation_menu() -> None:
    """Pronunciation guide sub-menu."""
    while True:
        console.print()
        choice = questionary.select(
            "🔊 Pronunciation Guide:",
            choices=[
                questionary.Choice("🎵  Tones — The four tones of Mandarin", value="tones"),
                questionary.Choice("🗣️   Consonants — Initial sounds (b, p, zh, ch...)", value="initials"),
                questionary.Choice("🔤  Vowels — Final sounds (a, e, ai, ou...)", value="finals"),
                questionary.Choice("💪  Your Advantages — DE/AT/RU superpowers", value="advantages"),
                questionary.Choice("🔍  Look Up — Pronunciation for a specific word", value="lookup"),
                questionary.Choice("⬅️   Back to main menu", value="back"),
            ],
            style=MENU_STYLE,
        ).ask()

        if choice is None or choice == "back":
            break
        elif choice == "tones":
            show_tone_guide()
        elif choice == "initials":
            show_initials_guide()
        elif choice == "finals":
            show_finals_guide()
        elif choice == "advantages":
            show_advantages()
        elif choice == "lookup":
            _pronunciation_lookup()


def _pronunciation_lookup() -> None:
    """Look up pronunciation for a specific word from the vocabulary."""
    from chinese_cli.vocab_data import search_vocab

    query = questionary.text(
        "Enter hanzi, pinyin, or translation:",
        style=MENU_STYLE,
    ).ask()
    if not query:
        return

    results = search_vocab(query)
    if not results:
        console.print(f"[yellow]  No results for '{query}'[/yellow]")
        return

    # Show pronunciation for first few results
    for v in results[:3]:
        console.print()
        console.print(render_word_pronunciation(v.hanzi, v.pinyin))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Main application loop."""
    try:
        _show_banner()

        # Initialize progress tracker
        tracker = ProgressTracker()

        # Select language
        lang = _select_language()
        lang_labels = {"de": "🇩🇪 Deutsch", "en": "🇬🇧 English", "both": "🇩🇪🇬🇧 Both"}
        console.print(f"\n  [dim]Language set to:[/dim] [bold cyan]{lang_labels[lang]}[/bold cyan]\n")

        # Show quick stats if returning user
        stats = tracker.get_stats()
        if stats["total_learned"] > 0:
            due = stats["due_now"]
            console.print(
                f"  [dim]Welcome back! "
                f"Words: {stats['total_learned']} · "
                f"Streak: {'🔥' if stats['streak'] > 0 else '❄️'} {stats['streak']} · "
                f"Due: {'⏰ ' + str(due) if due > 0 else '✅ 0'}[/dim]\n"
            )

        # Main loop
        while True:
            choice = questionary.select(
                "What would you like to do?",
                choices=MENU_CHOICES,
                style=MENU_STYLE,
            ).ask()

            if choice is None or choice == "quit":
                tracker.save()
                console.print(
                    Panel(
                        "[bold yellow]再见！[/bold yellow] [dim]Goodbye![/dim]\n"
                        "[dim]See you next time. 加油! 💪[/dim]",
                        border_style="cyan",
                        width=40,
                    )
                )
                break
            elif choice == "learn":
                mode_learn(lang)
            elif choice == "flashcards":
                mode_flashcards(lang, tracker)
            elif choice == "quiz":
                mode_quiz(lang, tracker)
            elif choice == "review":
                mode_review(lang, tracker)
            elif choice == "stats":
                show_stats(tracker)
            elif choice == "pronunciation":
                _pronunciation_menu()
            elif choice == "search":
                _search_mode(lang)
            elif choice == "language":
                lang = _select_language()
                console.print(f"  [dim]Language changed to:[/dim] [bold cyan]{lang_labels[lang]}[/bold cyan]\n")

    except KeyboardInterrupt:
        console.print("\n\n  [dim]再见! Goodbye! 👋[/dim]\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
