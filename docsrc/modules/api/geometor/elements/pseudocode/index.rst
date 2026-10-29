geometor.elements.pseudocode
============================

.. py:module:: geometor.elements.pseudocode

.. autoapi-nested-parse::

   Pseudocode and tightened enunciation generator for GEOMETOR Elements 2.0.

   Transforms classical Heath RST propositions and statements into tightened,
   fact-oriented enunciations and structured ``.. step:: <kind> [justification]``
   sequences highlighting the GEOMETOR functional hierarchy (``given``,
   ``construct``, ``intersect``, ``assert``, ``conclude``) and native symbolic
   indications.



Attributes
----------

.. autoapisummary::

   geometor.elements.pseudocode.CURATED_ENUNCIATIONS


Functions
---------

.. autoapisummary::

   geometor.elements.pseudocode.tighten_enunciation_text
   geometor.elements.pseudocode.generate_pseudocode_rst


Module Contents
---------------

.. py:data:: CURATED_ENUNCIATIONS
   :type:  Dict[str, str]

.. py:function:: tighten_enunciation_text(text: str, canonical_ref: str = '') -> str

   Return a concise, fact-oriented enunciation string.


.. py:function:: generate_pseudocode_rst(heath_content_rst: str, canonical_ref: str, node_type: str) -> str

   Transform a Heath RST body (with G-Index roles/justifications) into Track 1 Pseudocode RST.


