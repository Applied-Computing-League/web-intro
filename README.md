# Practical Web Development

From Server-Rendered Pages to React with Python and FastAPI.

## Table of Contents

| Chapter | Topic | Code |
|---------|-------|------|
| 1 | How the Web Works | — |
| 2 | HTML | [chapter2](chapters/code/chapter2) |
| 3 | CSS Basics | [chapter3](chapters/code/chapter3) |
| 4 | Servers with FastAPI | [chapter4](chapters/code/chapter4) |

More chapters will be added.

## Prerequisites

- [Python 3.11+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) - Python package manager
- [Quarto](https://quarto.org/docs/get-started/) - Publishing system

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Applied-Computing-League/web-intro.git
   cd web-intro
   ```

2. Install Python dependencies with uv:
   ```bash
   uv sync
   ```

## Building the Book

### HTML (default)

```bash
uv run quarto render
```

The output will be in the `docs/` directory. Open `docs/index.html` in your browser to view.

### PDF

```bash
uv run quarto render --to pdf
```

> Note: PDF rendering requires a LaTeX distribution (e.g., [TinyTeX](https://yihui.org/tinytex/), [TeX Live](https://www.tug.org/texlive/), or [MiKTeX](https://miktex.org/)).

## Development

### Preview with live reload

```bash
uv run quarto preview
```

This starts a local server and opens the book in your browser. Changes to `.qmd` files will automatically trigger a rebuild.

### Render a single chapter

```bash
uv run quarto render chapters/chapter1.qmd
```

## Project Structure

```
web-intro/
├── _quarto.yml          # Quarto configuration
├── index.qmd            # Book preface
├── chapters/
│   ├── chapter1.qmd     # How the Web Works
│   ├── chapter2.qmd     # HTML
│   ├── chapter3.qmd     # CSS Basics
│   ├── chapter4.qmd     # Servers with FastAPI
│   ├── code/            # Completed code for each chapter
│   │   ├── chapter2/
│   │   ├── chapter3/
│   │   └── chapter4/
│   └── images/          # Chapter figures
├── docs/                # Rendered output (HTML)
├── references.bib       # Bibliography
├── references.qmd       # References page
└── pyproject.toml       # Python dependencies
```

## License

MIT License - see [LICENSE](LICENSE) for details.
