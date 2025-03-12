# Directory to Markdown Converter

![Project Preview](.github/bookworm.jpg)

[image](https://en.wikipedia.org/wiki/The_Bookworm_(Spitzweg))

A robust, configurable Python tool designed to transform your project directory into a clearly structured Markdown document—perfectly optimized for documentation, code reviews, and integration with language models.

The converter traverses directories, gracefully handles large files, logs processing details, and manages errors to ensure consistent, reliable outputs.

## Why Use This?

- **Effortless Documentation:** Automatically generate Markdown from source code, enhancing readability and clarity. Share a complete codebase with an LLM.
- **Flexible and Selective:** Include or exclude files by extension, set file-size limits, and skip unwanted directories such as `node_modules`, `.git`, and `__pycache__`.
- **Reliable:** Built-in error handling ensures uninterrupted processing, with clear logging at every step.

---

## Quick Start Examples

### Convert `.py` and `.txt` files:

```bash
python directory_to_markdown.py my_directory -o docs.md -t .py .txt
```

### Non-recursive directory scan:

```bash
python directory_to_markdown.py my_project -o project_docs.md --no-recursive
```

### Full conversion with defaults (all files):

```bash
python directory_to_markdown.py path/to/directory
```

---

## Command-line Options

| Option                      | Description                                    | Default       |
|-----------------------------|------------------------------------------------|---------------|
| `directory` *(required)*    | Directory containing target files.             | -             |
| `-o, --output`              | Output Markdown filename.                      | `output.md`   |
| `-t, --types`               | List file extensions to include (e.g., `.py`). | All files     |
| `-m, --max-size`            | Max file size (MB) to include.                 | `10` MB       |
| `--ignore`                  | Directories to exclude from scanning.          | Common dirs (`node_modules`, `.git`, etc.) |
| `-nr, --no-recursive`       | Disable recursive traversal.                   | Recursive enabled |

---

## Markdown Output Format

Each file is clearly encapsulated for easy parsing and readability:

>     ## relative/path/to/example.py
>     
>     ```py
>     def example():
>         pass
>     ```


This format ensures readability and easy parsing, suitable for automated ingestion by tools, including large language models (LLMs).

## Intended Use in LLM Contexts:

The structured output (`your_project.md`) facilitates direct ingestion into LLM contexts, providing high-quality, structured input for summarization, code explanation, translation, or AI-driven documentation tasks. Its clarity and consistency optimize comprehension and facilitate automated reasoning about codebases and repositories.
