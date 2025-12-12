geometor.elements
=================

.. py:module:: geometor.elements

.. autoapi-nested-parse::

   Tools for modeling and rendering geometric constructions from Euclid's Elements.

   Key Components:
   ---------------
   - **XML Parsing**: Tools (:func:`parse_element_xml`) to parse the XML source of Euclid's Elements.
   - **RST Generation**: Tools (:func:`generate_rst_from_xml`) to convert XML to ReStructuredText.
   - **Graphing**: Tools (:func:`build_graph`, :func:`generate_g_index`) to build dependency graphs and indexes.

   Usage:
   ------
   Use the provided functions to parse XML files and generate documentation.



Submodules
----------

.. toctree::
   :maxdepth: 1

   /modules/api/geometor/elements/__main__/index
   /modules/api/geometor/elements/app/index
   /modules/api/geometor/elements/elements/index
   /modules/api/geometor/elements/g_index/index
   /modules/api/geometor/elements/graph/index
   /modules/api/geometor/elements/ingest/index
   /modules/api/geometor/elements/legacy/index
   /modules/api/geometor/elements/rst_builder/index
   /modules/api/geometor/elements/rst_generator/index
   /modules/api/geometor/elements/transform/index
   /modules/api/geometor/elements/utils/index
   /modules/api/geometor/elements/xml_parser/index


Functions
---------

.. autoapisummary::

   geometor.elements.parse_element_xml
   geometor.elements.generate_rst_from_xml
   geometor.elements.build_rst_docs
   geometor.elements.generate_g_index
   geometor.elements.build_graph


Package Contents
----------------

.. py:function:: parse_element_xml(file_path: pathlib.Path)

   Parse a single element XML file.

   :param file_path: The path to the XML file.
   :type file_path: Path

   :returns: A dictionary containing the parsed element data (id, type, head, enunciation, etc.).
   :rtype: dict


.. py:function:: generate_rst_from_xml(xml_file_path: pathlib.Path, output_dir: pathlib.Path)

   Generate an RST file from an XML element file.

   :param xml_file_path: The path to the input XML file.
   :type xml_file_path: Path
   :param output_dir: The directory where the output RST file will be saved.
   :type output_dir: Path


.. py:function:: build_rst_docs(xml_dir: pathlib.Path, output_dir: pathlib.Path)

   Parses all XML files in xml_dir and generates RST files in output_dir.


.. py:function:: generate_g_index(output_dir: pathlib.Path | None = None) -> None

   Generate the G-Index (dependency graph index) for the elements.

   :param output_dir: The directory to output the generated RST files.
                      Defaults to the 'elements2' directory in the project root.
   :type output_dir: Path, optional


.. py:function:: build_graph(xml_dir: pathlib.Path | None = None) -> tuple[networkx.DiGraph, list[dict]]

   Build a NetworkX dependency graph from the XML source files.

   :param xml_dir: The directory containing the XML book files.
                   Defaults to 'resources/xml/books' in the project root.
   :type xml_dir: Path, optional

   :returns: A tuple containing the NetworkX DiGraph and a list of book data dictionaries.
   :rtype: tuple


