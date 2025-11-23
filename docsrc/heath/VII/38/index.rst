:order: 38
:number: 309
:type: prop
:dependencies: VII.15




.. figure:: VII.38.graphic.inverted.png

.. _VII.38:

VII.38
======

   If a number have any part whatever, it will be measured by a number called by the same name as the part.

For let the number A have any part whatever, B, and let C be a number called by the same name as the part B; I say that C measures A.

For, since B is a part of A called by the same name as C, and the unit D is also a part of C called by the same name as it, therefore, whatever part the unit D is of the number C, the same part is B of A also; therefore the unit D measures the number C the same number of times that B measures A.

Therefore, alternately, the unit D measures the number B the same number of times that C measures A. [:ref:`VII.15`]

Therefore C measures A. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.def.20" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.20/", target="_top"];
     "elem.7.5 elem.7.6" [style="rounded,filled", fillcolor=orange];
     "VII.38" [style="rounded,filled", fillcolor=lightblue, URL="/heath/VII/38/", target="_top"];
     "VII.15" [URL="/heath/VII/15/", target="_top"];
     "VII.12" [URL="/heath/VII/12/", target="_top"];
     "VII.12" -> "VII.def.20";
     "VII.12" -> "elem.7.5 elem.7.6";
     "VII.38" -> "VII.15";
     "VII.15" -> "VII.12";
   }



Required for
------------

:ref:`VII.39`