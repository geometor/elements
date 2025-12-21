"""Entry point for geometor.elements."""

from geometor.elements.g_index import generate_g_index


def main() -> None:
    """Execute the G-Index generation process.

    Scans the Euclid source documentation, builds a dependency graph,
    and renders the G-Index RST structure.
    """
    generate_g_index()


if __name__ == "__main__":
    main()
