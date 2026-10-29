:canonical_id: G.80
:original_id: III.5
:volume: II
:book: III
:type: prop

G.80 — Heath
============

.. rubric:: `III.5 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/05/>`_

.. enunciation::

   If two circles cut one another, they will not have the same centre.

For let the circles :g:`( A B C ) <g1:( A B C )>`, :g:`( C D G ) <g1:( C D G )>` cut one another at the points :g:`B <g1:B>`, :g:`C <g1:C>`;

I say that they will not have the same centre.

.. picture:: g1.svg
   :alt: Proposition 5 Diagram

For, if possible, let it be :g:`E <g1:E>`; let :g:`/ E C / <g1:/ E C />` be joined, and let :g:`/ E F G / <g1:/ E F G />` be drawn through at random.

Then, since the point :g:`E <g1:E>` is the centre of the circle :g:`( A B C ) <g1:( A B C )>`,

.. assertion:: [G.2] <G.2>

   :g:`/ E C / <g1:/ E C />` is :eq:`equal <g1:/ E C / = g1:/ E F />` to :g:`/ E F / <g1:/ E F />`.

Again, since the point :g:`E <g1:E>` is the centre of the circle :g:`( C D G ) <g1:( C D G )>`,

.. assertion::

   :g:`/ E C / <g1:/ E C />` is :eq:`equal <g1:/ E C / = g1:/ E G />` to :g:`/ E G / <g1:/ E G />`.

But :g:`/ E C / <g1:/ E C />` was proved :eq:`equal <g1:/ E C / = g1:/ E F />` to :g:`/ E F / <g1:/ E F />` also; therefore :g:`/ E F / <g1:/ E F />` is also :eq:`equal <g1:/ E F / = g1:/ E G />` to :g:`/ E G / <g1:/ E G />`, the less to the greater: which is impossible.

.. assertion::

   Therefore the point :g:`E <g1:E>` is not the centre of the circles :g:`( A B C ) <g1:( A B C )>`, :g:`( C D G ) <g1:( C D G )>`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.2" [label="G.2", tooltip="G.2 (I.def.15): A circle is a plane figure contained by one line such that all segments falling upon it from its center are equal.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.80" [label="G.80", tooltip="G.80 (III.5): If two circles cut one another, they will not have the same centre.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.80" -> "G.2";
   }

Required for
------------

:ref:`G.85 <G.85>`, :ref:`G.103 <G.103>`, :ref:`G.105 <G.105>`, :ref:`G.106 <G.106>`, :ref:`G.107 <G.107>`, :ref:`G.108 <G.108>`, :ref:`G.109 <G.109>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.133 <G.133>`, :ref:`G.134 <G.134>`, :ref:`G.198 <G.198>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.515 <G.515>`, :ref:`G.516 <G.516>`, :ref:`G.517 <G.517>`, :ref:`G.518 <G.518>`, :ref:`G.519 <G.519>`, :ref:`G.520 <G.520>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`
