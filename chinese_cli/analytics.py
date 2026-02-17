"""
Analytics module: weak word tracking, progress charts, and study reports.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING, Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

if TYPE_CHECKING:
    from chinese_cli.srs import ProgressTracker

console = Console()


# ---------------------------------------------------------------------------
# Weak Word Tracker
# ---------------------------------------------------------------------------

def get_weak_words(tracker: "ProgressTracker", limit: int = 15) -> list[dict[str, Any]]:
    """
    Identify the weakest words based on:
    - Low accuracy (most wrong answers)
    - Low ease factor (hardest to recall)
    - High review count but still low mastery
    """
    weak: list[dict[str, Any]] = []

    for hanzi, card in tracker.cards.items():
        if card.total_reviews == 0:
            continue

        # Weakness score: lower is weaker
        weakness = (
            (100 - card.accuracy) * 2  # Penalize low accuracy heavily
            + max(0, 2.5 - card.ease_factor) * 30  # Penalize low ease
            + max(0, card.total_reviews - card.correct_reviews) * 10  # Penalize wrong count
        )

        weak.append({
            "hanzi": hanzi,
            "accuracy": card.accuracy,
            "ease_factor": card.ease_factor,
            "total_reviews": card.total_reviews,
            "correct_reviews": card.correct_reviews,
            "mastery": card.mastery_level,
            "weakness_score": weakness,
        })

    # Sort by weakness score (highest = weakest)
    weak.sort(key=lambda x: x["weakness_score"], reverse=True)
    return weak[:limit]


def show_weak_words(tracker: "ProgressTracker") -> None:
    """Display the user's weakest words with analysis."""
    from chinese_cli.vocab_data import ALL_VOCAB

    weak = get_weak_words(tracker)

    if not weak:
        console.print(
            Panel(
                "[bold green]No weak words yet![/bold green]\n\n"
                "[dim]Start reviewing words to see which ones\n"
                "need the most practice.[/dim]",
                border_style="green",
                width=50,
            )
        )
        return

    hanzi_map = {v.hanzi: v for v in ALL_VOCAB}

    console.print()
    table = Table(
        title="🎯 Your Weakest Words — Focus Practice Here!",
        show_header=True,
        header_style="bold cyan",
        border_style="dim",
        width=75,
    )
    table.add_column("汉字", style="bold yellow", justify="center", width=8)
    table.add_column("Pinyin", style="green", width=14)
    table.add_column("Accuracy", justify="center", width=10)
    table.add_column("Reviews", justify="center", width=9)
    table.add_column("Level", width=12)
    table.add_column("Weakness", justify="center", width=10)

    for w in weak:
        vocab = hanzi_map.get(w["hanzi"])
        pinyin = vocab.pinyin if vocab else "?"

        # Color-code accuracy
        acc = w["accuracy"]
        if acc < 40:
            acc_str = f"[bold red]{acc:.0f}%[/bold red]"
        elif acc < 65:
            acc_str = f"[yellow]{acc:.0f}%[/yellow]"
        else:
            acc_str = f"[green]{acc:.0f}%[/green]"

        reviews = f"{w['correct_reviews']}/{w['total_reviews']}"

        # Weakness bar
        score = min(w["weakness_score"], 200)
        blocks = int(score / 200 * 8)
        bar = "🔴" * blocks + "⚪" * (8 - blocks)

        table.add_row(w["hanzi"], pinyin, acc_str, reviews, w["mastery"], bar)

    console.print(table)
    console.print(
        "\n  [dim]💡 Tip: Use Review mode to focus on these words.[/dim]\n"
    )


# ---------------------------------------------------------------------------
# Progress Charts (Sparklines)
# ---------------------------------------------------------------------------

SPARK_BLOCKS = "▁▂▃▄▅▆▇█"


def _sparkline(values: list[float], max_val: float | None = None) -> str:
    """Generate a sparkline string from a list of values."""
    if not values:
        return ""
    if max_val is None:
        max_val = max(values) if max(values) > 0 else 1
    scale = len(SPARK_BLOCKS) - 1
    return "".join(
        SPARK_BLOCKS[min(int(v / max_val * scale), scale)] for v in values
    )


