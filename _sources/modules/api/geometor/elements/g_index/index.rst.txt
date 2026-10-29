geometor.elements.g_index
=========================

.. py:module:: geometor.elements.g_index

.. autoapi-nested-parse::

   Generate the G-Index for Euclid's Elements.

   Processes the composed Heath Edition in `../euclid/docsrc/heath/` to produce:
   - Strictly numbered G-Index nodes (`G.1`, `G.2`, ...) in topological dependency order
   - GEOMETOR symbolic element indications in `:g:` roles (`/ A B /`, `< A B C >`, `< B A C )`, `( B C D )`, `[ A B ]`, `A`)
   - G-Index step justifications (`:just:`[G.4] <G.4>``, `.. assertion:: [G.2] <G.2>`)
   - Interactive inline SVG figures copied per G-node
   - Rich metadata (`:type:`, `:subtype:`, `:categories:`, `:tags:`, `:dependencies:`)
   - Transitive Graphviz dependency graphs and `Required for` back-links



Functions
---------

.. autoapisummary::

   geometor.elements.g_index.g_num_sort_key
   geometor.elements.g_index.transform_geom_roles
   geometor.elements.g_index.transform_justifications
   geometor.elements.g_index.transform_refs
   geometor.elements.g_index.clean_plain_excerpt
   geometor.elements.g_index.wrap_as_enunciation
   geometor.elements.g_index.generate_g_dot
   geometor.elements.g_index.sync_apparatus_resources
   geometor.elements.g_index.generate_g_index


Module Contents
---------------

.. py:function:: g_num_sort_key(g_name: str) -> int

   Return integer index for a 'G.<n>' identifier.


.. py:function:: transform_geom_roles(rst_text: str) -> str

   Replace cryptic `$AB$` display labels in `:g:` roles with GEOMETOR symbolic indications.

   Examples:
   - ``:g:`$AB$ <0255.g1:/ A B />``` -> ``:g:`/ A B / <0255.g1:/ A B />```
   - ``:g:`$ABC$ <0255.g1:< A B C >>``` -> ``:g:`< A B C > <0255.g1:< A B C >>```
   - ``:g:`$BAC$ <0261.g1:< B A C )>``` -> ``:g:`< B A C ) <0261.g1:< B A C )>```
   - ``:g:`$BCD$ <0255.g1:( B C D )>``` -> ``:g:`( B C D ) <0255.g1:( B C D )>```
   - ``:g:`$A$ <0255.g1:A>``` -> ``:g:`A <0255.g1:A>```


.. py:function:: transform_justifications(rst_text: str, current_book: str, id_map: Dict[str, str]) -> str

   Rewrite `:just:` roles and `.. assertion::` / `.. subclause::` justifications to G-Index IDs.


.. py:function:: transform_refs(rst_text: str, id_map: Dict[str, str]) -> str

   Rewrite any `:ref:` roles whose target is in `id_map` to the corresponding G-ID.


.. py:function:: clean_plain_excerpt(rst_body: str) -> str

   Extract a clean one-line plain-text excerpt from the enunciation or first paragraph.


.. py:function:: wrap_as_enunciation(statement_rst: str) -> str

   Wrap a definition, postulate, or common notion statement in an `.. enunciation::` block.


.. py:function:: generate_g_dot(G: networkx.DiGraph, node_ref: str, id_map: Dict[str, str]) -> str

   Generate a Graphviz DOT string for the transitive proof chain of `node_ref` using G-IDs.


.. py:function:: sync_apparatus_resources(project_root: pathlib.Path) -> None

   Copy glossary.json, persons.json, citations.json, and enunciations.json from euclid/resources/heath/ into elements/resources/.


.. py:function:: generate_g_index(output_dir: Optional[pathlib.Path] = None, books: Optional[List[str]] = None) -> Dict[str, Any]

   Generate the complete G-Index RST structure from ../euclid/docsrc/heath/.

   :param output_dir: Directory to write generated G-Index RST files (`docsrc/elements2`).
   :param books: Optional list of Roman book numerals to include (defaults to all 13 books).

   :returns: Summary statistics dictionary.


