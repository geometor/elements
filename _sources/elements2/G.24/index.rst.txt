:order: 24
:original_id: I.15
:type: prop
:dependencies: G.21, G.1, G.6, G.22
:excerpt: If two straight lines cut one another, they make the vertical angles equal to one another.

**Heath ID:** `I.15 <https://geometor.github.io/euclid/I/15/>`_

.. picture:: G.24.png

.. _G.24:

G.24
====

    If two straight lines cut one another, they make the vertical angles equal to one another.

For let the straight lines ``AB``, ``CD`` cut one another at the point ``E``; 

I say that the angle ``AEC`` is equal to the angle ``DEB``, and the angle ``CEB`` to the angle ``AED``.
        

For, since the straight line ``AE`` stands on the straight line ``CD``, making the angles ``CEA``, ``AED``, the angles ``CEA``, ``AED`` are equal to two right angles [:ref:`G.21`]
        

Again, since the straight line ``DE`` stands on the straight line ``AB``, making the angles ``AED``, ``DEB``, the angles ``AED``, ``DEB`` are equal to two right angles. [:ref:`G.21`]
        

But the angles ``CEA``, ``AED`` were also proved equal to two right angles; therefore the angles ``CEA``, ``AED`` are equal to the angles ``AED``
         ``DEB``. [:ref:`G.22` and :ref:`G.1`] Let the angle ``AED`` be subtracted from each; therefore the remaining angle ``CEA`` is equal to the remaining angle ``BED``. [:ref:`G.6`]

Similarly it can be proved that the angles ``CEB``, ``DEA`` are also equal.

Therefore etc. Q. E. D. 


.. _I.15.p.1:


**I.15.p.1**


[From this it is manifest that, if two straight lines cut one another, they will make the angles at the point of section equal to four right angles.

Porism.

[From this it is manifest that, if two straight lines cut one another, they will make the angles at the point of section equal to four right angles.


.. note::


   **1. the vertical angles.**

   

   The difference between ``adjacent`` angles (αἱ ἐφεξῆς γωνίαι) and ``vertical`` angles (αἱ κατὰ κορυφὴν γωνίαι) is thus explained by Proclus (p. 298, 14-24). The first term describes the angles made by two straight lines when one only is divided by the other, i.e. when one straight line meets another at a point which is not either of its extremities, but is not itself produced beyond the point of meeting. When the first straight line ``is`` produced, so that the lines cross at the point, they make two pairs of ``vertical`` angles (which are more clearly described as ``vertically opposite`` angles), and which are so called because their convergence is from opposite directions to one point (the intersection of the lines) as vertex (κορυφή).


.. note::


   **26. at the point of section,**

   

   literally at the section,

    πρὸς τῇ τομῆ.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.24" [label="G.24", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.24/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.24" -> "G.6";
     "G.8" -> "G.6";
     "G.21" -> "G.19";
     "G.24" -> "G.21";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.11" -> "G.10";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.19" -> "G.15";
     "G.19" -> "G.5";
     "G.8" -> "G.5";
     "G.5" -> "G.1";
     "G.24" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.14" -> "G.12";
     "G.24" -> "G.22";
     "G.15" -> "G.14";
     "G.9" -> "G.8";
     "G.19" -> "G.9";
     "G.12" -> "G.9";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.12" -> "G.11";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
   }



Required for
------------

:ref:`G.25`, :ref:`G.26`, :ref:`G.27`, :ref:`G.28`, :ref:`G.30`, :ref:`G.31`, :ref:`G.32`, :ref:`G.34`, :ref:`G.35`, :ref:`G.36`, :ref:`G.38`, :ref:`G.39`, :ref:`G.42`, :ref:`G.43`, :ref:`G.44`, :ref:`G.45`, :ref:`G.46`, :ref:`G.47`, :ref:`G.48`, :ref:`G.49`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.56`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`
