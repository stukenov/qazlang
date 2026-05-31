# 🇰🇿 QazLang - Programming in Kazakh Language

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Made in Kazakhstan](https://img.shields.io/badge/Made%20in-Kazakhstan%20%F0%9F%87%B0%F0%9F%87%BF-00AFCA.svg)](https://github.com/stukenov/qazlang)

**The world's first programming language with native Kazakh syntax** — write code in Kazakh, Russian, and more, breaking the English-only barrier.

QazLang (Қазақ тілінде бағдарламалау тілі) is a revolutionary programming framework that allows developers to write code in their native Kazakh language. Breaking the barrier of English-only programming languages, QazLang empowers Kazakh speakers to express computational logic in their mother tongue.

## 🌟 Why QazLang?

Programming languages have traditionally been dominated by English keywords and syntax. QazLang challenges this paradigm by providing:

- **Native Language Programming**: Write code in Kazakh with keywords like `ЖАСАУ` (create), `ТАҢДАУ` (select), and `ӨҢДЕ` (edit)
- **Cultural Relevance**: Programming constructs that reflect Kazakh linguistic patterns
- **Educational Accessibility**: Lower barriers to entry for Kazakh-speaking students
- **Multilingual Support**: Extended support for Russian and other languages

## ✨ Features

### 🎯 Core Language Features

- **Database Operations** (`.qazsql` files): SQL-like syntax in Kazakh
- **UI Development** (`.qalang` files): Declarative UI components
- **Business Logic** (`.pylang` files): Business-oriented programming constructs
- **Multi-paradigm**: Support for procedural, functional, and declarative programming

### 🔤 Supported Language Variants

- **Kazakh** (`.qalang`, `.qazsql`) - Primary focus
- **Russian** (`.руяз`, `.pysql`) - Full support
- **Japanese** (`.япоб`) - Experimental
- **Python Integration** - Seamless interoperability with Python

## 🚀 Quick Start

### Example: Database Query in Kazakh

```kazakh
ТАҢДАУ атауы, ТҮРІ, ОРТАША_МӘН(БАҒАСЫ)
МАТЕРИАЛДАРДАН
ҚАЙДА ТҮРІ = (ТАҢДАУ 'материалдың түрі' МАТЕРИАЛ_ТҮРЛЕРІНЕН);
```

**English equivalent:**
```sql
SELECT name, type, AVG(price)
FROM materials
WHERE type = (SELECT 'material_type' FROM material_types);
```

### Example: Creating a Table in Kazakh

```kazakh
қойма КЕСТЕСІ ЖАСАУ
партия_нөмірі БАҒАНЫ ОРНАТУ
атауы_материал  БАҒАНЫ ОРНАТУ
саны  БАҒАНЫ ОРНАТУ
сатып_алу_бағасы  БАҒАНЫ ОРНАТУ
    сату_бағасы РЕТІНДЕ (сатып_алу_бағасы * (ТАҢДАУ ВАЛЮТА_КУРСЫНАН курстар_валют)),
    (атауы_материал) БАЙЛАНЫСТЫ МАТЕРИАЛДАР(атауы);
```

### Example: Creating a Web Page in Kazakh

```kazakh
ЖАСАУ БЕТ материалдарды_басқару
    ТАҚЫРЫП "Материалдарды басқару"
    СИПАТТАМА "Қоймадағы материалдарды басқару беті";

ЖАСАУ ПІШІН материалды_қосу БЕТТЕ материалдарды_басқару
    ЕНГІЗУ_ӨРІСІ "атауы_материал" ТҮРІ: мәтін ЖАПСЫРМА: "Материалдың атауын енгізіңіз" МІНДЕТТІ: иә
    ТҮЙМЕ "қосу" ӘРЕКЕТ: материалдыҚосу;
```

### Example: Stored Procedure in Kazakh

```kazakh
ЖАСАУ ПРОЦЕДУРА бағаны_есептеу (атауы_материал МӘТІН)
БАСТАУ
    ТАҢДАУ сату_бағасы қоймадан ҚАЙДА атауы_материал = атауы_материал
    ШЫҒАРУ 'материалдың сату бағасы: ', сату_бағасы
АЯҚТАУ;
```

### Example: Simple UI in Kazakh

```kazakh
аты, сипаты, саны       ӨРІС
тағамдар                КЕСТЕ
тағамдар_тізімі         ФОРМА
тағам                   БЕТ
                        ҚОС
                        КӨРСЕТ
                        ӨШІР
                        ӨҢДЕ;
```

## 📖 Language Reference

### Kazakh Keywords

| Kazakh | English | Usage |
|--------|---------|-------|
| `ЖАСАУ` | CREATE | Create new objects (tables, procedures, pages) |
| `ТАҢДАУ` | SELECT | Query data |
| `ЖАҢАРТУ` | UPDATE | Update existing data |
| `ЖОЮ` | DELETE | Delete data |
| `ОРНАТУ` | SET | Set values |
| `ҚАЙДА` | WHERE | Conditional filtering |
| `ЖӘНЕ` | AND | Logical AND |
| `БАСТАУ` | BEGIN | Start a block |
| `АЯҚТАУ` | END | End a block |
| `ШЫҒАРУ` | OUTPUT | Print/output data |
| `ЖИЫНТЫҚ` | SUM | Aggregate function |
| `ОРТАША_МӘН` | AVG | Average function |
| `КЕСТЕ` | TABLE | Table |
| `БЕТ` | PAGE | Page/Form |
| `ТҮЙМЕ` | BUTTON | Button |
| `ӨРІС` | FIELD | Field/Input |
| `ҚОС` | ADD | Add |
| `ӨШІР` | DELETE | Remove |
| `ӨҢДЕ` | EDIT | Edit |
| `КӨРСЕТ` | SHOW | Display |

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher

### Clone and Install

```bash
git clone https://github.com/stukenov/qazlang.git
cd qazlang
```

No external dependencies are required — `lang-parser.py` uses only the Python standard library (`re`).

### Run a Program

The `lang-parser.py` interpreter reads a native-language source file and generates HTML. Drive it from a short Python script (mirroring the usage example included at the bottom of `lang-parser.py`):

```python
from importlib import import_module
parser_module = import_module("lang-parser")  # or: exec(open("lang-parser.py").read())

parser = parser_module.RuLangParser()

with open("РуЯзык.руяз", "r", encoding="utf-8") as file:
    source = file.read()

html = parser.parse(source)

with open("output.html", "w", encoding="utf-8") as file:
    file.write(html)
```

The parser recognizes native-language UI keywords directly from the source — for example `СОЗДАТЬ СТРАНИЦУ` (CREATE PAGE), `СОЗДАТЬ ФОРМУ` (CREATE FORM), `ПОЛЕ ВВОДА` (INPUT FIELD), and `КНОПКА` (BUTTON) — and emits the corresponding HTML (`example-excel.html` shows sample output). The `.qalang` and `.qazsql` files demonstrate the Kazakh syntax shown above.

## 📚 File Extensions

- `.qalang` - Kazakh language files (SAP/ERP business logic)
- `.qazsql` - Kazakh SQL dialect
- `.pylang` - Python-style Kazakh syntax
- `.pysql` - Russian SQL dialect
- `.руяз` - Russian language files
- `.япоб` - Japanese Business-Oriented Programming

## 🎯 Use Cases

### Enterprise Resource Planning (ERP)
QazLang was designed with business applications in mind. The examples include SAP integration patterns for:
- Purchase requisitions (`ЗапросНаПокупку`)
- Inventory management (`қойма` - warehouse)
- Material management (`материалдарды_басқару`)

### Education
Perfect for teaching programming concepts in Kazakh language:
- Reduces cognitive load for Kazakh-speaking students
- Makes programming more accessible to non-English speakers
- Preserves and promotes Kazakh language in technology

### Web Development
Declarative UI syntax for creating web interfaces:
- Forms and input fields
- Tables and data display
- Buttons and user interactions

## 🌍 Global Impact

QazLang is part of a growing movement to democratize programming by making it accessible in native languages. While English has dominated programming for decades, languages like QazLang prove that code can be just as expressive and powerful in any human language.

### Similar Projects Worldwide
- **Arabic**: عربي (Arabic)
- **Chinese**: 文言 (wenyan-lang)
- **Hindi**: हिंदी (Hindi programming)
- **Bengali**: বাংলা (Bangla)

QazLang joins this movement by bringing programming to the 18+ million Kazakh speakers worldwide.

## 🤝 Contributing

We welcome contributions from the community! Whether you're:
- A native Kazakh speaker with programming knowledge
- A linguist interested in programming language design
- A developer passionate about language accessibility
- An educator looking to teach programming in Kazakh

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Language Design Philosophy

QazLang follows these principles:

1. **Natural Language Mapping**: Keywords reflect natural Kazakh language patterns
2. **Unicode Support**: Full support for Kazakh Cyrillic characters
3. **Backward Compatibility**: Can integrate with existing Python codebases
4. **Readability**: Code should read like natural Kazakh prose
5. **Expressiveness**: Kazakh keywords should be as powerful as English equivalents

## 🔬 Technical Architecture

```
qazlang/
├── lang-parser.py      # Main parser for .ruяз and .qalang files
├── pseudo-python.py    # Python integration layer
├── SAP-QazLang.qalang  # Kazakh ERP/SAP examples
├── SAP-PyLang.pylang   # Russian ERP/SAP examples
├── SQL-QAZ.qazsql      # Kazakh SQL examples
└── example-excel.html  # UI example output
```

### Parser Architecture

The parser converts native language syntax to executable code:
1. Lexical analysis of Kazakh/Russian keywords
2. AST (Abstract Syntax Tree) generation
3. Code generation (Python/SQL/HTML)
4. Runtime execution

## 📊 Roadmap

- [ ] Complete Kazakh keyword library
- [ ] IDE syntax highlighting support (VS Code, PyCharm)
- [ ] Standard library in Kazakh
- [ ] Package manager (`qpm` - QazLang Package Manager)
- [ ] REPL (Read-Eval-Print Loop) in Kazakh
- [ ] Jupyter notebook integration
- [ ] Web-based playground
- [ ] Documentation in Kazakh and English
- [ ] Tutorial series for beginners

## 🔗 Related projects

QazLang is part of a broader Kazakh-language technology stack aimed at bringing modern computing to native speakers:

- **[kazakh-nlp-toolkit](https://github.com/stukenov/kazakh-nlp-toolkit)** — natural language processing tools for Kazakh
- **[slm](https://github.com/stukenov/slm)** — small language model work for low-resource languages
- **[turkic-tts](https://github.com/stukenov/turkic-tts)** — text-to-speech for Turkic languages

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

## 🙏 Acknowledgments

Special thanks to:
- The Kazakh linguistic community
- Developers working on multilingual programming languages
- Everyone who believes programming should be accessible in any language

## 📞 Contact

**Project Maintainer**: stukenov

**Repository**: [https://github.com/stukenov/qazlang](https://github.com/stukenov/qazlang)

---

**Қазақстан технологиясы әлемге!** 🇰🇿
*Kazakhstan technology to the world!*

---

### Star this repository if you believe programming should be multilingual! ⭐
