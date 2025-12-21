geometor.elements.graph
=======================

.. py:module:: geometor.elements.graph

.. autoapi-nested-parse::

   Graph manipulation utilities (RST version).



Attributes
----------

.. autoapisummary::

   geometor.elements.graph.ROMAN_NUMERALS
   geometor.elements.graph.ROMAN_TO_INT


Functions
---------

.. autoapisummary::

   geometor.elements.graph.parse_rst_file
   geometor.elements.graph.build_graph


Module Contents
---------------

.. py:data:: ROMAN_NUMERALS

.. py:data:: ROMAN_TO_INT

.. py:function:: parse_rst_file(file_path: pathlib.Path) -> dict

   Parse an RST file to extract metadata and content.


.. py:function:: build_graph(source_dir: pathlib.Path | None = None) -> tuple[networkx.DiGraph, list[dict]]

   Build a NetworkX dependency graph from the RST source files.


