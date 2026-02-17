"""
Character writing hints — radical breakdowns and stroke descriptions.

Provides structural analysis of Chinese characters by decomposing them
into semantic/phonetic components, helping with memorization.
"""

from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


# ---------------------------------------------------------------------------
# Radical Database
# ---------------------------------------------------------------------------

RADICALS: dict[str, dict[str, str]] = {
    # Common standalone radicals
    "人": {"meaning": "Person/Mensch", "pinyin": "rén", "note": "Often appears as 亻 on the left"},
    "口": {"meaning": "Mund/mouth", "pinyin": "kǒu", "note": "Box shape = mouth"},
    "女": {"meaning": "Frau/woman", "pinyin": "nǚ", "note": ""},
    "子": {"meaning": "Kind/child", "pinyin": "zǐ", "note": ""},
    "心": {"meaning": "Herz/heart", "pinyin": "xīn", "note": "Appears as 忄 on the left"},
    "手": {"meaning": "Hand/hand", "pinyin": "shǒu", "note": "Appears as 扌 on the left"},
    "水": {"meaning": "Wasser/water", "pinyin": "shuǐ", "note": "Appears as 氵 on the left"},
    "火": {"meaning": "Feuer/fire", "pinyin": "huǒ", "note": "Appears as 灬 at the bottom"},
    "木": {"meaning": "Baum/tree", "pinyin": "mù", "note": ""},
    "金": {"meaning": "Gold/Metall/metal", "pinyin": "jīn", "note": "Appears as 钅 on the left"},
    "土": {"meaning": "Erde/earth", "pinyin": "tǔ", "note": ""},
    "日": {"meaning": "Sonne/Tag/sun/day", "pinyin": "rì", "note": ""},
    "月": {"meaning": "Mond/Monat/moon/month", "pinyin": "yuè", "note": ""},
    "目": {"meaning": "Auge/eye", "pinyin": "mù", "note": ""},
    "言": {"meaning": "Sprache/speech", "pinyin": "yán", "note": "Appears as 讠 on the left"},
    "走": {"meaning": "gehen/walk", "pinyin": "zǒu", "note": ""},
    "力": {"meaning": "Kraft/power", "pinyin": "lì", "note": ""},
    "大": {"meaning": "groß/big", "pinyin": "dà", "note": "Person with arms spread = big"},
    "小": {"meaning": "klein/small", "pinyin": "xiǎo", "note": ""},
    "中": {"meaning": "Mitte/middle", "pinyin": "zhōng", "note": "Arrow through center"},
    "门": {"meaning": "Tor/gate", "pinyin": "mén", "note": "Traditional: 門"},
    "马": {"meaning": "Pferd/horse", "pinyin": "mǎ", "note": "Traditional: 馬"},
    "车": {"meaning": "Auto/Wagen/vehicle", "pinyin": "chē", "note": "Traditional: 車"},
    "电": {"meaning": "Elektrizität/electricity", "pinyin": "diàn", "note": ""},
    "贝": {"meaning": "Muschel/shell (= money)", "pinyin": "bèi", "note": "Used in money-related chars"},
    "虫": {"meaning": "Insekt/insect", "pinyin": "chóng", "note": ""},
    "竹": {"meaning": "Bambus/bamboo", "pinyin": "zhú", "note": "Appears as ⺮ on top"},
    "丝": {"meaning": "Seide/silk", "pinyin": "sī", "note": "Thread-related characters"},
    "石": {"meaning": "Stein/stone", "pinyin": "shí", "note": ""},
    "页": {"meaning": "Seite/Kopf/page/head", "pinyin": "yè", "note": "Used in face/head characters"},
}


# ---------------------------------------------------------------------------
# Character Decomposition Database
# ---------------------------------------------------------------------------

