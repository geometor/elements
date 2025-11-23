# Background

This project has been through a number of iterations over the years. Beginning
with the xml content, we produced all 13 books as Grav markdown files for each
element. And books 1 & 2 are fairly clean and well structured. But a lot of this work was done with macros in vim. 

Many scripts were written to do this parsing along the way - the code is
scattered around the repo. It was done piecemeal with little documentation. And we have found that the xml tags used in each book is slightly different.

Hovever, we want to get the whole thing into RST with our Sphinx customization.
This platform will provide tremendous capabilities for cross-linking refs,
glossaries, etc.


# Goals

The project will focus on the following:

- **Formalization**: Translating the text of Euclid's Elements into a more structured and machine-readable format. Semantically and symbolically consistent throughout.
- **Dependency Mapping**: Identifying the dependency chain between definitions, postulates, and propositions.
- **Content Transformation**: Converting the xml content from the `resources` folder into reStructuredText (RST) within the `docsrc/elements2` directory. This will involve:
    -   Retitling propositions for clarity.
    -   Establishing a consistent categorization and linking system.
    -   Integrating with Sphinx for documentation generation.
- **Canonical Consistency** - links and labelling - predicable urls

I want to start over, from the xml element files, reparsing the xml directly
into what we need for RST. The books have been cleanly split into xml files for
each element. We can examine these and develop new translations scripts to
create the RST structure we are looking for.

But before we begin we need to document the process and design the system for
organization. In `docsrc/elements` I experimented with departing from numbered
indexes to phrases - which would be the key for refs and the url path. This is
tedious, however a reference like "Book3 prop11" or worse "III.11" is useless semantically.

# Current Progress

- The `elements_transform` script (located at `src/geometor/elements/transform.py`) has been updated to generate RST for all 13 books of the Elements.
- The output directory for generated RST has been moved to `docsrc/heath`.
- Extracted graphic images are now inverted (white lines on black background) for better visibility in dark mode environments.
- Fixed `width` attributes have been removed from figure directives in the generated RST to allow for responsive sizing.
- The XML parsing ignores `<lb>` and `<pb>` tags during RST generation.
- Collection and note directives are implemented for dynamic lists and Heath's footnotes.
- A new, comprehensive, modular ingestion pipeline (`src/geometor/elements/ingest`) has been established to process Heath's Euclid from PDF sources.
- This pipeline supports full extraction and organization of text and images for all three volumes of Euclid's Elements.
- A separate refinement pipeline handles the analysis of propositions, dynamic cropping of images, and graphic extraction.
- `scan_propositions.py` generates `index.json` files within each book's `propositions` directory (e.g., `resources/heath/volume_I/book_i/propositions/index.json`), supporting per-book scanning.
- `scan_propositions.py` accurately scans propositions, calculating pixel-based offsets for cropping (respecting header/footer margins).
- `stitch_propositions.py` consumes the per-book indexes to generate stitched proposition images in `resources/heath/propositions/`.
- `process_book.sh` allows for easy batch processing (scanning and stitching) of a single book by ID (e.g., `I`).
- Canonical naming for cropped images (e.g., `I.1.png`) is consistently applied.
- Extracted graphics are now saved in the same directory as cropped propositions (`resources/heath/cropped/`) with the suffix `.graphic.png`.
- Added safeguards to `scan_propositions.py` and `cropping.py` to prevent accidental overwrites of manual index tweaks.
- Integrated automatic bleed removal and image cleanup into the proposition stitching pipeline to improve image quality.
- Legacy scripts for image processing have been deprecated or moved.