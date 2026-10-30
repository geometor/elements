:order: 281
:number: 281
:canonical_id: G.281
:original_id: IX.11
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, proportion, unit, number, continued-proportion, porism
:dependencies: G.215
:excerpt: If as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the proportional numbers.

.. _G.281:
.. _IX.11:

G.281
=====

.. rubric:: `IX.11 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/11/>`_

.. enunciation::

   If as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the proportional numbers.

.. signature:: theorem

   | :fn:`many_numbers_please_ix_11 <G.281>`\ (:g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>`)
   | **given** there be as many numbers as we please, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>`, beginning from the unit :g:`A <g1:A>` and in continued proportion
   | **prove** :g:`B <g1:B>`, the least of the numbers :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>`, measures :g:`E <g1:E>` according to some one of the numbers :g:`C <g1:C>`, :g:`D <g1:D>`

.. picture:: g1.svg
   :alt: Proposition 11 Diagram

.. step:: given

   there be as many numbers as we please, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>`, beginning from the unit :g:`A <g1:A>` and in continued proportion

.. step:: assert

   For since, as the unit :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`D <g1:D>` to :g:`E <g1:E>`,

.. step:: assert

   Therefore the unit :g:`A <g1:A>` measures the number :g:`B <g1:B>` the same number of times as :g:`D <g1:D>` measures :g:`E <g1:E>`;

.. step:: assert ∵ unit_measure_number <G.215>

   Therefore, alternately, the unit :g:`A <g1:A>` measures :g:`D <g1:D>` the same number of times as :g:`B <g1:B>` measures :g:`E <g1:E>`.

.. step:: assert

   The unit :g:`A <g1:A>` measures :g:`D <g1:D>` according to the units in it;

.. step:: assert

   Therefore :g:`B <g1:B>` also measures :g:`E <g1:E>` according to the units in :g:`D <g1:D>`;

.. step:: assert

   So that :g:`B <g1:B>` the less measures :g:`E <g1:E>` the greater according to some number of those which have place among the proportional numbers.—

.. step:: conclude

   PORISM. And it is manifest that, whatever place the measuring number has, reckoned from the unit, the same place also has the number according to which it measures, reckoned from the number measured, in the direction of the number before it.—

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
     "G.281" [label="G.281", tooltip="G.281 (IX.11): If as many numbers as we please beginning from an unit be in continued proportion, the less measures the greater according to some one of the numbers which have place among the pro...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.205" -> "G.204";
     "G.212" -> "G.204";
     "G.212" -> "G.205";
     "G.212" -> "G.210";
     "G.215" -> "G.212";
     "G.281" -> "G.215";
   }

Required for
------------

:ref:`G.283 <G.283>`, :ref:`G.284 <G.284>`, :ref:`G.306 <G.306>`, :ref:`G.312 <G.312>`

.. toctree::
   :hidden:

   code
   heath