CHARACTER_HINTS: dict[str, dict[str, str]] = {
    # Basics
    "好": {
        "components": "女 (Frau) + 子 (Kind)",
        "mnemonic": "A woman 女 with a child 子 = GOOD 好. A happy family!",
        "strokes": "6",
    },
    "你": {
        "components": "亻 (Person) + 尔",
        "mnemonic": "A person 亻 standing = YOU 你",
        "strokes": "7",
    },
    "我": {
        "components": "手 (Hand) + 戈 (Hellebarde/halberd)",
        "mnemonic": "A hand wielding a weapon = I/ME 我 (defending myself)",
        "strokes": "7",
    },
    "他": {
        "components": "亻 (Person) + 也 (auch/also)",
        "mnemonic": "Another person = HE 他",
        "strokes": "5",
    },
    "她": {
        "components": "女 (Frau) + 也 (auch/also)",
        "mnemonic": "That woman = SHE 她 (note: 女 for female!)",
        "strokes": "6",
    },
    "大": {
        "components": "一 (eins) + 人 (Person)",
        "mnemonic": "A person with arms spread wide = BIG 大",
        "strokes": "3",
    },
    "小": {
        "components": "⺌ (three drops)",
        "mnemonic": "Small drops falling = SMALL 小",
        "strokes": "3",
    },
    "中": {
        "components": "口 (Mund/box) + 丨 (Strich/line)",
        "mnemonic": "A line through the MIDDLE of a box = MIDDLE/CHINA 中",
        "strokes": "4",
    },

    # Tech
    "电": {
        "components": "日 (Sonne) + 乚 (Haken/hook)",
        "mnemonic": "Sun energy with a wire = ELECTRICITY 电",
        "strokes": "5",
    },
    "脑": {
        "components": "月 (Mond/Körper) + 凶 + 匕",
        "mnemonic": "Body part (月) = BRAIN 脑. 电脑 = 'electric brain' = computer!",
        "strokes": "10",
    },
    "机": {
        "components": "木 (Baum/wood) + 几 (Tisch/table)",
        "mnemonic": "Wooden mechanism = MACHINE 机. 手机 = 'hand machine' = phone!",
        "strokes": "6",
    },
    "网": {
        "components": "冂 (Rahmen/frame) + 㐅㐅",
        "mnemonic": "A frame with crossing threads = NET/NETWORK 网 (like a real net!)",
        "strokes": "6",
    },
    "码": {
        "components": "石 (Stein/stone) + 马 (Pferd/horse)",
        "mnemonic": "Stone markers (counting stones) = CODE 码. 代码 = source code!",
        "strokes": "8",
    },
    "据": {
        "components": "扌 (Hand) + 居 (wohnen/reside)",
        "mnemonic": "Hand grasping facts = DATA 据. 数据 = numerical data!",
        "strokes": "11",
    },
    "件": {
        "components": "亻 (Person) + 牛 (Rind/cow)",
        "mnemonic": "A person handling items = PIECE/SOFTWARE 件. 软件 = software!",
        "strokes": "6",
    },
    "安": {
        "components": "宀 (Dach/roof) + 女 (Frau/woman)",
        "mnemonic": "A woman under a roof = PEACE/SAFE 安. 安全 = security!",
        "strokes": "6",
    },
    "全": {
        "components": "入 (eintreten/enter) + 王 (König/king)",
        "mnemonic": "A king entering = COMPLETE/ALL 全. 安全 = security!",
        "strokes": "6",
    },
    "学": {
        "components": "⺌ + 冖 (Decke/cover) + 子 (Kind/child)",
        "mnemonic": "A child under covers studying = LEARN 学",
        "strokes": "8",
    },
    "习": {
        "components": "冫 + 习",
        "mnemonic": "Wings flapping repeatedly = PRACTICE 习. 学习 = study!",
        "strokes": "3",
    },
    "开": {
        "components": "一 + 廾 (two hands)",
        "mnemonic": "Two hands pushing open = OPEN 开. 开发 = development!",
        "strokes": "4",
    },
    "发": {
        "components": "⺁ + 又 (wieder/again)",
        "mnemonic": "Going out again = SEND/DEVELOP 发. 开发 = development!",
        "strokes": "5",
    },
    "数": {
        "components": "米 (Reis/rice) + 女 (Frau) + 攵 (schlagen/hit)",
        "mnemonic": "Counting grains of rice = NUMBER/COUNT 数. 数据 = data!",
        "strokes": "13",
    },
    "是": {
        "components": "日 (Sonne/sun) + 正 (richtig/correct)",
        "mnemonic": "The sun is correct = IS/YES 是",
        "strokes": "9",
    },
    "不": {
        "components": "一 + 下-like",
        "mnemonic": "A bird trying to fly but can't rise = NOT 不",
        "strokes": "4",
    },
    "要": {
        "components": "覀 (west) + 女 (Frau/woman)",
        "mnemonic": "What you want/need = WANT/NEED 要",
        "strokes": "9",
    },
    "会": {
        "components": "人 (Person) + 云 (Wolke/cloud)",
        "mnemonic": "People gathering like clouds = MEETING/CAN 会. 开会 = hold a meeting!",
        "strokes": "6",
    },
    "工": {
        "components": "Two horizontal lines + vertical",
        "mnemonic": "A carpenter's square = WORK 工. 工程师 = engineer!",
        "strokes": "3",
    },
    "程": {
        "components": "禾 (Getreide/grain) + 呈 (present)",
        "mnemonic": "Measuring grain journey = PROCESS/JOURNEY 程. 编程 = programming!",
        "strokes": "12",
    },
    "请": {
        "components": "讠 (Sprache/speech) + 青 (grün/green/young)",
        "mnemonic": "Words spoken with youthful politeness = PLEASE 请",
        "strokes": "10",
    },
    "看": {
        "components": "手 (Hand) + 目 (Auge/eye)",
        "mnemonic": "Hand over eyes, looking = LOOK/SEE 看",
        "strokes": "9",
    },
    "用": {
        "components": "冂 + 丨丨",
        "mnemonic": "A container being utilized = USE 用. 用户 = user!",
        "strokes": "5",
    },
    "百": {
        "components": "一 (eins/one) + 白 (weiß/white)",
        "mnemonic": "One white (hundred) = HUNDRED 百",
        "strokes": "6",
    },
    "千": {
        "components": "丿 + 十 (zehn/ten)",
        "mnemonic": "Many tens = THOUSAND 千",
        "strokes": "3",
    },
    "万": {
        "components": "Simplified form",
        "mnemonic": "Ten thousand = 万. Traditional is 萬 (much more complex!)",
        "strokes": "3",
    },
    "知": {
        "components": "矢 (Pfeil/arrow) + 口 (Mund/mouth)",
        "mnemonic": "Arrow-fast speech = to KNOW 知. 知道 = to know!",
        "strokes": "8",
    },
    "道": {
        "components": "辶 (gehen/walk) + 首 (Kopf/head)",
        "mnemonic": "Walking with your head (thinking) = WAY/PATH/DAO 道",
        "strokes": "12",
    },
}


