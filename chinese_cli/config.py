"""
Configuration system for 龙码 LóngMǎ.

Manages user preferences stored in ~/.chinese-cli/config.json.
Provides sensible defaults for all settings.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


CONFIG_DIR = Path.home() / ".chinese-cli"
CONFIG_FILE = CONFIG_DIR / "config.json"


@dataclass
class AppConfig:
    """Application configuration with sensible defaults."""

    # Display
    language: str = "both"  # "de", "en", "both"

    # Session sizes
    flashcard_session_size: int = 15
    quiz_session_size: int = 10
    review_session_size: int = 20

    # Difficulty
    max_hsk_level: int = 5  # Only show words up to this HSK level
    auto_unlock_hsk: bool = True  # Unlock higher HSK as mastery grows

    # Daily challenge
    show_daily_challenge: bool = True

    # Sound
    sound_enabled: bool = True

    # Session timer
    show_session_timer: bool = True

    def save(self) -> None:
        """Persist config to disk."""
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        CONFIG_FILE.write_text(
            json.dumps(asdict(self), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    @classmethod
    def load(cls) -> "AppConfig":
        """Load config from disk, falling back to defaults."""
        if not CONFIG_FILE.exists():
            return cls()
        try:
            data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
            # Only use known fields, ignore unknown keys
            known = {f.name for f in cls.__dataclass_fields__.values()}
            filtered = {k: v for k, v in data.items() if k in known}
            return cls(**filtered)
        except (json.JSONDecodeError, TypeError):
            return cls()

    def update(self, **kwargs: Any) -> None:
        """Update config values and save."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()
