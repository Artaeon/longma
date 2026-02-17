"""
Pronunciation guide for Mandarin Chinese Pinyin.

Maps every Pinyin initial, final, and tone to approximations in:
- German / Austrian (Mühlviertlerisch where helpful)
- English
- Russian (where relevant)

Designed for a DE/AT native speaker with EN C1 and some Russian.
"""

from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


# ---------------------------------------------------------------------------
# TONE GUIDE
# ---------------------------------------------------------------------------

TONES: list[dict[str, str]] = [
    {
        "tone": "1st — ā (high flat)",
        "symbol": "—",
        "description": "Hold a steady high pitch, like singing a single note.",
        "de_hint": "Wie wenn du beim Arzt 'Aaah' sagst — gleichmäßig hoch.",
        "en_hint": "Like a doctor's 'Ahhh' — flat and high.",
        "example": "mā (妈) = Mama / mother",
    },
    {
        "tone": "2nd — á (rising)",
        "symbol": "↗",
        "description": "Pitch rises from mid to high, like asking a question.",
        "de_hint": "Wie wenn du fragend 'Waaas?' sagst — die Stimme geht rauf.",
        "en_hint": "Like saying 'What?!' with surprise — voice goes up.",
        "example": "má (麻) = Hanf / hemp",
    },
    {
        "tone": "3rd — ǎ (dip)",
        "symbol": "↘↗",
        "description": "Pitch falls then rises — like a valley shape. Goes low, then comes back up.",
        "de_hint": "Wie ein mühlviertlerisches 'Naaaa..ja' — erst runter, dann rauf.",
        "en_hint": "Like a sarcastic 'well...' — the voice dips low then rises.",
        "example": "mǎ (马) = Pferd / horse",
    },
    {
        "tone": "4th — à (falling)",
        "symbol": "↘",
        "description": "Sharp drop from high to low, like a command.",
        "de_hint": "Wie ein bestimmtes 'NEIN!' — kurz und scharf nach unten.",
        "en_hint": "Like shouting 'STOP!' — sharp and decisive downward.",
        "example": "mà (骂) = schimpfen / to scold",
    },
    {
        "tone": "Neutral — a (light)",
        "symbol": "·",
        "description": "Short, unstressed — like a thrown-away syllable.",
        "de_hint": "Wie das 'e' in 'bitte' — kurz und unbetont.",
        "en_hint": "Like the 'a' in 'sofa' — quick and light.",
        "example": "ma (吗) = (question particle)",
    },
]


# ---------------------------------------------------------------------------
# INITIALS (consonants at the start of a syllable)
# ---------------------------------------------------------------------------

