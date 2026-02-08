# Practical Web Development

From Server-Rendered Pages to React with Python and FastAPI.

> **[Read the English version (PDF)](docs/en/Practical-Web-Development-(en).pdf)**

A book that teaches web development starting from how HTTP works, through HTML, CSS, and server-side Python with FastAPI, all the way to HTMX, React, databases, authentication, and deployment. Opinionated, hands-on, and meant to be read in order. Each chapter builds on the previous one.

Assumes Python knowledge. No prior web experience needed.

## Table of Contents

| Chapter | Topic | Code |
|---------|-------|------|
| 1 | How the Web Works | — |
| 2 | HTML | [chapter2](en/code/chapter2) |
| 3 | CSS Basics | [chapter3](en/code/chapter3) |
| 4 | Servers with FastAPI | [chapter4](en/code/chapter4) |

More chapters will be added.

## Available Languages

| Language | Directory | Status |
|----------|-----------|--------|
| English | [en/](en/) | In progress |

## Prerequisites

- [Python 3.11+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) - Python package manager
- [Quarto](https://quarto.org/docs/get-started/) - Publishing system

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Applied-Computing-League/practical-web-development.git
   cd practical-web-development
   ```

2. Install Python dependencies with uv:
   ```bash
   uv sync
   ```

## Building the Book

### HTML (default)

```bash
uv run quarto render en/
```

The output will be in `docs/en/`. Open `docs/en/index.html` in your browser to view.

### PDF

```bash
uv run quarto render en/ --to pdf
```

> Note: PDF rendering requires a LaTeX distribution (e.g., [TinyTeX](https://yihui.org/tinytex/), [TeX Live](https://www.tug.org/texlive/), or [MiKTeX](https://miktex.org/)).

### Preview with live reload

```bash
uv run quarto preview en/
```

This starts a local server and opens the book in your browser. Changes to `.qmd` files will automatically trigger a rebuild.

## Project Structure

```
practical-web-development/
├── en/                          # English
│   ├── _quarto.yml
│   ├── index.qmd
│   ├── references.qmd
│   ├── references.bib
│   ├── chapters/
│   │   ├── chapter1.qmd
│   │   ├── chapter2.qmd
│   │   ├── chapter3.qmd
│   │   └── chapter4.qmd
│   ├── images/                  # Figures (language-specific)
│   │   ├── chapter1/
│   │   ├── chapter2/
│   │   ├── chapter3/
│   │   └── chapter4/
│   └── code/                    # Completed code per chapter
│       ├── chapter2/
│       ├── chapter3/
│       └── chapter4/
├── docs/                        # Rendered output
│   └── en/
├── README.md
├── LICENSE
├── pyproject.toml
└── .gitignore
```

## Adding a New Language

To translate the book into a new language:

1. Copy the `en/` directory as your starting point:
   ```bash
   cp -r en/ pt/   # for Portuguese, for example
   ```

2. In your new directory (e.g., `pt/`):
   - Translate all `.qmd` files (chapters, index, references)
   - Translate or recreate images that contain text (SVGs in `images/`)
   - Update `_quarto.yml`: change `output-dir` to `../docs/pt`, translate the title/subtitle, and update `output-file` to use your language code (e.g., `"Practical Web Development (pt)"`)
   - Code in `code/` may need translated comments

3. Update the cover image:
   - Edit `images/cover.svg` — translate the text elements (title, subtitle, author) to your language
   - Convert the SVG to PNG for PDF rendering (requires `rsvg-convert`, installed via `librsvg`):
     ```bash
     rsvg-convert -f png -w 2400 -h 3600 -o pt/images/cover.png pt/images/cover.svg
     ```

4. Build with:
   ```bash
   uv run quarto render pt/
   uv run quarto render pt/ --to pdf
   ```

4. Add yourself to the contributors table below and submit a pull request.

## Contributors

| Name | GitHub | Role | Language |
|------|--------|------|----------|
| Igor Benav | [@igorbenav](https://github.com/igorbenav) | Author | English |

When your translation or review is merged, add yourself in the same pull request to:

1. The **Contributors** table above (this README)
2. The **Contributors** table in your language's `index.qmd` (this appears in the actual book)

Roles: "Translator", "Reviewer", or both.

## License

MIT License - see [LICENSE](LICENSE) for details.
