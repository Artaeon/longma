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
]


# ---------------------------------------------------------------------------
# PUBLIC API
# ---------------------------------------------------------------------------

ALL_VOCAB: list[VocabEntry] = _BASICS + _TECH + _BUSINESS + _DAILY

CATEGORIES: dict[str, str] = {
    "basics": "📚 Basics — Greetings, numbers, pronouns",
    "tech": "💻 Tech — Software, hardware, AI, coding",
    "business": "💼 Business — Meetings, contracts, startups",
    "daily": "🍜 Daily — Food, transport, small talk",
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