INITIALS: list[dict[str, str]] = [
    # --- Easy (same as German/English) ---
    {"pinyin": "b", "ipa": "[p]", "de_approx": "wie 'b' in 'Ball' (unbehaucht)", "en_approx": "like 'b' in 'ball' (unaspirated, closer to 'p')", "note": ""},
    {"pinyin": "p", "ipa": "[pʰ]", "de_approx": "wie 'p' in 'Paar' (mit Luft)", "en_approx": "like 'p' in 'pat' (with a puff of air)", "note": ""},
    {"pinyin": "m", "ipa": "[m]", "de_approx": "wie 'm' in 'Mutter'", "en_approx": "like 'm' in 'mother'", "note": ""},
    {"pinyin": "f", "ipa": "[f]", "de_approx": "wie 'f' in 'Fisch'", "en_approx": "like 'f' in 'fish'", "note": ""},
    {"pinyin": "d", "ipa": "[t]", "de_approx": "wie 'd' in 'Dach' (unbehaucht)", "en_approx": "like 'd' in 'dog' (unaspirated)", "note": ""},
    {"pinyin": "t", "ipa": "[tʰ]", "de_approx": "wie 't' in 'Tisch' (mit Luft)", "en_approx": "like 't' in 'top' (with air puff)", "note": ""},
    {"pinyin": "n", "ipa": "[n]", "de_approx": "wie 'n' in 'Nase'", "en_approx": "like 'n' in 'nose'", "note": ""},
    {"pinyin": "l", "ipa": "[l]", "de_approx": "wie 'l' in 'Licht'", "en_approx": "like 'l' in 'light'", "note": ""},
    {"pinyin": "g", "ipa": "[k]", "de_approx": "wie 'g' in 'gut' (unbehaucht)", "en_approx": "like 'g' in 'go' (unaspirated)", "note": ""},
    {"pinyin": "k", "ipa": "[kʰ]", "de_approx": "wie 'k' in 'Kaffee' (mit Luft)", "en_approx": "like 'k' in 'kite' (with air puff)", "note": ""},
    {"pinyin": "h", "ipa": "[x]", "de_approx": "wie 'ch' in 'ach' oder 'Buch'", "en_approx": "like 'ch' in Scottish 'loch'", "note": "🇦🇹 Im Mühlviertlerischen ähnlich dem 'ch' in 'I moch des'"},

    # --- Moderate ---
    {"pinyin": "j", "ipa": "[tɕ]", "de_approx": "wie 'dj' — Zunge vorne am Gaumen", "en_approx": "like 'j' in 'jeep' but softer, tongue touches palate", "note": ""},
    {"pinyin": "q", "ipa": "[tɕʰ]", "de_approx": "wie 'tch' mit Luft — Zunge vorne", "en_approx": "like 'ch' in 'cheese' with more air", "note": ""},
    {"pinyin": "x", "ipa": "[ɕ]", "de_approx": "wie 'ch' in 'ich' (Vordergaumen!)", "en_approx": "like 'sh' in 'she' but tongue more forward", "note": "🇩🇪 Genau das deutsche 'ich'-ch! Du kannst es schon!"},

    # --- Tricky (retroflexes) ---
    {"pinyin": "zh", "ipa": "[ʈʂ]", "de_approx": "wie 'dsch' — Zunge zurückgerollt", "en_approx": "like 'j' in 'judge' with tongue curled back", "note": "🇷🇺 Ähnlich dem russischen 'ж' (zh), Zunge nach hinten"},
    {"pinyin": "ch", "ipa": "[ʈʂʰ]", "de_approx": "wie 'tsch' mit Luft — Zunge zurück", "en_approx": "like 'ch' in 'church' with tongue curled back", "note": "🇦🇹 Im Dialekt: stell dir ein kräftiges 'Tschüss' vor"},
    {"pinyin": "sh", "ipa": "[ʂ]", "de_approx": "wie 'sch' — aber Zunge rückwärts gebogen", "en_approx": "like 'sh' in 'ship' with tongue curled back", "note": ""},
    {"pinyin": "r", "ipa": "[ɻ]", "de_approx": "zwischen 'r' und 'sch' — Zunge zurück", "en_approx": "like 'r' in 'run' mixed with 'zh'", "note": "🇷🇺 Ähnlich dem weichen russischen 'р/ж' Mix"},

    # --- Flat tongue ---
    {"pinyin": "z", "ipa": "[ts]", "de_approx": "wie 'z' in 'Zug' (genau so!)", "en_approx": "like 'ds' in 'cards'", "note": "🇩🇪 Das kannst du als Deutscher perfekt!"},
    {"pinyin": "c", "ipa": "[tsʰ]", "de_approx": "wie 'z' in 'Zug' aber mit mehr Luft", "en_approx": "like 'ts' in 'cats' with extra air", "note": ""},
    {"pinyin": "s", "ipa": "[s]", "de_approx": "wie 's' in 'Sonne'", "en_approx": "like 's' in 'sun'", "note": ""},

    # --- Special ---
    {"pinyin": "w", "ipa": "[w]", "de_approx": "wie englisches 'w' in 'water'", "en_approx": "like 'w' in 'water'", "note": ""},
    {"pinyin": "y", "ipa": "[j]", "de_approx": "wie 'j' in 'ja'", "en_approx": "like 'y' in 'yes'", "note": "🇩🇪 Genau wie das deutsche 'j'!"},
]


