elements.transform
==================

.. py:module:: elements.transform


Attributes
----------

.. autoapisummary::

   elements.transform.ROMAN_NUMERALS
   elements.transform.SECTION_TYPE_MAP
   elements.transform.CATEGORIES_KEYWORDS
   elements.transform.TAGS_KEYWORDS


Functions
---------

.. autoapisummary::

   elements.transform.get_taxonomy
   elements.transform.convert_inline_xml_to_rst
   elements.transform.parse_book_xml
   elements.transform.analyze_dependencies
   elements.transform.generate_proof_chain_dot
   elements.transform.generate_rst_files
   elements.transform.generate_dependency_graph
   elements.transform.main


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

.. py:function:: analyze_dependencies(graph, element_ref)

   Analyzes the dependency graph for a given element.
   An edge u -> v means u depends on v.


.. py:function:: generate_proof_chain_dot(graph, element_ref, ref_to_path_map)

.. py:function:: generate_rst_files(book_data, output_dir, graph, ref_to_path_map, metadata)

.. py:function:: generate_dependency_graph(graph, output_dir='docsrc/elements2')

.. py:function:: main()

