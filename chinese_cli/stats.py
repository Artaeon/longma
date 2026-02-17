"""
Progress statistics and visualisation.
"""

from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from chinese_cli.srs import ProgressTracker
from chinese_cli.vocab_data import ALL_VOCAB, CATEGORIES, get_vocab_by_category

console = Console()


def _bar(filled: int, total: int, width: int = 20, color: str = "cyan") -> str:
    """Render a simple progress bar string."""
    if total == 0:
        return f"[dim]{'░' * width}[/dim] 0/0"
    pct = filled / total
    filled_blocks = round(pct * width)
    empty_blocks = width - filled_blocks
    return f"[{color}]{'█' * filled_blocks}[/{color}][dim]{'░' * empty_blocks}[/dim] {filled}/{total}"


def show_stats(tracker: ProgressTracker) -> None:
    """Display comprehensive learning statistics."""
    stats = tracker.get_stats()
    total_vocab = len(ALL_VOCAB)

    # --- Header ---
    console.print()
    streak_emoji = "🔥" if stats["streak"] > 0 else "❄️"
    console.print(
        Panel(
            f"[bold white]Learning Progress[/bold white]\n\n"
            f"  {streak_emoji}  Streak: [bold cyan]{stats['streak']}[/bold cyan] day(s)\n"
            f"  📅  Total sessions: [cyan]{stats['total_sessions']}[/cyan]\n"
            f"  📊  Average accuracy: [{'green' if stats['avg_accuracy'] >= 70 else 'yellow'}]"
            f"{stats['avg_accuracy']:.1f}%[/{'green' if stats['avg_accuracy'] >= 70 else 'yellow'}]",
            title="📈 Statistics",
            border_style="cyan",
            width=55,
        )
    )

    # --- Mastery breakdown ---
    mastery_table = Table(
        show_header=True,
        header_style="bold white",
        border_style="dim",
        width=55,
    )
    mastery_table.add_column("Level", style="bold", width=14)
    mastery_table.add_column("Count", justify="center", width=8)
    mastery_table.add_column("Progress", width=28)

    levels = [
        ("🆕 New", stats["new"], "dim"),
        ("📖 Learning", stats["learning"], "yellow"),
        ("🔄 Reviewing", stats["reviewing"], "cyan"),
        ("⭐ Mastered", stats["mastered"], "green"),
    ]

    for label, count, color in levels:
        mastery_table.add_row(
            label,
            str(count),
            _bar(count, stats["total_learned"] if stats["total_learned"] > 0 else 1, color=color),
        )

    console.print(mastery_table)

    # --- Overall progress ---
    console.print(
        f"\n  [bold]Overall:[/bold] {_bar(stats['total_learned'], total_vocab, width=30)}"
        f"  [dim]({stats['total_learned']}/{total_vocab} words encountered)[/dim]"
    )

    # --- Category breakdown ---
    console.print()
    cat_table = Table(
        title="📂 Category Breakdown",
        show_header=True,
        header_style="bold cyan",
        border_style="dim",
        width=55,
    )
    cat_table.add_column("Category", width=30)
    cat_table.add_column("Studied", justify="center", width=10)
    cat_table.add_column("Total", justify="center", width=10)

    for cat_key, cat_desc in CATEGORIES.items():
        cat_vocab = get_vocab_by_category(cat_key)
        studied = sum(1 for v in cat_vocab if v.hanzi in tracker.cards)
        cat_table.add_row(cat_desc.split("—")[0].strip(), str(studied), str(len(cat_vocab)))

    console.print(cat_table)

    # --- Due cards ---
    due = stats["due_now"]
    if due > 0:
        console.print(
            f"\n  [bold yellow]⏰ {due} card(s) due for review![/bold yellow]"
        )
    else:
        console.print(
            "\n  [bold green]✅ No cards due — all caught up![/bold green]"
        )

    console.print()