def show_progress_charts(tracker: "ProgressTracker") -> None:
    """Display visual progress charts with sparklines."""
    from chinese_cli.vocab_data import ALL_VOCAB, CATEGORIES

    console.print()

    # 1) Mastery distribution bar
    stats = tracker.get_stats()
    total_words = len(ALL_VOCAB)

    mastery_data = [
        ("🆕 New", total_words - stats["total_learned"], "dim"),
        ("📖 Learning", stats.get("learning", 0), "yellow"),
        ("🔄 Reviewing", stats.get("reviewing", 0), "cyan"),
        ("⭐ Mastered", stats.get("mastered", 0), "green"),
    ]

    console.print(
        Panel(
            "[bold]Mastery Distribution[/bold]",
            border_style="cyan",
            width=60,
        )
    )

    for label, count, color in mastery_data:
        bar_len = int(count / total_words * 40) if total_words > 0 else 0
        bar = "█" * bar_len + "░" * (40 - bar_len)
        console.print(f"  {label:16s} [{color}]{bar}[/{color}] {count}/{total_words}")

    console.print()

    # 2) Category progress
    console.print(
        Panel("[bold]Category Progress[/bold]", border_style="cyan", width=60)
    )

    for cat_key, cat_name in CATEGORIES.items():
        from chinese_cli.vocab_data import get_vocab_by_category
        cat_vocab = get_vocab_by_category(cat_key)
        learned = sum(1 for v in cat_vocab if v.hanzi in tracker.cards)
        total = len(cat_vocab)
        pct = (learned / total * 100) if total > 0 else 0

        bar_len = int(pct / 100 * 30)
        bar = "█" * bar_len + "░" * (30 - bar_len)
        console.print(f"  {cat_name:30s} [{pct:.0f}%] {bar}")

    console.print()

    # 3) Accuracy sparkline across reviewed words
    accuracies = [
        card.accuracy
        for card in sorted(tracker.cards.values(), key=lambda c: c.last_reviewed)
        if card.total_reviews > 0
    ]

    if accuracies:
        spark = _sparkline(accuracies, max_val=100)
        avg = sum(accuracies) / len(accuracies)
        console.print(
            Panel(
                f"[bold]Accuracy Trend[/bold] (oldest → newest)\n\n"
                f"  [cyan]{spark}[/cyan]\n\n"
                f"  Average: [{'green' if avg >= 70 else 'yellow'}]{avg:.1f}%"
                f"[/{'green' if avg >= 70 else 'yellow'}]  "
                f"Words tracked: [cyan]{len(accuracies)}[/cyan]",
                border_style="cyan",
                width=60,
            )
        )
    else:
        console.print("  [dim]No accuracy data yet. Start reviewing![/dim]")

    console.print()


# ---------------------------------------------------------------------------
# Exportable Study Report
# ---------------------------------------------------------------------------

def export_study_report(tracker: "ProgressTracker", filepath: str | None = None) -> str:
    """
    Generate an exportable study report in Markdown format.
    Returns the filepath where the report was saved.
    """
    from chinese_cli.vocab_data import ALL_VOCAB, CATEGORIES, get_vocab_by_category

    if filepath is None:
        report_dir = Path.home() / ".chinese-cli" / "reports"
        report_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        filepath = str(report_dir / f"study_report_{timestamp}.md")

    stats = tracker.get_stats()
    total_words = len(ALL_VOCAB)
    weak = get_weak_words(tracker, limit=10)
    hanzi_map = {v.hanzi: v for v in ALL_VOCAB}

    lines = [
        "# 龙码 LóngMǎ — Study Report",
        f"",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"",
        f"## Overview",
        f"",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Words Studied | {stats['total_learned']} / {total_words} |",
        f"| Mastered | {stats.get('mastered', 0)} |",
        f"| Reviewing | {stats.get('reviewing', 0)} |",
        f"| Learning | {stats.get('learning', 0)} |",
        f"| Streak | {stats['streak']} day(s) |",
        f"| Total Sessions | {stats['total_sessions']} |",
        f"| Average Accuracy | {stats['avg_accuracy']:.1f}% |",
        f"| Due for Review | {stats['due_now']} |",
        f"",
        f"## Category Progress",
        f"",
        f"| Category | Words Learned | Total | Progress |",
        f"|----------|---------------|-------|----------|",
    ]

    for cat_key, cat_name in CATEGORIES.items():
        cat_vocab = get_vocab_by_category(cat_key)
        learned = sum(1 for v in cat_vocab if v.hanzi in tracker.cards)
        total = len(cat_vocab)
        pct = (learned / total * 100) if total > 0 else 0
        bar = "█" * int(pct / 10) + "░" * (10 - int(pct / 10))
        lines.append(f"| {cat_name} | {learned} | {total} | {bar} {pct:.0f}% |")

    lines.extend([
        f"",
        f"## Weakest Words",
        f"",
        f"| Hanzi | Pinyin | Accuracy | Reviews | Level |",
        f"|-------|--------|----------|---------|-------|",
    ])

    for w in weak:
        vocab = hanzi_map.get(w["hanzi"])
        pinyin = vocab.pinyin if vocab else "?"
        lines.append(
            f"| {w['hanzi']} | {pinyin} | {w['accuracy']:.0f}% | "
            f"{w['correct_reviews']}/{w['total_reviews']} | {w['mastery']} |"
        )

    lines.extend([
        f"",
        f"## Mastered Words",
        f"",
    ])

    mastered = [
        h for h, c in tracker.cards.items()
        if c.mastery_level == "mastered"
    ]
    if mastered:
        for h in mastered:
            v = hanzi_map.get(h)
            if v:
                lines.append(f"- **{v.hanzi}** ({v.pinyin}) — {v.german} / {v.english}")
    else:
        lines.append("_No mastered words yet. Keep studying! 加油！_")

    lines.extend([
        f"",
        f"---",
        f"*Generated by 龙码 LóngMǎ — Dragon Code*",
    ])

    report_content = "\n".join(lines)
    Path(filepath).write_text(report_content, encoding="utf-8")

    console.print(
        Panel(
            f"[bold green]✅ Report exported![/bold green]\n\n"
            f"[dim]{filepath}[/dim]",
            border_style="green",
            width=55,
        )
    )

    return filepath
