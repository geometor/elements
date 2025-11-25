:order: 46
:original_id: I.33
:type: prop
:dependencies: G.38, G.42, G.11

.. _G.46:

G.46
====

**Heath ID:** :ref:`I.33`

   The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.

Let ``AB``, ``CD`` be equal and parallel, and let the straight  lines ``AC``, ``BD`` join them (at the extremities which are) in the same directions (respectively); I say that ``AC``, ``BD`` are also equal and parallel.

Let ``BC`` be joined. 

Then, since ``AB`` is parallel to ``CD``,  and ``BC`` has fallen upon them, the alternate angles ``ABC``, ``BCD`` are equal to one another. [:ref:`G.42`]

And, since ``AB`` is equal to ``CD``, and ``BC`` is common, the two sides ``AB``, ``BC`` are equal to the two sides ``DC``, ``CB``; and the angle ``ABC`` is equal to the angle ``BCD``; therefore the base ``AC`` is equal to the base ``BD``, and the griangle ``ABC`` is equal to the triangle ``DCB``, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend; [:ref:`G.11`] therefore the angle ``ACB`` is equal to the angle ``CBD``.

And, since the straight line ``BC`` falling on the two straight lines ``AC``, ``BD`` has made the alternate angles equal to one another, ``AC`` is parallel to ``BD``. [:ref:`G.38`]

And it was also proved equal to it.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. joining...(at the extremities which are) in the same directions (respectively).**

   

   I have for clearness' sake inserted the words in brackets though they are not in the original Greek, which has joining...in the same directions

    or on the same sides,

    ἐπὶ τὰ αυτὰ μέρη ἐπιζευγνύουσαι. The expression tiwards the same parts,

    though usage has sanctioned it, is perhaps not quite satisfactory.


.. note::


   **15. DC, CB**

   

   and 18. DCB. The Greek has  ``BC``, ``CD``

    and ``BCD``

    in these places respectively. Euclid is not always careful to write in corresponding order the letters denoting corresponding points in congruent figures. On the contrary, he evidently prefers the alphabetical order, and seems to disdain to alter it for the sake of beginners or others who might be confused by it. In the case of angles alteration is perhaps unnecessary; but in the case of triangles and pairs of corresponding sides I have ventured to alter the order to that which the mathematician of to-day expects.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.38" [label="G.38", fillcolor="#222244", URL="/elements2/G.38/", target="_top"];
     "G.46" [label="G.46", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.46/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.41" [label="G.41", fillcolor="#444422", URL="/elements2/G.41/", target="_top"];
     "G.37" [label="G.37", fillcolor="#224422", URL="/elements2/G.37/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.40" [label="G.40", fillcolor="#442222", URL="/elements2/G.40/", target="_top"];
     "G.42" [label="G.42", fillcolor="#222244", URL="/elements2/G.42/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.46" -> "G.38";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.21" -> "G.19";
     "G.9" -> "G.8";
     "G.24" -> "G.22";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.42" -> "G.41";
     "G.38" -> "G.37";
     "G.25" -> "G.17";
     "G.42" -> "G.40";
     "G.46" -> "G.42";
     "G.38" -> "G.25";
     "G.17" -> "G.16";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.46" -> "G.11";
     "G.11" -> "G.10";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.15" -> "G.14";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.14" -> "G.12";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`G.49`, :ref:`G.51`, :ref:`G.53`, :ref:`G.55`, :ref:`G.57`, :ref:`G.58`
