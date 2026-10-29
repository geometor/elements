:canonical_id: G.303
:original_id: IX.30
:volume: II
:book: IX
:type: prop

G.303 — Heath
=============

.. rubric:: `IX.30 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/30/>`_

.. enunciation::

   If an odd number measure an even number, it will also measure the half of it.

For let the odd number :g:`A <g1:A>` measure the even number :g:`B <g1:B>`;

I say that it will also measure the half of it.

.. picture:: g1.svg
   :alt: Book IX, Proposition 30

.. subclause::

   For, since :g:`A <g1:A>` measures :g:`B <g1:B>`, let it measure it according to :g:`C <g1:C>`;

I say that :g:`C <g1:C>` is not odd.

For, if possible, let it be so.

.. subclause::

   Then, since :g:`A <g1:A>` measures :g:`B <g1:B>` according to :g:`C <g1:C>`,

.. assertion::

   therefore :g:`A <g1:A>` by multiplying :g:`C <g1:C>` has made :g:`B <g1:B>`.

.. assertion::

   Therefore :g:`B <g1:B>` is made up of odd numbers the multitude of which is odd.

.. assertion::

   Therefore :g:`B <g1:B>` is odd: :just:`[G.296] <G.296>` which is absurd, for by hypothesis it is even.

.. assertion::

   Therefore :g:`C <g1:C>` is not odd; therefore :g:`C <g1:C>` is even.

.. assertion::

   Thus :g:`A <g1:A>` measures :g:`B <g1:B>` an even number of times.

.. assertion::

   For this reason then it also measures the half of it.

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
     "G.303" [label="G.303", tooltip="G.303 (IX.30): If an odd number measure an even number, it will also measure the half of it.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.293" -> "G.292";
     "G.295" -> "G.293";
     "G.296" -> "G.293";
     "G.295" -> "G.294";
     "G.296" -> "G.294";
     "G.296" -> "G.295";
     "G.303" -> "G.296";
   }

Required for
------------

:ref:`G.304 <G.304>`
