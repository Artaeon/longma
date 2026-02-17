"""
Spaced Repetition System (SM-2 algorithm).

Tracks learning progress per word and determines optimal review intervals.
Progress is persisted to ~/.chinese-cli/progress.json.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DATA_DIR = Path.home() / ".chinese-cli"
PROGRESS_FILE = DATA_DIR / "progress.json"


@dataclass
class CardState:
    """SM-2 state for a single vocabulary card."""

    hanzi: str
    ease_factor: float = 2.5  # E-Factor
    interval: int = 0  # days until next review
    repetitions: int = 0  # consecutive correct answers
    next_review: float = 0.0  # unix timestamp
    total_reviews: int = 0
    correct_reviews: int = 0
    last_reviewed: float = 0.0

    @property
    def is_due(self) -> bool:
        """Check if this card is due for review."""
        return time.time() >= self.next_review

    @property
    def mastery_level(self) -> str:
        """Human-readable mastery level."""
        if self.repetitions == 0:
            return "new"
        elif self.repetitions < 3:
            return "learning"
        elif self.repetitions < 6:
            return "reviewing"
        else:
            return "mastered"

    @property
    def accuracy(self) -> float:
        """Accuracy percentage."""
        if self.total_reviews == 0:
            return 0.0
        return (self.correct_reviews / self.total_reviews) * 100


def _sm2_update(card: CardState, quality: int) -> CardState:
    """
    Apply the SM-2 algorithm.

    quality: 0-5
        0 = complete blackout
        1 = wrong, remembered after seeing answer
        2 = wrong, but answer felt familiar
        3 = correct, with significant difficulty
        4 = correct, with some hesitation
        5 = perfect recall
    """
    card.total_reviews += 1
    card.last_reviewed = time.time()

    if quality >= 3:
        card.correct_reviews += 1
        if card.repetitions == 0:
            card.interval = 1
        elif card.repetitions == 1:
            card.interval = 6
        else:
            card.interval = round(card.interval * card.ease_factor)
        card.repetitions += 1
    else:
        # Reset on failure
        card.repetitions = 0
        card.interval = 1

    # Update ease factor
    card.ease_factor = max(
        1.3,
        card.ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)),
    )

    # Schedule next review
    card.next_review = time.time() + (card.interval * 86400)

    return card


class ProgressTracker:
    """Manages all card states and persists progress to disk."""

    def __init__(self) -> None:
        self.cards: dict[str, CardState] = {}
        self.streak: int = 0
        self.last_session_date: str = ""
        self.total_sessions: int = 0
        self._load()

    def _load(self) -> None:
        """Load progress from disk."""
        if not PROGRESS_FILE.exists():
            return
        try:
            data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
            self.streak = data.get("streak", 0)
            self.last_session_date = data.get("last_session_date", "")
            self.total_sessions = data.get("total_sessions", 0)
            for hanzi, state in data.get("cards", {}).items():
                self.cards[hanzi] = CardState(**state)
        except (json.JSONDecodeError, TypeError, KeyError):
            pass  # Start fresh if corrupt

    def save(self) -> None:
        """Persist progress to disk."""
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        data: dict[str, Any] = {
            "streak": self.streak,
            "last_session_date": self.last_session_date,
            "total_sessions": self.total_sessions,
            "cards": {hanzi: asdict(card) for hanzi, card in self.cards.items()},
        }
        PROGRESS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    def get_card(self, hanzi: str) -> CardState:
        """Get or create a card state for a given hanzi."""
        if hanzi not in self.cards:
            self.cards[hanzi] = CardState(hanzi=hanzi)
        return self.cards[hanzi]

    def review(self, hanzi: str, quality: int) -> CardState:
        """Review a card and update its state. quality: 0-5."""
        card = self.get_card(hanzi)
        _sm2_update(card, quality)
        self._update_streak()
        self.save()
        return card

    def _update_streak(self) -> None:
        """Update the daily streak."""
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        if self.last_session_date != today:
            yesterday = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            if self.last_session_date == yesterday or self.last_session_date == "":
                self.streak += 1
            else:
                # Check if it was actually yesterday
                from datetime import timedelta

                try:
                    last = datetime.strptime(self.last_session_date, "%Y-%m-%d")
                    diff = (datetime.strptime(today, "%Y-%m-%d") - last).days
                    if diff == 1:
                        self.streak += 1
                    elif diff > 1:
                        self.streak = 1
                except ValueError:
                    self.streak = 1
            self.last_session_date = today
            self.total_sessions += 1

    def get_due_cards(self) -> list[str]:
        """Return list of hanzi that are due for review."""
        return [hanzi for hanzi, card in self.cards.items() if card.is_due]

    def get_stats(self) -> dict[str, Any]:
        """Return summary statistics."""
        total = len(self.cards)
        if total == 0:
            return {
                "total_learned": 0,
                "new": 0,
                "learning": 0,
                "reviewing": 0,
                "mastered": 0,
                "due_now": 0,
                "streak": self.streak,
                "total_sessions": self.total_sessions,
                "avg_accuracy": 0.0,
            }

        mastery = {"new": 0, "learning": 0, "reviewing": 0, "mastered": 0}
        total_acc = 0.0
        reviewed_count = 0
        for card in self.cards.values():
            mastery[card.mastery_level] += 1
            if card.total_reviews > 0:
                total_acc += card.accuracy
                reviewed_count += 1

        return {
            "total_learned": total,
            **mastery,
            "due_now": len(self.get_due_cards()),
            "streak": self.streak,
            "total_sessions": self.total_sessions,
            "avg_accuracy": total_acc / reviewed_count if reviewed_count > 0 else 0.0,
        }
