:order: 9
:original_id: I.3
:type: prop
:dependencies: G.8, G.1, G.2, G.4
:excerpt: Given two unequal straight lines, to cut off from the greater a straight line equal to the less.

**Heath ID:** `I.3 <https://geometor.github.io/euclid/I/3/>`_

.. picture:: G.9.png

.. _G.9:

G.9
===

    Given two unequal straight lines, to cut off from the greater a straight line equal to the less.

Let ``AB``, ``C`` be the-two given unequal straight lines, and let ``AB`` be the greater of them.

Thus it is required to cut off from ``AB`` the greater a straight line equal to ``C`` the less.

At the point ``A`` let ``AD`` be placed equal to the straight line ``C``; [:ref:`G.8`] and with centre ``A`` and distance ``AD`` let the circle ``DEF`` be described. [:ref:`G.4`] Now, since the point ``A`` is the centre of the circle ``DEF``, ``AE`` is equal to ``AD``. [:ref:`G.2`] But ``C`` is also equal to ``AD``. Therefore each of the straight lines ``AE``, ``C`` is equal to ``AD``; so that ``AE`` is also equal to ``C``. [:ref:`G.1`]

Therefore, given the two straight lines ``AB``, ``C``, from ``AB`` the greater ``AE`` has been cut off equal to ``C`` the less.


**Q. E. D.**


(Being) what it was required to do.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.9" [label="G.9", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.9/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.8" -> "G.6";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.8" -> "G.5";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
   }



Required for
------------

:ref:`G.17`, :ref:`G.19`, :ref:`G.20`, :ref:`G.21`, :ref:`G.23`, :ref:`G.24`, :ref:`G.25`, :ref:`G.26`, :ref:`G.27`, :ref:`G.28`, :ref:`G.30`, :ref:`G.31`, :ref:`G.32`, :ref:`G.33`, :ref:`G.34`, :ref:`G.35`, :ref:`G.36`, :ref:`G.38`, :ref:`G.39`, :ref:`G.42`, :ref:`G.43`, :ref:`G.44`, :ref:`G.45`, :ref:`G.46`, :ref:`G.47`, :ref:`G.48`, :ref:`G.49`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.56`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`, :ref:`G.12`, :ref:`G.14`, :ref:`G.15`, :ref:`G.16`
