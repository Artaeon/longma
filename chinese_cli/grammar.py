"""
Chinese grammar patterns reference.

Essential Mandarin grammar structures with examples,
explanations in German and English.
"""

from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


GRAMMAR_PATTERNS: list[dict[str, str]] = [
    {
        "name": "Subject + Verb + Object (SVO)",
        "pattern": "S + V + O",
        "level": "HSK 1",
        "de_explanation": "Chinesisch hat dieselbe Grundstruktur wie Englisch: Subjekt-Verb-Objekt.",
        "en_explanation": "Chinese follows the same basic word order as English: Subject-Verb-Object.",
        "example_cn": "我学中文。",
        "example_py": "Wǒ xué zhōngwén.",
        "example_de": "Ich lerne Chinesisch.",
        "example_en": "I study Chinese.",
    },
    {
        "name": "是 (shì) — to be",
        "pattern": "A + 是 + B",
        "level": "HSK 1",
        "de_explanation": "'是' funktioniert wie 'sein' — verbindet Subjekt mit Beschreibung/Identität.",
        "en_explanation": "'是' works like 'is/am/are' — links subject to a noun/identity.",
        "example_cn": "我是工程师。",
        "example_py": "Wǒ shì gōngchéngshī.",
        "example_de": "Ich bin Ingenieur.",
        "example_en": "I am an engineer.",
    },
    {
        "name": "不 (bù) — Negation",
        "pattern": "S + 不 + V",
        "level": "HSK 1",
        "de_explanation": "'不' kommt VOR das Verb — wie 'nicht' aber an fixer Position.",
        "en_explanation": "'不' goes BEFORE the verb — like 'not' but always pre-verbal.",
        "example_cn": "我不知道。",
        "example_py": "Wǒ bù zhīdào.",
        "example_de": "Ich weiß nicht.",
        "example_en": "I don't know.",
    },
    {
        "name": "吗 (ma) — Yes/No Questions",
        "pattern": "Statement + 吗？",
        "level": "HSK 1",
        "de_explanation": "Einfach '吗' ans Ende hängen = Frage. Kein Umstellen nötig!",
        "en_explanation": "Just add '吗' to the end of a statement to make it a question. No word order change needed!",
        "example_cn": "你是程序员吗？",
        "example_py": "Nǐ shì chéngxùyuán ma?",
        "example_de": "Bist du Programmierer?",
        "example_en": "Are you a programmer?",
    },
    {
        "name": "了 (le) — Completed Action",
        "pattern": "S + V + 了 + O",
        "level": "HSK 2",
        "de_explanation": "'了' nach dem Verb = Aktion ist abgeschlossen. Ähnlich wie Perfekt.",
        "en_explanation": "'了' after the verb = action is completed. Similar to past tense.",
        "example_cn": "我修复了那个bug。",
        "example_py": "Wǒ xiūfù le nàge bug.",
        "example_de": "Ich habe den Bug behoben.",
        "example_en": "I fixed that bug.",
    },
    {
        "name": "在 (zài) — Action in Progress",
        "pattern": "S + 在 + V",
        "level": "HSK 2",
        "de_explanation": "'在' vor dem Verb = gerade dabei. Wie '-ing' im Englischen.",
        "en_explanation": "'在' before the verb = currently doing. Like '-ing' in English.",
        "example_cn": "我在写代码。",
        "example_py": "Wǒ zài xiě dàimǎ.",
        "example_de": "Ich schreibe gerade Code.",
        "example_en": "I am writing code.",
    },
    {
        "name": "的 (de) — Possession / Description",
        "pattern": "A + 的 + B",
        "level": "HSK 1",
        "de_explanation": "'的' zeigt Besitz oder Beschreibung — wie 's' oder 'von'.",
        "en_explanation": "'的' shows possession or description — like 's' or 'of'.",
        "example_cn": "我的电脑很快。",
        "example_py": "Wǒ de diànnǎo hěn kuài.",
        "example_de": "Mein Computer ist sehr schnell.",
        "example_en": "My computer is very fast.",
    },
    {
        "name": "很 (hěn) — Adjective Predicate",
        "pattern": "S + 很 + Adj",
        "level": "HSK 1",
        "de_explanation": "Adjektive brauchen '很' als Brücke (nicht wirklich 'sehr').",
        "en_explanation": "Adjectives need '很' as a linking word (not really 'very').",
        "example_cn": "这个API很好用。",
        "example_py": "Zhège API hěn hǎoyòng.",
        "example_de": "Diese API ist benutzerfreundlich.",
        "example_en": "This API is user-friendly.",
    },
    {
        "name": "想 (xiǎng) — Want / Think",
        "pattern": "S + 想 + V + O",
        "level": "HSK 2",
        "de_explanation": "'想' = wollen/möchten — kommt vor dem Hauptverb.",
        "en_explanation": "'想' = want/would like — comes before the main verb.",
        "example_cn": "我想学人工智能。",
        "example_py": "Wǒ xiǎng xué réngōng zhìnéng.",
        "example_de": "Ich möchte künstliche Intelligenz lernen.",
        "example_en": "I want to study artificial intelligence.",
    },
    {
        "name": "可以 (kěyǐ) — Permission / Ability",
        "pattern": "S + 可以 + V + O",
        "level": "HSK 2",
        "de_explanation": "'可以' = können/dürfen — wie 'can' oder 'may'.",
        "en_explanation": "'可以' = can/may — expresses permission or ability.",
        "example_cn": "你可以用这个框架。",
        "example_py": "Nǐ kěyǐ yòng zhège kuàngjià.",
        "example_de": "Du kannst dieses Framework verwenden.",
        "example_en": "You can use this framework.",
    },
    {
        "name": "会 (huì) — Learned Ability / Will",
        "pattern": "S + 会 + V",
        "level": "HSK 2",
        "de_explanation": "'会' = können (gelernt) oder Zukunft. Wie 'can' oder 'will'.",
        "en_explanation": "'会' = can (learned skill) or will (future). Context-dependent.",
        "example_cn": "我会写Python。",
        "example_py": "Wǒ huì xiě Python.",
        "example_de": "Ich kann Python schreiben.",
        "example_en": "I can write Python.",
    },
    {
        "name": "把 (bǎ) — Object Manipulation",
        "pattern": "S + 把 + O + V + Result",
        "level": "HSK 3",
        "de_explanation": "'把' bringt das Objekt nach vorne — betont was man damit MACHT.",
        "en_explanation": "'把' brings the object before the verb — emphasizes what happens to it.",
        "example_cn": "把代码提交到Git。",
        "example_py": "Bǎ dàimǎ tíjiāo dào Git.",
        "example_de": "Committe den Code zu Git.",
        "example_en": "Commit the code to Git.",
    },
    {
        "name": "被 (bèi) — Passive Voice",
        "pattern": "S + 被 + (Agent) + V",
        "level": "HSK 3",
        "de_explanation": "'被' = Passiv — wie 'wurde'. Oft negativ konnotiert.",
        "en_explanation": "'被' creates passive voice — like 'was/were'. Often implies negative events.",
        "example_cn": "服务器被黑客攻击了。",
        "example_py": "Fúwùqì bèi hēikè gōngjī le.",
        "example_de": "Der Server wurde von Hackern angegriffen.",
        "example_en": "The server was attacked by hackers.",
    },
    {
        "name": "如果...就 — If...Then",
        "pattern": "如果 + Condition, 就 + Result",
        "level": "HSK 3",
        "de_explanation": "Wenn-Dann Konstruktion. '如果' = wenn, '就' = dann.",
        "en_explanation": "If-then construction. '如果' = if, '就' = then.",
        "example_cn": "如果测试通过，就可以上线。",
        "example_py": "Rúguǒ cèshì tōngguò, jiù kěyǐ shàngxiàn.",
        "example_de": "Wenn die Tests bestehen, kann es live gehen.",
        "example_en": "If the tests pass, it can go live.",
    },
    {
        "name": "虽然...但是 — Although...But",
        "pattern": "虽然 + A, 但是 + B",
        "level": "HSK 3",
        "de_explanation": "Obwohl-Aber. Im Chinesischen braucht man BEIDES!",
        "en_explanation": "Although-but. In Chinese you need BOTH conjunctions!",
        "example_cn": "虽然很难，但是很有趣。",
        "example_py": "Suīrán hěn nán, dànshì hěn yǒuqù.",
        "example_de": "Obwohl es schwer ist, ist es sehr interessant.",
        "example_en": "Although it's hard, it's very interesting.",
    },
]


