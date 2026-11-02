:canonical_id: G.355
:original_id: IX.24
:title: G.355 even number even
:volume: II
:book: IX
:type: prop

G.355 even number even — Heath
==============================

.. rubric:: `IX.24 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/24/>`_

.. enunciation::

   If from an :term:`even number <G.302>` an even number be subtracted, the remainder will be even.

For from the even number :g:`/ A B / <g1:/ A B />` let the even number :g:`/ B C / <g1:/ B C />` be subtracted :

I say that the remainder :g:`/ A C / <g1:/ A C />` is even.

.. picture:: g1.svg
   :alt: Book IX, Proposition 24

.. subclause::

   For, since :g:`/ A B / <g1:/ A B />` is even, it has a half part. :just:`[G.302] <G.302>`

.. subclause::

   For the same reason :g:`/ B C / <g1:/ B C />` also has a half part ;

.. assertion::

   so that the remainder [:g:`/ A C / <g1:/ A C />` also has a half part, and] :g:`/ A C / <g1:/ A C />` is therefore even.

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
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.355" [label="G.355", tooltip="G.355 (IX.24): If from an even number an even number be subtracted, the remainder is even.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.355" -> "G.302";
   }

Required for
------------

:ref:`G.356 <G.356>`, :ref:`G.357 <G.357>`, :ref:`G.358 <G.358>`
