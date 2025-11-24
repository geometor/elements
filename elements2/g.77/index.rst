:order: 77
:original_id: III.2
:type: prop
:dependencies: g.25, g.28, g.12, g.76

.. _g.77:

G.77
====

**Heath ID:** :ref:`III.2`

   If on the circumference of a circle two points be taken at random, the straight line joining the points will fall within the circle.

Let ``ABC`` be a circle, and let two points ``A``, ``B`` be taken at random on its circumference; I say that the straight line joined from ``A`` to ``B`` will fall within the circle.

For suppose it does not, but, if possible, let it fall outside, as ``AEB``; let the centre of the circle ``ABC`` be taken [:ref:`g.76`], and let it be ``D``; let ``DA``, ``DB`` be joined, and let ``DFE`` be drawn through.

Then, since ``DA`` is equal to ``DB``,


.. container:: center

   the angle ``DAE`` is also equal to the angle ``DBE``. [:ref:`g.12`]


And, since one side ``AEB`` of the triangle ``DAE`` is produced,


.. container:: center

   the angle ``DEB`` is greater than the angle ``DAE``. [:ref:`g.25`]


But the angle ``DAE`` is equal to the angle ``DBE``;


.. container:: center

   therefore the angle ``DEB`` is greater than the angle ``DBE``.


And the greater angle is subtended by the greater side; [:ref:`g.28`]


.. container:: center

   therefore ``DB`` is greater than ``DE``. But ``DB`` is equal to ``DF``;



.. container:: center

   therefore ``DF`` is greater than ``DE``,



.. container:: center

   the less than the greater : which is impossible.


Therefore the straight line joined from ``A`` to ``B`` will not fall outside the circle.

Similarly we can prove that neither will it fall on the circumference itself;


.. container:: center

   therefore it will fall within.


Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.76" [label="G.76", URL="/elements2/g.76/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.27" [label="G.27", URL="/elements2/g.27/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.77" [label="G.77", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.77/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
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
     "G.77" -> "G.76";
     "G.17" -> "G.16";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.28" -> "G.27";
     "G.24" -> "G.21";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.15" -> "G.14";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.76" -> "G.15";
     "G.77" -> "G.28";
     "G.27" -> "G.25";
     "G.77" -> "G.25";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.76" -> "G.18";
     "G.24" -> "G.22";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
     "G.77" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`g.90`
