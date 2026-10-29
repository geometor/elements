:order: 308
:number: 308
:canonical_id: G.308
:original_id: IX.33
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, number, even-number, odd-number, reductio-ad-absurdum
:dependencies: G.305, G.307
:excerpt: If a number have its half odd, it is even-times odd only.

.. _G.308:
.. _IX.33:

G.308
=====

.. rubric:: `IX.33 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/33/>`_

.. enunciation::

   If a number have its half odd, it is even-times odd only.

For let the number :g:`A <0425.g1:A>` have its half odd;

I say that :g:`A <0425.g1:A>` is even-times odd only.

.. picture:: 0425.g1.svg
   :alt: Proposition 33 Diagram

.. assertion::

   Now that it is even-times odd is manifest; for the half of it, being odd, measures it an even number of times. :just:`[G.307] <G.307>`

I say next that it is also even-times odd only.

.. subclause::

   For, if :g:`A <0425.g1:A>` is even-times even also,

.. assertion::

   it will be measured by an even number according to an even number; :just:`[G.305] <G.305>`

.. assertion::

   so that the half of it will also be measured by an even number though it is odd: which is absurd.

.. assertion::

   Therefore :g:`A <0425.g1:A>` is even-times odd only.

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
     "G.305" [label="G.305", tooltip="G.305 (VII.def.8): An even-times even number is that which is measured by an even number according to an even number.", fillcolor="#224422", URL="../G.305/index.html", target="_top"];
     "G.307" [label="G.307", tooltip="G.307 (VII.def.9): An even-times odd number is that which is measured by an even number according to an odd number.", fillcolor="#224422", URL="../G.307/index.html", target="_top"];
     "G.308" [label="G.308", tooltip="G.308 (IX.33): If a number have its half odd, it is even-times odd only.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.308" -> "G.305";
     "G.308" -> "G.307";
   }