# ---------------------------------------------------------------------------
# FINALS (vowels / endings)
# ---------------------------------------------------------------------------

FINALS: list[dict[str, str]] = [
    {"pinyin": "a", "ipa": "[a]", "de_approx": "wie 'a' in 'Vater'", "en_approx": "like 'a' in 'father'", "note": ""},
    {"pinyin": "o", "ipa": "[o]", "de_approx": "wie 'o' in 'Ofen'", "en_approx": "like 'o' in 'more'", "note": ""},
    {"pinyin": "e", "ipa": "[ɤ]", "de_approx": "wie ein dunkles 'ö' — Mund kaum offen", "en_approx": "like 'u' in 'duh' — mouth barely open", "note": "⚠️ NICHT wie deutsch 'e'! Eher ein tiefes 'öh'"},
    {"pinyin": "i", "ipa": "[i]", "de_approx": "wie 'i' in 'Igel'", "en_approx": "like 'ee' in 'see'", "note": ""},
    {"pinyin": "u", "ipa": "[u]", "de_approx": "wie 'u' in 'Uhr'", "en_approx": "like 'oo' in 'moon'", "note": ""},
    {"pinyin": "ü", "ipa": "[y]", "de_approx": "wie 'ü' in 'über' — DU KANNST DAS!", "en_approx": "no English equivalent — say 'ee' with lips rounded like 'oo'", "note": "🇩🇪🏆 Großer Vorteil! Deutsche können 'ü' bereits perfekt!"},

    {"pinyin": "ai", "ipa": "[ai]", "de_approx": "wie 'ei' in 'Ei'", "en_approx": "like 'eye'", "note": "🇩🇪 Genau wie deutsches 'ei'!"},
    {"pinyin": "ei", "ipa": "[ei]", "de_approx": "wie 'ei' in 'Hey'", "en_approx": "like 'ay' in 'day'", "note": ""},
    {"pinyin": "ao", "ipa": "[au]", "de_approx": "wie 'au' in 'Haus'", "en_approx": "like 'ow' in 'how'", "note": "🇩🇪 Genau wie deutsches 'au'!"},
    {"pinyin": "ou", "ipa": "[ou]", "de_approx": "wie 'ou' in 'Couch' (englisch)", "en_approx": "like 'o' in 'go'", "note": ""},

    {"pinyin": "an", "ipa": "[an]", "de_approx": "wie 'an' in 'Anfang'", "en_approx": "like 'an' in 'fan'", "note": ""},
    {"pinyin": "en", "ipa": "[ən]", "de_approx": "wie 'en' in 'offen'", "en_approx": "like 'un' in 'fun'", "note": ""},
    {"pinyin": "ang", "ipa": "[aŋ]", "de_approx": "wie 'ang' in 'Anfang' + nasales 'ng'", "en_approx": "like 'ong' in 'song' but with 'a'", "note": ""},
    {"pinyin": "eng", "ipa": "[əŋ]", "de_approx": "wie 'äng' — nasales ng am Ende", "en_approx": "like 'ung' in 'lung'", "note": ""},
    {"pinyin": "ong", "ipa": "[uŋ]", "de_approx": "wie 'ung' in 'Ordnung'", "en_approx": "like 'oong'", "note": ""},

    {"pinyin": "ia", "ipa": "[ia]", "de_approx": "wie 'ja' schnell gesprochen", "en_approx": "like 'ya' in 'yacht'", "note": ""},
    {"pinyin": "ie", "ipa": "[iɛ]", "de_approx": "wie 'je' — i + offenes e", "en_approx": "like 'ye' in 'yes'", "note": ""},
    {"pinyin": "iu", "ipa": "[iou]", "de_approx": "wie 'jo' — i + ou", "en_approx": "like 'yo' in 'yoga'", "note": ""},
    {"pinyin": "ian", "ipa": "[iɛn]", "de_approx": "wie 'jen' — i + en", "en_approx": "like 'yen'", "note": ""},
    {"pinyin": "iang", "ipa": "[iaŋ]", "de_approx": "wie 'jang'", "en_approx": "like 'yang'", "note": ""},
    {"pinyin": "ing", "ipa": "[iŋ]", "de_approx": "wie 'ing' in 'Ding'", "en_approx": "like 'ing' in 'sing'", "note": "🇩🇪 Genau gleich!"},
    {"pinyin": "iong", "ipa": "[yŋ]", "de_approx": "wie 'jung' mit gerundeten Lippen", "en_approx": "like 'yoong'", "note": ""},

    {"pinyin": "ua", "ipa": "[ua]", "de_approx": "wie 'wa' in 'Wasser'", "en_approx": "like 'wa' in 'water'", "note": ""},
    {"pinyin": "uo", "ipa": "[uo]", "de_approx": "wie 'wo' in 'wo'", "en_approx": "like 'wo' in 'war'", "note": ""},
    {"pinyin": "ui", "ipa": "[uei]", "de_approx": "wie 'wäi'", "en_approx": "like 'way'", "note": ""},
    {"pinyin": "uan", "ipa": "[uan]", "de_approx": "wie 'wan'", "en_approx": "like 'wan'", "note": ""},
    {"pinyin": "un", "ipa": "[uən]", "de_approx": "wie 'wen' mit rundem Mund", "en_approx": "like 'won'", "note": ""},
    {"pinyin": "uang", "ipa": "[uaŋ]", "de_approx": "wie 'wang'", "en_approx": "like 'wong' with 'a'", "note": ""},

    {"pinyin": "üe", "ipa": "[yɛ]", "de_approx": "wie 'üe' — deutsch 'ü' + offenes 'e'", "en_approx": "say German 'ü' then open to 'eh'", "note": "🇩🇪 Vorteil: du kennst das 'ü' schon!"},
    {"pinyin": "üan", "ipa": "[yan]", "de_approx": "wie 'üen' — ü + en", "en_approx": "like 'you-en' compressed", "note": ""},
    {"pinyin": "ün", "ipa": "[yn]", "de_approx": "wie 'ün' in 'grün'", "en_approx": "like German 'ün' — no English equivalent", "note": "🇩🇪🏆 Genau wie 'grün'!"},

    {"pinyin": "er", "ipa": "[ɐɻ]", "de_approx": "wie 'ar' — Zunge zurückrollen", "en_approx": "like 'ar' in American 'car'", "note": "The famous Beijing 'r' sound"},
]


