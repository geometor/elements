:order: 46
:original_id: I.33
:type: prop
:dependencies: g.38, g.42, g.11

.. _g.46:

G.46
====

**Heath ID:** :ref:`I.33`

   The straight lines joining equal and parallel straight lines (at the extremities which are) in the same directions (respectively) are themselves also equal and parallel.

Let ``AB``, ``CD`` be equal and parallel, and let the straight  lines ``AC``, ``BD`` join them (at the extremities which are) in the same directions (respectively); I say that ``AC``, ``BD`` are also equal and parallel.

Let ``BC`` be joined. 

Then, since ``AB`` is parallel to ``CD``,  and ``BC`` has fallen upon them, the alternate angles ``ABC``, ``BCD`` are equal to one another. [:ref:`g.42`]

And, since ``AB`` is equal to ``CD``, and ``BC`` is common, the two sides ``AB``, ``BC`` are equal to the two sides ``DC``, ``CB``; and the angle ``ABC`` is equal to the angle ``BCD``; therefore the base ``AC`` is equal to the base ``BD``, and the griangle ``ABC`` is equal to the triangle ``DCB``, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend; [:ref:`g.11`] therefore the angle ``ACB`` is equal to the angle ``CBD``.

And, since the straight line ``BC`` falling on the two straight lines ``AC``, ``BD`` has made the alternate angles equal to one another, ``AC`` is parallel to ``BD``. [:ref:`g.38`]

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
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.46" [label="G.46", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.46/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.17" -> "G.16";
     "G.42" -> "G.41";
     "G.46" -> "G.42";
     "G.42" -> "G.40";
     "G.46" -> "G.38";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.38" -> "G.37";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.38" -> "G.25";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.24" -> "G.22";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.46" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`g.49`, :ref:`g.51`, :ref:`g.53`, :ref:`g.55`, :ref:`g.57`, :ref:`g.58`, :ref:`g.72`, :ref:`g.75`, :ref:`g.66`, :ref:`g.67`, :ref:`g.69`, :ref:`g.116`, :ref:`g.117`, :ref:`g.118`, :ref:`g.131`, :ref:`g.132`, :ref:`g.133`, :ref:`g.167`, :ref:`g.177`, :ref:`g.178`, :ref:`g.179`, :ref:`g.182`, :ref:`g.183`, :ref:`g.184`, :ref:`g.185`, :ref:`g.186`, :ref:`g.189`, :ref:`g.168`, :ref:`g.191`, :ref:`g.194`, :ref:`g.195`, :ref:`g.196`, :ref:`g.197`, :ref:`g.198`, :ref:`g.199`, :ref:`g.200`, :ref:`g.201`, :ref:`g.169`, :ref:`g.202`, :ref:`g.203`, :ref:`g.204`, :ref:`g.170`, :ref:`g.171`, :ref:`g.172`, :ref:`g.173`, :ref:`g.175`, :ref:`g.176`, :ref:`g.258`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.483`, :ref:`g.348`, :ref:`g.351`, :ref:`g.355`, :ref:`g.356`, :ref:`g.357`, :ref:`g.358`, :ref:`g.361`, :ref:`g.363`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.494`, :ref:`g.502`, :ref:`g.509`, :ref:`g.510`, :ref:`g.511`, :ref:`g.514`, :ref:`g.518`, :ref:`g.519`, :ref:`g.520`, :ref:`g.521`, :ref:`g.522`, :ref:`g.524`, :ref:`g.526`, :ref:`g.527`, :ref:`g.528`, :ref:`g.529`, :ref:`g.530`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.553`, :ref:`g.555`, :ref:`g.531`, :ref:`g.532`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`, :ref:`g.557`, :ref:`g.568`, :ref:`g.569`, :ref:`g.571`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.558`, :ref:`g.560`, :ref:`g.562`, :ref:`g.563`, :ref:`g.565`, :ref:`g.567`
