geometor.elements.transform
===========================

.. py:module:: geometor.elements.transform


Attributes
----------

.. autoapisummary::

   geometor.elements.transform.ROMAN_NUMERALS
   geometor.elements.transform.SECTION_TYPE_MAP
   geometor.elements.transform.CATEGORIES_KEYWORDS
   geometor.elements.transform.TAGS_KEYWORDS


Functions
---------

.. autoapisummary::

   geometor.elements.transform.get_taxonomy
   geometor.elements.transform.convert_inline_xml_to_rst
   geometor.elements.transform.parse_book_xml
   geometor.elements.transform.analyze_dependencies
   geometor.elements.transform.generate_proof_chain_dot
   geometor.elements.transform.generate_rst_files
   geometor.elements.transform.generate_dependency_graph
   geometor.elements.transform.main


Module Contents
---------------

.. py:data:: ROMAN_NUMERALS

.. py:data:: SECTION_TYPE_MAP

.. py:data:: CATEGORIES_KEYWORDS
   :value: ['construct', 'describe', 'bisect']


.. py:data:: TAGS_KEYWORDS
   :value: ['line', 'circle', 'triangle']


.. py:function:: get_taxonomy(enunciation_text: str) -> tuple[list[str], list[str]]

.. py:function:: convert_inline_xml_to_rst(element: xml.etree.ElementTree.Element | None, dependencies: list[str], is_enunciation: bool = False) -> str

.. py:function:: parse_book_xml(file_path: str | pathlib.Path, entry_number_start: int = 0) -> tuple[dict, int]

.. py:function:: analyze_dependencies(graph: networkx.DiGraph, element_ref: str) -> dict[str, list[str]]

   Analyzes the dependency graph for a given element.
   An edge u -> v means u depends on v.


.. py:function:: generate_proof_chain_dot(graph: networkx.DiGraph, element_ref: str, ref_to_path_map: dict[str, tuple[str, str]]) -> str

.. py:function:: generate_rst_files(book_data: dict, output_dir: str | pathlib.Path, graph: networkx.DiGraph, ref_to_path_map: dict[str, tuple[str, str]], metadata: dict) -> None

.. py:function:: generate_dependency_graph(graph: networkx.DiGraph, output_dir: str | pathlib.Path = 'docsrc/elements2') -> None

.. py:function:: main()

