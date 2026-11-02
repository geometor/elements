:order: 26
:number: 26
:canonical_id: G.26
:original_id: I.6
:title: G.26 triangle with equal base angles is isosceles
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, segment, angle, triangle, trilateral, plane-angle, plane, equality, reductio-ad-absurdum
:dependencies: G.9, G.11, G.22
:excerpt: If two angles of a triangle are equal, the sides subtending the equal angles are also equal.

.. _G.26:
.. _I.6:

G.26 triangle with equal base angles is isosceles
=================================================

.. rubric:: `I.6 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/06/>`_

.. enunciation::

   If two :term:`angles <G.22>` of a :term:`triangle <G.11>` are equal, the sides subtending the equal angles are also equal.

.. signature:: theorem

   | :fn:`equal_angles_isosceles <G.26>`\ (:g:`< A B C > <g1:< A B C >>`, :g:`< A B C ) <g1:< A B C )>`, :g:`< A C B ) <g1:< A C B )>`)
   | **given** :g:`< A B C > <g1:< A B C >>` be a triangle having :g:`< A B C ) <g1:< A B C )>` :eq:`equal <g1:< A B C ) = g1:< A C B )>` to :g:`< A C B ) <g1:< A C B )>`
   | **prove** the side :g:`/ A B / <g1:/ A B />` is also :eq:`equal <g1:/ A B / = g1:/ A C />` to the side :g:`/ A C / <g1:/ A C />`

.. picture:: g1.svg
   :alt: Proposition 6 figure

.. step:: given

   :g:`< A B C > <g1:< A B C >>` be a triangle having :g:`< A B C ) <g1:< A B C )>` :eq:`equal <g1:< A B C ) = g1:< A C B )>` to :g:`< A C B ) <g1:< A C B )>`

.. step:: assert

   If :g:`/ A B / <g1:/ A B />` is unequal to :g:`/ A C / <g1:/ A C />`, one of them is greater.

.. step:: assert

   Let :g:`/ A B / <g1:/ A B />` be greater

.. step:: construct

   :fn:`cut_equal_segment <G.21>`\ (:g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />`) → :g:`/ D B / <g1:/ D B />` (:eq:`equal <g1:/ D B / = g1:/ A C />`)

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`D <g1:D>`, :g:`C <g1:C>`) → :g:`/ D C / <g1:/ D C />`

.. step:: assert

   Since :g:`/ D B / <g1:/ D B />` is :eq:`equal <g1:/ D B / = g1:/ A C />` to :g:`/ A C / <g1:/ A C />`, and :g:`/ B C / <g1:/ B C />` is common → the two sides :g:`/ D B / <g1:/ D B />`, :g:`/ B C / <g1:/ B C />` are :eq:`equal <g1:/ D B / = g1:/ A C />` to the two sides :g:`/ A C / <g1:/ A C />`, :g:`/ C B / <g1:/ C B />` respectively;

.. step:: assert

   And :g:`< D B C ) <g1:< D B C )>` is :eq:`equal <g1:< D B C ) = g1:< A C B )>` to :g:`< A C B ) <g1:< A C B )>`

.. step:: assert

   Therefore the base :g:`/ D C / <g1:/ D C />` is :eq:`equal <g1:/ D C / = g1:/ A B />` to the base :g:`/ A B / <g1:/ A B />`,

.. step:: assert

   And :g:`< D B C > <g1:< D B C >>` will be :eq:`equal <g1:< D B C > = g1:< A C B >>` to :g:`< A C B > <g1:< A C B >>`,

.. step:: assert

   The less to the greater: which is absurd.

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />` is not unequal to :g:`/ A C / <g1:/ A C />`

.. step:: conclude

   It is therefore :eq:`equal <g1:/ A B / = g1:/ A C />` to it.

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
     "G.26" [label="G.26", tooltip="G.26 (I.6): If two angles of a triangle are equal, the sides subtending the equal angles are also equal.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.26" -> "G.9";
     "G.26" -> "G.11";
     "G.26" -> "G.22";
   }

Required for
------------

:ref:`G.85 <G.85>`, :ref:`G.91 <G.91>`, :ref:`G.92 <G.92>`, :ref:`G.94 <G.94>`, :ref:`G.130 <G.130>`, :ref:`G.161 <G.161>`, :ref:`G.162 <G.162>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.166 <G.166>`, :ref:`G.212 <G.212>`, :ref:`G.345 <G.345>`, :ref:`G.400 <G.400>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.477 <G.477>`, :ref:`G.494 <G.494>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.585 <G.585>`, :ref:`G.586 <G.586>`, :ref:`G.589 <G.589>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
