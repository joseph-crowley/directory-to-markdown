# Project: Directory to Markdown Converter

This Python project efficiently converts files from a specified directory into a well-structured Markdown document, including proper error handling, logging, and configurability suitable for professional environments.

## Features:

- **Recursive File Traversal**:
  - Traverses directories recursively, or non-recursively based on the provided option.
  - Ignores directories specified (default: `node_modules`, `__pycache__`, `.git`, `.vscode`, `.idea`).

- **File Filtering**:
  - Filters files based on user-specified file types (extensions).
  - By default, includes all file types if none specified.

- **Robustness and Error Handling**:
  - Skips files exceeding a specified maximum size (default: 10 MB) to prevent memory issues.
  - Handles file read errors gracefully, logging warnings or errors without interrupting processing.

- **Logging**:
  - Detailed logging at each step using Python's `logging` module.
  - Logs processed files, skipped files (due to size or errors), and general processing status.

- **Command-Line Interface**:
  - Configurable via intuitive command-line arguments using Python's `argparse`.

## Usage Examples:

### Include only `.py` and `.txt` files:

```bash
python directory_to_markdown.py path/to/myfiles -o my_output.md -t .py .txt
```

### Non-recursive traversal:

```bash
python directory_to_markdown.py path/to/myfiles -nr
```

### Custom maximum file size (5 MB):

```bash
python directory_to_markdown.py myfiles -m 5
```

### Specify directories to ignore:

```bash
python directory_to_markdown.py myfiles --ignore node_modules .git myfolder
```

## Command-Line Arguments Reference:

- `directory` *(required)*: Directory path containing target files.
- `-o`, `--output`: Output Markdown file name (default: `output.md`).
- `-t`, `--types`: File extensions to include (e.g., `.py`, `.txt`). Include all if omitted.
- `--ignore`: Directories to ignore during traversal (default: common dev dirs).
- `-nr`, `--no-recursive`: Disable recursive directory traversal.
- `-m`, `--max-size`: Maximum file size in MB to process (default: `10 MB`).

## Output Markdown Format:

Each file’s contents are encapsulated clearly:

> ## relative/path/to/file.py
> 
>     ```py
>     # File contents go here
>     def example():
>         pass
>     ```

This format ensures readability and easy parsing, suitable for automated ingestion by tools, including large language models (LLMs).

## Intended Use in LLM Contexts:

The structured output (`your_project.md`) facilitates direct ingestion into LLM contexts, providing high-quality, structured input for summarization, code explanation, translation, or AI-driven documentation tasks. Its clarity and consistency optimize comprehension and facilitate automated reasoning about codebases and repositories.