# ---------------------------------------------------------------------------
# LANGUAGE-ADVANTAGE TIPS  (your secret weapons!)
# ---------------------------------------------------------------------------

LANGUAGE_ADVANTAGES: list[dict[str, str]] = [
    {
        "title": "🏆 German 'ü' = Chinese 'ü'",
        "detail": (
            "The Chinese 'ü' (as in 女 nǚ, 绿 lǜ) is IDENTICAL to the German 'ü' in 'über' or 'grün'.\n"
            "English speakers struggle with this for months. You already have it!\n"
            "Beispiel: 女 (nǚ) = sprich es wie 'nü' in 'Nüsse'."
        ),
    },
    {
        "title": "🏆 German 'ch' = Chinese 'x' and 'h'",
        "detail": (
            "The German 'ich'-Laut (like in 'ich', 'Licht') is very close to Chinese 'x' (as in 学 xué).\n"
            "The German 'ach'-Laut (like in 'Bach', 'Buch') is close to Chinese 'h' (as in 好 hǎo).\n"
            "As a Mühlviertler, you use these daily!"
        ),
    },
    {
        "title": "🏆 German 'z/ts' = Chinese 'z/c'",
        "detail": (
            "Chinese 'z' sounds like German 'z' in 'Zug' — exactly the same [ts] sound!\n"
            "Chinese 'c' is the same but with more air (aspirated), like a sharp 'ts!'.\n"
            "English speakers really struggle here. You don't."
        ),
    },
    {
        "title": "🏆 German 'ei/ai/au' = Chinese 'ei/ai/ao'",
        "detail": (
            "Chinese 'ai' = German 'ei' (like in 'Ei') → 买 mǎi\n"
            "Chinese 'ao' = German 'au' (like in 'Haus') → 好 hǎo\n"
            "These diphthongs are nearly identical!"
        ),
    },
    {
        "title": "🇦🇹 Mühlviertler Advantage: Throat Sounds",
        "detail": (
            "The Mühlviertlerisch dialect uses stronger guttural/throat sounds\n"
            "('I moch des', 'recht', 'nochad') — this muscular habit helps with\n"
            "Chinese 'zh', 'ch', 'sh' retroflexes. Your tongue is already used to\n"
            "working in the back of the mouth!"
        ),
    },
    {
        "title": "🇷🇺 Russian Helps: Retroflex Sounds",
        "detail": (
            "Russian 'ж' (zh) and 'ш' (sh) are similar to Chinese 'zh' and 'sh'.\n"
            "The concept of tongue-curling (retroflex) exists in both languages.\n"
            "If you can say 'жизнь' you're halfway to 'zhī dào' (知道)!"
        ),
    },
    {
        "title": "💡 Tones Are Like Music, Not Grammar",
        "detail": (
            "As a German speaker, you already use pitch patterns:\n"
            "• Questions go UP ↗ ('Wirklich?') → 2nd tone\n"
            "• Commands go DOWN ↘ ('Komm!') → 4th tone\n"
            "• Hesitation dips ↘↗ ('Naaaja...') → 3rd tone\n"
            "You already do this — you just need to make it consistent!"
        ),
    },
]