def show_grammar_patterns(lang: str = "both") -> None:
    """Display the grammar patterns reference."""
    console.print()
    console.print(
        Panel(
            "[bold]📖 Essential Grammar Patterns 语法 (Yǔfǎ)[/bold]\n\n"
            "[dim]15 core patterns from HSK 1–3 that cover\n"
            "most everyday and tech conversation structures.[/dim]",
            border_style="cyan",
            width=65,
        )
    )

    for gp in GRAMMAR_PATTERNS:
        # Build explanation based on lang
        if lang == "de":
            explanation = gp["de_explanation"]
            translation = gp["example_de"]
        elif lang == "en":
            explanation = gp["en_explanation"]
            translation = gp["example_en"]
        else:
            explanation = f"{gp['de_explanation']}\n{gp['en_explanation']}"
            translation = f"{gp['example_de']}  •  {gp['example_en']}"

        console.print(
            Panel(
                f"[bold magenta]{gp['pattern']}[/bold magenta]\n\n"
                f"[white]{explanation}[/white]\n\n"
                f"[bold yellow]{gp['example_cn']}[/bold yellow]\n"
                f"[green]{gp['example_py']}[/green]\n"
                f"[dim]{translation}[/dim]",
                title=f"[bold]{gp['name']}[/bold]  [dim]{gp['level']}[/dim]",
                border_style="cyan",
                width=65,
                padding=(1, 2),
            )
        )
    console.print()
