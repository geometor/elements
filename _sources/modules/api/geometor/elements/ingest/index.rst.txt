geometor.elements.ingest
========================

.. py:module:: geometor.elements.ingest

.. autoapi-nested-parse::

   Geometor Elements Ingestion Pipeline

   This module contains the tools and logic for ingesting Euclid's Elements from
   PDF sources (Heath edition), organizing them, and extracting propositions and metadata.

   Pipeline Stages:
   1. Ingestion (`pipeline.py`):

       - Extraction (`extraction.py`): Converts PDF pages to images and text, and extracts the Table of Contents.
       - Organization (`organization.py`): Structures the extracted files into folders based on the TOC.

   2. Refinement (`refine.py`):

       - Analysis (`analysis.py`): Scans the text to identify and index propositions.
       - Cropping (`cropping.py`): Crops proposition text and extracts graphics based on manual instructions.
       - Metadata (`metadata_extraction/metadata_extraction.py`): Extracts metadata for documentation generation.

   Usage:
       Run the ingestion pipeline:
       $ python -m geometor.elements.ingest.pipeline

       Run the refinement pipeline:
       $ python -m geometor.elements.ingest.refine



Submodules
----------

.. toctree::
   :maxdepth: 1

   /modules/api/geometor/elements/ingest/analysis/index
   /modules/api/geometor/elements/ingest/cleanup/index
   /modules/api/geometor/elements/ingest/compare_models/index
   /modules/api/geometor/elements/ingest/config/index
   /modules/api/geometor/elements/ingest/cropping/index
   /modules/api/geometor/elements/ingest/detect_graphics/index
   /modules/api/geometor/elements/ingest/detect_graphics_cv/index
   /modules/api/geometor/elements/ingest/extraction/index
   /modules/api/geometor/elements/ingest/generate_index/index
   /modules/api/geometor/elements/ingest/image_processing/index
   /modules/api/geometor/elements/ingest/metadata_extraction/index
   /modules/api/geometor/elements/ingest/organization/index
   /modules/api/geometor/elements/ingest/pipeline/index
   /modules/api/geometor/elements/ingest/refine/index
   /modules/api/geometor/elements/ingest/scan_propositions/index
   /modules/api/geometor/elements/ingest/stitch_propositions/index
   /modules/api/geometor/elements/ingest/utils/index


Functions
---------

.. autoapisummary::

   geometor.elements.ingest.run_pipeline
   geometor.elements.ingest.run_refinement


Package Contents
----------------

.. py:function:: run_pipeline()

.. py:function:: run_refinement()

