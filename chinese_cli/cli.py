"""
汉语学习工具 — Chinese Learning CLI  (龙码 LóngMǎ)

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
from chinese_cli.config import AppConfig
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
# Sound effects
# ---------------------------------------------------------------------------

def _sound(kind: str, config: AppConfig) -> None:
    """Play terminal bell sound if enabled."""
    if not config.sound_enabled:
        return
    if kind == "correct":
        sys.stdout.write("\a")
        sys.stdout.flush()


# ---------------------------------------------------------------------------
# Welcome banner
# ---------------------------------------------------------------------------

BANNER = r"""
[bold cyan]
  ╔══════════════════════════════════════════════════╗
  ║                                                  ║
  ║     龙 码  LóngMǎ                                ║
  ║     ─────────────────                             ║
  ║     Dragon Code · Chinese Learning CLI           ║
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
    questionary.Separator("─── Advanced ───"),
    questionary.Choice("🎵  Tone Practice — Identify tones", value="tones"),
    questionary.Choice("✍️   Dictation — Type the Pinyin", value="dictation"),
    questionary.Choice("🏗️   Sentence Builder — Grammar practice", value="sentences"),
    questionary.Choice("📋  HSK Test — Timed exam simulator", value="hsk_test"),
    questionary.Separator("─── Reference ───"),
    questionary.Choice("🔊  Pronunciation — How to say it", value="pronunciation"),
    questionary.Choice("✏️   Characters — Radical breakdowns", value="characters"),
    questionary.Choice("📖  Grammar — Essential patterns", value="grammar"),
    questionary.Separator("─── Analytics ───"),
    questionary.Choice("📈  Stats — View your progress", value="stats"),
    questionary.Choice("📊  Charts — Progress visualisation", value="charts"),
    questionary.Choice("🎯  Weak Words — Focus practice", value="weak_words"),
    questionary.Choice("📄  Export — Generate study report", value="export"),
    questionary.Separator("─── Tools ───"),
    questionary.Choice("🔍  Search — Find a word", value="search"),
    questionary.Choice("📦  Import — Load custom vocab (CSV/JSON)", value="import"),
    questionary.Choice("⚙️   Settings — Language & preferences", value="settings"),
    questionary.Choice("👋  Quit — 再见！", value="quit"),
]

