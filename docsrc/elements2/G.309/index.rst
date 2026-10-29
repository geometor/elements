:order: 309
:number: 309
:canonical_id: G.309
:original_id: IX.34
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, number, even-number, odd-number, reductio-ad-absurdum
:dependencies: G.305
:excerpt: If a number neither be one of those which are continually doubled from a dyad, nor have its half odd, it is both even-times even and even-times odd.

.. _G.309:
.. _IX.34:

G.309
=====

.. rubric:: `IX.34 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/34/>`_

.. enunciation::

   If a number neither be one of those which are continually doubled from a dyad, nor have its half odd, it is both even-times even and even-times odd.

For let the number :g:`A <0425.g2:A>` neither be one of those doubled from a dyad, nor have its half odd;

I say that :g:`A <0425.g2:A>` is both even-times even and even-times odd.

.. picture:: 0425.g2.svg
   :alt: Proposition 34 Diagram

.. assertion::

   Now that :g:`A <0425.g2:A>` is even-times even is manifest; for it has not its half odd. :just:`[G.305] <G.305>`

I say next that it is also even-times odd.

.. subclause::

   For, if we bisect :g:`A <0425.g2:A>`, then bisect its half, and do this continually, we shall come upon some odd number which will measure :g:`A <0425.g2:A>` according to an even number.

.. subclause::

   For, if not, we shall come upon a dyad, and :g:`A <0425.g2:A>` will be among those which are doubled from a dyad: which is contrary to the hypothesis.

.. assertion::

   Thus :g:`A <0425.g2:A>` is even-times odd.

.. subclause::

   But it was also proved even-times even.

.. assertion::

   Therefore :g:`A <0425.g2:A>` is both even-times even and even-times odd.

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
     "G.309" [label="G.309", tooltip="G.309 (IX.34): If a number neither be one of those which are continually doubled from a dyad, nor have its half odd, it is both even-times even and even-times odd.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.309" -> "G.305";
   }
