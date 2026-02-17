"""
Plugin system for importing custom vocabulary from CSV and JSON files.

Supports:
- CSV files with columns: hanzi, pinyin, english, german, category, hsk_level
- JSON files with array of vocab objects
- Validation and deduplication against existing vocabulary
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from chinese_cli.vocab_data import ALL_VOCAB, VocabEntry

console = Console()

CUSTOM_VOCAB_DIR = Path.home() / ".chinese-cli" / "custom_vocab"


def _validate_entry(data: dict[str, Any]) -> VocabEntry | None:
    """Validate and create a VocabEntry from raw data. Returns None if invalid."""
    required = ["hanzi", "pinyin", "english", "german"]
    for field in required:
        if field not in data or not str(data[field]).strip():
            return None

    return VocabEntry(
        hanzi=str(data["hanzi"]).strip(),
        pinyin=str(data["pinyin"]).strip(),
        english=str(data["english"]).strip(),
        german=str(data["german"]).strip(),
        category=str(data.get("category", "custom")).strip(),
        hsk_level=int(data.get("hsk_level", 1)),
        example_hanzi=str(data.get("example_hanzi", "")).strip(),
        example_pinyin=str(data.get("example_pinyin", "")).strip(),
        example_en=str(data.get("example_en", "")).strip(),
        example_de=str(data.get("example_de", "")).strip(),
        tags=tuple(data.get("tags", ())),
    )


def import_csv(filepath: str | Path) -> list[VocabEntry]:
    """
    Import vocabulary from a CSV file.

    Expected columns: hanzi, pinyin, english, german
    Optional columns: category, hsk_level, example_hanzi, example_pinyin,
                      example_en, example_de
    """
    filepath = Path(filepath)
    if not filepath.exists():
        console.print(f"[red]File not found: {filepath}[/red]")
        return []

    entries: list[VocabEntry] = []
    existing_hanzi = {v.hanzi for v in ALL_VOCAB}
    skipped = 0
    dupes = 0

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("hanzi", "").strip() in existing_hanzi:
                    dupes += 1
                    continue

                entry = _validate_entry(row)
                if entry:
                    entries.append(entry)
                    existing_hanzi.add(entry.hanzi)
                else:
                    skipped += 1

    except (csv.Error, UnicodeDecodeError) as e:
        console.print(f"[red]Error reading CSV: {e}[/red]")
        return []

    console.print(
        Panel(
            f"[bold green]✅ Imported {len(entries)} word(s)[/bold green]\n"
            f"[dim]Skipped: {skipped} invalid, {dupes} duplicates[/dim]",
            border_style="green",
            width=50,
        )
    )
    return entries


def import_json(filepath: str | Path) -> list[VocabEntry]:
    """
    Import vocabulary from a JSON file.

    Expected format: array of objects with hanzi, pinyin, english, german fields.
    """
    filepath = Path(filepath)
    if not filepath.exists():
        console.print(f"[red]File not found: {filepath}[/red]")
        return []

    existing_hanzi = {v.hanzi for v in ALL_VOCAB}
    entries: list[VocabEntry] = []
    skipped = 0
    dupes = 0

    try:
        data = json.loads(filepath.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            console.print("[red]JSON must be an array of objects.[/red]")
            return []

        for item in data:
            if not isinstance(item, dict):
                skipped += 1
                continue

            if item.get("hanzi", "").strip() in existing_hanzi:
                dupes += 1
                continue

            entry = _validate_entry(item)
            if entry:
                entries.append(entry)
                existing_hanzi.add(entry.hanzi)
            else:
                skipped += 1

    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        console.print(f"[red]Error reading JSON: {e}[/red]")
        return []

    console.print(
        Panel(
            f"[bold green]✅ Imported {len(entries)} word(s)[/bold green]\n"
            f"[dim]Skipped: {skipped} invalid, {dupes} duplicates[/dim]",
            border_style="green",
            width=50,
        )
    )
    return entries


def save_custom_vocab(entries: list[VocabEntry]) -> None:
    """Save imported vocabulary to the custom vocab directory."""
    CUSTOM_VOCAB_DIR.mkdir(parents=True, exist_ok=True)
    filepath = CUSTOM_VOCAB_DIR / "custom_words.json"

    # Load existing custom words
    existing: list[dict[str, Any]] = []
    if filepath.exists():
        try:
            existing = json.loads(filepath.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            existing = []

    existing_hanzi = {e.get("hanzi") for e in existing}

    # Add new entries
    for entry in entries:
        if entry.hanzi not in existing_hanzi:
            existing.append({
                "hanzi": entry.hanzi,
                "pinyin": entry.pinyin,
                "english": entry.english,
                "german": entry.german,
                "category": entry.category,
                "hsk_level": entry.hsk_level,
                "example_hanzi": entry.example_hanzi,
                "example_pinyin": entry.example_pinyin,
                "example_en": entry.example_en,
                "example_de": entry.example_de,
            })

    filepath.write_text(
        json.dumps(existing, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    console.print(
        f"  [dim]Saved to {filepath}[/dim]\n"
        f"  [dim]Total custom words: {len(existing)}[/dim]"
    )


def load_custom_vocab() -> list[VocabEntry]:
    """Load custom vocabulary from disk."""
    filepath = CUSTOM_VOCAB_DIR / "custom_words.json"
    if not filepath.exists():
        return []

    try:
        data = json.loads(filepath.read_text(encoding="utf-8"))
        entries = []
        for item in data:
            entry = _validate_entry(item)
            if entry:
                entries.append(entry)
        return entries
    except (json.JSONDecodeError, TypeError):
        return []


def show_import_menu() -> None:
    """Interactive import menu."""
    import questionary

    console.print()
    filepath = questionary.path(
        "Path to vocabulary file (CSV or JSON):",
        style=questionary.Style([
            ("highlighted", "fg:cyan bold"),
            ("answer", "fg:green bold"),
        ]),
    ).ask()

    if not filepath:
        return

    path = Path(filepath)
    if path.suffix.lower() == ".csv":
        entries = import_csv(path)
    elif path.suffix.lower() == ".json":
        entries = import_json(path)
    else:
        console.print("[yellow]Unsupported format. Use .csv or .json[/yellow]")
        return

    if entries:
        save_custom_vocab(entries)

        # Show preview
        table = Table(
            title=f"📦 Imported Words Preview (first 5)",
            show_header=True,
            header_style="bold cyan",
            border_style="dim",
        )
        table.add_column("汉字", style="bold yellow", width=10)
        table.add_column("Pinyin", style="green", width=14)
        table.add_column("Deutsch", width=20)
        table.add_column("English", width=20)

        for entry in entries[:5]:
            table.add_row(entry.hanzi, entry.pinyin, entry.german, entry.english)

        console.print(table)
        console.print()
