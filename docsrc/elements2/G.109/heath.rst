:canonical_id: G.109
:original_id: III.11
:title: G.109 circles touch internally
:volume: II
:book: III
:type: prop

G.109 circles touch internally — Heath
======================================

.. rubric:: `III.11 <https://geometor.github.io/euclid/heath/volume_II/book_iii/propositions/11/>`_

.. enunciation::

   If two :term:`circles <G.10>` :term:`touch one another <G.103>` internally, and their :term:`centres <G.14>` be taken, the :term:`straight line <G.4>` joining their centres, if it be also produced, will fall on the :term:`point <G.1>` of contact of the circles.

For let the two circles :g:`( A B C ) <g1:( A B C )>`, :g:`( A D E ) <g1:( A D E )>` touch one another internally at the point :g:`A <g1:A>`, and let the centre :g:`F <g1:F>` of the circle :g:`( A B C ) <g1:( A B C )>`, and the centre :g:`G <g1:G>` of :g:`( A D E ) <g1:( A D E )>`, be taken;

I say that the straight line joined from :g:`G <g1:G>` to :g:`F <g1:F>` and produced will fall on :g:`A <g1:A>`.

.. picture:: g1.svg
   :alt: Diagram for Proposition 11 showing circles ABC and ADE touching internally at A

For suppose it does not, but, if possible, let it fall as :g:`/ F G H / <g1:/ F G H />`, and let :g:`/ A F / <g1:/ A F />`, :g:`/ A G / <g1:/ A G />` be joined.

Then, since :g:`/ A G / <g1:/ A G />`, :g:`/ G F / <g1:/ G F />` are greater than :g:`/ F A / <g1:/ F A />`, that is, than :g:`/ F H / <g1:/ F H />`,

.. subclause::

   let :g:`/ F G / <g1:/ F G />` be subtracted from each;

.. assertion::

   therefore the remainder :g:`/ A G / <g1:/ A G />` is greater than the remainder :g:`/ G H / <g1:/ G H />`.

But :g:`/ A G / <g1:/ A G />` is :eq:`equal <g1:/ A G / = g1:/ G D />` to :g:`/ G D / <g1:/ G D />`;

.. assertion::

   therefore :g:`/ G D / <g1:/ G D />` is also greater than :g:`/ G H / <g1:/ G H />`,

.. subclause::

   the less than the greater: which is impossible.

.. assertion::

   Therefore the straight line joined from :g:`F <g1:F>` to :g:`G <g1:G>` will not fall outside;

.. assertion::

   therefore it will fall at :g:`A <g1:A>` on the point of contact.

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
     "G.1" [label="G.1", tooltip="G.1 (I.def.1): A point A is that which has no part.", fillcolor="#224422", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.2): A line [ A B ] is a projection of a relationship of two points A, B.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.def.3): The extremities of a segment / A B / are points A, B.", fillcolor="#224422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.def.4): A segment / A B / is a portion of a line [ A B ] between two points A, B on the line.", fillcolor="#224422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.def.5): A surface is that which has length and breadth only.", fillcolor="#224422", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.def.6): The extremities of a surface are lines or arcs.", fillcolor="#224422", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.def.7): A plane surface lies evenly with the lines on itself.", fillcolor="#224422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.def.15): A circle ( A B ) is a plane figure contained by one arc defined by a center A and a point B establishing its defining radius / A B /, such that all segments / A B /, / A C /, / A D...", fillcolor="#224422", URL="../G.10/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.14/index.html", target="_top"];
     "G.103" [label="G.103", tooltip="G.103 (III.def.3): Circles are said totouch one another which, meeting one another, do not cut one another.", fillcolor="#224422", URL="../G.103/index.html", target="_top"];
     "G.109" [label="G.109", tooltip="G.109 (III.11): If two circles touch one another internally, and their centres be taken, the segment joining their centres, if it be also produced, will fall on the point of contact of the circles...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.14" -> "G.1";
     "G.109" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.109" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.14" -> "G.10";
     "G.109" -> "G.10";
     "G.109" -> "G.14";
     "G.109" -> "G.103";
   }

Required for
------------

:ref:`G.112 <G.112>`
