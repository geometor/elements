geometor.elements.graph
=======================

.. py:module:: geometor.elements.graph

.. autoapi-nested-parse::

   Graph construction and semantic metadata extraction for GEOMETOR Elements.

   Crawls the composed Heath Edition RST source in `../euclid/docsrc/heath/` across
   all 3 volumes (Books I–XIII), extracting discrete nodes for definitions,
   postulates, common notions, and propositions, along with their dependency edges,
   interactive SVG diagrams, categories, and semantic tags.



Attributes
----------

.. autoapisummary::

   geometor.elements.graph.ROMAN_NUMERALS
   geometor.elements.graph.ROMAN_TO_INT
   geometor.elements.graph.VALID_BOOKS
   geometor.elements.graph.BOOK_TO_VOLUME
   geometor.elements.graph.BOOK_DOMAIN_CATEGORIES
   geometor.elements.graph.SECTION_TYPE_ORDER
   geometor.elements.graph.G_DEP_TYPE_ORDER
   geometor.elements.graph.CONCEPT_PATTERNS


Functions
---------

.. autoapisummary::

   geometor.elements.graph.normalize_canonical_id
   geometor.elements.graph.get_node_type
   geometor.elements.graph.canonical_sort_key
   geometor.elements.graph.g_dependency_sort_key
   geometor.elements.graph.infer_justification_target
   geometor.elements.graph.parse_justification_arg
   geometor.elements.graph.parse_metadata_and_body
   geometor.elements.graph.strip_folio_milestones
   geometor.elements.graph.strip_footnotes
   geometor.elements.graph.extract_primitive_tags
   geometor.elements.graph.extract_taxonomy
   geometor.elements.graph.parse_grouped_items_file
   geometor.elements.graph.parse_proposition_file
   geometor.elements.graph.build_graph


Module Contents
---------------

.. py:data:: ROMAN_NUMERALS

.. py:data:: ROMAN_TO_INT

.. py:data:: VALID_BOOKS

.. py:data:: BOOK_TO_VOLUME

.. py:data:: BOOK_DOMAIN_CATEGORIES
   :type:  Dict[str, List[str]]

.. py:data:: SECTION_TYPE_ORDER

.. py:data:: G_DEP_TYPE_ORDER

.. py:data:: CONCEPT_PATTERNS
   :type:  List[Tuple[str, re.Pattern[str]]]

.. py:function:: normalize_canonical_id(ref_id: str) -> str

   Normalize cross-book shared definition IDs (e.g. VIII.def.20 -> VII.def.20).


.. py:function:: get_node_type(ref_id: str) -> str

   Classify a canonical Euclid ID into 'prop', 'def', 'post', or 'cn'.


.. py:function:: canonical_sort_key(ref_id: str, type_order_map: Optional[Dict[str, int]] = None) -> Tuple[int, int, int, int, str]

   Return a deterministic sort key for canonical Euclid IDs.


.. py:function:: g_dependency_sort_key(ref_id: str) -> Tuple[int, int, int, int, str]

   Sort key for G-Index dependency traversal (cn, def, post, prop).


.. py:function:: infer_justification_target(display: str, current_book: Optional[str] = None) -> Optional[str]

   Infer canonical target ID(s) from justification text when <target> is omitted.


.. py:function:: parse_justification_arg(raw_arg: str, current_book: Optional[str] = None) -> Tuple[str, Optional[str]]

   Parse a justification string into (display_text, normalized_target_ids).


.. py:function:: parse_metadata_and_body(rst_text: str) -> Tuple[Dict[str, str], str]

   Split an RST document into its leading field-list metadata dict and remaining body.


.. py:function:: strip_folio_milestones(rst_body: str) -> str

   Remove .. _folio-...: labels and .. folio:: directives from an RST body.


.. py:function:: strip_footnotes(rst_body: str) -> str

   Remove Heath's inline footnote references ([#f1]_) and footnote definition blocks (.. [#f1] ...).


.. py:function:: extract_primitive_tags(rst_body: str) -> List[str]

   Identify GEOMETOR geometric primitive tags from :g: role targets in rst_body.


.. py:function:: extract_taxonomy(node_ref: str, node_type: str, book_roman: str, rst_body: str) -> Tuple[List[str], List[str], Optional[str]]

   Derive (categories, tags, subtype) for a G-Index node from its content and structure.


.. py:function:: parse_grouped_items_file(rst_path: pathlib.Path, heath_root: pathlib.Path) -> List[Dict[str, Any]]

   Extract individual anchored items (definitions, postulates, common notions) from a grouped RST file.


.. py:function:: parse_proposition_file(rst_path: pathlib.Path, heath_root: pathlib.Path) -> Dict[str, Any]

   Parse a composed proposition index.rst file from euclid/docsrc/heath/.


.. py:function:: build_graph(source_dir: Optional[pathlib.Path] = None, books: Optional[List[str]] = None) -> Tuple[networkx.DiGraph, List[Dict[str, Any]]]

   Build the complete NetworkX dependency graph from ../euclid/docsrc/heath/.

   :param source_dir: Path to `euclid/docsrc/heath`. Defaults to sibling repo.
   :param books: Optional list of Roman book numerals to include (defaults to I..XIII).

   :returns: Tuple of (DiGraph, all_books_data).


