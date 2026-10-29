"""Entry point for geometor.elements."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
from typing import List, Optional

_SRC_DIR = Path(__file__).resolve().parents[2]
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

from geometor.elements.g_index import generate_g_index


def main(argv: Optional[List[str]] = None) -> None:
    """Execute the G-Index generation process from the composed Euclid Heath edition."""
    parser = argparse.ArgumentParser(
        prog="elements",
        description="Generate the GEOMETOR Elements 2.0 (G-Index) from ../euclid/docsrc/heath/.",
    )
    parser.add_argument(
        "--books",
        type=str,
        default=None,
        help="Comma-separated list of Roman book numerals to include (e.g. 'I' or 'I,II,III'). Defaults to all 13 books.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Target directory for generated RST files (defaults to docsrc/elements2).",
    )
    args = parser.parse_args(argv)

    books = (
        [b.strip().upper() for b in args.books.split(",") if b.strip()]
        if args.books
        else None
    )
    generate_g_index(output_dir=args.output_dir, books=books)


if __name__ == "__main__":
    main()
