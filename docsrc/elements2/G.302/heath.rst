:canonical_id: G.302
:original_id: IX.29
:volume: II
:book: IX
:type: prop

G.302 — Heath
=============

.. rubric:: `IX.29 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/29/>`_

.. enunciation::

   If an odd number by multiplying an odd number make some number, the product will be odd.

For let the odd number :g:`A <g1:A>` by multiplying the odd number :g:`B <g1:B>` make :g:`C <g1:C>` ;

I say that :g:`C <g1:C>` is odd.

.. picture:: g1.svg
   :alt: Book IX, Proposition 29

.. subclause::

   For, since :g:`A <g1:A>` by multiplying :g:`B <g1:B>` has made :g:`C <g1:C>`,

.. assertion::

   therefore :g:`C <g1:C>` is made up of as many numbers equal to :g:`B <g1:B>` as there are units in :g:`A <g1:A>`. :just:`[G.222] <G.222>`

.. subclause::

   And each of the numbers :g:`A <g1:A>`, :g:`B <g1:B>` is odd;

.. assertion::

   therefore :g:`C <g1:C>` is made up of odd numbers the multitude of which is odd.

.. assertion:: [G.296] <G.296>

   Thus :g:`C <g1:C>` is odd.

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
     "G.222" [label="G.222", tooltip="G.222 (VII.def.15): A number is said tomultiply a number when that which is multiplied is added to itself as many times as there are units in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.222/index.html", target="_top"];
     "G.292" [label="G.292", tooltip="G.292 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.292/index.html", target="_top"];
     "G.293" [label="G.293", tooltip="G.293 (IX.21): If as many even numbers as we please be added together, the whole is even.", fillcolor="#222244", URL="../G.293/index.html", target="_top"];
     "G.294" [label="G.294", tooltip="G.294 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by an unit from an even number.", fillcolor="#224422", URL="../G.294/index.html", target="_top"];
     "G.295" [label="G.295", tooltip="G.295 (IX.22): If as many odd numbers as we please be added together, and their multitude be even, the whole is even.", fillcolor="#222244", URL="../G.295/index.html", target="_top"];
     "G.296" [label="G.296", tooltip="G.296 (IX.23): If as many odd numbers as we please be added together, and their multitude be odd, the whole is odd.", fillcolor="#222244", URL="../G.296/index.html", target="_top"];
     "G.302" [label="G.302", tooltip="G.302 (IX.29): If an odd number by multiplying an odd number make some number, the product is odd.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.302" -> "G.222";
     "G.293" -> "G.292";
     "G.295" -> "G.293";
     "G.296" -> "G.293";
     "G.295" -> "G.294";
     "G.296" -> "G.294";
     "G.296" -> "G.295";
     "G.302" -> "G.296";
   }
