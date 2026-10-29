:canonical_id: G.239
:original_id: VII.38
:volume: II
:book: VII
:type: prop

G.239 — Heath
=============

.. rubric:: `VII.38 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/38/>`_

.. enunciation::

   If a number have any part whatever, it will be measured by a number called by the same name as the part.

For let the number :g:`A <g1:A>` have any part whatever, :g:`B <g1:B>`, and let :g:`C <g1:C>` be a number called by the same name as the part :g:`B <g1:B>`;

I say that :g:`C <g1:C>` measures :g:`A <g1:A>`.

.. picture:: g1.svg
   :alt: Proposition 38

.. subclause::

   For, since :g:`B <g1:B>` is a part of :g:`A <g1:A>` called by the same name as :g:`C <g1:C>`, and the unit :g:`D <g1:D>` is also a part of :g:`C <g1:C>` called by the same name as it,

.. assertion::

   therefore, whatever part the unit :g:`D <g1:D>` is of the number :g:`C <g1:C>`, the same part is :g:`B <g1:B>` of :g:`A <g1:A>` also;

.. assertion::

   therefore the unit :g:`D <g1:D>` measures the number :g:`C <g1:C>` the same number of times that :g:`B <g1:B>` measures :g:`A <g1:A>`.

.. assertion::

   Therefore, alternately, the unit :g:`D <g1:D>` measures the number :g:`B <g1:B>` the same number of times that :g:`C <g1:C>` measures :g:`A <g1:A>`. :just:`[G.215] <G.215>`

.. assertion::

   Therefore :g:`C <g1:C>` measures :g:`A <g1:A>`.

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
     "G.204" [label="G.204", tooltip="G.204 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.204/index.html", target="_top"];
     "G.205" [label="G.205", tooltip="G.205 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.205/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VII.def.20): **Numbers** areproportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.210/index.html", target="_top"];
     "G.212" [label="G.212", tooltip="G.212 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.212/index.html", target="_top"];
     "G.215" [label="G.215", tooltip="G.215 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.215/index.html", target="_top"];
     "G.239" [label="G.239", tooltip="G.239 (VII.38): If a number have any part whatever, it is measured by a number called by the same name as the part.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.205" -> "G.204";
     "G.212" -> "G.204";
     "G.212" -> "G.205";
     "G.212" -> "G.210";
     "G.215" -> "G.212";
     "G.239" -> "G.215";
   }

Required for
------------

:ref:`G.240 <G.240>`
