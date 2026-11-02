:canonical_id: G.233
:original_id: VI.21
:title: G.233 figures similar polygon
:volume: II
:book: VI
:type: prop

G.233 figures similar polygon — Heath
=====================================

.. rubric:: `VI.21 <https://geometor.github.io/euclid/heath/volume_II/book_vi/propositions/21/>`_

.. enunciation::

   :term:`Figures <G.9>` which are similar to the same :term:`rectilineal figure <G.11>` are also similar to one another.

For let each of the rectilineal figures :g:`A <g1:A>`, :g:`B <g1:B>` be similar to :g:`C <g1:C>`;

I say that :g:`A <g1:A>` is also similar to :g:`B <g1:B>`.

.. subclause::

   For, since :g:`A <g1:A>` is similar to :g:`C <g1:C>`,

.. assertion::

   it is equiangular with it and has the sides about the equal :term:`angles <G.22>` :term:`proportional <G.180>`. :just:`[G.217] <G.217>`

.. picture:: g1.svg
   :alt: Book VI, Proposition 21

.. subclause::

   Again, since :g:`B <g1:B>` is similar to :g:`C <g1:C>`,

.. assertion::

   it is equiangular with it and has the sides about the equal angles proportional.

.. assertion::

   Therefore each of the figures :g:`A <g1:A>`, :g:`B <g1:B>` is equiangular with :g:`C <g1:C>` and with :g:`C <g1:C>` has the sides about the equal angles proportional;

.. assertion::

   therefore :g:`A <g1:A>` is similar to :g:`B <g1:B>`.

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
     "G.1" [label="G.1", tooltip="G.1 (I.def.1): A point A is that which has no part.", fillcolor="#224422", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.2): A line [ A B ] is a projection of a relationship of two points A, B.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.def.3): The extremities of a segment / A B / are points A, B.", fillcolor="#224422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.def.4): A segment / A B / is a portion of a line [ A B ] between two points A, B on the line.", fillcolor="#224422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.def.5): A surface is that which has length and breadth only.", fillcolor="#224422", URL="../G.5/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.def.7): A plane surface lies evenly with the lines on itself.", fillcolor="#224422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.217" [label="G.217", tooltip="G.217 (VI.def.1): Similar polygons are such as have theirangles severally equal and the sides about the equal anglesproportional.", fillcolor="#224422", URL="../G.217/index.html", target="_top"];
     "G.233" [label="G.233", tooltip="G.233 (VI.21): Figures which are similar to the same polygon are also similar to one another.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.22" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.7" -> "G.4";
     "G.11" -> "G.4";
     "G.22" -> "G.4";
     "G.7" -> "G.5";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.233" -> "G.9";
     "G.233" -> "G.11";
     "G.217" -> "G.22";
     "G.170" -> "G.169";
     "G.176" -> "G.170";
     "G.180" -> "G.176";
     "G.217" -> "G.180";
     "G.233" -> "G.217";
   }

Required for
------------

:ref:`G.236 <G.236>`, :ref:`G.238 <G.238>`, :ref:`G.239 <G.239>`, :ref:`G.240 <G.240>`, :ref:`G.241 <G.241>`, :ref:`G.243 <G.243>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.451 <G.451>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.601 <G.601>`