MENU_STYLE = questionary.Style([
    ("highlighted", "fg:cyan bold"),
    ("pointer", "fg:cyan bold"),
    ("answer", "fg:green bold"),
    ("question", "fg:white bold"),
    ("separator", "fg:magenta"),
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


def _settings_menu(config: AppConfig, lang_ref: list[str]) -> None:
    """Settings sub-menu for preferences."""
    while True:
        console.print()
        choice = questionary.select(
            "⚙️  Settings:",
            choices=[
                questionary.Choice(
                    f"🌐  Language — Currently: {lang_ref[0]}", value="language"
                ),
                questionary.Choice(
                    f"🔊  Sound — {'ON ✅' if config.sound_enabled else 'OFF ❌'}",
                    value="sound",
                ),
                questionary.Choice(
                    f"🌟  Daily Challenge — {'ON ✅' if config.show_daily_challenge else 'OFF ❌'}",
                    value="daily",
                ),
                questionary.Choice(
                    f"⏱️   Session Timer — {'ON ✅' if config.show_session_timer else 'OFF ❌'}",
                    value="timer",
                ),
                questionary.Choice(
                    f"📊  HSK Level Cap — HSK {config.max_hsk_level}",
                    value="hsk_cap",
                ),
                questionary.Choice("⬅️   Back", value="back"),
            ],
            style=MENU_STYLE,
        ).ask()

        if choice is None or choice == "back":
            break
        elif choice == "language":
            lang_ref[0] = _select_language()
            config.update(language=lang_ref[0])
            console.print(f"  [bold green]✓[/bold green] Language set to {lang_ref[0]}")
        elif choice == "sound":
            config.update(sound_enabled=not config.sound_enabled)
            state = "ON ✅" if config.sound_enabled else "OFF ❌"
            console.print(f"  [bold green]✓[/bold green] Sound: {state}")
        elif choice == "daily":
            config.update(show_daily_challenge=not config.show_daily_challenge)
            state = "ON ✅" if config.show_daily_challenge else "OFF ❌"
            console.print(f"  [bold green]✓[/bold green] Daily Challenge: {state}")
        elif choice == "timer":
            config.update(show_session_timer=not config.show_session_timer)
            state = "ON ✅" if config.show_session_timer else "OFF ❌"
            console.print(f"  [bold green]✓[/bold green] Session Timer: {state}")
        elif choice == "hsk_cap":
            level = questionary.select(
                "Max HSK level to show:",
                choices=[
                    questionary.Choice(f"HSK {i}", value=i) for i in range(1, 6)
                ],
                style=MENU_STYLE,
            ).ask()
            if level:
                config.update(max_hsk_level=level)
                console.print(f"  [bold green]✓[/bold green] HSK cap set to {level}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Main application loop."""
    try:
        _show_banner()

        # Load config
        config = AppConfig.load()

        # Initialize progress tracker
        tracker = ProgressTracker()

        # Select language (or use saved preference)
        if config.language in ("de", "en", "both"):
            lang = config.language
        else:
            lang = _select_language()

        lang_labels = {"de": "🇩🇪 Deutsch", "en": "🇬🇧 English", "both": "🇩🇪🇬🇧 Both"}
        console.print(f"\n  [dim]Language:[/dim] [bold cyan]{lang_labels[lang]}[/bold cyan]\n")

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

        # Daily challenge on launch
        if config.show_daily_challenge:
            from chinese_cli.advanced_modes import daily_challenge
            daily_challenge(lang)

        # Mutable reference for settings menu
        lang_ref = [lang]

        # Session timer
        session_start = time.time()

        # Main loop
        while True:
            choice = questionary.select(
                "What would you like to do?",
                choices=MENU_CHOICES,
                style=MENU_STYLE,
            ).ask()

            if choice is None or choice == "quit":
                tracker.save()

                # Session summary
                elapsed = time.time() - session_start
                mins = int(elapsed // 60)
                secs = int(elapsed % 60)

                console.print(
                    Panel(
                        f"[bold yellow]再见！[/bold yellow] [dim]Goodbye![/dim]\n"
                        f"[dim]Session: {mins}:{secs:02d} · See you next time. 加油! 💪[/dim]",
                        border_style="cyan",
                        width=45,
                    )
                )
                break

            # Use the potentially updated lang
            lang = lang_ref[0]

            # Core modes
            if choice == "learn":
                mode_learn(lang)
            elif choice == "flashcards":
                mode_flashcards(lang, tracker)
            elif choice == "quiz":
                mode_quiz(lang, tracker)
            elif choice == "review":
                mode_review(lang, tracker)

            # Advanced modes
            elif choice == "tones":
                from chinese_cli.advanced_modes import mode_tone_practice
                mode_tone_practice(tracker)
            elif choice == "dictation":
                from chinese_cli.advanced_modes import mode_pinyin_dictation
                mode_pinyin_dictation(lang, tracker)
            elif choice == "sentences":
                from chinese_cli.advanced_modes import mode_sentence_builder
                mode_sentence_builder(lang)
            elif choice == "hsk_test":
                from chinese_cli.advanced_modes import mode_hsk_simulator
                mode_hsk_simulator(lang, tracker)

            # Reference
            elif choice == "pronunciation":
                _pronunciation_menu()
            elif choice == "characters":
                from chinese_cli.characters import show_radical_table
                show_radical_table()
            elif choice == "grammar":
                from chinese_cli.grammar import show_grammar_patterns
                show_grammar_patterns(lang)

            # Analytics
            elif choice == "stats":
                show_stats(tracker)
            elif choice == "charts":
                from chinese_cli.analytics import show_progress_charts
                show_progress_charts(tracker)
            elif choice == "weak_words":
                from chinese_cli.analytics import show_weak_words
                show_weak_words(tracker)
            elif choice == "export":
                from chinese_cli.analytics import export_study_report
                export_study_report(tracker)

            # Tools
            elif choice == "search":
                _search_mode(lang)
            elif choice == "import":
                from chinese_cli.plugins import show_import_menu
                show_import_menu()
            elif choice == "settings":
                _settings_menu(config, lang_ref)

    except KeyboardInterrupt:
        console.print("\n\n  [dim]再见! Goodbye! 👋[/dim]\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
