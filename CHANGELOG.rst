changelog
=========

0.1.3
-----

-   Refined docstrings and type hinting.
-   Fixed `from __future__ import annotations` placement.

0.1.1
-----
*2025-11-23*

**changed**

.. + Updated `transform.py` to target `docsrc/heath` as the primary output directory for generated RST.
.. + Extended `transform.py` to process all 13 books of the Elements.
.. + Modified `transform.py` to invert colors for extracted graphic images (for dark mode compatibility).
.. + Removed fixed `width` attribute from figure directives in generated RST to allow for responsive sizing.
.. + Updated dependency graph links to point to the new `heath` directory structure.
.. + Removed the deprecated `docsrc/elements2` directory.

0.1.0
-----
*2025-11-23*

**added**

.. + Integrated automatic bleed removal and image cleanup into the proposition stitching pipeline.
.. + Added `clean_image` function in `src/geometor/elements/ingest/cleanup.py` to remove background noise and artifacts (bleed-through) from scanned images.
.. + Updated `stitch_propositions.py` to apply cleanup processing during the stitching phase.

**changed**

.. + Removed temporary bleed test scripts and images from the project root.

0.0.20
------
*2025-11-21*

**changed**

.. + Updated `stitch_propositions.py`, `cropping.py`, and `crop_propositions.py` to save extracted graphics to the `cropped` directory (alongside stitched propositions) instead of a separate `graphics` folder.
.. + Changed the filename suffix for extracted graphics from `_graphic.png` to `.graphic.png` (e.g., `I.1.graphic.png`).
.. + Added a warning and safeguard return statement to `scan_propositions.py` and `cropping.py` to prevent accidental overwrites of manual work.

0.0.19
------
*2025-11-21*

**added**

.. + Added `process_book.sh` helper script for scanning and stitching propositions of a single book.
.. + Implemented per-book `index.json` generation in `scan_propositions.py` (saved to `resources/heath/volume_X/book_y/propositions/index.json`).
.. + Added command-line argument `--book` to `scan_propositions.py` and `stitch_propositions.py` to target specific books.

**changed**

.. + Updated `scan_propositions.py` to support scanning individual books and storing indexes locally within the book's directory structure.
.. + Updated `stitch_propositions.py` to consume per-book `index.json` files and support book-specific processing.
.. + Refined regex for end-of-proposition detection to handle variations in spacing (e.g., "Q. E . D.").

0.0.18
------
*2025-11-21*

**changed**

.. + Standardized Heath resource folder structure (`resources/heath/`).
.. + Moved JSON index files (`pages.json`, `proposition_index.json`, `toc.json`) into `resources/heath/`.
.. + Refined `scan_propositions.py` to use pixel-based offsets and correct boundary detection.
.. + Updated `stitch_propositions.py` to generate stitched images with body-text cropping.

0.0.17
------
*2025-11-20*

**added**

.. + Introduced a modular ingestion pipeline (`geometor.elements.ingest`) for processing Heath's Euclid PDFs.
.. + Implemented dynamic cropping and stitching of proposition images based on text analysis.
.. + Created a separate refinement pipeline (`geometor.elements.ingest.refine`) for analysis, cropping, and metadata extraction.

**changed**

.. + Updated configuration to dynamically manage paths and global settings.
.. + Canonical naming of cropped proposition images now uses Book numeral (e.g., `I.1.png`).
.. + Renamed `resources/extracted` to `resources/heath` as the primary output directory for all extracted and processed assets.
.. + `proposition_index.json`, `pages.json`, and `toc.json` are now saved to their respective volume directories within `resources/heath`.

**fixed**

.. + Corrected volume identification logic in analysis to prevent misattribution of propositions.

0.0.16
------
*2025-11-18*

**added**

.. + Created a Python script to semi-automate cropping of proposition images from Heath's Euclid scans.
.. + Implemented JSON-based instruction file for defining crop coordinates.
.. + Added functionality to stitch multi-page propositions.
.. + Added functionality to extract diagram graphics from stitched proposition images.

0.0.15
------
*2025-11-18*

**added**

.. + Added metadata file (`resources/metadata.json`) to store book titles and subtitles.
.. + Updated transform script to use metadata in generated documentation.
.. + Improved formatting for subtitles and introductions in book index pages.

0.0.14
------
*2025-11-17*

**added**

.. + Added clickable nodes to the dependency graphs with root-relative URLs.
.. + Styled end nodes in orange to distinguish them from other nodes.
.. + Set graphviz output to SVG for better rendering and interactivity.

0.0.13
------
*2025-11-17*

**added**

.. + Added a table of contents to the book index pages using the `contents` directive.
.. + Moved the collection titles out of the `collection` directive and into the main document flow as section headings.

0.0.12
------
*2025-11-16*

**added**

.. + Implemented collection directives in the RST generation script to dynamically create sorted lists of definitions, postulates, common notions, and propositions.
.. + Added cumulative numbering for all elements across all books.
.. + Implemented note directives to render Heath's footnotes from the XML source.

0.0.11
------
*2025-11-16*

**changed**

.. + Refactored XML source files, consolidating them into book-level files.
.. + Corrected misplaced proposition reference in `elem.1.22`.

0.0.10
------
*2025-11-16*

**fixed**

.. + Corrected porism handling in the RST generation script to prevent duplicate content and ensure canonical IDs are used for headings.

0.0.9
-----
*2025-11-16*

**added**

.. + Added taxonomy fields to the generated RST files, including `:type:`, `:categories:`, and `:tags:`.

0.0.8
-----
*2025-11-16*

**changed**

.. + Updated the `elements_transform` script to include images in the generated RST files.
.. + Added `width` attribute to the figure directive to control image size.

**fixed**

.. + Removed placeholder figures from the generated RST files.

0.0.7
-----
*2025-11-15*

**added**

.. + Extended RST generation to include Books 1-6 of Euclid's Elements.

**changed**

.. + Removed the "Proof." heading from the generated RST files for a cleaner output.
.. - Deleted the old `generate_rsts.py` script, centralizing RST generation in the `elements_transform` tool.

0.0.6
-----
*2025-11-15*

**added**

.. + Support for parsing and generating RST for Book III of Euclid's Elements.

**fixed**

.. + Corrected RST reference linking for various element types (Definitions, Propositions, Common Notions).
.. + Addressed issue with porisms not being parsed and included in the generated RST files.

**changed**

.. + Refactored inline XML to RST conversion logic for better handling of nested tags and enunciation-specific formatting.

0.0.5
-----
*2025-11-15*

**fixed**

.. + Fixed XML parsing for nested tags within `<hi>` elements.
.. + Corrected handling of `<term>` elements to ensure proper bolding.
.. + Standardized enunciation formatting as blockquotes for Books I and II.

**added**

.. + Added Book II to the RST generation test suite.

0.0.4
-----
*2025-11-15*

**added**

.. + Added `elements_transform` script for converting Euclid's Elements from XML to RST.
.. + Established new, structured RST output in `docsrc/elements2/`.

**changed**

.. - Removed old, manually created documentation from `docsrc/elements/`.

0.0.3
-----
*2025-11-11*

**added**

.. + Added dependency extraction from XML files.
.. + Added fallback logic to handle XML files without explicit Enunc/Proof sections.

**changed**

.. + Improved RST generation to include a list of dependencies.