def get_character_hint(hanzi: str) -> str | None:
    """Get the decomposition hint for a single character."""
    if hanzi in CHARACTER_HINTS:
        info = CHARACTER_HINTS[hanzi]
        return (
            f"📐 {info['components']}\n"
            f"🧠 {info['mnemonic']}\n"
            f"✏️  {info['strokes']} strokes"
        )
    return None


def render_character_panel(hanzi: str) -> Panel | None:
    """Render a detailed character analysis panel."""
    # Handle multi-character words
    chars = list(hanzi)
    lines: list[str] = []

    for ch in chars:
        if ch in CHARACTER_HINTS:
            info = CHARACTER_HINTS[ch]
            lines.append(
                f"  [bold yellow]{ch}[/bold yellow]  ({info['strokes']} strokes)\n"
                f"    📐 {info['components']}\n"
                f"    🧠 {info['mnemonic']}"
            )
        elif ch in RADICALS:
            rad = RADICALS[ch]
            lines.append(
                f"  [bold yellow]{ch}[/bold yellow]  (Radical)\n"
                f"    📐 {rad['meaning']} ({rad['pinyin']})\n"
                f"    {'💡 ' + rad['note'] if rad['note'] else ''}"
            )

    if not lines:
        return None

    return Panel(
        "\n\n".join(lines),
        title=f"✏️  Zeichenanalyse: {hanzi}",
        border_style="blue",
        width=60,
        padding=(1, 2),
    )


def show_radical_table() -> None:
    """Display the radical reference table."""
    console.print()
    table = Table(
        title="📚 Common Radicals (部首 Bùshǒu)",
        show_header=True,
        header_style="bold cyan",
        border_style="dim",
        width=75,
    )
    table.add_column("Radical", style="bold yellow", justify="center", width=8)
    table.add_column("Pinyin", style="green", width=8)
    table.add_column("Meaning", width=25)
    table.add_column("Note", style="dim", width=30)

    for char, info in RADICALS.items():
        table.add_row(char, info["pinyin"], info["meaning"], info["note"])

    console.print(table)
    console.print()
