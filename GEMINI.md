# GEOMETOR Elements

A digital reconstruction of Euclid's Elements focused on symbolic dependency mapping and G-Index generation.

## Mission

To codify the logical structure of Euclid's *Elements* into a computable dependency graph (the G-Index), enabling the exploration of geometric truth as a genealogical tree of propositions.

## Overview

`geometor.elements` is the logic and serialization layer of the GEOMETOR Euclid project. It separates the **symbolic structure** from the **semantic discovery** performed in the sister `euclid` repository.

It is responsible for:

-   **G-Index Generation**: Creating a dependency-aware index (G.1, G.2...) that maps the entire logical flow of the *Elements*.
-   **Structured Analysis**: Extracting metadata and relationships from the processed RST source.
-   **Symbolic Modeling**: Bridging the textual propositions with the `geometor.model` symbolic engine.
-   **Visualization**: Generating Graphviz dependency trees for every element.

## Key Repos

-   **elements**: This repository. Code for G-Index generation and dependency analysis.
-   **euclid**: The source of truth for the modernized text and semantic discovery (`../euclid/docsrc/heath/`).
-   **model**: The symbolic engine used for geometric construction.

## Key Modules

-   `graph.py`: Crawls the composed RST Heath Edition in `../euclid/docsrc/heath/`, splitting definitions, postulates, and common notions into discrete anchored items and building the `networkx.DiGraph` with categories, tags, and interactive SVG assets.
-   `g_index.py`: Sequences propositions and dependencies into `G.1`..`G.N`, rewrites `:g:` roles to explicit GEOMETOR symbolic indications (`/ A B /`, `< A B C >`, `< B A C )`, `( B C D )`, `[ A B ]`, `A`), rewrites justifications to `G.<n>` links, and renders the Book Codex RST in `docsrc/elements2/`.
-   `__main__.py`: CLI entry point supporting `--books` and `--output-dir`.
