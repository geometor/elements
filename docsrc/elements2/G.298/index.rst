:order: 298
:number: 298
:canonical_id: G.298
:original_id: IX.25
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, segment, number, even-number, odd-number
:dependencies: G.294, G.297
:excerpt: If from an even number an odd number be subtracted, the remainder will be odd.

.. _G.298:
.. _IX.25:

G.298
=====

.. rubric:: `IX.25 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/25/>`_

.. enunciation::

   If from an even number an odd number be subtracted, the remainder will be odd.

For from the even number :g:`/ A B / <0421.g1:/ A B />` let the odd number :g:`/ B C / <0421.g1:/ B C />` be subtracted ;

I say that the remainder :g:`/ A C / <0421.g1:/ A C />` is odd.

.. picture:: 0421.g1.svg
   :alt: Book IX, Proposition 25

For let the unit :g:`/ C D / <0421.g1:/ C D />` be subtracted from :g:`/ B C / <0421.g1:/ B C />` ;

.. assertion:: [G.294] <G.294>

   therefore :g:`/ B D / <0421.g1:/ B D />` is even.

.. subclause::

   But :g:`/ A B / <0421.g1:/ A B />` is also even ;

.. assertion:: [G.297] <G.297>

   therefore the remainder :g:`/ A D / <0421.g1:/ A D />` is also even.

.. subclause::

   And :g:`/ C D / <0421.g1:/ C D />` is an unit ;

.. assertion:: [G.294] <G.294>

   therefore :g:`/ A C / <0421.g1:/ A C />` is odd.

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
     "G.292" [label="G.292", tooltip="G.292 (VII.def.6): An even number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.292/index.html", target="_top"];
     "G.294" [label="G.294", tooltip="G.294 (VII.def.7): An odd number is that which is not divisible into two equal parts, or that which differs by an unit from an even number.", fillcolor="#224422", URL="../G.294/index.html", target="_top"];
     "G.297" [label="G.297", tooltip="G.297 (IX.24): If from an even number an even number be subtracted, the remainder will be even.", fillcolor="#222244", URL="../G.297/index.html", target="_top"];
     "G.298" [label="G.298", tooltip="G.298 (IX.25): If from an even number an odd number be subtracted, the remainder will be odd.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.297" -> "G.292";
     "G.298" -> "G.294";
     "G.298" -> "G.297";
   }
