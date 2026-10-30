geometor.elements.pseudocode
============================

.. py:module:: geometor.elements.pseudocode

.. autoapi-nested-parse::

   Pseudocode, formal signature, and tightened enunciation generator for GEOMETOR Elements 2.0.

   Transforms classical Heath RST propositions and statements into:
   - Tightened, fact-oriented enunciations (``.. enunciation::``)
   - Formal proposition/rule signatures (``.. signature::``) with ``given`` and ``construct`` / ``prove`` contracts
   - Composable function invocations (``:fn:`name <G.x>`(...) → ...``) for ``construct`` steps
   - Symbolic intersection steps (``... ∩ ... → ...``) for ``intersect`` steps
   - Semantic rule justifications (``∵ rule_name``) for ``assert`` / ``conclude`` steps



Attributes
----------

.. autoapisummary::

   geometor.elements.pseudocode.CURATED_ENUNCIATIONS
   geometor.elements.pseudocode.SEMANTIC_NAMES


Functions
---------

.. autoapisummary::

   geometor.elements.pseudocode.get_semantic_name
   geometor.elements.pseudocode.tighten_enunciation_text
   geometor.elements.pseudocode.generate_pseudocode_rst


Module Contents
---------------

.. py:data:: CURATED_ENUNCIATIONS
   :type:  Dict[str, str]

.. py:data:: SEMANTIC_NAMES
   :type:  Dict[str, str]

.. py:function:: get_semantic_name(canonical_ref: str, node_type: str = 'prop', subtype: Optional[str] = None, enun_text: str = '') -> str

   Return a concise snake_case function or rule name for any G-node.


.. py:function:: tighten_enunciation_text(text: str, canonical_ref: str = '') -> str

   Return a concise, fact-oriented enunciation string.


.. py:function:: generate_pseudocode_rst(heath_content_rst: str, canonical_ref: str, node_type: str, g_name: str = '', subtype: Optional[str] = None, id_map: Optional[Dict[str, str]] = None, g_to_sem_name: Optional[Dict[str, str]] = None) -> str

   Transform a Heath RST body (with G-Index roles/justifications) into Track 1 Pseudocode RST.


