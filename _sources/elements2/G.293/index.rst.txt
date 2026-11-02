:order: 293
:number: 293
:canonical_id: G.293
:original_id: VII.37
:title: G.293 number measured number
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, number, part-aliquot, unit, alternando
:dependencies: G.169, G.248, G.268
:excerpt: If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.

.. _G.293:
.. _VII.37:

G.293 number measured number
============================

.. rubric:: `VII.37 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/37/>`_

.. enunciation::

   If a :term:`number <G.248>` be :term:`measured <G.169>` by any number, the number which is measured will have a part called by the same name as the measuring number.

.. signature:: theorem

   | :fn:`number_measured_number <G.293>`\ ()
   | **prove** :g:`A <g1:A>` has a part called by the same name as :g:`B <g1:B>`

.. picture:: g1.svg
   :alt: Proposition 37

.. step:: construct

   Let the number :g:`A <g1:A>` be measured by any number :g:`B <g1:B>`

.. step:: assert

   As many times as :g:`B <g1:B>` measures :g:`A <g1:A>`, so many :term:`units <G.247>` let there be in :g:`C <g1:C>`.

.. step:: assert

   Since :g:`B <g1:B>` measures :g:`A <g1:A>` according to the units in :g:`C <g1:C>`, and the unit :g:`D <g1:D>` also measures the number :g:`C <g1:C>` according to the units in it,

.. step:: assert

   Therefore the unit :g:`D <g1:D>` measures the number :g:`C <g1:C>` the same number of times as :g:`B <g1:B>` measures :g:`A <g1:A>`.

.. step:: assert ∵ unit_measure_number <G.268>

   Therefore, :term:`alternately <G.194>`, the unit :g:`D <g1:D>` measures the number :g:`B <g1:B>` the same number of times as :g:`C <g1:C>` measures :g:`A <g1:A>`; therefore, whatever part the unit :g:`D <g1:D>` is of the number :g:`B <g1:B>`, the :term:`same part <G.253>` is :g:`C <g1:C>` of :g:`A <g1:A>` also.

.. step:: assert

   The unit :g:`D <g1:D>` is a part of the number :g:`B <g1:B>` called by the same name as it;

.. step:: conclude

   Therefore :g:`C <g1:C>` is also a part of :g:`A <g1:A>` called by the same name as :g:`B <g1:B>`, so that :g:`A <g1:A>` has a part :g:`C <g1:C>` which is called by the same name as :g:`B <g1:B>`.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (V.def.12): Alternate ratio means taking theantecedent in relation to the antecedent and the consequent in relation to the consequent.", fillcolor="#224422", URL="../G.194/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.254" [label="G.254", tooltip="G.254 (VII.def.4): Butparts when it does notmeasure it.", fillcolor="#224422", URL="../G.254/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.257" [label="G.257", tooltip="G.257 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.257/index.html", target="_top"];
     "G.258" [label="G.258", tooltip="G.258 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.258/index.html", target="_top"];
     "G.263" [label="G.263", tooltip="G.263 (VII.def.20): Numbers areproportional when the first is thesame multiple, or thesame part, or thesame parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.263/index.html", target="_top"];
     "G.265" [label="G.265", tooltip="G.265 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.265/index.html", target="_top"];
     "G.268" [label="G.268", tooltip="G.268 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.268/index.html", target="_top"];
     "G.293" [label="G.293", tooltip="G.293 (VII.37): If a number be measured by any number, the number which is measured will have a part called by the same name as the measuring number.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.170" -> "G.169";
     "G.253" -> "G.169";
     "G.254" -> "G.169";
     "G.256" -> "G.169";
     "G.268" -> "G.169";
     "G.293" -> "G.169";
     "G.257" -> "G.170";
     "G.194" -> "G.181";
     "G.265" -> "G.181";
     "G.268" -> "G.194";
     "G.248" -> "G.247";
     "G.268" -> "G.247";
     "G.253" -> "G.248";
     "G.256" -> "G.248";
     "G.257" -> "G.248";
     "G.258" -> "G.248";
     "G.265" -> "G.248";
     "G.268" -> "G.248";
     "G.293" -> "G.248";
     "G.257" -> "G.253";
     "G.263" -> "G.253";
     "G.258" -> "G.254";
     "G.263" -> "G.254";
     "G.257" -> "G.256";
     "G.263" -> "G.256";
     "G.258" -> "G.257";
     "G.265" -> "G.257";
     "G.265" -> "G.258";
     "G.265" -> "G.263";
     "G.268" -> "G.265";
     "G.293" -> "G.268";
   }

Required for
------------

:ref:`G.295 <G.295>`

.. toctree::
   :hidden:

   code
   heath
