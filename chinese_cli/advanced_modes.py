"""
Advanced learning modes: Tone Practice, Pinyin Dictation, Sentence Builder,
Daily Challenge, HSK Test Simulator.
"""

from __future__ import annotations

import random
import time
from datetime import datetime, timezone
from hashlib import md5
from typing import TYPE_CHECKING

import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from chinese_cli.characters import get_character_hint, render_character_panel
from chinese_cli.pronunciation import (
    TONES,
    get_pronunciation_guide,
    render_word_pronunciation,
    _get_tone_from_pinyin,
)
from chinese_cli.vocab_data import ALL_VOCAB, VocabEntry, get_vocab_by_category

if TYPE_CHECKING:
    from chinese_cli.srs import ProgressTracker

console = Console()

STYLE = questionary.Style([
    ("highlighted", "fg:cyan bold"),
    ("pointer", "fg:cyan bold"),
    ("answer", "fg:green bold"),
])


# ---------------------------------------------------------------------------
# DAILY CHALLENGE — Word of the Day
# ---------------------------------------------------------------------------

def daily_challenge(lang: str) -> None:
    """Show a 'word of the day' based on today's date (deterministic)."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    # Deterministic index from date hash
    idx = int(md5(today.encode()).hexdigest(), 16) % len(ALL_VOCAB)
    word = ALL_VOCAB[idx]

    pron = get_pronunciation_guide(word.pinyin)
    char_hint = get_character_hint(word.hanzi[0]) if word.hanzi else None

    # Translation
    if lang == "de":
        trans = word.german
        ex_trans = word.example_de
    elif lang == "en":
        trans = word.english
        ex_trans = word.example_en
    else:
        trans = f"{word.german}  •  {word.english}"
        ex_trans = f"{word.example_de}  •  {word.example_en}"

    content = (
        f"[bold yellow]{word.hanzi}[/bold yellow]\n"
        f"[green]{word.pinyin}[/green]\n"
    )
    if pron:
        content += f"[magenta]🔊 {pron}[/magenta]\n"
    content += (
        f"\n[bold white]{trans}[/bold white]\n"
    )
    if char_hint:
        content += f"\n[dim blue]{char_hint}[/dim blue]\n"
    if word.example_hanzi:
        content += (
            f"\n[dim]───── Example ─────[/dim]\n"
            f"[yellow]{word.example_hanzi}[/yellow]\n"
            f"[green]{word.example_pinyin}[/green]\n"
            f"[dim]{ex_trans}[/dim]"
        )

    console.print()
    console.print(
        Panel(
            content,
            title=f"🌟 Word of the Day — {today}",
            border_style="yellow",
            width=60,
            padding=(1, 2),
        )
    )
    console.print()


# ---------------------------------------------------------------------------
# TONE PRACTICE
# ---------------------------------------------------------------------------

def mode_tone_practice(tracker: "ProgressTracker") -> None:
    """Practice identifying tones of Chinese words."""
    console.print()

    vocab = list(ALL_VOCAB)
    random.shuffle(vocab)
    session_size = min(15, len(vocab))
    vocab = vocab[:session_size]
    correct = 0

    start_time = time.time()

    console.print(
        Panel(
            "[bold]🎵 Tone Practice[/bold]\n\n"
            "[dim]For each word, identify the tone of the highlighted syllable.\n"
            "Press Ctrl+C to quit early.[/dim]",
            border_style="magenta",
            width=55,
        )
    )

    try:
        for i, word in enumerate(vocab, 1):
            # Pick a syllable from the pinyin
            syllables = word.pinyin.split()
            target_syl = random.choice(syllables)
            correct_tone = _get_tone_from_pinyin(target_syl)

            if correct_tone == 0:
                # Skip neutral tone words
                continue

            console.print(f"\n[dim]Question {i}/{session_size}[/dim]")
            console.print(
                f"  [bold yellow]{word.hanzi}[/bold yellow]  —  "
                f"What tone is [bold cyan]{target_syl}[/bold cyan]?"
            )

            answer = questionary.select(
                "Select the tone:",
                choices=[
                    questionary.Choice(f"1st — high flat  {TONES[0]['symbol']}", value=1),
                    questionary.Choice(f"2nd — rising     {TONES[1]['symbol']}", value=2),
                    questionary.Choice(f"3rd — dip        {TONES[2]['symbol']}", value=3),
                    questionary.Choice(f"4th — falling    {TONES[3]['symbol']}", value=4),
                ],
                style=STYLE,
            ).ask()

            if answer == correct_tone:
                console.print(f"  [bold green]✓ Correct! {TONES[correct_tone - 1]['tone']}[/bold green]")
                correct += 1
                tracker.review(word.hanzi, 4)
            else:
                console.print(
                    f"  [bold red]✗ Wrong![/bold red]  "
                    f"Correct: [cyan]{TONES[correct_tone - 1]['tone']}[/cyan]\n"
                    f"  [dim]{TONES[correct_tone - 1]['de_hint']}[/dim]"
                )
                tracker.review(word.hanzi, 1)

    except KeyboardInterrupt:
        console.print("\n[dim]Session interrupted.[/dim]")

    elapsed = time.time() - start_time
    total = min(i, session_size) if 'i' in dir() else 0
    acc = (correct / total * 100) if total > 0 else 0

    _show_session_summary("Tone Practice", correct, total, elapsed, acc)


# ---------------------------------------------------------------------------
# PINYIN DICTATION
# ---------------------------------------------------------------------------

def mode_pinyin_dictation(lang: str, tracker: "ProgressTracker") -> None:
    """Show translation, user types the pinyin — tests active recall."""
    console.print()

    vocab = list(ALL_VOCAB)
    random.shuffle(vocab)
    session_size = min(12, len(vocab))
    vocab = vocab[:session_size]
    correct = 0

    start_time = time.time()

    if lang == "de":
        trans_label = "Deutsch"
    elif lang == "en":
        trans_label = "English"
    else:
        trans_label = "Translation"

    console.print(
        Panel(
            "[bold]✍️  Pinyin Dictation[/bold]\n\n"
            "[dim]Given the translation, type the Pinyin (without tones).\n"
            "Press Enter to skip, Ctrl+C to quit.[/dim]",
            border_style="blue",
            width=55,
        )
    )

    try:
        for i, word in enumerate(vocab, 1):
            if lang == "de":
                prompt_text = word.german
            elif lang == "en":
                prompt_text = word.english
            else:
                prompt_text = f"{word.german}  •  {word.english}"

            console.print(f"\n[dim]Word {i}/{session_size}[/dim]")
            console.print(
                f"  [bold white]{prompt_text}[/bold white]\n"
                f"  [dim](Hanzi: {word.hanzi})[/dim]"
            )

            answer = questionary.text(
                "Pinyin:",
                style=STYLE,
            ).ask()

            if answer is None:
                break

            # Normalize for comparison: strip tones and spaces
            tone_map = str.maketrans("āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ", "aaaaeeeeiiiioooouuuuüüüü")
            expected = word.pinyin.lower().translate(tone_map).replace(" ", "")
            given = answer.lower().strip().translate(tone_map).replace(" ", "")
            # Also handle v for ü
            given = given.replace("v", "ü")

            pron = get_pronunciation_guide(word.pinyin)

            if given == expected:
                console.print(f"  [bold green]✓ Correct! {word.pinyin}[/bold green]")
                if pron:
                    console.print(f"  [magenta]🔊 {pron}[/magenta]")
                correct += 1
                tracker.review(word.hanzi, 5)
            elif answer.strip() == "":
                console.print(f"  [yellow]⏭  Skipped. Answer: {word.pinyin}[/yellow]")
                if pron:
                    console.print(f"  [magenta]🔊 {pron}[/magenta]")
            else:
                console.print(
                    f"  [bold red]✗ Not quite![/bold red]  "
                    f"Correct: [green]{word.pinyin}[/green]  Your answer: [dim]{answer}[/dim]"
                )
                if pron:
                    console.print(f"  [magenta]🔊 {pron}[/magenta]")
                tracker.review(word.hanzi, 1)

    except KeyboardInterrupt:
        console.print("\n[dim]Session interrupted.[/dim]")

    elapsed = time.time() - start_time
    total = min(i, session_size) if 'i' in dir() else 0
    acc = (correct / total * 100) if total > 0 else 0

    _show_session_summary("Pinyin Dictation", correct, total, elapsed, acc)


# ---------------------------------------------------------------------------
# SENTENCE BUILDER
# ---------------------------------------------------------------------------

# Simple sentence templates for practice
SENTENCE_TEMPLATES: list[dict[str, str | list[str]]] = [
    {
        "pattern": "S + V + O",
        "template_cn": "{subject}{verb}{object}。",
        "template_py": "{subject_py} {verb_py} {object_py}.",
        "slots": ["subject", "verb", "object"],
        "hint_de": "Subjekt + Verb + Objekt (wie im Englischen)",
        "hint_en": "Subject + Verb + Object",
    },
    {
        "pattern": "S + 不 + V + O",
        "template_cn": "{subject}不{verb}{object}。",
        "template_py": "{subject_py} bù {verb_py} {object_py}.",
        "slots": ["subject", "verb", "object"],
        "hint_de": "Subjekt + nicht + Verb + Objekt",
        "hint_en": "Subject + not + Verb + Object",
    },
    {
        "pattern": "S + 很 + Adj",
        "template_cn": "{subject}很{adjective}。",
        "template_py": "{subject_py} hěn {adjective_py}.",
        "slots": ["subject", "adjective"],
        "hint_de": "Subjekt + sehr + Adjektiv (Brücke für Adjektive)",
        "hint_en": "Subject + very + Adjective (linking word for adj predicates)",
    },
    {
        "pattern": "S + 想 + V + O",
        "template_cn": "{subject}想{verb}{object}。",
        "template_py": "{subject_py} xiǎng {verb_py} {object_py}.",
        "slots": ["subject", "verb", "object"],
        "hint_de": "Subjekt + möchte + Verb + Objekt",
        "hint_en": "Subject + want + Verb + Object",
    },
]

# Word pools for sentence building
WORD_POOLS: dict[str, list[dict[str, str]]] = {
    "subject": [
        {"cn": "我", "py": "wǒ", "de": "ich", "en": "I"},
        {"cn": "你", "py": "nǐ", "de": "du", "en": "you"},
        {"cn": "他", "py": "tā", "de": "er", "en": "he"},
        {"cn": "她", "py": "tā", "de": "sie", "en": "she"},
        {"cn": "我们", "py": "wǒmen", "de": "wir", "en": "we"},
    ],
    "verb": [
        {"cn": "学", "py": "xué", "de": "lernen", "en": "study"},
        {"cn": "写", "py": "xiě", "de": "schreiben", "en": "write"},
        {"cn": "用", "py": "yòng", "de": "benutzen", "en": "use"},
        {"cn": "看", "py": "kàn", "de": "sehen", "en": "look at"},
        {"cn": "知道", "py": "zhīdào", "de": "wissen", "en": "know"},
        {"cn": "开发", "py": "kāifā", "de": "entwickeln", "en": "develop"},
    ],
    "object": [
        {"cn": "中文", "py": "zhōngwén", "de": "Chinesisch", "en": "Chinese"},
        {"cn": "代码", "py": "dàimǎ", "de": "Code", "en": "code"},
        {"cn": "软件", "py": "ruǎnjiàn", "de": "Software", "en": "software"},
        {"cn": "数据库", "py": "shùjùkù", "de": "Datenbank", "en": "database"},
        {"cn": "人工智能", "py": "réngōng zhìnéng", "de": "KI", "en": "AI"},
    ],
    "adjective": [
        {"cn": "好", "py": "hǎo", "de": "gut", "en": "good"},
        {"cn": "快", "py": "kuài", "de": "schnell", "en": "fast"},
        {"cn": "大", "py": "dà", "de": "groß", "en": "big"},
        {"cn": "难", "py": "nán", "de": "schwierig", "en": "difficult"},
        {"cn": "重要", "py": "zhòngyào", "de": "wichtig", "en": "important"},
    ],
}


def mode_sentence_builder(lang: str) -> None:
    """Interactive sentence building practice."""
    console.print()

    console.print(
        Panel(
            "[bold]🏗️ Sentence Builder[/bold]\n\n"
            "[dim]Build Chinese sentences using grammar patterns.\n"
            "Select words to fill in the blanks![/dim]",
            border_style="green",
            width=55,
        )
    )

    rounds = 5
    for round_num in range(1, rounds + 1):
        template = random.choice(SENTENCE_TEMPLATES)

        console.print(f"\n[dim]Sentence {round_num}/{rounds}[/dim]")

        if lang == "de":
            hint = template["hint_de"]
        elif lang == "en":
            hint = template["hint_en"]
        else:
            hint = f"{template['hint_de']}  •  {template['hint_en']}"

        console.print(
            f"  [bold magenta]Pattern: {template['pattern']}[/bold magenta]\n"
            f"  [dim]{hint}[/dim]\n"
        )

        # Let user pick words for each slot
        chosen: dict[str, dict[str, str]] = {}
        for slot in template["slots"]:
            pool = WORD_POOLS.get(slot, [])
            if not pool:
                continue

            if lang == "de":
                label_fn = lambda w: f"{w['cn']} ({w['py']}) — {w['de']}"
            elif lang == "en":
                label_fn = lambda w: f"{w['cn']} ({w['py']}) — {w['en']}"
            else:
                label_fn = lambda w: f"{w['cn']} ({w['py']}) — {w['de']} / {w['en']}"

            choices = [
                questionary.Choice(label_fn(w), value=w["cn"])
                for w in pool
            ]

            answer = questionary.select(
                f"Choose {slot}:",
                choices=choices,
                style=STYLE,
            ).ask()

            if answer is None:
                return

            chosen[slot] = next(w for w in pool if w["cn"] == answer)

        # Build the sentence
        cn_parts = {slot: chosen[slot]["cn"] for slot in template["slots"]}
        py_parts = {f"{slot}_py": chosen[slot]["py"] for slot in template["slots"]}

        sentence_cn = template["template_cn"].format(**cn_parts)
        sentence_py = template["template_py"].format(**py_parts)

        console.print(
            Panel(
                f"[bold yellow]{sentence_cn}[/bold yellow]\n"
                f"[green]{sentence_py}[/green]",
                title="✅ Your Sentence",
                border_style="green",
                width=55,
                padding=(1, 2),
            )
        )

    console.print("\n[dim cyan]Great practice! 加油！💪[/dim cyan]\n")


# ---------------------------------------------------------------------------
# HSK TEST SIMULATOR
# ---------------------------------------------------------------------------

def mode_hsk_simulator(lang: str, tracker: "ProgressTracker") -> None:
    """Timed HSK-style test simulation."""
    console.print()

    # Select HSK level
    level = questionary.select(
        "Select HSK level:",
        choices=[
            questionary.Choice("HSK 1 (beginner)", value=1),
            questionary.Choice("HSK 2 (elementary)", value=2),
            questionary.Choice("HSK 3 (intermediate)", value=3),
            questionary.Choice("HSK 4 (upper-intermediate)", value=4),
            questionary.Choice("HSK 5 (advanced)", value=5),
            questionary.Choice("All levels", value=0),
        ],
        style=STYLE,
    ).ask()

    if level is None:
        return

    # Filter vocabulary
    from chinese_cli.vocab_data import get_vocab_by_hsk
    if level == 0:
        vocab = list(ALL_VOCAB)
    else:
        vocab = get_vocab_by_hsk(level)

    if len(vocab) < 4:
        console.print("[yellow]Not enough words for this HSK level.[/yellow]")
        return

    random.shuffle(vocab)
    test_size = min(20, len(vocab))
    test_words = vocab[:test_size]
    correct = 0

    # Time limit: 30 seconds per question
    time_per_q = 30
    total_time = test_size * time_per_q

    console.print(
        Panel(
            f"[bold]📋 HSK Test Simulator[/bold]\n\n"
            f"Level: [cyan]{'All' if level == 0 else f'HSK {level}'}[/cyan]\n"
            f"Questions: [cyan]{test_size}[/cyan]\n"
            f"Time limit: [cyan]{total_time // 60}:{total_time % 60:02d}[/cyan]\n\n"
            f"[dim]Mixed question types: translation, pinyin, and fill-in.\n"
            f"Press Ctrl+C to end early.[/dim]",
            border_style="red",
            width=55,
        )
    )

    start_time = time.time()

    try:
        for i, word in enumerate(test_words, 1):
            elapsed = time.time() - start_time
            remaining = max(0, total_time - elapsed)

            if remaining <= 0:
                console.print("\n[bold red]⏰ Time's up![/bold red]")
                break

            console.print(
                f"\n[dim]Question {i}/{test_size} · "
                f"⏱️ {int(remaining // 60)}:{int(remaining % 60):02d} remaining[/dim]"
            )

            # Alternate question types
            q_type = i % 3

            if q_type == 0:
                # Type 1: Hanzi → Translation
                console.print(f"  [bold yellow]{word.hanzi}[/bold yellow]  ({word.pinyin})")
                console.print("  [dim]Select the correct translation:[/dim]\n")

                distractors = [v for v in ALL_VOCAB if v.hanzi != word.hanzi]
                random.shuffle(distractors)
                options = [word] + distractors[:3]
                random.shuffle(options)

                if lang == "de":
                    choices = [questionary.Choice(opt.german, value=opt.hanzi) for opt in options]
                elif lang == "en":
                    choices = [questionary.Choice(opt.english, value=opt.hanzi) for opt in options]
                else:
                    choices = [
                        questionary.Choice(f"{opt.german}  •  {opt.english}", value=opt.hanzi)
                        for opt in options
                    ]

                answer = questionary.select("Answer:", choices=choices, style=STYLE).ask()
                is_correct = answer == word.hanzi

            elif q_type == 1:
                # Type 2: Translation → Hanzi
                if lang == "de":
                    prompt = word.german
                elif lang == "en":
                    prompt = word.english
                else:
                    prompt = f"{word.german}  •  {word.english}"

                console.print(f"  [bold white]{prompt}[/bold white]")
                console.print("  [dim]Select the correct Hanzi:[/dim]\n")

                distractors = [v for v in ALL_VOCAB if v.hanzi != word.hanzi]
                random.shuffle(distractors)
                options = [word] + distractors[:3]
                random.shuffle(options)

                choices = [
                    questionary.Choice(f"{opt.hanzi}  ({opt.pinyin})", value=opt.hanzi)
                    for opt in options
                ]

                answer = questionary.select("Answer:", choices=choices, style=STYLE).ask()
                is_correct = answer == word.hanzi

            else:
                # Type 3: Hanzi → Pinyin (from choices)
                console.print(f"  [bold yellow]{word.hanzi}[/bold yellow]")
                console.print("  [dim]Select the correct Pinyin:[/dim]\n")

                distractors = [v for v in ALL_VOCAB if v.hanzi != word.hanzi]
                random.shuffle(distractors)
                options = [word] + distractors[:3]
                random.shuffle(options)

                choices = [
                    questionary.Choice(opt.pinyin, value=opt.hanzi)
                    for opt in options
                ]

                answer = questionary.select("Answer:", choices=choices, style=STYLE).ask()
                is_correct = answer == word.hanzi

            if answer is None:
                break

            if is_correct:
                console.print("  [bold green]✓ Correct![/bold green]")
                correct += 1
                tracker.review(word.hanzi, 4)
            else:
                if lang == "de":
                    expected = f"{word.hanzi} ({word.pinyin}) = {word.german}"
                elif lang == "en":
                    expected = f"{word.hanzi} ({word.pinyin}) = {word.english}"
                else:
                    expected = f"{word.hanzi} ({word.pinyin}) = {word.german} / {word.english}"
                console.print(f"  [bold red]✗ Wrong![/bold red]  Correct: [yellow]{expected}[/yellow]")
                tracker.review(word.hanzi, 1)

    except KeyboardInterrupt:
        console.print("\n[dim]Test ended early.[/dim]")

    elapsed = time.time() - start_time
    total = min(i, test_size) if 'i' in dir() else 0
    acc = (correct / total * 100) if total > 0 else 0

    # Grade
    if acc >= 90:
        grade = "[bold green]A — Excellent! 优秀！[/bold green]"
    elif acc >= 80:
        grade = "[bold cyan]B — Good! 良好！[/bold cyan]"
    elif acc >= 70:
        grade = "[bold yellow]C — Pass! 及格！[/bold yellow]"
    elif acc >= 60:
        grade = "[bold yellow]D — Borderline 还需努力[/bold yellow]"
    else:
        grade = "[bold red]F — Keep studying! 继续加油！[/bold red]"

    console.print(
        Panel(
            f"[bold]HSK Test Results[/bold]\n\n"
            f"Score: [cyan]{correct}[/cyan] / {total}\n"
            f"Accuracy: [{'green' if acc >= 70 else 'yellow' if acc >= 50 else 'red'}]{acc:.0f}%"
            f"[/{'green' if acc >= 70 else 'yellow' if acc >= 50 else 'red'}]\n"
            f"Time: {int(elapsed // 60)}:{int(elapsed % 60):02d}\n\n"
            f"Grade: {grade}",
            title="📋 HSK Test Results",
            border_style="red",
            width=50,
        )
    )


# ---------------------------------------------------------------------------
# Session Summary Helper
# ---------------------------------------------------------------------------

def _show_session_summary(
    mode_name: str, correct: int, total: int, elapsed: float, acc: float
) -> None:
    """Display a standardized session summary with timer."""
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)

    console.print(
        Panel(
            f"[bold]{mode_name} Complete![/bold]\n\n"
            f"Score: [cyan]{correct}[/cyan] / {total}\n"
            f"Accuracy: [{'green' if acc >= 70 else 'yellow' if acc >= 50 else 'red'}]{acc:.0f}%"
            f"[/{'green' if acc >= 70 else 'yellow' if acc >= 50 else 'red'}]\n"
            f"⏱️  Time: {minutes}:{seconds:02d}",
            title="📊 Session Summary",
            border_style="cyan",
            width=45,
        )
    )
