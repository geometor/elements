:canonical_id: G.287
:original_id: VII.31
:title: G.287 composite number measured
:volume: II
:book: VII
:type: prop

G.287 composite number measured — Heath
=======================================

.. rubric:: `VII.31 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/31/>`_

.. enunciation::

   Any :term:`composite number <G.286>` is :term:`measured <G.253>` by some :term:`prime number <G.283>`.

Let :g:`A <g1:A>` be a composite number;

I say that :g:`A <g1:A>` is measured by some prime number.

.. subclause::

   For, since :g:`A <g1:A>` is composite, some :term:`number <G.248>` will measure it.

Let a number measure it, and let it be :g:`B <g1:B>`.

.. picture:: g1.svg
   :alt: Proposition 31 diagram

.. subclause::

   Now, if :g:`B <g1:B>` is prime, what was enjoined will have been done.

.. subclause::

   But if it is composite, some number will measure it.

Let a number measure it, and let it be :g:`C <g1:C>`.

.. subclause::

   Then, since :g:`C <g1:C>` measures :g:`B <g1:B>`, and :g:`B <g1:B>` measures :g:`A <g1:A>`,

.. assertion::

   therefore :g:`C <g1:C>` also measures :g:`A <g1:A>`.

.. subclause::

   And, if :g:`C <g1:C>` is prime, what was enjoined will have been done.

.. subclause::

   But if it is composite, some number will measure it.

.. assertion::

   Thus, if the investigation be continued in this way, some prime number will be found which will measure the number before it, which will also measure :g:`A <g1:A>`.

.. subclause::

   For, if it is not found, an infinite series of numbers will measure the number :g:`A <g1:A>`, each of which is less than the other: which is impossible in numbers.

.. assertion::

   Therefore some prime number will be found which will measure the one before it, which will also measure :g:`A <g1:A>`.

.. assertion::

   Therefore any composite number is measured by some prime number.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.283" [label="G.283", tooltip="G.283 (VII.def.11): Aprime number is that which ismeasured by anunit alone.", fillcolor="#224422", URL="../G.283/index.html", target="_top"];
     "G.286" [label="G.286", tooltip="G.286 (VII.def.13): Acomposite number is that which ismeasured by somenumber.", fillcolor="#224422", URL="../G.286/index.html", target="_top"];
     "G.287" [label="G.287", tooltip="G.287 (VII.31): Any composite number is measured by some prime number.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.253" -> "G.169";
     "G.283" -> "G.169";
     "G.286" -> "G.169";
     "G.287" -> "G.169";
     "G.248" -> "G.247";
     "G.283" -> "G.247";
     "G.253" -> "G.248";
     "G.286" -> "G.248";
     "G.287" -> "G.248";
     "G.283" -> "G.253";
     "G.286" -> "G.253";
     "G.287" -> "G.283";
     "G.287" -> "G.286";
   }

Required for
------------

:ref:`G.288 <G.288>`, :ref:`G.343 <G.343>`, :ref:`G.350 <G.350>`, :ref:`G.364 <G.364>`, :ref:`G.370 <G.370>`
