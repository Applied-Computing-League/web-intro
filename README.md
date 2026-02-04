# Practical Web Development

A book on web development, from server-rendered pages to React with Python and FastAPI.

## Prerequisites

- [Python 3.11+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) - Python package manager
- [Quarto](https://quarto.org/docs/get-started/) - Publishing system

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/igorbenav/web-intro.git
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
├── _quarto.yml      # Quarto configuration
├── index.qmd        # Book preface
├── chapters/        # Book chapters
├── docs/            # Rendered output (HTML)
├── references.bib   # Bibliography
├── references.qmd   # References page
└── pyproject.toml   # Python dependencies
```

## License

MIT License - see [LICENSE](LICENSE) for details.