# ---------------------------------------------------------------------------
# PRONUNCIATION GUIDE FOR INDIVIDUAL WORDS
# ---------------------------------------------------------------------------

def get_pronunciation_guide(pinyin: str) -> str:
    """
    Generate a pronunciation hint for a given pinyin syllable.
    Returns a concise German/English approximation string.
    """
    # Normalize
    clean = pinyin.strip().lower()

    # Find matching initial
    initial_hint = ""
    matched_initial = ""
    for ini in sorted(INITIALS, key=lambda x: -len(x["pinyin"])):
        if clean.startswith(ini["pinyin"]):
            initial_hint = ini["de_approx"]
            matched_initial = ini["pinyin"]
            break

    # Find matching final
    final_hint = ""
    remainder = clean[len(matched_initial):] if matched_initial else clean
    # Strip tone marks for matching
    tone_map = str.maketrans("āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ", "aaaaeeeeiiiioooouuuuüüüü")
    remainder_clean = remainder.translate(tone_map)

    for fin in sorted(FINALS, key=lambda x: -len(x["pinyin"])):
        if remainder_clean.startswith(fin["pinyin"]) or remainder_clean == fin["pinyin"]:
            final_hint = fin["de_approx"]
            break

    parts = []
    if initial_hint:
        parts.append(initial_hint)
    if final_hint:
        parts.append(final_hint)

    return " + ".join(parts) if parts else ""


def _get_tone_from_pinyin(pinyin: str) -> int:
    """Detect which tone a pinyin syllable uses (1-4, 0 for neutral)."""
    tone1 = "āēīōūǖ"
    tone2 = "áéíóúǘ"
    tone3 = "ǎěǐǒǔǚ"
    tone4 = "àèìòùǜ"
    for ch in pinyin:
        if ch in tone1:
            return 1
        if ch in tone2:
            return 2
        if ch in tone3:
            return 3
        if ch in tone4:
            return 4
    return 0


def render_word_pronunciation(hanzi: str, pinyin: str) -> Panel:
    """
    Render a detailed pronunciation panel for a single word.
    Shows the pinyin breakdown with DE/EN approximations and tone info.
    """
    syllables = pinyin.strip().split()
    lines = []

    for syl in syllables:
        tone_num = _get_tone_from_pinyin(syl)
        tone_data = TONES[tone_num - 1] if 1 <= tone_num <= 4 else TONES[4]
        guide = get_pronunciation_guide(syl)

        tone_label = f"[cyan]{tone_data['symbol']}[/cyan] {tone_data['tone'].split('—')[0].strip()}"

        lines.append(
            f"  [bold yellow]{syl}[/bold yellow]  {tone_label}\n"
            f"    🇩🇪 {guide if guide else '[dim]—[/dim]'}\n"
            f"    🗣️  {tone_data['de_hint']}"
        )

    content = "\n\n".join(lines)
    return Panel(
        content,
        title=f"🔊 Aussprache: {hanzi} ({pinyin})",
        border_style="magenta",
        width=65,
        padding=(1, 2),
    )


