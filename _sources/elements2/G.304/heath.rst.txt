:canonical_id: G.304
:original_id: IX.31
:volume: II
:book: IX
:type: prop

G.304 — Heath
=============

.. rubric:: `IX.31 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/31/>`_

.. enunciation::

   If an odd number be prime to any number, it will also be prime to the double of it.

For let the odd number :g:`A <g1:A>` be prime to any number :g:`B <g1:B>`, and let :g:`C <g1:C>` be double of :g:`B <g1:B>`;

I say that :g:`A <g1:A>` is prime to :g:`C <g1:C>`.

.. picture:: g1.svg
   :alt: Book IX, Proposition 31

For, if they are not prime to one another, some number will measure them.

Let a number measure them, and let it be :g:`D <g1:D>`.

.. subclause::

   Now :g:`A <g1:A>` is odd;

.. assertion::

   therefore :g:`D <g1:D>` is also odd.

.. subclause::

   And since :g:`D <g1:D>` which is odd measures :g:`C <g1:C>`, and :g:`C <g1:C>` is even,

.. assertion:: [G.303] <G.303>

   therefore [:g:`D <g1:D>`] will measure the half of :g:`C <g1:C>` also.

.. subclause::

   But :g:`B <g1:B>` is half of :g:`C <g1:C>`;

.. assertion::

   therefore :g:`D <g1:D>` measures :g:`B <g1:B>`.

.. subclause::

   But it also measures :g:`A <g1:A>`;

.. assertion::

   therefore :g:`D <g1:D>` measures :g:`A <g1:A>`, :g:`B <g1:B>` which are prime to one another: which is impossible.

.. assertion::

   Therefore :g:`A <g1:A>` cannot but be prime to :g:`C <g1:C>`.

.. assertion::

   Therefore :g:`A <g1:A>`, :g:`C <g1:C>` are prime to one another.

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
     "G.292" [label="G.292", tooltip="G.292 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.292/index.html", target="_top"];
     "G.293" [label="G.293", tooltip="G.293 (IX.21): If as many even numbers as we please be added together, the whole is even.", fillcolor="#222244", URL="../G.293/index.html", target="_top"];
     "G.294" [label="G.294", tooltip="G.294 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by an unit from an even number.", fillcolor="#224422", URL="../G.294/index.html", target="_top"];
     "G.295" [label="G.295", tooltip="G.295 (IX.22): If as many odd numbers as we please be added together, and their multitude be even, the whole is even.", fillcolor="#222244", URL="../G.295/index.html", target="_top"];
     "G.296" [label="G.296", tooltip="G.296 (IX.23): If as many odd numbers as we please be added together, and their multitude be odd, the whole is odd.", fillcolor="#222244", URL="../G.296/index.html", target="_top"];
     "G.303" [label="G.303", tooltip="G.303 (IX.30): If an odd number measure an even number, it will also measure the half of it.", fillcolor="#222244", URL="../G.303/index.html", target="_top"];
     "G.304" [label="G.304", tooltip="G.304 (IX.31): If an odd number be prime to any number, it is prime to the double of it.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.293" -> "G.292";
     "G.295" -> "G.293";
     "G.296" -> "G.293";
     "G.295" -> "G.294";
     "G.296" -> "G.294";
     "G.296" -> "G.295";
     "G.303" -> "G.296";
     "G.304" -> "G.303";
   }
