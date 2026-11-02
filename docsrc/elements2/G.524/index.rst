:order: 524
:number: 524
:canonical_id: G.524
:original_id: XI.def.11
:title: G.524 solid angle
:volume: III
:book: XI
:type: def
:categories: definition, solid-geometry
:category: definition, solid-geometry
:tags: book-xi, solid-angle, line, surface, plane-angle, plane-surface, point, plane
:dependencies: G.1, G.2, G.5, G.7, G.22
:excerpt: Asolid angle is the inclination constituted by more than twolines which meet one another and are not in the samesurface, towards all the lines. Otherwise: Asolid angle is that which is contained by more than twoplane angles which are not in the sameplane and are constructed to onepoint.

.. _G.524:
.. _XI.def.11:

G.524 solid angle
=================

.. rubric:: `XI.def.11 <https://geometor.github.io/euclid/heath/volume_III/book_xi/definitions/#xi-def-11>`_

.. enunciation::

   A:term:`**solid angle** <solid-angle>` is the inclination constituted by more than two:term:`lines <G.2>` which meet one another and are not in the same:term:`surface <G.533>`, towards all the lines. Otherwise: A:term:`**solid angle** <solid-angle>` is that which is contained by more than two:term:`plane angles <G.22>` which are not in the same:term:`plane <G.7>` and are constructed to one:term:`point <G.1>`.

.. signature:: def

   | :fn:`solid_angle_inclination_def <G.524>`

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
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.524" [label="G.524", tooltip="G.524 (XI.def.11): Asolid angle is the inclination constituted by more than twolines which meet one another and are not in the samesurface, towards all the lines. Otherwise: Asolid angle is that whic...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.524" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.22" -> "G.2";
     "G.524" -> "G.2";
     "G.4" -> "G.3";
     "G.7" -> "G.4";
     "G.22" -> "G.4";
     "G.7" -> "G.5";
     "G.524" -> "G.5";
     "G.22" -> "G.7";
     "G.524" -> "G.7";
     "G.524" -> "G.22";
   }

Required for
------------

:ref:`G.525 <G.525>`, :ref:`G.526 <G.526>`, :ref:`G.528 <G.528>`, :ref:`G.532 <G.532>`, :ref:`G.536 <G.536>`, :ref:`G.546 <G.546>`

.. toctree::
   :hidden:

   heath
