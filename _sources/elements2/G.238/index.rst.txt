:order: 238
:number: 238
:canonical_id: G.238
:original_id: VII.37
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, number
:dependencies: G.215
:excerpt: If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.

.. _G.238:
.. _VII.37:

G.238
=====

.. rubric:: `VII.37 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/37/>`_

.. enunciation::

   If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.

For let the number :g:`A <0347.g1:A>` be measured by any number :g:`B <0347.g1:B>`;

I say that :g:`A <0347.g1:A>` has a part called by the same name as :g:`B <0347.g1:B>`.

.. picture:: 0347.g1.svg
   :alt: Proposition 37

For, as many times as :g:`B <0347.g1:B>` measures :g:`A <0347.g1:A>`, so many units let there be in :g:`C <0347.g1:C>`.

.. subclause::

   Since :g:`B <0347.g1:B>` measures :g:`A <0347.g1:A>` according to the units in :g:`C <0347.g1:C>`, and the unit :g:`D <0347.g1:D>` also measures the number :g:`C <0347.g1:C>` according to the units in it,

.. assertion::

   therefore the unit :g:`D <0347.g1:D>` measures the number :g:`C <0347.g1:C>` the same number of times as :g:`B <0347.g1:B>` measures :g:`A <0347.g1:A>`.

.. assertion::

   Therefore, alternately, the unit :g:`D <0347.g1:D>` measures the number :g:`B <0347.g1:B>` the same number of times as :g:`C <0347.g1:C>` measures :g:`A <0347.g1:A>`; :just:`[G.215] <G.215>` therefore, whatever part the unit :g:`D <0347.g1:D>` is of the number :g:`B <0347.g1:B>`, the same part is :g:`C <0347.g1:C>` of :g:`A <0347.g1:A>` also.

.. subclause::

   But the unit :g:`D <0347.g1:D>` is a part of the number :g:`B <0347.g1:B>` called by the same name as it;

.. assertion::

   therefore :g:`C <0347.g1:C>` is also a part of :g:`A <0347.g1:A>` called by the same name as :g:`B <0347.g1:B>`, so that :g:`A <0347.g1:A>` has a part :g:`C <0347.g1:C>` which is called by the same name as :g:`B <0347.g1:B>`.

.. qed::

   :just:`Q. E. D.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.204" [label="G.204", tooltip="G.204 (VII.5): If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.204/index.html", target="_top"];
     "G.205" [label="G.205", tooltip="G.205 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.205/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VII.def.20): **Numbers** are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.210/index.html", target="_top"];
     "G.212" [label="G.212", tooltip="G.212 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.212/index.html", target="_top"];
     "G.215" [label="G.215", tooltip="G.215 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.215/index.html", target="_top"];
     "G.238" [label="G.238", tooltip="G.238 (VII.37): If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.205" -> "G.204";
     "G.212" -> "G.204";
     "G.212" -> "G.205";
     "G.212" -> "G.210";
     "G.215" -> "G.212";
     "G.238" -> "G.215";
   }

Required for
------------

:ref:`G.240 <G.240>`
