:canonical_id: G.284
:original_id: VII.29
:title: G.284 prime number prime
:volume: II
:book: VII
:type: prop

G.284 prime number prime — Heath
================================

.. rubric:: `VII.29 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/29/>`_

.. enunciation::

   Any :term:`prime number <G.283>` is :term:`prime to <G.249>` any :term:`number <G.248>` which it does not :term:`measure <G.253>`.

Let :g:`A <g1:A>` be a prime number, and let it not measure :g:`B <g1:B>`;

I say that :g:`B <g1:B>`, :g:`A <g1:A>` are prime to one another.

.. picture:: g1.svg
   :alt: Book VII, Proposition 29

.. subclause::

   For, if :g:`B <g1:B>`, :g:`A <g1:A>` are not prime to one another, some number will measure them.

Let :g:`C <g1:C>` measure them.

.. subclause::

   Since :g:`C <g1:C>` measures :g:`B <g1:B>`, and :g:`A <g1:A>` does not measure :g:`B <g1:B>`,

.. assertion::

   therefore :g:`C <g1:C>` is not the same with :g:`A <g1:A>`.

.. subclause::

   Now, since :g:`C <g1:C>` measures :g:`B <g1:B>`, :g:`A <g1:A>`,

.. assertion::

   therefore it also measures :g:`A <g1:A>` which is prime, though it is not the same with it : which is impossible.

.. assertion::

   Therefore no number will measure :g:`B <g1:B>`, :g:`A <g1:A>`.

.. assertion::

   Therefore :g:`A <g1:A>`, :g:`B <g1:B>` are prime to one another.

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
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.249" [label="G.249", tooltip="G.249 (VII.def.12): Numbers prime to one another are those which aremeasured by anunit alone as a common measure.", fillcolor="#224422", URL="../G.249/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.283" [label="G.283", tooltip="G.283 (VII.def.11): Aprime number is that which ismeasured by anunit alone.", fillcolor="#224422", URL="../G.283/index.html", target="_top"];
     "G.284" [label="G.284", tooltip="G.284 (VII.29): Any prime number is prime to any number which it does not measure.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.249" -> "G.169";
     "G.253" -> "G.169";
     "G.283" -> "G.169";
     "G.284" -> "G.169";
     "G.248" -> "G.247";
     "G.249" -> "G.247";
     "G.283" -> "G.247";
     "G.253" -> "G.248";
     "G.284" -> "G.248";
     "G.284" -> "G.249";
     "G.283" -> "G.253";
     "G.284" -> "G.283";
   }

Required for
------------

:ref:`G.285 <G.285>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.344 <G.344>`, :ref:`G.364 <G.364>`, :ref:`G.370 <G.370>`
