"""
Vocabulary database for the Chinese learning CLI.

~120 tech-focused Mandarin Chinese words with German and English translations,
organized into categories: basics, tech, business, daily.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class VocabEntry:
    """A single vocabulary word / phrase."""

    hanzi: str
    pinyin: str
    english: str
    german: str
    category: str  # basics | tech | business | daily
    hsk_level: int  # 1-6
    example_hanzi: str = ""
    example_pinyin: str = ""
    example_en: str = ""
    example_de: str = ""
    tags: tuple[str, ...] = ()


# ---------------------------------------------------------------------------
# CATEGORY: BASICS
# ---------------------------------------------------------------------------

_BASICS: list[VocabEntry] = [
    VocabEntry(
        hanzi="你好", pinyin="nǐ hǎo", english="hello", german="Hallo",
        category="basics", hsk_level=1,
        example_hanzi="你好，我是工程师。", example_pinyin="Nǐ hǎo, wǒ shì gōngchéngshī.",
        example_en="Hello, I am an engineer.", example_de="Hallo, ich bin Ingenieur.",
    ),
    VocabEntry(
        hanzi="谢谢", pinyin="xiè xiè", english="thank you", german="Danke",
        category="basics", hsk_level=1,
        example_hanzi="谢谢你的帮助。", example_pinyin="Xiè xiè nǐ de bāngzhù.",
        example_en="Thank you for your help.", example_de="Danke für deine Hilfe.",
    ),
    VocabEntry(
        hanzi="再见", pinyin="zài jiàn", english="goodbye", german="Auf Wiedersehen",
        category="basics", hsk_level=1,
        example_hanzi="明天再见！", example_pinyin="Míngtiān zài jiàn!",
        example_en="See you tomorrow!", example_de="Bis morgen!",
    ),
    VocabEntry(
        hanzi="是", pinyin="shì", english="to be / yes", german="sein / ja",
        category="basics", hsk_level=1,
        example_hanzi="我是程序员。", example_pinyin="Wǒ shì chéngxùyuán.",
        example_en="I am a programmer.", example_de="Ich bin Programmierer.",
    ),
    VocabEntry(
        hanzi="不", pinyin="bù", english="no / not", german="nein / nicht",
        category="basics", hsk_level=1,
        example_hanzi="这不是问题。", example_pinyin="Zhè bù shì wèntí.",
        example_en="This is not a problem.", example_de="Das ist kein Problem.",
    ),
    VocabEntry(
        hanzi="我", pinyin="wǒ", english="I / me", german="ich / mich",
        category="basics", hsk_level=1,
        example_hanzi="我在写代码。", example_pinyin="Wǒ zài xiě dàimǎ.",
        example_en="I am writing code.", example_de="Ich schreibe Code.",
    ),
    VocabEntry(
        hanzi="你", pinyin="nǐ", english="you", german="du",
        category="basics", hsk_level=1,
        example_hanzi="你会编程吗？", example_pinyin="Nǐ huì biānchéng ma?",
        example_en="Can you program?", example_de="Kannst du programmieren?",
    ),
    VocabEntry(
        hanzi="他/她", pinyin="tā", english="he / she", german="er / sie",
        category="basics", hsk_level=1,
        example_hanzi="她是产品经理。", example_pinyin="Tā shì chǎnpǐn jīnglǐ.",
        example_en="She is a product manager.", example_de="Sie ist Produktmanagerin.",
    ),
    VocabEntry(
        hanzi="们", pinyin="men", english="(plural marker)", german="(Plural-Marker)",
        category="basics", hsk_level=1,
        example_hanzi="我们是一个团队。", example_pinyin="Wǒmen shì yī gè tuánduì.",
        example_en="We are a team.", example_de="Wir sind ein Team.",
    ),
    VocabEntry(
        hanzi="什么", pinyin="shén me", english="what", german="was",
        category="basics", hsk_level=1,
        example_hanzi="你做什么工作？", example_pinyin="Nǐ zuò shénme gōngzuò?",
        example_en="What work do you do?", example_de="Was arbeitest du?",
    ),
    VocabEntry(
        hanzi="怎么", pinyin="zěn me", english="how", german="wie",
        category="basics", hsk_level=2,
        example_hanzi="这个怎么用？", example_pinyin="Zhè ge zěnme yòng?",
        example_en="How do you use this?", example_de="Wie benutzt man das?",
    ),
    VocabEntry(
        hanzi="很", pinyin="hěn", english="very", german="sehr",
        category="basics", hsk_level=1,
        example_hanzi="代码很干净。", example_pinyin="Dàimǎ hěn gānjìng.",
        example_en="The code is very clean.", example_de="Der Code ist sehr sauber.",
    ),
    VocabEntry(
        hanzi="好", pinyin="hǎo", english="good", german="gut",
        category="basics", hsk_level=1,
        example_hanzi="这个方案很好。", example_pinyin="Zhè ge fāng'àn hěn hǎo.",
        example_en="This solution is very good.", example_de="Diese Lösung ist sehr gut.",
    ),
    VocabEntry(
        hanzi="大", pinyin="dà", english="big / large", german="groß",
        category="basics", hsk_level=1,
        example_hanzi="大数据很重要。", example_pinyin="Dà shùjù hěn zhòngyào.",
        example_en="Big data is important.", example_de="Big Data ist wichtig.",
    ),
    VocabEntry(
        hanzi="小", pinyin="xiǎo", english="small", german="klein",
        category="basics", hsk_level=1,
        example_hanzi="我们是一个小团队。", example_pinyin="Wǒmen shì yī gè xiǎo tuánduì.",
        example_en="We are a small team.", example_de="Wir sind ein kleines Team.",
    ),
    VocabEntry(
        hanzi="一", pinyin="yī", english="one", german="eins",
        category="basics", hsk_level=1,
        example_hanzi="等一下。", example_pinyin="Děng yīxià.",
        example_en="Wait a moment.", example_de="Warte einen Moment.",
    ),
    VocabEntry(
        hanzi="二", pinyin="èr", english="two", german="zwei",
        category="basics", hsk_level=1,
        example_hanzi="版本二已经发布。", example_pinyin="Bǎnběn èr yǐjīng fābù.",
        example_en="Version two is already released.", example_de="Version zwei ist bereits veröffentlicht.",
    ),
    VocabEntry(
        hanzi="三", pinyin="sān", english="three", german="drei",
        category="basics", hsk_level=1,
        example_hanzi="三个月后发布。", example_pinyin="Sān gè yuè hòu fābù.",
        example_en="Release in three months.", example_de="Veröffentlichung in drei Monaten.",
    ),
    VocabEntry(
        hanzi="十", pinyin="shí", english="ten", german="zehn",
        category="basics", hsk_level=1,
        example_hanzi="我们有十个开发者。", example_pinyin="Wǒmen yǒu shí gè kāifāzhě.",
        example_en="We have ten developers.", example_de="Wir haben zehn Entwickler.",
    ),
    VocabEntry(
        hanzi="百", pinyin="bǎi", english="hundred", german="hundert",
        category="basics", hsk_level=2,
        example_hanzi="有一百个用户。", example_pinyin="Yǒu yī bǎi gè yònghù.",
        example_en="There are one hundred users.", example_de="Es gibt einhundert Nutzer.",
    ),
    VocabEntry(
        hanzi="可以", pinyin="kě yǐ", english="can / may", german="können / dürfen",
        category="basics", hsk_level=2,
        example_hanzi="你可以试一下。", example_pinyin="Nǐ kěyǐ shì yīxià.",
        example_en="You can try it.", example_de="Du kannst es versuchen.",
    ),
    VocabEntry(
        hanzi="想", pinyin="xiǎng", english="want / think", german="wollen / denken",
        category="basics", hsk_level=2,
        example_hanzi="我想学编程。", example_pinyin="Wǒ xiǎng xué biānchéng.",
        example_en="I want to learn programming.", example_de="Ich möchte Programmieren lernen.",
    ),
    VocabEntry(
        hanzi="知道", pinyin="zhī dào", english="to know", german="wissen",
        category="basics", hsk_level=2,
        example_hanzi="我知道怎么修复。", example_pinyin="Wǒ zhīdào zěnme xiūfù.",
        example_en="I know how to fix it.", example_de="Ich weiß, wie man es repariert.",
    ),
    VocabEntry(
        hanzi="时间", pinyin="shí jiān", english="time", german="Zeit",
        category="basics", hsk_level=2,
        example_hanzi="没有时间了。", example_pinyin="Méi yǒu shíjiān le.",
        example_en="There is no more time.", example_de="Es ist keine Zeit mehr.",
    ),
    VocabEntry(
        hanzi="今天", pinyin="jīn tiān", english="today", german="heute",
        category="basics", hsk_level=1,
        example_hanzi="今天发布新版本。", example_pinyin="Jīntiān fābù xīn bǎnběn.",
        example_en="Release new version today.", example_de="Heute wird die neue Version veröffentlicht.",
    ),
    VocabEntry(
        hanzi="明天", pinyin="míng tiān", english="tomorrow", german="morgen",
        category="basics", hsk_level=1,
        example_hanzi="明天有代码审查。", example_pinyin="Míngtiān yǒu dàimǎ shěnchá.",
        example_en="There is a code review tomorrow.", example_de="Morgen gibt es ein Code Review.",
    ),
    VocabEntry(
        hanzi="请", pinyin="qǐng", english="please", german="bitte",
        category="basics", hsk_level=1,
        example_hanzi="请检查代码。", example_pinyin="Qǐng jiǎnchá dàimǎ.",
        example_en="Please check the code.", example_de="Bitte überprüfe den Code.",
    ),
    VocabEntry(
        hanzi="对不起", pinyin="duì bu qǐ", english="sorry", german="Entschuldigung",
        category="basics", hsk_level=1,
        example_hanzi="对不起，我迟到了。", example_pinyin="Duìbuqǐ, wǒ chídào le.",
        example_en="Sorry, I am late.", example_de="Entschuldigung, ich bin zu spät.",
    ),
    VocabEntry(
        hanzi="没关系", pinyin="méi guān xi", english="no problem", german="kein Problem",
        category="basics", hsk_level=1,
        example_hanzi="没关系，我们可以修复。", example_pinyin="Méi guānxi, wǒmen kěyǐ xiūfù.",
        example_en="No problem, we can fix it.", example_de="Kein Problem, wir können es reparieren.",
    ),
    VocabEntry(
        hanzi="学习", pinyin="xué xí", english="to study / learn", german="lernen / studieren",
        category="basics", hsk_level=1,
        example_hanzi="我在学习中文。", example_pinyin="Wǒ zài xuéxí zhōngwén.",
        example_en="I am studying Chinese.", example_de="Ich lerne Chinesisch.",
    ),
]

# ---------------------------------------------------------------------------
# CATEGORY: TECH
# ---------------------------------------------------------------------------

_TECH: list[VocabEntry] = [
    VocabEntry(
        hanzi="电脑", pinyin="diàn nǎo", english="computer", german="Computer",
        category="tech", hsk_level=2,
        example_hanzi="我的电脑很快。", example_pinyin="Wǒ de diànnǎo hěn kuài.",
        example_en="My computer is very fast.", example_de="Mein Computer ist sehr schnell.",
    ),
    VocabEntry(
        hanzi="手机", pinyin="shǒu jī", english="mobile phone", german="Handy",
        category="tech", hsk_level=2,
        example_hanzi="用手机测试应用。", example_pinyin="Yòng shǒujī cèshì yìngyòng.",
        example_en="Test the app on mobile.", example_de="Die App am Handy testen.",
    ),
    VocabEntry(
        hanzi="软件", pinyin="ruǎn jiàn", english="software", german="Software",
        category="tech", hsk_level=4,
        example_hanzi="我们开发软件。", example_pinyin="Wǒmen kāifā ruǎnjiàn.",
        example_en="We develop software.", example_de="Wir entwickeln Software.",
    ),
    VocabEntry(
        hanzi="硬件", pinyin="yìng jiàn", english="hardware", german="Hardware",
        category="tech", hsk_level=4,
        example_hanzi="硬件有问题。", example_pinyin="Yìngjiàn yǒu wèntí.",
        example_en="There is a hardware problem.", example_de="Es gibt ein Hardware-Problem.",
    ),
    VocabEntry(
        hanzi="网络", pinyin="wǎng luò", english="network / internet", german="Netzwerk / Internet",
        category="tech", hsk_level=3,
        example_hanzi="网络连接不稳定。", example_pinyin="Wǎngluò liánjiē bù wěndìng.",
        example_en="The network connection is unstable.", example_de="Die Netzwerkverbindung ist instabil.",
    ),
    VocabEntry(
        hanzi="代码", pinyin="dài mǎ", english="code", german="Code",
        category="tech", hsk_level=4,
        example_hanzi="请检查代码。", example_pinyin="Qǐng jiǎnchá dàimǎ.",
        example_en="Please check the code.", example_de="Bitte überprüfe den Code.",
    ),
    VocabEntry(
        hanzi="编程", pinyin="biān chéng", english="programming", german="Programmierung",
        category="tech", hsk_level=4,
        example_hanzi="编程是我的工作。", example_pinyin="Biānchéng shì wǒ de gōngzuò.",
        example_en="Programming is my job.", example_de="Programmieren ist mein Beruf.",
    ),
    VocabEntry(
        hanzi="程序员", pinyin="chéng xù yuán", english="programmer", german="Programmierer",
        category="tech", hsk_level=4,
        example_hanzi="他是一个好程序员。", example_pinyin="Tā shì yī gè hǎo chéngxùyuán.",
        example_en="He is a good programmer.", example_de="Er ist ein guter Programmierer.",
    ),
    VocabEntry(
        hanzi="工程师", pinyin="gōng chéng shī", english="engineer", german="Ingenieur",
        category="tech", hsk_level=4,
        example_hanzi="软件工程师很忙。", example_pinyin="Ruǎnjiàn gōngchéngshī hěn máng.",
        example_en="Software engineers are busy.", example_de="Software-Ingenieure sind beschäftigt.",
    ),
    VocabEntry(
        hanzi="数据", pinyin="shù jù", english="data", german="Daten",
        category="tech", hsk_level=4,
        example_hanzi="我们需要数据。", example_pinyin="Wǒmen xūyào shùjù.",
        example_en="We need data.", example_de="Wir brauchen Daten.",
    ),
    VocabEntry(
        hanzi="数据库", pinyin="shù jù kù", english="database", german="Datenbank",
        category="tech", hsk_level=5,
        example_hanzi="数据库需要优化。", example_pinyin="Shùjùkù xūyào yōuhuà.",
        example_en="The database needs optimization.", example_de="Die Datenbank muss optimiert werden.",
    ),
    VocabEntry(
        hanzi="服务器", pinyin="fú wù qì", english="server", german="Server",
        category="tech", hsk_level=5,
        example_hanzi="服务器宕机了。", example_pinyin="Fúwùqì dǎngjī le.",
        example_en="The server is down.", example_de="Der Server ist ausgefallen.",
    ),
    VocabEntry(
        hanzi="云计算", pinyin="yún jì suàn", english="cloud computing", german="Cloud Computing",
        category="tech", hsk_level=5,
        example_hanzi="我们用云计算。", example_pinyin="Wǒmen yòng yún jìsuàn.",
        example_en="We use cloud computing.", example_de="Wir nutzen Cloud Computing.",
    ),
    VocabEntry(
        hanzi="人工智能", pinyin="rén gōng zhì néng", english="artificial intelligence (AI)", german="Künstliche Intelligenz (KI)",
        category="tech", hsk_level=5,
        example_hanzi="人工智能改变了世界。", example_pinyin="Rén gōng zhìnéng gǎibiàn le shìjiè.",
        example_en="AI has changed the world.", example_de="KI hat die Welt verändert.",
    ),
    VocabEntry(
        hanzi="机器学习", pinyin="jī qì xué xí", english="machine learning", german="maschinelles Lernen",
        category="tech", hsk_level=5,
        example_hanzi="机器学习需要大数据。", example_pinyin="Jīqì xuéxí xūyào dà shùjù.",
        example_en="Machine learning needs big data.", example_de="Maschinelles Lernen braucht Big Data.",
    ),
    VocabEntry(
        hanzi="算法", pinyin="suàn fǎ", english="algorithm", german="Algorithmus",
        category="tech", hsk_level=5,
        example_hanzi="这个算法很高效。", example_pinyin="Zhè ge suànfǎ hěn gāoxiào.",
        example_en="This algorithm is very efficient.", example_de="Dieser Algorithmus ist sehr effizient.",
    ),
    VocabEntry(
        hanzi="开源", pinyin="kāi yuán", english="open source", german="Open Source",
        category="tech", hsk_level=5,
        example_hanzi="这是一个开源项目。", example_pinyin="Zhè shì yī gè kāiyuán xiàngmù.",
        example_en="This is an open source project.", example_de="Das ist ein Open-Source-Projekt.",
    ),
    VocabEntry(
        hanzi="应用", pinyin="yìng yòng", english="application / app", german="Anwendung / App",
        category="tech", hsk_level=3,
        example_hanzi="这个应用很好用。", example_pinyin="Zhè ge yìngyòng hěn hǎo yòng.",
        example_en="This app is very useful.", example_de="Diese App ist sehr nützlich.",
    ),
    VocabEntry(
        hanzi="网站", pinyin="wǎng zhàn", english="website", german="Webseite",
        category="tech", hsk_level=3,
        example_hanzi="网站上线了。", example_pinyin="Wǎngzhàn shàngxiàn le.",
        example_en="The website is online.", example_de="Die Webseite ist online.",
    ),
    VocabEntry(
        hanzi="下载", pinyin="xià zài", english="to download", german="herunterladen",
        category="tech", hsk_level=3,
        example_hanzi="请下载最新版本。", example_pinyin="Qǐng xiàzài zuìxīn bǎnběn.",
        example_en="Please download the latest version.", example_de="Bitte lade die neueste Version herunter.",
    ),
    VocabEntry(
        hanzi="上传", pinyin="shàng chuán", english="to upload", german="hochladen",
        category="tech", hsk_level=3,
        example_hanzi="上传到服务器。", example_pinyin="Shàngchuán dào fúwùqì.",
        example_en="Upload to the server.", example_de="Auf den Server hochladen.",
    ),
    VocabEntry(
        hanzi="密码", pinyin="mì mǎ", english="password", german="Passwort",
        category="tech", hsk_level=3,
        example_hanzi="请输入密码。", example_pinyin="Qǐng shūrù mìmǎ.",
        example_en="Please enter the password.", example_de="Bitte gib das Passwort ein.",
    ),
    VocabEntry(
        hanzi="安全", pinyin="ān quán", english="security / safe", german="Sicherheit / sicher",
        category="tech", hsk_level=3,
        example_hanzi="网络安全很重要。", example_pinyin="Wǎngluò ānquán hěn zhòngyào.",
        example_en="Cybersecurity is important.", example_de="Cybersicherheit ist wichtig.",
    ),
    VocabEntry(
        hanzi="更新", pinyin="gēng xīn", english="to update", german="aktualisieren",
        category="tech", hsk_level=3,
        example_hanzi="请更新软件。", example_pinyin="Qǐng gēngxīn ruǎnjiàn.",
        example_en="Please update the software.", example_de="Bitte aktualisiere die Software.",
    ),
    VocabEntry(
        hanzi="测试", pinyin="cè shì", english="to test", german="testen",
        category="tech", hsk_level=4,
        example_hanzi="我们需要测试代码。", example_pinyin="Wǒmen xūyào cèshì dàimǎ.",
        example_en="We need to test the code.", example_de="Wir müssen den Code testen.",
    ),
    VocabEntry(
        hanzi="错误", pinyin="cuò wù", english="error / bug", german="Fehler / Bug",
        category="tech", hsk_level=3,
        example_hanzi="代码有一个错误。", example_pinyin="Dàimǎ yǒu yī gè cuòwù.",
        example_en="There is an error in the code.", example_de="Es gibt einen Fehler im Code.",
    ),
    VocabEntry(
        hanzi="修复", pinyin="xiū fù", english="to fix / repair", german="reparieren / beheben",
        category="tech", hsk_level=4,
        example_hanzi="我已经修复了错误。", example_pinyin="Wǒ yǐjīng xiūfù le cuòwù.",
        example_en="I have already fixed the bug.", example_de="Ich habe den Fehler bereits behoben.",
    ),
    VocabEntry(
        hanzi="功能", pinyin="gōng néng", english="feature / function", german="Funktion / Feature",
        category="tech", hsk_level=4,
        example_hanzi="新功能上线了。", example_pinyin="Xīn gōngnéng shàngxiàn le.",
        example_en="The new feature is live.", example_de="Das neue Feature ist live.",
    ),
    VocabEntry(
        hanzi="版本", pinyin="bǎn běn", english="version", german="Version",
        category="tech", hsk_level=4,
        example_hanzi="这是最新版本。", example_pinyin="Zhè shì zuìxīn bǎnběn.",
        example_en="This is the latest version.", example_de="Das ist die neueste Version.",
    ),
    VocabEntry(
        hanzi="接口", pinyin="jiē kǒu", english="API / interface", german="Schnittstelle / API",
        category="tech", hsk_level=5,
        example_hanzi="接口文档在哪里？", example_pinyin="Jiēkǒu wéndàng zài nǎlǐ?",
        example_en="Where is the API documentation?", example_de="Wo ist die API-Dokumentation?",
    ),
    VocabEntry(
        hanzi="前端", pinyin="qián duān", english="frontend", german="Frontend",
        category="tech", hsk_level=5,
        example_hanzi="前端用React。", example_pinyin="Qiánduān yòng React.",
        example_en="The frontend uses React.", example_de="Das Frontend nutzt React.",
    ),
    VocabEntry(
        hanzi="后端", pinyin="hòu duān", english="backend", german="Backend",
        category="tech", hsk_level=5,
        example_hanzi="后端用Python。", example_pinyin="Hòuduān yòng Python.",
        example_en="The backend uses Python.", example_de="Das Backend nutzt Python.",
    ),
    VocabEntry(
        hanzi="框架", pinyin="kuàng jià", english="framework", german="Framework",
        category="tech", hsk_level=5,
        example_hanzi="我们用这个框架。", example_pinyin="Wǒmen yòng zhè ge kuàngjià.",
        example_en="We use this framework.", example_de="Wir nutzen dieses Framework.",
    ),
    VocabEntry(
        hanzi="部署", pinyin="bù shǔ", english="to deploy", german="deployen / bereitstellen",
        category="tech", hsk_level=5,
        example_hanzi="明天部署新版本。", example_pinyin="Míngtiān bùshǔ xīn bǎnběn.",
        example_en="Deploy the new version tomorrow.", example_de="Morgen wird die neue Version deployt.",
    ),
    VocabEntry(
        hanzi="搜索", pinyin="sōu suǒ", english="to search", german="suchen",
        category="tech", hsk_level=3,
        example_hanzi="搜索用户数据。", example_pinyin="Sōusuǒ yònghù shùjù.",
        example_en="Search user data.", example_de="Benutzerdaten suchen.",
    ),
    VocabEntry(
        hanzi="用户", pinyin="yòng hù", english="user", german="Benutzer",
        category="tech", hsk_level=4,
        example_hanzi="用户体验很重要。", example_pinyin="Yònghù tǐyàn hěn zhòngyào.",
        example_en="User experience is important.", example_de="Die Benutzererfahrung ist wichtig.",
    ),
    VocabEntry(
        hanzi="系统", pinyin="xì tǒng", english="system", german="System",
        category="tech", hsk_level=4,
        example_hanzi="系统需要重启。", example_pinyin="Xìtǒng xūyào chóngqǐ.",
        example_en="The system needs a restart.", example_de="Das System muss neu gestartet werden.",
    ),
    VocabEntry(
        hanzi="开发", pinyin="kāi fā", english="to develop", german="entwickeln",
        category="tech", hsk_level=4,
        example_hanzi="我们在开发新产品。", example_pinyin="Wǒmen zài kāifā xīn chǎnpǐn.",
        example_en="We are developing a new product.", example_de="Wir entwickeln ein neues Produkt.",
    ),
    VocabEntry(
        hanzi="技术", pinyin="jì shù", english="technology", german="Technologie",
        category="tech", hsk_level=3,
        example_hanzi="技术发展很快。", example_pinyin="Jìshù fāzhǎn hěn kuài.",
        example_en="Technology develops quickly.", example_de="Technologie entwickelt sich schnell.",
    ),
    VocabEntry(
        hanzi="设计", pinyin="shè jì", english="design", german="Design / Entwurf",
        category="tech", hsk_level=4,
        example_hanzi="UI设计很重要。", example_pinyin="UI shèjì hěn zhòngyào.",
        example_en="UI design is important.", example_de="UI-Design ist wichtig.",
    ),
    VocabEntry(
        hanzi="文档", pinyin="wén dàng", english="document / docs", german="Dokumentation",
        category="tech", hsk_level=4,
        example_hanzi="文档需要更新。", example_pinyin="Wéndàng xūyào gēngxīn.",
        example_en="The docs need updating.", example_de="Die Dokumentation muss aktualisiert werden.",
    ),
    VocabEntry(
        hanzi="调试", pinyin="tiáo shì", english="to debug", german="debuggen",
        category="tech", hsk_level=5,
        example_hanzi="我在调试代码。", example_pinyin="Wǒ zài tiáoshì dàimǎ.",
        example_en="I'm debugging the code.", example_de="Ich debugge den Code.",
    ),
    VocabEntry(
        hanzi="重启", pinyin="chóng qǐ", english="to restart", german="neustarten",
        category="tech", hsk_level=4,
        example_hanzi="请重启服务器。", example_pinyin="Qǐng chóngqǐ fúwùqì.",
        example_en="Please restart the server.", example_de="Bitte starte den Server neu.",
    ),
    VocabEntry(
        hanzi="备份", pinyin="bèi fèn", english="backup", german="Backup / Sicherung",
        category="tech", hsk_level=5,
        example_hanzi="记得备份数据。", example_pinyin="Jìde bèifèn shùjù.",
        example_en="Remember to back up data.", example_de="Vergiss nicht zu sichern.",
    ),
    VocabEntry(
        hanzi="登录", pinyin="dēng lù", english="to log in", german="einloggen",
        category="tech", hsk_level=4,
        example_hanzi="请登录系统。", example_pinyin="Qǐng dēnglù xìtǒng.",
        example_en="Please log in.", example_de="Bitte einloggen.",
    ),
    VocabEntry(
        hanzi="注册", pinyin="zhù cè", english="to register", german="registrieren",
        category="tech", hsk_level=4,
        example_hanzi="请注册一个账户。", example_pinyin="Qǐng zhùcè yī gè zhànghù.",
        example_en="Please register.", example_de="Bitte registrieren.",
    ),
    VocabEntry(
        hanzi="屏幕", pinyin="píng mù", english="screen", german="Bildschirm",
        category="tech", hsk_level=4,
        example_hanzi="屏幕太小了。", example_pinyin="Píngmù tài xiǎo le.",
        example_en="The screen is too small.", example_de="Der Bildschirm ist zu klein.",
    ),
    VocabEntry(
        hanzi="键盘", pinyin="jiàn pán", english="keyboard", german="Tastatur",
        category="tech", hsk_level=4,
        example_hanzi="我需要新键盘。", example_pinyin="Wǒ xūyào xīn jiànpán.",
        example_en="I need a new keyboard.", example_de="Ich brauche eine neue Tastatur.",
    ),
    VocabEntry(
        hanzi="鼠标", pinyin="shǔ biāo", english="mouse (computer)", german="Maus",
        category="tech", hsk_level=4,
        example_hanzi="鼠标坏了。", example_pinyin="Shǔbiāo huài le.",
        example_en="The mouse is broken.", example_de="Die Maus ist kaputt.",
    ),
    VocabEntry(
        hanzi="打印", pinyin="dǎ yìn", english="to print", german="drucken",
        category="tech", hsk_level=4,
        example_hanzi="请打印文件。", example_pinyin="Qǐng dǎyìn wénjiàn.",
        example_en="Please print the document.", example_de="Bitte drucke das Dokument.",
    ),
    VocabEntry(
        hanzi="复制", pinyin="fù zhì", english="to copy", german="kopieren",
        category="tech", hsk_level=4,
        example_hanzi="复制代码。", example_pinyin="Fùzhì dàimǎ.",
        example_en="Copy the code.", example_de="Den Code kopieren.",
    ),
    VocabEntry(
        hanzi="删除", pinyin="shān chú", english="to delete", german="löschen",
        category="tech", hsk_level=4,
        example_hanzi="删除旧文件。", example_pinyin="Shānchú jiù wénjiàn.",
        example_en="Delete old files.", example_de="Alte Dateien löschen.",
    ),
    VocabEntry(
        hanzi="保存", pinyin="bǎo cún", english="to save", german="speichern",
        category="tech", hsk_level=3,
        example_hanzi="保存你的工作。", example_pinyin="Bǎocún nǐ de gōngzuò.",
        example_en="Save your work.", example_de="Speichere deine Arbeit.",
    ),
    VocabEntry(
        hanzi="文件", pinyin="wén jiàn", english="file", german="Datei",
        category="tech", hsk_level=3,
        example_hanzi="打开文件。", example_pinyin="Dǎkāi wénjiàn.",
        example_en="Open the file.", example_de="Öffne die Datei.",
    ),
    VocabEntry(
        hanzi="网页", pinyin="wǎng yè", english="web page", german="Webseite",
        category="tech", hsk_level=3,
        example_hanzi="网页加载很慢。", example_pinyin="Wǎngyè jiāzài hěn màn.",
        example_en="The page loads slowly.", example_de="Die Seite lädt langsam.",
    ),
    VocabEntry(
        hanzi="链接", pinyin="liàn jiē", english="link / URL", german="Link",
        category="tech", hsk_level=4,
        example_hanzi="请发链接。", example_pinyin="Qǐng fā liànjiē.",
        example_en="Please send the link.", example_de="Bitte den Link senden.",
    ),
    VocabEntry(
        hanzi="图片", pinyin="tú piàn", english="image", german="Bild",
        category="tech", hsk_level=3,
        example_hanzi="上传图片。", example_pinyin="Shàngchuán túpiàn.",
        example_en="Upload the image.", example_de="Das Bild hochladen.",
    ),
    VocabEntry(
        hanzi="视频", pinyin="shì pín", english="video", german="Video",
        category="tech", hsk_level=3,
        example_hanzi="看教程视频。", example_pinyin="Kàn jiàochéng shìpín.",
        example_en="Watch a tutorial video.", example_de="Ein Tutorial ansehen.",
    ),
    VocabEntry(
        hanzi="消息", pinyin="xiāo xī", english="message", german="Nachricht",
        category="tech", hsk_level=3,
        example_hanzi="收到一条消息。", example_pinyin="Shōudào yī tiáo xiāoxī.",
        example_en="Received a message.", example_de="Eine Nachricht erhalten.",
    ),
    VocabEntry(
        hanzi="发送", pinyin="fā sòng", english="to send", german="senden",
        category="tech", hsk_level=3,
        example_hanzi="发送邮件。", example_pinyin="Fāsòng yóujiàn.",
        example_en="Send the email.", example_de="Die E-Mail senden.",
    ),
    VocabEntry(
        hanzi="解决", pinyin="jiě jué", english="to solve", german="lösen",
        category="tech", hsk_level=4,
        example_hanzi="问题已经解决。", example_pinyin="Wèntí yǐjīng jiějué.",
        example_en="The problem is solved.", example_de="Das Problem ist gelöst.",
    ),
    VocabEntry(
        hanzi="优化", pinyin="yōu huà", english="to optimize", german="optimieren",
        category="tech", hsk_level=5,
        example_hanzi="优化性能。", example_pinyin="Yōuhuà xìngnéng.",
        example_en="Optimize performance.", example_de="Leistung optimieren.",
    ),
    VocabEntry(
        hanzi="速度", pinyin="sù dù", english="speed", german="Geschwindigkeit",
        category="tech", hsk_level=3,
        example_hanzi="网速太慢了。", example_pinyin="Wǎng sù tài màn le.",
        example_en="Internet speed is too slow.", example_de="Internet ist zu langsam.",
    ),
    VocabEntry(
        hanzi="连接", pinyin="lián jiē", english="connection", german="Verbindung",
        category="tech", hsk_level=4,
        example_hanzi="无法连接服务器。", example_pinyin="Wúfǎ liánjiē fúwùqì.",
        example_en="Cannot connect to server.", example_de="Keine Verbindung zum Server.",
    ),
    VocabEntry(
        hanzi="内存", pinyin="nèi cún", english="memory / RAM", german="Arbeitsspeicher",
        category="tech", hsk_level=5,
        example_hanzi="内存不够。", example_pinyin="Nèicún bú gòu.",
        example_en="Not enough memory.", example_de="Nicht genug Speicher.",
    ),
    VocabEntry(
        hanzi="权限", pinyin="quán xiàn", english="permission", german="Berechtigung",
        category="tech", hsk_level=5,
        example_hanzi="你没有权限。", example_pinyin="Nǐ méiyǒu quánxiàn.",
        example_en="You don't have permission.", example_de="Keine Berechtigung.",
    ),
    VocabEntry(
        hanzi="安装", pinyin="ān zhuāng", english="to install", german="installieren",
        category="tech", hsk_level=4,
        example_hanzi="安装新软件。", example_pinyin="Ānzhuāng xīn ruǎnjiàn.",
        example_en="Install new software.", example_de="Neue Software installieren.",
    ),
    VocabEntry(
        hanzi="卸载", pinyin="xiè zài", english="to uninstall", german="deinstallieren",
        category="tech", hsk_level=5,
        example_hanzi="卸载旧版本。", example_pinyin="Xièzài jiù bǎnběn.",
        example_en="Uninstall old version.", example_de="Alte Version deinstallieren.",
    ),
    VocabEntry(
        hanzi="运行", pinyin="yùn xíng", english="to run / execute", german="ausführen",
        category="tech", hsk_level=4,
        example_hanzi="运行程序。", example_pinyin="Yùnxíng chéngxù.",
        example_en="Run the program.", example_de="Das Programm ausführen.",
    ),
]

# ---------------------------------------------------------------------------
# CATEGORY: BUSINESS
# ---------------------------------------------------------------------------

_BUSINESS: list[VocabEntry] = [
    VocabEntry(
        hanzi="公司", pinyin="gōng sī", english="company", german="Firma / Unternehmen",
        category="business", hsk_level=2,
        example_hanzi="你在哪个公司工作？", example_pinyin="Nǐ zài nǎ ge gōngsī gōngzuò?",
        example_en="Which company do you work at?", example_de="Bei welcher Firma arbeitest du?",
    ),
    VocabEntry(
        hanzi="会议", pinyin="huì yì", english="meeting", german="Besprechung / Meeting",
        category="business", hsk_level=3,
        example_hanzi="下午有会议。", example_pinyin="Xiàwǔ yǒu huìyì.",
        example_en="There is a meeting in the afternoon.", example_de="Am Nachmittag gibt es ein Meeting.",
    ),
    VocabEntry(
        hanzi="项目", pinyin="xiàng mù", english="project", german="Projekt",
        category="business", hsk_level=4,
        example_hanzi="这个项目很大。", example_pinyin="Zhè ge xiàngmù hěn dà.",
        example_en="This project is big.", example_de="Dieses Projekt ist groß.",
    ),
    VocabEntry(
        hanzi="合同", pinyin="hé tong", english="contract", german="Vertrag",
        category="business", hsk_level=4,
        example_hanzi="请签合同。", example_pinyin="Qǐng qiān hétong.",
        example_en="Please sign the contract.", example_de="Bitte unterschreibe den Vertrag.",
    ),
    VocabEntry(
        hanzi="客户", pinyin="kè hù", english="client / customer", german="Kunde / Kundin",
        category="business", hsk_level=4,
        example_hanzi="客户很满意。", example_pinyin="Kèhù hěn mǎnyì.",
        example_en="The client is satisfied.", example_de="Der Kunde ist zufrieden.",
    ),
    VocabEntry(
        hanzi="合作", pinyin="hé zuò", english="cooperation", german="Zusammenarbeit / Kooperation",
        category="business", hsk_level=3,
        example_hanzi="我们需要合作。", example_pinyin="Wǒmen xūyào hézuò.",
        example_en="We need to cooperate.", example_de="Wir müssen zusammenarbeiten.",
    ),
    VocabEntry(
        hanzi="经理", pinyin="jīng lǐ", english="manager", german="Manager / Leiter",
        category="business", hsk_level=3,
        example_hanzi="产品经理在开会。", example_pinyin="Chǎnpǐn jīnglǐ zài kāi huì.",
        example_en="The product manager is in a meeting.", example_de="Der Produktmanager ist in einem Meeting.",
    ),
    VocabEntry(
        hanzi="团队", pinyin="tuán duì", english="team", german="Team",
        category="business", hsk_level=3,
        example_hanzi="我们团队很棒。", example_pinyin="Wǒmen tuánduì hěn bàng.",
        example_en="Our team is great.", example_de="Unser Team ist großartig.",
    ),
    VocabEntry(
        hanzi="市场", pinyin="shì chǎng", english="market", german="Markt",
        category="business", hsk_level=3,
        example_hanzi="中国市场很大。", example_pinyin="Zhōngguó shìchǎng hěn dà.",
        example_en="The Chinese market is big.", example_de="Der chinesische Markt ist groß.",
    ),
    VocabEntry(
        hanzi="投资", pinyin="tóu zī", english="investment", german="Investition",
        category="business", hsk_level=4,
        example_hanzi="我们需要投资。", example_pinyin="Wǒmen xūyào tóuzī.",
        example_en="We need investment.", example_de="Wir brauchen Investitionen.",
    ),
    VocabEntry(
        hanzi="创业", pinyin="chuàng yè", english="to start a business / startup", german="Unternehmensgründung / Startup",
        category="business", hsk_level=4,
        example_hanzi="他在创业。", example_pinyin="Tā zài chuàngyè.",
        example_en="He is starting a business.", example_de="Er gründet ein Unternehmen.",
    ),
    VocabEntry(
        hanzi="产品", pinyin="chǎn pǐn", english="product", german="Produkt",
        category="business", hsk_level=3,
        example_hanzi="产品需要改进。", example_pinyin="Chǎnpǐn xūyào gǎijìn.",
        example_en="The product needs improvement.", example_de="Das Produkt muss verbessert werden.",
    ),
    VocabEntry(
        hanzi="计划", pinyin="jì huà", english="plan", german="Plan",
        category="business", hsk_level=3,
        example_hanzi="我们有一个计划。", example_pinyin="Wǒmen yǒu yī gè jìhuà.",
        example_en="We have a plan.", example_de="Wir haben einen Plan.",
    ),
    VocabEntry(
        hanzi="目标", pinyin="mù biāo", english="goal / target", german="Ziel",
        category="business", hsk_level=4,
        example_hanzi="我们的目标很清楚。", example_pinyin="Wǒmen de mùbiāo hěn qīngchǔ.",
        example_en="Our goal is clear.", example_de="Unser Ziel ist klar.",
    ),
    VocabEntry(
        hanzi="成功", pinyin="chéng gōng", english="success", german="Erfolg",
        category="business", hsk_level=3,
        example_hanzi="项目成功了！", example_pinyin="Xiàngmù chénggōng le!",
        example_en="The project was successful!", example_de="Das Projekt war erfolgreich!",
    ),
    VocabEntry(
        hanzi="失败", pinyin="shī bài", english="failure", german="Misserfolg / Scheitern",
        category="business", hsk_level=4,
        example_hanzi="失败是成功之母。", example_pinyin="Shībài shì chénggōng zhī mǔ.",
        example_en="Failure is the mother of success.", example_de="Scheitern ist die Mutter des Erfolgs.",
    ),
    VocabEntry(
        hanzi="竞争", pinyin="jìng zhēng", english="competition", german="Wettbewerb / Konkurrenz",
        category="business", hsk_level=4,
        example_hanzi="市场竞争很激烈。", example_pinyin="Shìchǎng jìngzhēng hěn jīliè.",
        example_en="Market competition is fierce.", example_de="Der Marktwettbewerb ist hart.",
    ),
    VocabEntry(
        hanzi="方案", pinyin="fāng àn", english="plan / proposal", german="Lösung / Vorschlag",
        category="business", hsk_level=4,
        example_hanzi="这个方案可以。", example_pinyin="Zhè ge fāng'àn kěyǐ.",
        example_en="This proposal works.", example_de="Dieser Vorschlag funktioniert.",
    ),
    VocabEntry(
        hanzi="需求", pinyin="xū qiú", english="requirement / demand", german="Anforderung / Bedarf",
        category="business", hsk_level=4,
        example_hanzi="客户的需求很多。", example_pinyin="Kèhù de xūqiú hěn duō.",
        example_en="The client has many requirements.", example_de="Der Kunde hat viele Anforderungen.",
    ),
    VocabEntry(
        hanzi="报告", pinyin="bào gào", english="report", german="Bericht",
        category="business", hsk_level=3,
        example_hanzi="请写一个报告。", example_pinyin="Qǐng xiě yī gè bàogào.",
        example_en="Please write a report.", example_de="Bitte schreibe einen Bericht.",
    ),
    VocabEntry(
        hanzi="预算", pinyin="yù suàn", english="budget", german="Budget",
        category="business", hsk_level=5,
        example_hanzi="预算不够。", example_pinyin="Yùsuàn bú gòu.",
        example_en="The budget is not enough.", example_de="Das Budget reicht nicht.",
    ),
    VocabEntry(
        hanzi="利润", pinyin="lì rùn", english="profit", german="Gewinn / Profit",
        category="business", hsk_level=5,
        example_hanzi="利润增长了百分之十。", example_pinyin="Lìrùn zēngzhǎng le bǎi fēn zhī shí.",
        example_en="Profit increased by 10%.", example_de="Der Gewinn stieg um 10%.",
    ),
    VocabEntry(
        hanzi="谈判", pinyin="tán pàn", english="negotiation", german="Verhandlung",
        category="business", hsk_level=5,
        example_hanzi="谈判很顺利。", example_pinyin="Tánpàn hěn shùnlì.",
        example_en="The negotiation went smoothly.", example_de="Die Verhandlung verlief reibungslos.",
    ),
    VocabEntry(
        hanzi="邮件", pinyin="yóu jiàn", english="email", german="E-Mail",
        category="business", hsk_level=3,
        example_hanzi="请发邮件给我。", example_pinyin="Qǐng fā yóujiàn gěi wǒ.",
        example_en="Please send me an email.", example_de="Bitte schick mir eine E-Mail.",
    ),
    VocabEntry(
        hanzi="工作", pinyin="gōng zuò", english="work / job", german="Arbeit",
        category="business", hsk_level=1,
        example_hanzi="工作很忙。", example_pinyin="Gōngzuò hěn máng.",
        example_en="Work is very busy.", example_de="Die Arbeit ist sehr stressig.",
    ),
]

# ---------------------------------------------------------------------------
# CATEGORY: DAILY
# ---------------------------------------------------------------------------

_DAILY: list[VocabEntry] = [
    VocabEntry(
        hanzi="吃", pinyin="chī", english="to eat", german="essen",
        category="daily", hsk_level=1,
        example_hanzi="我们去吃饭吧。", example_pinyin="Wǒmen qù chī fàn ba.",
        example_en="Let's go eat.", example_de="Lass uns essen gehen.",
    ),
    VocabEntry(
        hanzi="喝", pinyin="hē", english="to drink", german="trinken",
        category="daily", hsk_level=1,
        example_hanzi="喝杯咖啡吧。", example_pinyin="Hē bēi kāfēi ba.",
        example_en="Let's have a coffee.", example_de="Lass uns einen Kaffee trinken.",
    ),
    VocabEntry(
        hanzi="咖啡", pinyin="kā fēi", english="coffee", german="Kaffee",
        category="daily", hsk_level=2,
        example_hanzi="我要一杯咖啡。", example_pinyin="Wǒ yào yī bēi kāfēi.",
        example_en="I want a cup of coffee.", example_de="Ich möchte einen Kaffee.",
    ),
    VocabEntry(
        hanzi="茶", pinyin="chá", english="tea", german="Tee",
        category="daily", hsk_level=1,
        example_hanzi="中国茶很好喝。", example_pinyin="Zhōngguó chá hěn hǎo hē.",
        example_en="Chinese tea is very tasty.", example_de="Chinesischer Tee schmeckt sehr gut.",
    ),
    VocabEntry(
        hanzi="饭", pinyin="fàn", english="food / rice / meal", german="Essen / Reis / Mahlzeit",
        category="daily", hsk_level=1,
        example_hanzi="午饭吃什么？", example_pinyin="Wǔfàn chī shénme?",
        example_en="What to eat for lunch?", example_de="Was gibt es zum Mittagessen?",
    ),
    VocabEntry(
        hanzi="水", pinyin="shuǐ", english="water", german="Wasser",
        category="daily", hsk_level=1,
        example_hanzi="请给我一杯水。", example_pinyin="Qǐng gěi wǒ yī bēi shuǐ.",
        example_en="Please give me a glass of water.", example_de="Bitte gib mir ein Glas Wasser.",
    ),
    VocabEntry(
        hanzi="钱", pinyin="qián", english="money", german="Geld",
        category="daily", hsk_level=2,
        example_hanzi="多少钱？", example_pinyin="Duōshǎo qián?",
        example_en="How much money?", example_de="Wie viel kostet das?",
    ),
    VocabEntry(
        hanzi="买", pinyin="mǎi", english="to buy", german="kaufen",
        category="daily", hsk_level=2,
        example_hanzi="我想买一个新电脑。", example_pinyin="Wǒ xiǎng mǎi yī gè xīn diànnǎo.",
        example_en="I want to buy a new computer.", example_de="Ich möchte einen neuen Computer kaufen.",
    ),
    VocabEntry(
        hanzi="去", pinyin="qù", english="to go", german="gehen",
        category="daily", hsk_level=1,
        example_hanzi="我去上班。", example_pinyin="Wǒ qù shàng bān.",
        example_en="I go to work.", example_de="Ich gehe zur Arbeit.",
    ),
    VocabEntry(
        hanzi="来", pinyin="lái", english="to come", german="kommen",
        category="daily", hsk_level=1,
        example_hanzi="来我们办公室。", example_pinyin="Lái wǒmen bàngōngshì.",
        example_en="Come to our office.", example_de="Komm in unser Büro.",
    ),
    VocabEntry(
        hanzi="住", pinyin="zhù", english="to live / stay", german="wohnen / leben",
        category="daily", hsk_level=1,
        example_hanzi="你住在哪里？", example_pinyin="Nǐ zhù zài nǎlǐ?",
        example_en="Where do you live?", example_de="Wo wohnst du?",
    ),
    VocabEntry(
        hanzi="出租车", pinyin="chū zū chē", english="taxi", german="Taxi",
        category="daily", hsk_level=2,
        example_hanzi="我们叫出租车吧。", example_pinyin="Wǒmen jiào chūzūchē ba.",
        example_en="Let's call a taxi.", example_de="Lass uns ein Taxi rufen.",
    ),
    VocabEntry(
        hanzi="地铁", pinyin="dì tiě", english="subway / metro", german="U-Bahn",
        category="daily", hsk_level=2,
        example_hanzi="我坐地铁上班。", example_pinyin="Wǒ zuò dìtiě shàng bān.",
        example_en="I take the subway to work.", example_de="Ich fahre mit der U-Bahn zur Arbeit.",
    ),
    VocabEntry(
        hanzi="天气", pinyin="tiān qì", english="weather", german="Wetter",
        category="daily", hsk_level=2,
        example_hanzi="今天天气很好。", example_pinyin="Jīntiān tiānqì hěn hǎo.",
        example_en="The weather is nice today.", example_de="Heute ist das Wetter schön.",
    ),
    VocabEntry(
        hanzi="朋友", pinyin="péng yǒu", english="friend", german="Freund / Freundin",
        category="daily", hsk_level=1,
        example_hanzi="他是我的同事和朋友。", example_pinyin="Tā shì wǒ de tóngshì hé péngyǒu.",
        example_en="He is my colleague and friend.", example_de="Er ist mein Kollege und Freund.",
    ),
    VocabEntry(
        hanzi="家", pinyin="jiā", english="home / family", german="Zuhause / Familie",
        category="daily", hsk_level=1,
        example_hanzi="我在家工作。", example_pinyin="Wǒ zài jiā gōngzuò.",
        example_en="I work from home.", example_de="Ich arbeite von Zuhause.",
    ),
    VocabEntry(
        hanzi="累", pinyin="lèi", english="tired", german="müde",
        category="daily", hsk_level=2,
        example_hanzi="今天很累。", example_pinyin="Jīntiān hěn lèi.",
        example_en="I'm very tired today.", example_de="Heute bin ich sehr müde.",
    ),
    VocabEntry(
        hanzi="忙", pinyin="máng", english="busy", german="beschäftigt",
        category="daily", hsk_level=1,
        example_hanzi="最近很忙。", example_pinyin="Zuìjìn hěn máng.",
        example_en="I've been very busy lately.", example_de="In letzter Zeit bin ich sehr beschäftigt.",
    ),
    VocabEntry(
        hanzi="高兴", pinyin="gāo xìng", english="happy", german="glücklich / froh",
        category="daily", hsk_level=1,
        example_hanzi="认识你很高兴。", example_pinyin="Rènshí nǐ hěn gāoxìng.",
        example_en="Nice to meet you.", example_de="Freut mich, dich kennenzulernen.",
    ),
    VocabEntry(
        hanzi="问题", pinyin="wèn tí", english="question / problem", german="Frage / Problem",
        category="daily", hsk_level=2,
        example_hanzi="有问题吗？", example_pinyin="Yǒu wèntí ma?",
        example_en="Any questions?", example_de="Gibt es Fragen?",
    ),
    VocabEntry(
        hanzi="帮助", pinyin="bāng zhù", english="to help", german="helfen",
        category="daily", hsk_level=2,
        example_hanzi="你能帮助我吗？", example_pinyin="Nǐ néng bāngzhù wǒ ma?",
        example_en="Can you help me?", example_de="Kannst du mir helfen?",
    ),
    VocabEntry(
        hanzi="睡觉", pinyin="shuì jiào", english="to sleep", german="schlafen",
        category="daily", hsk_level=1,
        example_hanzi="我要睡觉了。", example_pinyin="Wǒ yào shuìjiào le.",
        example_en="I'm going to sleep.", example_de="Ich gehe schlafen.",
    ),
    VocabEntry(
        hanzi="早上", pinyin="zǎo shàng", english="morning", german="Morgen / Vormittag",
        category="daily", hsk_level=2,
        example_hanzi="早上有站会。", example_pinyin="Zǎoshàng yǒu zhàn huì.",
        example_en="There is a standup in the morning.", example_de="Am Morgen gibt es ein Standup.",
    ),
    VocabEntry(
        hanzi="晚上", pinyin="wǎn shàng", english="evening", german="Abend",
        category="daily", hsk_level=2,
        example_hanzi="晚上去吃饭。", example_pinyin="Wǎnshàng qù chī fàn.",
        example_en="Let's go eat in the evening.", example_de="Abends gehen wir essen.",
    ),
    VocabEntry(
        hanzi="中国", pinyin="zhōng guó", english="China", german="China",
        category="daily", hsk_level=1,
        example_hanzi="中国的科技发展很快。", example_pinyin="Zhōngguó de kējì fāzhǎn hěn kuài.",
        example_en="China's tech development is fast.", example_de="Chinas Technologieentwicklung ist schnell.",
    ),
    VocabEntry(
        hanzi="年", pinyin="nián", english="year", german="Jahr",
        category="daily", hsk_level=1,
        example_hanzi="明年我去中国。", example_pinyin="Míngnián wǒ qù Zhōngguó.",
        example_en="Next year I go to China.", example_de="Nächstes Jahr gehe ich nach China.",
    ),
    VocabEntry(
        hanzi="月", pinyin="yuè", english="month", german="Monat",
        category="daily", hsk_level=1,
        example_hanzi="一个月后。", example_pinyin="Yī gè yuè hòu.",
        example_en="In one month.", example_de="In einem Monat.",
    ),
    VocabEntry(
        hanzi="星期", pinyin="xīng qī", english="week", german="Woche",
        category="daily", hsk_level=2,
        example_hanzi="这个星期很忙。", example_pinyin="Zhè ge xīngqī hěn máng.",
        example_en="This week is busy.", example_de="Diese Woche ist stressig.",
    ),
    VocabEntry(
        hanzi="小时", pinyin="xiǎo shí", english="hour", german="Stunde",
        category="daily", hsk_level=2,
        example_hanzi="会议要两个小时。", example_pinyin="Huìyì yào liǎng gè xiǎoshí.",
        example_en="The meeting takes two hours.", example_de="Das Meeting dauert zwei Stunden.",
    ),
    VocabEntry(
        hanzi="分钟", pinyin="fēn zhōng", english="minute", german="Minute",
        category="daily", hsk_level=2,
        example_hanzi="请等五分钟。", example_pinyin="Qǐng děng wǔ fēnzhōng.",
        example_en="Please wait five minutes.", example_de="Bitte fünf Minuten warten.",
    ),
    VocabEntry(
        hanzi="昨天", pinyin="zuó tiān", english="yesterday", german="gestern",
        category="daily", hsk_level=1,
        example_hanzi="昨天有bug。", example_pinyin="Zuótiān yǒu bug.",
        example_en="Yesterday there was a bug.", example_de="Gestern gab es einen Bug.",
    ),
    VocabEntry(
        hanzi="现在", pinyin="xiàn zài", english="now", german="jetzt",
        category="daily", hsk_level=1,
        example_hanzi="现在开始吧。", example_pinyin="Xiànzài kāishǐ ba.",
        example_en="Let's start now.", example_de="Fangen wir jetzt an.",
    ),
    VocabEntry(
        hanzi="以后", pinyin="yǐ hòu", english="after / later", german="danach / später",
        category="daily", hsk_level=2,
        example_hanzi="以后再说。", example_pinyin="Yǐhòu zài shuō.",
        example_en="We'll talk later.", example_de="Besprechen wir später.",
    ),
    VocabEntry(
        hanzi="以前", pinyin="yǐ qián", english="before / ago", german="vorher / früher",
        category="daily", hsk_level=2,
        example_hanzi="以前我在维也纳工作。", example_pinyin="Yǐqián wǒ zài Wéiyěnà gōngzuò.",
        example_en="I used to work in Vienna.", example_de="Früher habe ich in Wien gearbeitet.",
    ),
    VocabEntry(
        hanzi="生日", pinyin="shēng rì", english="birthday", german="Geburtstag",
        category="daily", hsk_level=2,
        example_hanzi="生日快乐！", example_pinyin="Shēngrì kuàilè!",
        example_en="Happy birthday!", example_de="Alles Gute zum Geburtstag!",
    ),
    VocabEntry(
        hanzi="医院", pinyin="yī yuàn", english="hospital", german="Krankenhaus",
        category="daily", hsk_level=2,
        example_hanzi="医院在哪里？", example_pinyin="Yīyuàn zài nǎlǐ?",
        example_en="Where is the hospital?", example_de="Wo ist das Krankenhaus?",
    ),
    VocabEntry(
        hanzi="医生", pinyin="yī shēng", english="doctor", german="Arzt / Ärztin",
        category="daily", hsk_level=2,
        example_hanzi="我要看医生。", example_pinyin="Wǒ yào kàn yīshēng.",
        example_en="I need to see a doctor.", example_de="Ich muss zum Arzt.",
    ),
    VocabEntry(
        hanzi="药", pinyin="yào", english="medicine", german="Medizin / Arznei",
        category="daily", hsk_level=3,
        example_hanzi="我需要吃药。", example_pinyin="Wǒ xūyào chī yào.",
        example_en="I need to take medicine.", example_de="Ich muss Medizin nehmen.",
    ),
    VocabEntry(
        hanzi="头疼", pinyin="tóu téng", english="headache", german="Kopfschmerzen",
        category="daily", hsk_level=3,
        example_hanzi="我头疼。", example_pinyin="Wǒ tóuténg.",
        example_en="I have a headache.", example_de="Ich habe Kopfschmerzen.",
    ),
    VocabEntry(
        hanzi="冷", pinyin="lěng", english="cold", german="kalt",
        category="daily", hsk_level=2,
        example_hanzi="今天很冷。", example_pinyin="Jīntiān hěn lěng.",
        example_en="It's cold today.", example_de="Heute ist es kalt.",
    ),
    VocabEntry(
        hanzi="热", pinyin="rè", english="hot", german="heiß",
        category="daily", hsk_level=2,
        example_hanzi="夏天很热。", example_pinyin="Xiàtiān hěn rè.",
        example_en="Summer is hot.", example_de="Der Sommer ist heiß.",
    ),
    VocabEntry(
        hanzi="下雨", pinyin="xià yǔ", english="to rain", german="regnen",
        category="daily", hsk_level=2,
        example_hanzi="明天会下雨。", example_pinyin="Míngtiān huì xià yǔ.",
        example_en="It will rain tomorrow.", example_de="Morgen wird es regnen.",
    ),
    VocabEntry(
        hanzi="漂亮", pinyin="piào liàng", english="beautiful", german="schön / hübsch",
        category="daily", hsk_level=2,
        example_hanzi="维也纳很漂亮。", example_pinyin="Wéiyěnà hěn piàoliàng.",
        example_en="Vienna is beautiful.", example_de="Wien ist wunderschön.",
    ),
    VocabEntry(
        hanzi="快", pinyin="kuài", english="fast / quick", german="schnell",
        category="daily", hsk_level=2,
        example_hanzi="快一点！", example_pinyin="Kuài yīdiǎn!",
        example_en="Hurry up!", example_de="Beeil dich!",
    ),
    VocabEntry(
        hanzi="慢", pinyin="màn", english="slow", german="langsam",
        category="daily", hsk_level=2,
        example_hanzi="请说慢一点。", example_pinyin="Qǐng shuō màn yīdiǎn.",
        example_en="Please speak slower.", example_de="Bitte sprich langsamer.",
    ),
    VocabEntry(
        hanzi="新", pinyin="xīn", english="new", german="neu",
        category="daily", hsk_level=1,
        example_hanzi="新的一年！", example_pinyin="Xīn de yī nián!",
        example_en="New year!", example_de="Neues Jahr!",
    ),
    VocabEntry(
        hanzi="旧", pinyin="jiù", english="old (things)", german="alt (Sachen)",
        category="daily", hsk_level=3,
        example_hanzi="旧电脑太慢了。", example_pinyin="Jiù diànnǎo tài màn le.",
        example_en="The old computer is too slow.", example_de="Der alte Computer ist zu langsam.",
    ),
    VocabEntry(
        hanzi="多少", pinyin="duō shǎo", english="how many / how much", german="wie viel(e)",
        category="daily", hsk_level=1,
        example_hanzi="多少钱？", example_pinyin="Duōshǎo qián?",
        example_en="How much?", example_de="Wie viel?",
    ),
    VocabEntry(
        hanzi="有", pinyin="yǒu", english="to have / there is", german="haben / es gibt",
        category="daily", hsk_level=1,
        example_hanzi="你有时间吗？", example_pinyin="Nǐ yǒu shíjiān ma?",
        example_en="Do you have time?", example_de="Hast du Zeit?",
    ),
    VocabEntry(
        hanzi="没有", pinyin="méi yǒu", english="not have / don't have", german="nicht haben",
        category="daily", hsk_level=1,
        example_hanzi="我没有钱。", example_pinyin="Wǒ méiyǒu qián.",
        example_en="I don't have money.", example_de="Ich habe kein Geld.",
    ),
    VocabEntry(
        hanzi="喜欢", pinyin="xǐ huān", english="to like", german="mögen / gern haben",
        category="daily", hsk_level=2,
        example_hanzi="我喜欢编程。", example_pinyin="Wǒ xǐhuān biānchéng.",
        example_en="I like programming.", example_de="Ich programmiere gern.",
    ),
    VocabEntry(
        hanzi="看", pinyin="kàn", english="to look / watch / read", german="schauen / lesen",
        category="daily", hsk_level=1,
        example_hanzi="看一下代码。", example_pinyin="Kàn yīxià dàimǎ.",
        example_en="Take a look at the code.", example_de="Schau dir den Code an.",
    ),
    VocabEntry(
        hanzi="打电话", pinyin="dǎ diàn huà", english="to make a phone call", german="anrufen / telefonieren",
        category="daily", hsk_level=2,
        example_hanzi="我给你打电话。", example_pinyin="Wǒ gěi nǐ dǎ diànhuà.",
        example_en="I'll call you.", example_de="Ich rufe dich an.",
    ),
    VocabEntry(
        hanzi="上班", pinyin="shàng bān", english="to go to work", german="zur Arbeit gehen",
        category="daily", hsk_level=2,
        example_hanzi="我九点上班。", example_pinyin="Wǒ jiǔ diǎn shàng bān.",
        example_en="I go to work at 9.", example_de="Ich gehe um 9 Uhr zur Arbeit.",
    ),
    VocabEntry(
        hanzi="下班", pinyin="xià bān", english="to get off work", german="Feierabend machen",
        category="daily", hsk_level=2,
        example_hanzi="六点下班。", example_pinyin="Liù diǎn xià bān.",
        example_en="Get off work at 6.", example_de="Um 6 Uhr Feierabend.",
    ),
    VocabEntry(
        hanzi="休息", pinyin="xiū xī", english="to rest", german="sich ausruhen",
        category="daily", hsk_level=2,
        example_hanzi="休息一下吧。", example_pinyin="Xiūxī yīxià ba.",
        example_en="Take a break.", example_de="Mach mal Pause.",
    ),
    VocabEntry(
        hanzi="运动", pinyin="yùn dòng", english="sports / exercise", german="Sport / Bewegung",
        category="daily", hsk_level=2,
        example_hanzi="我每天运动。", example_pinyin="Wǒ měitiān yùndòng.",
        example_en="I exercise every day.", example_de="Ich treibe jeden Tag Sport.",
    ),
    VocabEntry(
        hanzi="跑步", pinyin="pǎo bù", english="to jog / run", german="joggen / laufen",
        category="daily", hsk_level=3,
        example_hanzi="早上跑步。", example_pinyin="Zǎoshàng pǎobù.",
        example_en="Go jogging in the morning.", example_de="Morgens joggen gehen.",
    ),
    VocabEntry(
        hanzi="游泳", pinyin="yóu yǒng", english="to swim", german="schwimmen",
        category="daily", hsk_level=3,
        example_hanzi="我喜欢游泳。", example_pinyin="Wǒ xǐhuān yóuyǒng.",
        example_en="I like swimming.", example_de="Ich schwimme gern.",
    ),
    VocabEntry(
        hanzi="电影", pinyin="diàn yǐng", english="movie / film", german="Film / Kino",
        category="daily", hsk_level=2,
        example_hanzi="晚上看电影。", example_pinyin="Wǎnshàng kàn diànyǐng.",
        example_en="Watch a movie tonight.", example_de="Abends einen Film schauen.",
    ),
    VocabEntry(
        hanzi="音乐", pinyin="yīn yuè", english="music", german="Musik",
        category="daily", hsk_level=2,
        example_hanzi="我喜欢听音乐。", example_pinyin="Wǒ xǐhuān tīng yīnyuè.",
        example_en="I like listening to music.", example_de="Ich höre gern Musik.",
    ),
    VocabEntry(
        hanzi="超市", pinyin="chāo shì", english="supermarket", german="Supermarkt",
        category="daily", hsk_level=2,
        example_hanzi="去超市买东西。", example_pinyin="Qù chāoshì mǎi dōngxi.",
        example_en="Go shopping at the supermarket.", example_de="Im Supermarkt einkaufen gehen.",
    ),
    VocabEntry(
        hanzi="银行", pinyin="yín háng", english="bank", german="Bank",
        category="daily", hsk_level=2,
        example_hanzi="银行在哪里？", example_pinyin="Yínháng zài nǎlǐ?",
        example_en="Where is the bank?", example_de="Wo ist die Bank?",
    ),
    VocabEntry(
        hanzi="手", pinyin="shǒu", english="hand", german="Hand",
        category="daily", hsk_level=2,
        example_hanzi="洗手。", example_pinyin="Xǐ shǒu.",
        example_en="Wash your hands.", example_de="Hände waschen.",
    ),
    VocabEntry(
        hanzi="眼睛", pinyin="yǎn jīng", english="eye(s)", german="Auge(n)",
        category="daily", hsk_level=2,
        example_hanzi="眼睛很累。", example_pinyin="Yǎnjīng hěn lèi.",
        example_en="My eyes are tired.", example_de="Meine Augen sind müde.",
    ),
    VocabEntry(
        hanzi="身体", pinyin="shēn tǐ", english="body / health", german="Körper / Gesundheit",
        category="daily", hsk_level=2,
        example_hanzi="身体很重要。", example_pinyin="Shēntǐ hěn zhòngyào.",
        example_en="Health is important.", example_de="Gesundheit ist wichtig.",
    ),
    VocabEntry(
        hanzi="四", pinyin="sì", english="four", german="vier",
        category="daily", hsk_level=1,
        example_hanzi="四个人。", example_pinyin="Sì gè rén.",
        example_en="Four people.", example_de="Vier Personen.",
    ),
    VocabEntry(
        hanzi="五", pinyin="wǔ", english="five", german="fünf",
        category="daily", hsk_level=1,
        example_hanzi="五分钟。", example_pinyin="Wǔ fēnzhōng.",
        example_en="Five minutes.", example_de="Fünf Minuten.",
    ),
    VocabEntry(
        hanzi="六", pinyin="liù", english="six", german="sechs",
        category="daily", hsk_level=1,
        example_hanzi="六点下班。", example_pinyin="Liù diǎn xià bān.",
        example_en="Get off at 6.", example_de="Um 6 Uhr Feierabend.",
    ),
    VocabEntry(
        hanzi="七", pinyin="qī", english="seven", german="sieben",
        category="daily", hsk_level=1,
        example_hanzi="一个星期七天。", example_pinyin="Yī gè xīngqī qī tiān.",
        example_en="Seven days in a week.", example_de="Eine Woche hat sieben Tage.",
    ),
    VocabEntry(
        hanzi="八", pinyin="bā", english="eight", german="acht",
        category="daily", hsk_level=1,
        example_hanzi="八是吉利数字。", example_pinyin="Bā shì jílì shùzì.",
        example_en="Eight is a lucky number.", example_de="Acht ist eine Glückszahl.",
    ),
    VocabEntry(
        hanzi="九", pinyin="jiǔ", english="nine", german="neun",
        category="daily", hsk_level=1,
        example_hanzi="九点上班。", example_pinyin="Jiǔ diǎn shàng bān.",
        example_en="Start work at 9.", example_de="Um 9 Uhr Arbeitsbeginn.",
    ),
    VocabEntry(
        hanzi="零", pinyin="líng", english="zero", german="null",
        category="daily", hsk_level=2,
        example_hanzi="返回零。", example_pinyin="Fǎnhuí líng.",
        example_en="Return zero.", example_de="Null zurückgeben.",
    ),
    VocabEntry(
        hanzi="千", pinyin="qiān", english="thousand", german="tausend",
        category="daily", hsk_level=3,
        example_hanzi="一千个用户。", example_pinyin="Yī qiān gè yònghù.",
        example_en="One thousand users.", example_de="Eintausend Benutzer.",
    ),
    VocabEntry(
        hanzi="万", pinyin="wàn", english="ten thousand", german="zehntausend",
        category="daily", hsk_level=3,
        example_hanzi="一万行代码。", example_pinyin="Yī wàn háng dàimǎ.",
        example_en="Ten thousand lines of code.", example_de="Zehntausend Zeilen Code.",
    ),
    VocabEntry(
        hanzi="穿", pinyin="chuān", english="to wear", german="tragen / anziehen",
        category="daily", hsk_level=2,
        example_hanzi="穿什么好？", example_pinyin="Chuān shénme hǎo?",
        example_en="What should I wear?", example_de="Was soll ich anziehen?",
    ),
    VocabEntry(
        hanzi="衣服", pinyin="yī fú", english="clothes", german="Kleidung",
        category="daily", hsk_level=2,
        example_hanzi="买新衣服。", example_pinyin="Mǎi xīn yīfú.",
        example_en="Buy new clothes.", example_de="Neue Kleidung kaufen.",
    ),
    VocabEntry(
        hanzi="生气", pinyin="shēng qì", english="angry", german="wütend / verärgert",
        category="daily", hsk_level=3,
        example_hanzi="别生气。", example_pinyin="Bié shēngqì.",
        example_en="Don't be angry.", example_de="Sei nicht wütend.",
    ),
    VocabEntry(
        hanzi="开心", pinyin="kāi xīn", english="happy / joyful", german="fröhlich / glücklich",
        category="daily", hsk_level=2,
        example_hanzi="今天很开心。", example_pinyin="Jīntiān hěn kāixīn.",
        example_en="I'm happy today.", example_de="Heute bin ich fröhlich.",
    ),
    VocabEntry(
        hanzi="难过", pinyin="nán guò", english="sad", german="traurig",
        category="daily", hsk_level=3,
        example_hanzi="别难过。", example_pinyin="Bié nánguò.",
        example_en="Don't be sad.", example_de="Sei nicht traurig.",
    ),
    VocabEntry(
        hanzi="害怕", pinyin="hài pà", english="afraid / scared", german="Angst haben",
        category="daily", hsk_level=3,
        example_hanzi="别害怕。", example_pinyin="Bié hàipà.",
        example_en="Don't be afraid.", example_de="Hab keine Angst.",
    ),
    VocabEntry(
        hanzi="聪明", pinyin="cōng míng", english="smart / clever", german="klug / intelligent",
        category="daily", hsk_level=3,
        example_hanzi="这个孩子很聪明。", example_pinyin="Zhè ge háizi hěn cōngmíng.",
        example_en="This child is very smart.", example_de="Dieses Kind ist sehr klug.",
    ),
    VocabEntry(
        hanzi="重要", pinyin="zhòng yào", english="important", german="wichtig",
        category="daily", hsk_level=2,
        example_hanzi="这很重要。", example_pinyin="Zhè hěn zhòngyào.",
        example_en="This is important.", example_de="Das ist wichtig.",
    ),
    VocabEntry(
        hanzi="简单", pinyin="jiǎn dān", english="simple / easy", german="einfach",
        category="daily", hsk_level=3,
        example_hanzi="这个问题很简单。", example_pinyin="Zhè ge wèntí hěn jiǎndān.",
        example_en="This problem is simple.", example_de="Dieses Problem ist einfach.",
    ),
    VocabEntry(
        hanzi="难", pinyin="nán", english="difficult / hard", german="schwer / schwierig",
        category="daily", hsk_level=3,
        example_hanzi="中文很难。", example_pinyin="Zhōngwén hěn nán.",
        example_en="Chinese is difficult.", example_de="Chinesisch ist schwer.",
    ),
    VocabEntry(
        hanzi="容易", pinyin="róng yì", english="easy", german="leicht / einfach",
        category="daily", hsk_level=3,
        example_hanzi="Python很容易学。", example_pinyin="Python hěn róngyì xué.",
        example_en="Python is easy to learn.", example_de="Python ist leicht zu lernen.",
    ),
]

# ---------------------------------------------------------------------------
# CATEGORY: TRAVEL
# ---------------------------------------------------------------------------

_TRAVEL: list[VocabEntry] = [
    VocabEntry(
        hanzi="飞机", pinyin="fēi jī", english="airplane", german="Flugzeug",
        category="travel", hsk_level=2,
        example_hanzi="我坐飞机去北京。", example_pinyin="Wǒ zuò fēijī qù Běijīng.",
        example_en="I fly to Beijing.", example_de="Ich fliege nach Peking.",
    ),
    VocabEntry(
        hanzi="机场", pinyin="jī chǎng", english="airport", german="Flughafen",
        category="travel", hsk_level=3,
        example_hanzi="机场在哪里？", example_pinyin="Jīchǎng zài nǎlǐ?",
        example_en="Where is the airport?", example_de="Wo ist der Flughafen?",
    ),
    VocabEntry(
        hanzi="火车", pinyin="huǒ chē", english="train", german="Zug",
        category="travel", hsk_level=2,
        example_hanzi="我坐火车去上海。", example_pinyin="Wǒ zuò huǒchē qù Shànghǎi.",
        example_en="I take the train to Shanghai.", example_de="Ich fahre mit dem Zug nach Shanghai.",
    ),
    VocabEntry(
        hanzi="火车站", pinyin="huǒ chē zhàn", english="train station", german="Bahnhof",
        category="travel", hsk_level=2,
        example_hanzi="火车站很近。", example_pinyin="Huǒchēzhàn hěn jìn.",
        example_en="The train station is nearby.", example_de="Der Bahnhof ist in der Nähe.",
    ),
    VocabEntry(
        hanzi="酒店", pinyin="jiǔ diàn", english="hotel", german="Hotel",
        category="travel", hsk_level=3,
        example_hanzi="酒店在市中心。", example_pinyin="Jiǔdiàn zài shì zhōngxīn.",
        example_en="The hotel is in the city center.", example_de="Das Hotel ist im Stadtzentrum.",
    ),
    VocabEntry(
        hanzi="护照", pinyin="hù zhào", english="passport", german="Reisepass",
        category="travel", hsk_level=3,
        example_hanzi="请出示护照。", example_pinyin="Qǐng chūshì hùzhào.",
        example_en="Please show your passport.", example_de="Bitte zeigen Sie den Reisepass.",
    ),
    VocabEntry(
        hanzi="签证", pinyin="qiān zhèng", english="visa", german="Visum",
        category="travel", hsk_level=4,
        example_hanzi="我需要签证。", example_pinyin="Wǒ xūyào qiānzhèng.",
        example_en="I need a visa.", example_de="Ich brauche ein Visum.",
    ),
    VocabEntry(
        hanzi="地图", pinyin="dì tú", english="map", german="Karte / Landkarte",
        category="travel", hsk_level=3,
        example_hanzi="你有地图吗？", example_pinyin="Nǐ yǒu dìtú ma?",
        example_en="Do you have a map?", example_de="Hast du eine Karte?",
    ),
    VocabEntry(
        hanzi="旅行", pinyin="lǚ xíng", english="to travel / trip", german="reisen / Reise",
        category="travel", hsk_level=3,
        example_hanzi="我喜欢旅行。", example_pinyin="Wǒ xǐhuān lǚxíng.",
        example_en="I like traveling.", example_de="Ich reise gern.",
    ),
    VocabEntry(
        hanzi="左", pinyin="zuǒ", english="left", german="links",
        category="travel", hsk_level=2,
        example_hanzi="往左转。", example_pinyin="Wǎng zuǒ zhuǎn.",
        example_en="Turn left.", example_de="Biegen Sie links ab.",
    ),
    VocabEntry(
        hanzi="右", pinyin="yòu", english="right", german="rechts",
        category="travel", hsk_level=2,
        example_hanzi="往右走。", example_pinyin="Wǎng yòu zǒu.",
        example_en="Go right.", example_de="Gehen Sie nach rechts.",
    ),
    VocabEntry(
        hanzi="远", pinyin="yuǎn", english="far", german="weit",
        category="travel", hsk_level=2,
        example_hanzi="很远吗？", example_pinyin="Hěn yuǎn ma?",
        example_en="Is it far?", example_de="Ist es weit?",
    ),
    VocabEntry(
        hanzi="近", pinyin="jìn", english="near", german="nah",
        category="travel", hsk_level=2,
        example_hanzi="很近，走路五分钟。", example_pinyin="Hěn jìn, zǒulù wǔ fēnzhōng.",
        example_en="Very near, 5 minutes walk.", example_de="Sehr nah, 5 Minuten zu Fuß.",
    ),
    VocabEntry(
        hanzi="路", pinyin="lù", english="road / way", german="Straße / Weg",
        category="travel", hsk_level=2,
        example_hanzi="这条路怎么走？", example_pinyin="Zhè tiáo lù zěnme zǒu?",
        example_en="How to get to this road?", example_de="Wie komme ich zu dieser Straße?",
    ),
    VocabEntry(
        hanzi="行李", pinyin="xíng lǐ", english="luggage", german="Gepäck",
        category="travel", hsk_level=3,
        example_hanzi="我的行李在哪？", example_pinyin="Wǒ de xínglǐ zài nǎ?",
        example_en="Where is my luggage?", example_de="Wo ist mein Gepäck?",
    ),
    VocabEntry(
        hanzi="票", pinyin="piào", english="ticket", german="Ticket / Fahrkarte",
        category="travel", hsk_level=2,
        example_hanzi="买两张票。", example_pinyin="Mǎi liǎng zhāng piào.",
        example_en="Buy two tickets.", example_de="Zwei Tickets kaufen.",
    ),
    VocabEntry(
        hanzi="北京", pinyin="běi jīng", english="Beijing", german="Peking",
        category="travel", hsk_level=1,
        example_hanzi="北京是中国的首都。", example_pinyin="Běijīng shì Zhōngguó de shǒudū.",
        example_en="Beijing is China's capital.", example_de="Peking ist die Hauptstadt Chinas.",
    ),
    VocabEntry(
        hanzi="上海", pinyin="shàng hǎi", english="Shanghai", german="Shanghai",
        category="travel", hsk_level=1,
        example_hanzi="上海是科技中心。", example_pinyin="Shànghǎi shì kējì zhōngxīn.",
        example_en="Shanghai is a tech hub.", example_de="Shanghai ist ein Tech-Zentrum.",
    ),
    VocabEntry(
        hanzi="深圳", pinyin="shēn zhèn", english="Shenzhen", german="Shenzhen",
        category="travel", hsk_level=3,
        example_hanzi="深圳是硬件之都。", example_pinyin="Shēnzhèn shì yìngjiàn zhī dū.",
        example_en="Shenzhen is the hardware capital.", example_de="Shenzhen ist die Hardware-Hauptstadt.",
    ),
    VocabEntry(
        hanzi="公交车", pinyin="gōng jiāo chē", english="bus", german="Bus",
        category="travel", hsk_level=2,
        example_hanzi="坐公交车去公司。", example_pinyin="Zuò gōngjiāochē qù gōngsī.",
        example_en="Take the bus to the company.", example_de="Den Bus zur Firma nehmen.",
    ),
    VocabEntry(
        hanzi="打车", pinyin="dǎ chē", english="take a taxi / ride-hail", german="Taxi nehmen",
        category="travel", hsk_level=3,
        example_hanzi="我们打车去吧。", example_pinyin="Wǒmen dǎchē qù ba.",
        example_en="Let's take a taxi.", example_de="Lass uns ein Taxi nehmen.",
    ),
    VocabEntry(
        hanzi="走", pinyin="zǒu", english="to walk / go", german="gehen / laufen",
        category="travel", hsk_level=1,
        example_hanzi="我们走吧！", example_pinyin="Wǒmen zǒu ba!",
        example_en="Let's go!", example_de="Gehen wir!",
    ),
    VocabEntry(
        hanzi="到", pinyin="dào", english="to arrive", german="ankommen",
        category="travel", hsk_level=2,
        example_hanzi="我到了。", example_pinyin="Wǒ dào le.",
        example_en="I've arrived.", example_de="Ich bin angekommen.",
    ),
    VocabEntry(
        hanzi="哪里", pinyin="nǎ lǐ", english="where", german="wo",
        category="travel", hsk_level=1,
        example_hanzi="厕所在哪里？", example_pinyin="Cèsuǒ zài nǎlǐ?",
        example_en="Where is the toilet?", example_de="Wo ist die Toilette?",
    ),
    VocabEntry(
        hanzi="这里", pinyin="zhè lǐ", english="here", german="hier",
        category="travel", hsk_level=1,
        example_hanzi="我在这里。", example_pinyin="Wǒ zài zhèlǐ.",
        example_en="I'm here.", example_de="Ich bin hier.",
    ),
    VocabEntry(
        hanzi="那里", pinyin="nà lǐ", english="there", german="dort",
        category="travel", hsk_level=1,
        example_hanzi="在那里等我。", example_pinyin="Zài nàlǐ děng wǒ.",
        example_en="Wait for me there.", example_de="Warte dort auf mich.",
    ),
    VocabEntry(
        hanzi="回", pinyin="huí", english="to return", german="zurückkehren",
        category="travel", hsk_level=2,
        example_hanzi="我明天回奥地利。", example_pinyin="Wǒ míngtiān huí Àodìlì.",
        example_en="I return to Austria tomorrow.", example_de="Morgen kehre ich nach Österreich zurück.",
    ),
    VocabEntry(
        hanzi="高铁", pinyin="gāo tiě", english="high-speed rail", german="Hochgeschwindigkeitszug",
        category="travel", hsk_level=4,
        example_hanzi="中国的高铁很快。", example_pinyin="Zhōngguó de gāotiě hěn kuài.",
        example_en="China's high-speed rail is very fast.", example_de="Chinas Hochgeschwindigkeitszug ist sehr schnell.",
    ),
    VocabEntry(
        hanzi="安检", pinyin="ān jiǎn", english="security check", german="Sicherheitskontrolle",
        category="travel", hsk_level=4,
        example_hanzi="请过安检。", example_pinyin="Qǐng guò ānjiǎn.",
        example_en="Please go through security.", example_de="Bitte gehen Sie durch die Sicherheitskontrolle.",
    ),
    VocabEntry(
        hanzi="换", pinyin="huàn", english="to change / exchange", german="wechseln / tauschen",
        category="travel", hsk_level=3,
        example_hanzi="在哪里换钱？", example_pinyin="Zài nǎlǐ huàn qián?",
        example_en="Where can I exchange money?", example_de="Wo kann ich Geld wechseln?",
    ),
]

# ---------------------------------------------------------------------------
# CATEGORY: RESTAURANT
# ---------------------------------------------------------------------------

_RESTAURANT: list[VocabEntry] = [
    VocabEntry(
        hanzi="菜单", pinyin="cài dān", english="menu", german="Speisekarte",
        category="restaurant", hsk_level=3,
        example_hanzi="请给我菜单。", example_pinyin="Qǐng gěi wǒ càidān.",
        example_en="Please give me the menu.", example_de="Bitte geben Sie mir die Speisekarte.",
    ),
    VocabEntry(
        hanzi="点菜", pinyin="diǎn cài", english="to order food", german="bestellen",
        category="restaurant", hsk_level=3,
        example_hanzi="我想点菜。", example_pinyin="Wǒ xiǎng diǎncài.",
        example_en="I'd like to order.", example_de="Ich möchte bestellen.",
    ),
    VocabEntry(
        hanzi="好吃", pinyin="hǎo chī", english="delicious", german="lecker",
        category="restaurant", hsk_level=2,
        example_hanzi="这个菜很好吃！", example_pinyin="Zhè ge cài hěn hǎochī!",
        example_en="This dish is delicious!", example_de="Dieses Gericht ist lecker!",
    ),
    VocabEntry(
        hanzi="辣", pinyin="là", english="spicy", german="scharf",
        category="restaurant", hsk_level=3,
        example_hanzi="不要太辣。", example_pinyin="Bú yào tài là.",
        example_en="Not too spicy please.", example_de="Nicht zu scharf bitte.",
    ),
    VocabEntry(
        hanzi="米饭", pinyin="mǐ fàn", english="rice", german="Reis",
        category="restaurant", hsk_level=2,
        example_hanzi="来一碗米饭。", example_pinyin="Lái yī wǎn mǐfàn.",
        example_en="One bowl of rice please.", example_de="Eine Schüssel Reis bitte.",
    ),
    VocabEntry(
        hanzi="面条", pinyin="miàn tiáo", english="noodles", german="Nudeln",
        category="restaurant", hsk_level=3,
        example_hanzi="我要一碗面条。", example_pinyin="Wǒ yào yī wǎn miàntiáo.",
        example_en="I want a bowl of noodles.", example_de="Ich hätte gerne eine Schüssel Nudeln.",
    ),
    VocabEntry(
        hanzi="饺子", pinyin="jiǎo zi", english="dumplings", german="Teigtaschen",
        category="restaurant", hsk_level=3,
        example_hanzi="来一盘饺子。", example_pinyin="Lái yī pán jiǎozi.",
        example_en="One plate of dumplings.", example_de="Einen Teller Teigtaschen bitte.",
    ),
    VocabEntry(
        hanzi="鸡肉", pinyin="jī ròu", english="chicken", german="Hühnerfleisch",
        category="restaurant", hsk_level=3,
        example_hanzi="我要鸡肉。", example_pinyin="Wǒ yào jīròu.",
        example_en="I want chicken.", example_de="Ich möchte Hühnerfleisch.",
    ),
    VocabEntry(
        hanzi="牛肉", pinyin="niú ròu", english="beef", german="Rindfleisch",
        category="restaurant", hsk_level=3,
        example_hanzi="牛肉面很好吃。", example_pinyin="Niúròu miàn hěn hǎochī.",
        example_en="Beef noodles are delicious.", example_de="Rindfleischnudeln sind lecker.",
    ),
    VocabEntry(
        hanzi="鱼", pinyin="yú", english="fish", german="Fisch",
        category="restaurant", hsk_level=2,
        example_hanzi="我喜欢吃鱼。", example_pinyin="Wǒ xǐhuān chī yú.",
        example_en="I like eating fish.", example_de="Ich esse gerne Fisch.",
    ),
    VocabEntry(
        hanzi="蔬菜", pinyin="shū cài", english="vegetables", german="Gemüse",
        category="restaurant", hsk_level=3,
        example_hanzi="多吃蔬菜。", example_pinyin="Duō chī shūcài.",
        example_en="Eat more vegetables.", example_de="Iss mehr Gemüse.",
    ),
    VocabEntry(
        hanzi="啤酒", pinyin="pí jiǔ", english="beer", german="Bier",
        category="restaurant", hsk_level=3,
        example_hanzi="来两杯啤酒。", example_pinyin="Lái liǎng bēi píjiǔ.",
        example_en="Two beers please.", example_de="Zwei Bier bitte.",
    ),
    VocabEntry(
        hanzi="买单", pinyin="mǎi dān", english="check / bill", german="Rechnung",
        category="restaurant", hsk_level=3,
        example_hanzi="服务员，买单！", example_pinyin="Fúwùyuán, mǎidān!",
        example_en="Waiter, the check please!", example_de="Kellner, die Rechnung bitte!",
    ),
    VocabEntry(
        hanzi="服务员", pinyin="fú wù yuán", english="waiter / waitress", german="Kellner / Kellnerin",
        category="restaurant", hsk_level=3,
        example_hanzi="服务员，请过来。", example_pinyin="Fúwùyuán, qǐng guòlái.",
        example_en="Waiter, please come here.", example_de="Kellner, kommen Sie bitte her.",
    ),
    VocabEntry(
        hanzi="筷子", pinyin="kuài zi", english="chopsticks", german="Stäbchen / Essstäbchen",
        category="restaurant", hsk_level=3,
        example_hanzi="你会用筷子吗？", example_pinyin="Nǐ huì yòng kuàizi ma?",
        example_en="Can you use chopsticks?", example_de="Kannst du Stäbchen benutzen?",
    ),
    VocabEntry(
        hanzi="杯子", pinyin="bēi zi", english="cup / glass", german="Tasse / Glas",
        category="restaurant", hsk_level=2,
        example_hanzi="请给我一个杯子。", example_pinyin="Qǐng gěi wǒ yī gè bēizi.",
        example_en="Please give me a cup.", example_de="Bitte geben Sie mir eine Tasse.",
    ),
    VocabEntry(
        hanzi="甜", pinyin="tián", english="sweet", german="süß",
        category="restaurant", hsk_level=3,
        example_hanzi="这个蛋糕很甜。", example_pinyin="Zhè ge dàngāo hěn tián.",
        example_en="This cake is very sweet.", example_de="Dieser Kuchen ist sehr süß.",
    ),
    VocabEntry(
        hanzi="咸", pinyin="xián", english="salty", german="salzig",
        category="restaurant", hsk_level=4,
        example_hanzi="有点咸。", example_pinyin="Yǒudiǎn xián.",
        example_en="A bit salty.", example_de="Ein bisschen salzig.",
    ),
    VocabEntry(
        hanzi="酸", pinyin="suān", english="sour", german="sauer",
        category="restaurant", hsk_level=4,
        example_hanzi="酸辣汤很好喝。", example_pinyin="Suānlà tāng hěn hǎohē.",
        example_en="Hot and sour soup is great.", example_de="Saure scharfe Suppe ist sehr gut.",
    ),
    VocabEntry(
        hanzi="素食", pinyin="sù shí", english="vegetarian food", german="vegetarisches Essen",
        category="restaurant", hsk_level=4,
        example_hanzi="有素食吗？", example_pinyin="Yǒu sùshí ma?",
        example_en="Do you have vegetarian food?", example_de="Haben Sie vegetarisches Essen?",
    ),
    VocabEntry(
        hanzi="外卖", pinyin="wài mài", english="food delivery / takeout", german="Lieferung / Takeaway",
        category="restaurant", hsk_level=3,
        example_hanzi="点外卖吧。", example_pinyin="Diǎn wàimài ba.",
        example_en="Let's order delivery.", example_de="Lass uns etwas bestellen.",
    ),
    VocabEntry(
        hanzi="炒", pinyin="chǎo", english="to stir-fry", german="braten / anbraten",
        category="restaurant", hsk_level=3,
        example_hanzi="炒饭还是炒面？", example_pinyin="Chǎofàn háishì chǎomiàn?",
        example_en="Fried rice or fried noodles?", example_de="Gebratener Reis oder gebratene Nudeln?",
    ),
    VocabEntry(
        hanzi="汤", pinyin="tāng", english="soup", german="Suppe",
        category="restaurant", hsk_level=3,
        example_hanzi="我要一碗汤。", example_pinyin="Wǒ yào yī wǎn tāng.",
        example_en="I want a bowl of soup.", example_de="Ich möchte eine Schüssel Suppe.",
    ),
    VocabEntry(
        hanzi="火锅", pinyin="huǒ guō", english="hot pot", german="Feuertopf / Hot Pot",
        category="restaurant", hsk_level=4,
        example_hanzi="我们去吃火锅吧！", example_pinyin="Wǒmen qù chī huǒguō ba!",
        example_en="Let's go eat hot pot!", example_de="Lass uns Hot Pot essen gehen!",
    ),
    VocabEntry(
        hanzi="豆腐", pinyin="dòu fu", english="tofu", german="Tofu",
        category="restaurant", hsk_level=3,
        example_hanzi="麻婆豆腐很辣。", example_pinyin="Mápó dòufu hěn là.",
        example_en="Mapo tofu is very spicy.", example_de="Mapo Tofu ist sehr scharf.",
    ),
    VocabEntry(
        hanzi="包子", pinyin="bāo zi", english="steamed bun", german="Dampfbrötchen",
        category="restaurant", hsk_level=3,
        example_hanzi="早餐吃包子。", example_pinyin="Zǎocān chī bāozi.",
        example_en="Eat buns for breakfast.", example_de="Zum Frühstück Dampfbrötchen essen.",
    ),
    VocabEntry(
        hanzi="味道", pinyin="wèi dào", english="taste / flavor", german="Geschmack",
        category="restaurant", hsk_level=3,
        example_hanzi="味道怎么样？", example_pinyin="Wèidào zěnmeyàng?",
        example_en="How does it taste?", example_de="Wie schmeckt es?",
    ),
    VocabEntry(
        hanzi="饱", pinyin="bǎo", english="full (stomach)", german="satt",
        category="restaurant", hsk_level=3,
        example_hanzi="我吃饱了。", example_pinyin="Wǒ chī bǎo le.",
        example_en="I'm full.", example_de="Ich bin satt.",
    ),
    VocabEntry(
        hanzi="饿", pinyin="è", english="hungry", german="hungrig",
        category="restaurant", hsk_level=2,
        example_hanzi="我很饿。", example_pinyin="Wǒ hěn è.",
        example_en="I'm very hungry.", example_de="Ich bin sehr hungrig.",
    ),
    VocabEntry(
        hanzi="盘", pinyin="pán", english="plate / dish", german="Teller / Platte",
        category="restaurant", hsk_level=3,
        example_hanzi="一盘炒饭。", example_pinyin="Yī pán chǎofàn.",
        example_en="A plate of fried rice.", example_de="Ein Teller gebratener Reis.",
    ),
]

# ---------------------------------------------------------------------------
# CATEGORY: UNIVERSITY / EDUCATION
# ---------------------------------------------------------------------------

_UNIVERSITY: list[VocabEntry] = [
    VocabEntry(
        hanzi="大学", pinyin="dà xué", english="university", german="Universität",
        category="university", hsk_level=2,
        example_hanzi="我在大学学习计算机。", example_pinyin="Wǒ zài dàxué xuéxí jìsuànjī.",
        example_en="I study computer science at university.", example_de="Ich studiere Informatik an der Universität.",
    ),
    VocabEntry(
        hanzi="老师", pinyin="lǎo shī", english="teacher", german="Lehrer / Lehrerin",
        category="university", hsk_level=1,
        example_hanzi="老师教得很好。", example_pinyin="Lǎoshī jiāo de hěn hǎo.",
        example_en="The teacher teaches well.", example_de="Der Lehrer unterrichtet gut.",
    ),
    VocabEntry(
        hanzi="学生", pinyin="xué shēng", english="student", german="Student / Schüler",
        category="university", hsk_level=1,
        example_hanzi="我是大学生。", example_pinyin="Wǒ shì dàxuéshēng.",
        example_en="I am a university student.", example_de="Ich bin Student.",
    ),
    VocabEntry(
        hanzi="考试", pinyin="kǎo shì", english="exam / test", german="Prüfung / Klausur",
        category="university", hsk_level=2,
        example_hanzi="明天有考试。", example_pinyin="Míngtiān yǒu kǎoshì.",
        example_en="There is an exam tomorrow.", example_de="Morgen gibt es eine Prüfung.",
    ),
    VocabEntry(
        hanzi="毕业", pinyin="bì yè", english="to graduate", german="abschließen / graduieren",
        category="university", hsk_level=4,
        example_hanzi="我明年毕业。", example_pinyin="Wǒ míngnián bìyè.",
        example_en="I graduate next year.", example_de="Ich mache nächstes Jahr meinen Abschluss.",
    ),
    VocabEntry(
        hanzi="教室", pinyin="jiào shì", english="classroom", german="Klassenzimmer / Hörsaal",
        category="university", hsk_level=2,
        example_hanzi="教室在二楼。", example_pinyin="Jiàoshì zài èr lóu.",
        example_en="The classroom is on the second floor.", example_de="Das Klassenzimmer ist im zweiten Stock.",
    ),
    VocabEntry(
        hanzi="图书馆", pinyin="tú shū guǎn", english="library", german="Bibliothek",
        category="university", hsk_level=3,
        example_hanzi="我在图书馆学习。", example_pinyin="Wǒ zài túshūguǎn xuéxí.",
        example_en="I study at the library.", example_de="Ich lerne in der Bibliothek.",
    ),
    VocabEntry(
        hanzi="作业", pinyin="zuò yè", english="homework / assignment", german="Hausaufgabe / Aufgabe",
        category="university", hsk_level=2,
        example_hanzi="今天的作业很多。", example_pinyin="Jīntiān de zuòyè hěn duō.",
        example_en="There is a lot of homework today.", example_de="Heute gibt es viele Hausaufgaben.",
    ),
    VocabEntry(
        hanzi="课", pinyin="kè", english="class / lesson", german="Unterricht / Kurs",
        category="university", hsk_level=2,
        example_hanzi="下午有课。", example_pinyin="Xiàwǔ yǒu kè.",
        example_en="There are classes in the afternoon.", example_de="Am Nachmittag gibt es Unterricht.",
    ),
    VocabEntry(
        hanzi="专业", pinyin="zhuān yè", english="major / specialty", german="Fach / Studiengang",
        category="university", hsk_level=4,
        example_hanzi="我的专业是计算机。", example_pinyin="Wǒ de zhuānyè shì jìsuànjī.",
        example_en="My major is computer science.", example_de="Mein Studiengang ist Informatik.",
    ),
    VocabEntry(
        hanzi="研究", pinyin="yán jiū", english="research", german="Forschung / forschen",
        category="university", hsk_level=4,
        example_hanzi="他在研究人工智能。", example_pinyin="Tā zài yánjiū réngōng zhìnéng.",
        example_en="He is researching AI.", example_de="Er forscht an KI.",
    ),
    VocabEntry(
        hanzi="论文", pinyin="lùn wén", english="thesis / paper", german="Arbeit / Aufsatz",
        category="university", hsk_level=5,
        example_hanzi="我在写论文。", example_pinyin="Wǒ zài xiě lùnwén.",
        example_en="I am writing my thesis.", example_de="Ich schreibe meine Arbeit.",
    ),
    VocabEntry(
        hanzi="教授", pinyin="jiào shòu", english="professor", german="Professor",
        category="university", hsk_level=4,
        example_hanzi="教授讲得很清楚。", example_pinyin="Jiàoshòu jiǎng de hěn qīngchǔ.",
        example_en="The professor explains clearly.", example_de="Der Professor erklärt klar.",
    ),
    VocabEntry(
        hanzi="计算机", pinyin="jì suàn jī", english="computer (formal)", german="Rechner / Computer",
        category="university", hsk_level=3,
        example_hanzi="计算机科学很有趣。", example_pinyin="Jìsuànjī kēxué hěn yǒuqù.",
        example_en="Computer science is interesting.", example_de="Informatik ist interessant.",
    ),
    VocabEntry(
        hanzi="数学", pinyin="shù xué", english="mathematics", german="Mathematik",
        category="university", hsk_level=3,
        example_hanzi="数学是编程的基础。", example_pinyin="Shùxué shì biānchéng de jīchǔ.",
        example_en="Math is the foundation of programming.", example_de="Mathematik ist die Grundlage des Programmierens.",
    ),
    VocabEntry(
        hanzi="书", pinyin="shū", english="book", german="Buch",
        category="university", hsk_level=1,
        example_hanzi="这本书很好。", example_pinyin="Zhè běn shū hěn hǎo.",
        example_en="This book is very good.", example_de="Dieses Buch ist sehr gut.",
    ),
    VocabEntry(
        hanzi="字", pinyin="zì", english="character / word", german="Zeichen / Schriftzeichen",
        category="university", hsk_level=2,
        example_hanzi="这个字怎么写？", example_pinyin="Zhè ge zì zěnme xiě?",
        example_en="How do you write this character?", example_de="Wie schreibt man dieses Zeichen?",
    ),
    VocabEntry(
        hanzi="写", pinyin="xiě", english="to write", german="schreiben",
        category="university", hsk_level=1,
        example_hanzi="请写下来。", example_pinyin="Qǐng xiě xiàlái.",
        example_en="Please write it down.", example_de="Bitte schreibe es auf.",
    ),
    VocabEntry(
        hanzi="读", pinyin="dú", english="to read", german="lesen",
        category="university", hsk_level=2,
        example_hanzi="我每天读书。", example_pinyin="Wǒ měitiān dú shū.",
        example_en="I read every day.", example_de="Ich lese jeden Tag.",
    ),
    VocabEntry(
        hanzi="听", pinyin="tīng", english="to listen", german="hören / zuhören",
        category="university", hsk_level=1,
        example_hanzi="请听老师说。", example_pinyin="Qǐng tīng lǎoshī shuō.",
        example_en="Please listen to the teacher.", example_de="Bitte hör dem Lehrer zu.",
    ),
    VocabEntry(
        hanzi="说", pinyin="shuō", english="to speak / say", german="sprechen / sagen",
        category="university", hsk_level=1,
        example_hanzi="你说中文吗？", example_pinyin="Nǐ shuō zhōngwén ma?",
        example_en="Do you speak Chinese?", example_de="Sprichst du Chinesisch?",
    ),
    VocabEntry(
        hanzi="懂", pinyin="dǒng", english="to understand", german="verstehen",
        category="university", hsk_level=2,
        example_hanzi="你懂吗？", example_pinyin="Nǐ dǒng ma?",
        example_en="Do you understand?", example_de="Verstehst du?",
    ),
    VocabEntry(
        hanzi="练习", pinyin="liàn xí", english="to practice / exercise", german="üben / Übung",
        category="university", hsk_level=3,
        example_hanzi="我每天练习中文。", example_pinyin="Wǒ měitiān liànxí zhōngwén.",
        example_en="I practice Chinese every day.", example_de="Ich übe jeden Tag Chinesisch.",
    ),
    VocabEntry(
        hanzi="成绩", pinyin="chéng jì", english="grade / result", german="Note / Ergebnis",
        category="university", hsk_level=4,
        example_hanzi="考试成绩很好。", example_pinyin="Kǎoshì chéngjì hěn hǎo.",
        example_en="The exam results are good.", example_de="Die Prüfungsergebnisse sind gut.",
    ),
    VocabEntry(
        hanzi="同学", pinyin="tóng xué", english="classmate", german="Kommilitone / Mitschüler",
        category="university", hsk_level=2,
        example_hanzi="我和同学一起学习。", example_pinyin="Wǒ hé tóngxué yīqǐ xuéxí.",
        example_en="I study together with my classmate.", example_de="Ich lerne zusammen mit meinem Kommilitonen.",
    ),
    VocabEntry(
        hanzi="答案", pinyin="dá àn", english="answer / solution", german="Antwort / Lösung",
        category="university", hsk_level=4,
        example_hanzi="答案是什么？", example_pinyin="Dá'àn shì shénme?",
        example_en="What is the answer?", example_de="Was ist die Antwort?",
    ),
    VocabEntry(
        hanzi="问", pinyin="wèn", english="to ask", german="fragen",
        category="university", hsk_level=2,
        example_hanzi="我想问一个问题。", example_pinyin="Wǒ xiǎng wèn yī gè wèntí.",
        example_en="I want to ask a question.", example_de="Ich möchte eine Frage stellen.",
    ),
    VocabEntry(
        hanzi="中文", pinyin="zhōng wén", english="Chinese language", german="Chinesisch",
        category="university", hsk_level=1,
        example_hanzi="我在学中文。", example_pinyin="Wǒ zài xué zhōngwén.",
        example_en="I am learning Chinese.", example_de="Ich lerne Chinesisch.",
    ),
    VocabEntry(
        hanzi="英文", pinyin="yīng wén", english="English language", german="Englisch",
        category="university", hsk_level=2,
        example_hanzi="他的英文很好。", example_pinyin="Tā de yīngwén hěn hǎo.",
        example_en="His English is very good.", example_de="Sein Englisch ist sehr gut.",
    ),
    VocabEntry(
        hanzi="德文", pinyin="dé wén", english="German language", german="Deutsch",
        category="university", hsk_level=3,
        example_hanzi="我说德文。", example_pinyin="Wǒ shuō déwén.",
        example_en="I speak German.", example_de="Ich spreche Deutsch.",
    ),
]


# ---------------------------------------------------------------------------
# PUBLIC API
# ---------------------------------------------------------------------------

_BUILTIN_VOCAB: list[VocabEntry] = (
    _BASICS + _TECH + _BUSINESS + _DAILY + _TRAVEL + _RESTAURANT + _UNIVERSITY
)


def _load_all_vocab() -> list[VocabEntry]:
    """Load built-in vocabulary + any custom vocabulary from plugins."""
    try:
        from chinese_cli.plugins import load_custom_vocab
        custom = load_custom_vocab()
    except ImportError:
        custom = []
    # Deduplicate by hanzi
    seen = {v.hanzi for v in _BUILTIN_VOCAB}
    extras = [v for v in custom if v.hanzi not in seen]
    return _BUILTIN_VOCAB + extras


ALL_VOCAB: list[VocabEntry] = _load_all_vocab()

CATEGORIES: dict[str, str] = {
    "basics": "📚 Basics — Greetings, numbers, pronouns",
    "tech": "💻 Tech — Software, hardware, AI, coding",
    "business": "💼 Business — Meetings, contracts, startups",
    "daily": "🍜 Daily — Food, transport, small talk",
    "travel": "✈️  Travel — Airport, directions, cities",
    "restaurant": "🍲 Restaurant — Food, drinks, ordering",
    "university": "🎓 University — Classes, exams, campus",
}

CATEGORY_KEYS = list(CATEGORIES.keys())


def get_vocab_by_category(category: str) -> list[VocabEntry]:
    """Return vocabulary entries for a given category."""
    return [v for v in ALL_VOCAB if v.category == category]


def get_vocab_by_hsk(level: int) -> list[VocabEntry]:
    """Return vocabulary entries for a given HSK level."""
    return [v for v in ALL_VOCAB if v.hsk_level == level]


def search_vocab(query: str) -> list[VocabEntry]:
    """Search vocab by hanzi, pinyin, english, or german (case-insensitive)."""
    q = query.lower()
    return [
        v for v in ALL_VOCAB
        if q in v.hanzi or q in v.pinyin.lower() or q in v.english.lower() or q in v.german.lower()
    ]
