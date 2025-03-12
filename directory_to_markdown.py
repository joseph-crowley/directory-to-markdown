import os
import argparse
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

DEFAULT_IGNORE_DIRS = {'node_modules', '__pycache__', '.git', '.vscode', '.idea'}

def is_ignored(path, ignore_dirs):
    """Check if the path is inside any ignored directory."""
    for part in path.parts:
        if part in ignore_dirs:
            return True
    return False

def read_file_safely(file_path, max_size_mb=10):
    """Read file contents safely, checking file size and encoding."""
    try:
        file_size_mb = file_path.stat().st_size / (1024 * 1024)
        if file_size_mb > max_size_mb:
            logging.warning(f"Skipping large file '{file_path}' ({file_size_mb:.2f} MB)")
            return None

        return file_path.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        logging.error(f"Error reading '{file_path}': {e}")
        return None

def directory_to_markdown(
        directory_path, output_file, file_types=None, 
        ignore_dirs=None, recursive=True, max_file_size_mb=10):
    """
    Traverse directory, read selected files, and write their contents into a markdown file.

    Args:
        directory_path (str | Path): Directory to traverse.
        output_file (str | Path): Markdown file to generate.
        file_types (set[str]): File extensions to include (e.g., {'.py', '.txt'}).
        ignore_dirs (set[str]): Directory names to ignore.
        recursive (bool): Whether to traverse subdirectories.
        max_file_size_mb (int): Maximum file size to process in megabytes.
    """
    directory_path = Path(directory_path).resolve()
    output_file = Path(output_file).resolve()

    if ignore_dirs is None:
        ignore_dirs = DEFAULT_IGNORE_DIRS
    if file_types is not None:
        file_types = {ext.lower() for ext in file_types}

    logging.info(f"Scanning directory: {directory_path}")
    file_count = 0

    with output_file.open('w', encoding='utf-8') as md:
        for root, dirs, files in os.walk(directory_path):
            root_path = Path(root)

            # Remove ignored directories from traversal
            dirs[:] = [d for d in dirs if d not in ignore_dirs]

            for filename in files:
                file_path = root_path / filename

                if is_ignored(file_path, ignore_dirs):
                    continue

                if file_types and file_path.suffix.lower() not in file_types:
                    continue

                content = read_file_safely(file_path, max_file_size_mb)
                if content is None:
                    continue

                relative_file_path = file_path.relative_to(directory_path)
                language = file_path.suffix[1:] or ''  # remove dot, e.g., '.py' -> 'py'

                # Write filename as markdown header
                md.write(f"## {relative_file_path}\n\n")
                md.write(f"```{language}\n{content}\n```\n\n")

                file_count += 1
                logging.info(f"Processed file: {relative_file_path}")

            if not recursive:
                break  # If not recursive, break after first iteration

    logging.info(f"Markdown file '{output_file}' created successfully with {file_count} files processed.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Generate a markdown file with contents of files from a directory."
    )
    parser.add_argument("directory", help="Path to the directory containing files.")
    parser.add_argument(
        "-o", "--output", default="output.md",
        help="Output markdown file (default: output.md)"
    )
    parser.add_argument(
        "-t", "--types", nargs='*', default=[],
        help="File extensions to include (e.g., -t .py .txt). Include all if omitted."
    )
    parser.add_argument(
        "--ignore", nargs='*', default=list(DEFAULT_IGNORE_DIRS),
        help="Directories to ignore (default: node_modules __pycache__ .git .vscode .idea)"
    )
    parser.add_argument(
        "-nr", "--no-recursive", action='store_true',
        help="Disable recursive traversal."
    )
    parser.add_argument(
        "-m", "--max-size", type=int, default=10,
        help="Max file size (MB) to process (default: 10 MB)"
    )

    args = parser.parse_args()

    directory_to_markdown(
        args.directory, args.output,
        file_types=set(args.types) if args.types else None,
        ignore_dirs=set(args.ignore),
        recursive=not args.no_recursive,
        max_file_size_mb=args.max_size
    )