# ---------------------------------------------------------------------------
# INTERACTIVE PRONUNCIATION MODE
# ---------------------------------------------------------------------------

def show_tone_guide() -> None:
    """Display the complete tone guide."""
    console.print()
    table = Table(
        title="🎵 The Four Tones of Mandarin",
        show_header=True,
        header_style="bold cyan",
        border_style="dim",
        width=80,
    )
    table.add_column("Tone", style="bold", width=18)
    table.add_column("Shape", justify="center", width=6)
    table.add_column("🇩🇪 Deutsch", width=28)
    table.add_column("Example", width=22)

    for t in TONES:
        table.add_row(
            t["tone"],
            t["symbol"],
            t["de_hint"],
            t["example"],
        )

    console.print(table)
    console.print()


def show_initials_guide() -> None:
    """Display consonant pronunciation guide."""
    console.print()

    # Group into sections
    sections = [
        ("Easy — Same in German", INITIALS[:11]),
        ("Moderate — Palatal", INITIALS[11:14]),
        ("Tricky — Retroflex (tongue curled back)", INITIALS[14:18]),
        ("Flat Tongue", INITIALS[18:21]),
        ("Special", INITIALS[21:]),
    ]

    for section_name, items in sections:
        table = Table(
            title=section_name,
            show_header=True,
            header_style="bold cyan",
            border_style="dim",
            width=85,
        )
        table.add_column("Pinyin", style="bold yellow", width=8)
        table.add_column("🇩🇪 Deutsch / 🇦🇹 Österreich", width=35)
        table.add_column("🇬🇧 English", width=30)

        for item in items:
            de_col = item["de_approx"]
            if item["note"]:
                de_col += f"\n[dim]{item['note']}[/dim]"
            table.add_row(item["pinyin"], de_col, item["en_approx"])

        console.print(table)
        console.print()


def show_finals_guide() -> None:
    """Display vowel pronunciation guide."""
    console.print()

    # Group finals
    sections = [
        ("Simple Vowels", FINALS[:6]),
        ("Diphthongs (double vowels)", FINALS[6:10]),
        ("Nasal Endings (-n, -ng)", FINALS[10:15]),
        ("Compound Finals (i-)", FINALS[15:22]),
        ("Compound Finals (u-)", FINALS[22:28]),
        ("Compound Finals (ü-)", FINALS[28:31]),
        ("Special", FINALS[31:]),
    ]

    for section_name, items in sections:
        table = Table(
            title=section_name,
            show_header=True,
            header_style="bold cyan",
            border_style="dim",
            width=85,
        )
        table.add_column("Pinyin", style="bold yellow", width=8)
        table.add_column("🇩🇪 Deutsch / 🇦🇹 Österreich", width=35)
        table.add_column("🇬🇧 English", width=30)

        for item in items:
            de_col = item["de_approx"]
            if item["note"]:
                de_col += f"\n[dim]{item['note']}[/dim]"
            table.add_row(item["pinyin"], de_col, item["en_approx"])

        console.print(table)
        console.print()


def show_advantages() -> None:
    """Show language advantages tips."""
    console.print()
    console.print(
        Panel(
            "[bold]Your Language Superpowers for Chinese! 💪[/bold]\n\n"
            "[dim]Your German, Austrian dialect, and Russian background\n"
            "give you real advantages over English-only learners.[/dim]",
            border_style="green",
            width=65,
        )
    )

    for adv in LANGUAGE_ADVANTAGES:
        console.print(
            Panel(
                adv["detail"],
                title=adv["title"],
                border_style="cyan",
                width=65,
                padding=(1, 2),
            )
        )
    console.print()
