:order: 504
:number: 504
:canonical_id: G.504
:original_id: XI.3
:title: G.504 planes cut common
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, polygon, plane-surface, straight-line, line, extremity, plane, reductio-ad-absurdum
:dependencies: G.4, G.7
:excerpt: If two planes cut one another, their common section is a segment.

.. _G.504:
.. _XI.3:

G.504 planes cut common
=======================

.. rubric:: `XI.3 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/03/>`_

.. enunciation::

   If two :term:`planes <G.7>` cut one another, their common section is a :term:`segment <G.4>`.

.. signature:: theorem

   | :fn:`planes_cut_common <G.504>`\ ()
   | **prove** the line :g:`/ D B / <g1:/ D B />` is a segment

.. picture:: g1.svg
   :alt: Book XI, Proposition 3

.. step:: assert

   Let the two planes :g:`< A B > <g1:< A B >>`, :g:`< B C > <g1:< B C >>` cut one another, and let the :term:`line <G.2>` :g:`/ D B / <g1:/ D B />` be their common section

.. step:: construct

   If not, from :g:`D <g1:D>` to :g:`B <g1:B>` let :g:`/ D E B / <g1:/ D E B />` be joined in the plane :g:`< A B > <g1:< A B >>`, and in the plane :g:`< B C > <g1:< B C >>` :g:`/ D F B / <g1:/ D F B />`.

.. step:: assert

   Then :g:`/ D E B / <g1:/ D E B />`, :g:`/ D F B / <g1:/ D F B />` will have the same :term:`extremities <G.3>`, and will clearly enclose an area:

.. step:: assert

   Which is absurd.

.. step:: assert

   Therefore :g:`/ D E B / <g1:/ D E B />`, :g:`/ D F B / <g1:/ D F B />` are not segments.

.. step:: conclude

   Similarly we can prove that neither will there be any other segment joined from :g:`D <g1:D>` to :g:`B <g1:B>` except :g:`/ D B / <g1:/ D B />` the common section of the planes :g:`< A B > <g1:< A B >>`, :g:`< B C > <g1:< B C >>`.

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
     "G.504" [label="G.504", tooltip="G.504 (XI.3): If two planes cut one another, their common section is a segment.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.4" -> "G.3";
     "G.7" -> "G.4";
     "G.504" -> "G.4";
     "G.7" -> "G.5";
     "G.504" -> "G.7";
   }

Required for
------------

:ref:`G.507 <G.507>`, :ref:`G.508 <G.508>`, :ref:`G.509 <G.509>`, :ref:`G.510 <G.510>`, :ref:`G.511 <G.511>`, :ref:`G.512 <G.512>`, :ref:`G.513 <G.513>`, :ref:`G.514 <G.514>`, :ref:`G.515 <G.515>`, :ref:`G.517 <G.517>`, :ref:`G.518 <G.518>`, :ref:`G.522 <G.522>`, :ref:`G.523 <G.523>`, :ref:`G.528 <G.528>`, :ref:`G.530 <G.530>`, :ref:`G.531 <G.531>`, :ref:`G.532 <G.532>`, :ref:`G.541 <G.541>`, :ref:`G.542 <G.542>`, :ref:`G.543 <G.543>`, :ref:`G.544 <G.544>`, :ref:`G.545 <G.545>`, :ref:`G.546 <G.546>`, :ref:`G.547 <G.547>`, :ref:`G.549 <G.549>`, :ref:`G.550 <G.550>`, :ref:`G.554 <G.554>`, :ref:`G.555 <G.555>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.560 <G.560>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.592 <G.592>`, :ref:`G.594 <G.594>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`

.. toctree::
   :hidden:

   code
   heath
