:canonical_id: G.277
:original_id: IX.7
:volume: II
:book: IX
:type: prop

G.277 — Heath
=============

.. rubric:: `IX.7 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/07/>`_

.. enunciation::

   If a composite number by multiplying any number make some number, the product will be solid.

For let the composite number :g:`A <g1:A>` by multiplying any number :g:`B <g1:B>` make :g:`C <g1:C>`;

I say that :g:`C <g1:C>` is solid.

.. picture:: g1.svg
   :alt: Proposition 7 Diagram

.. subclause::

   For, since :g:`A <g1:A>` is composite,

.. assertion::

   it will be measured by some number. :just:`[G.276] <G.276>`

Let it be measured by :g:`D <g1:D>`; and, as many times as :g:`D <g1:D>` measures :g:`A <g1:A>`, so many units let there be in :g:`E <g1:E>`.

.. subclause::

   Since then :g:`D <g1:D>` measures :g:`A <g1:A>` according to the units in :g:`E <g1:E>`,

.. assertion:: [G.222] <G.222>

   therefore :g:`E <g1:E>` by multiplying :g:`D <g1:D>` has made :g:`A <g1:A>`.

.. subclause::

   And, since :g:`A <g1:A>` by multiplying :g:`B <g1:B>` has made :g:`C <g1:C>`, and :g:`A <g1:A>` is the product of :g:`D <g1:D>`, :g:`E <g1:E>`,

.. assertion::

   therefore the product of :g:`D <g1:D>`, :g:`E <g1:E>` by multiplying :g:`B <g1:B>` has made :g:`C <g1:C>`.

.. assertion::

   Therefore :g:`C <g1:C>` is solid, and :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`B <g1:B>` are its sides.

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
     "G.276" [label="G.276", tooltip="G.276 (VII.def.13): Acomposite number is that which is measured by some number.", fillcolor="#224422", URL="../G.276/index.html", target="_top"];
     "G.277" [label="G.277", tooltip="G.277 (IX.7): If a composite number by multiplying any number make some number, the product is solid.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.277" -> "G.222";
     "G.277" -> "G.276";
   }
