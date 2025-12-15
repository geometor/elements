geometor.elements.graph
=======================

.. py:module:: geometor.elements.graph

.. autoapi-nested-parse::

   Graph manipulation utilities.



Attributes
----------

.. autoapisummary::

   geometor.elements.graph.ROMAN_NUMERALS
   geometor.elements.graph.SECTION_TYPE_MAP
   geometor.elements.graph.CATEGORIES_KEYWORDS
   geometor.elements.graph.TAGS_KEYWORDS


Functions
---------

.. autoapisummary::

   geometor.elements.graph.get_taxonomy
   geometor.elements.graph.convert_inline_xml_to_rst
   geometor.elements.graph.parse_book_xml
   geometor.elements.graph.build_graph


Module Contents
---------------

.. py:data:: ROMAN_NUMERALS

.. py:data:: SECTION_TYPE_MAP

.. py:data:: CATEGORIES_KEYWORDS
   :value: ['construct', 'describe', 'bisect']


.. py:data:: TAGS_KEYWORDS
   :value: ['line', 'circle', 'triangle']


.. py:function:: get_taxonomy(enunciation_text: str) -> tuple[list[str], list[str]]

   Extract categories and tags from enunciation text.

   :param enunciation_text: The text of the enunciation.
   :type enunciation_text: str

   :returns: A tuple containing a list of categories and a list of tags.
   :rtype: tuple


.. py:function:: convert_inline_xml_to_rst(element: xml.etree.ElementTree.Element | None, dependencies: list[str], is_enunciation: bool = False) -> str

   Convert inline XML elements to RST format.


.. py:function:: parse_book_xml(file_path: str | pathlib.Path, entry_number_start: int = 0) -> tuple[dict, int]

   Parse a book XML file.


.. py:function:: build_graph(xml_dir: pathlib.Path | None = None) -> tuple[networkx.DiGraph, list[dict]]

   Build a NetworkX dependency graph from the XML source files.

   :param xml_dir: The directory containing the XML book files.
                   Defaults to 'resources/xml/books' in the project root.
   :type xml_dir: Path, optional

   :returns: A tuple containing the NetworkX DiGraph and a list of book data dictionaries.
   :rtype: tuple


