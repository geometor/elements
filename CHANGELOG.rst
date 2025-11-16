changelog
=========

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

0.0.2
-----
*2025-11-11*

**fixed**

.. + 

**added**

.. + 

**changed**

.. + 

changelog
=========

0.1.0 
-----
*2023-11-15*

**fixed**

.. + Fixed bug in data processing (`#42 <https://github.com/example/repo/issues/42>`_)
.. + Improved error handling in API calls

**added**

.. + Fixed bug in data processing (`#42 <https://github.com/example/repo/issues/42>`_)
.. + Improved error handling in API calls

**changed**

.. + Fixed bug in data processing (`#42 <https://github.com/example/repo/issues/42>`_)
.. + Improved error handling in API calls