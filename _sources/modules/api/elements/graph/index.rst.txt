elements.graph
==============

.. py:module:: elements.graph


Attributes
----------

.. autoapisummary::

   elements.graph.ROMAN_NUMERALS
   elements.graph.SECTION_TYPE_MAP
   elements.graph.CATEGORIES_KEYWORDS
   elements.graph.TAGS_KEYWORDS


Functions
---------

.. autoapisummary::

   elements.graph.get_taxonomy
   elements.graph.convert_inline_xml_to_rst
   elements.graph.parse_book_xml
   elements.graph.build_graph


Module Contents
---------------

.. py:data:: ROMAN_NUMERALS

.. py:data:: SECTION_TYPE_MAP

.. py:data:: CATEGORIES_KEYWORDS
   :value: ['construct', 'describe', 'bisect']


.. py:data:: TAGS_KEYWORDS
   :value: ['line', 'circle', 'triangle']


.. py:function:: get_taxonomy(enunciation_text)

.. py:function:: convert_inline_xml_to_rst(element, dependencies, is_enunciation=False)

.. py:function:: parse_book_xml(file_path, entry_number_start=0)

.. py:function:: build_graph(xml_dir=None)

