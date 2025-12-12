# GEOMETOR Elements

A digital reconstruction of Euclid's Elements for dependency mapping and analysis.

## Overview

`geometor.elements` converts the Heath edition of Euclid's *Elements* into structured data and reStructuredText (RST). It enables dependency analysis, diagram extraction, and the generation of hyperlink-rich documentation.

## Architecture

-   **Ingestion**: `ingest/` pipeline extracts and normalizes text/images from source PDFs.
-   **Refinement**: Processes diagrams and maps logical dependencies.
-   **Transformation**: `transform.py` generates the final RST structure for Sphinx.

## Index

-   `ingest/`: Source processing pipeline.
-   `transform.py`: Entry point for RST generation.
-   `graph.py`: Dependency graph generation logic.
-   `elements.py`: Core data structures.

## Getting Started

### Installation

```bash
git clone https://github.com/geometor/elements
cd elements
pip install -e .
```

### Usage

The project provides command-line tools for processing and transformation:

```bash
# Main entry point
elements

# Transform XML to RST
elements_transform
```

## Resources

-   **Source Code**: https://github.com/geometor/elements
-   **Issues**: https://github.com/geometor/elements/issues