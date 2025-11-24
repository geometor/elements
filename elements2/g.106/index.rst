:order: 106
:original_id: III.25
:type: prop
:dependencies: g.13, g.85

.. _g.106:

G.106
=====

**Heath ID:** :ref:`III.25`

   Given a segment of a circle, to describe the complete circle of which it is a segment.

Let ``ABC`` be the given segment of a circle; thus it is required to describe the complete circle belonging to the segment ``ABC``, that is, of which it is a segment.

For let ``AC`` be bisected at ``D``, let ``DB`` be drawn from the point ``D`` at right angles to ``AC``, and let ``AB``. be joined;


.. container:: center

   the angle ``ABD`` is then greater than, equal to, or less than the angle ``BAD``.


First let it be greater; and on the straight line ``BA``, and at the point ``A`` on it, let the angle ``BAE`` be constructed equal to the angle ``ABD``; let ``DB`` be drawn through to ``E``, and let ``EC`` be joined.

Then, since the angle ``ABE`` is equal to the angle ``BAE``,


.. container:: center

   the straight line ``EB`` is also equal to ``EA``. [:ref:`g.13`]


And, since ``AD`` is equal to ``DC``, and ``DE`` is common,


.. container:: center

   the two sides ``AD``, ``DE`` are equal to the two sides ``CD``, ``DE`` respectively;


and the angle ``ADE`` is equal to the angle ``CDE``, for each is right;


.. container:: center

   therefore the base ``AE`` is equal to the base ``CE``.


But ``AE`` was proved equal to ``BE``;


.. container:: center

   therefore ``BE`` is also equal to ``CE``;


therefore the three straight lines ``AE``, ``EB``, ``EC`` are equal to one another.

Therefore the circle drawn with centre ``E`` and distance one of the straight lines ``AE``, ``EB``, ``EC`` will also pass through the remaining points and will have been completed. [:ref:`g.85`]

Therefore, given a segment of a circle, the complete circle has been described.

And it is manifest that the segment ``ABC`` is less than a semicircle, because the centre ``E`` happens to be outside it.

Similarly, even if the angle ``ABD`` be equal to the angle ``BAD``, ``AD`` being equal to each of the two ``BD``, ``DC``,


.. container:: center

   the three straight lines ``DA``, ``DB``, ``DC`` will be equal to one another, 
           ``D`` will be the centre of the completed circle, and ``ABC`` will clearly be a semicircle.


But, if the angle ``ABD`` be less than the angle ``BAD``, and if we construct, on the straight line ``BA`` and at the point ``A`` on it, an angle equal to the angle ``ABD``, the centre will fall on ``DB`` within the segment ``ABC``, and the segment

``ABC`` will clearly be greater than a semicircle.

Therefore, given a segment of a circle, the complete circle has been described. Q. E. F.
to describe the complete circle, προσαναγράψαι τὸν κύκλον, literally “to describe the circle ``on to it``.’


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.85" [label="G.85", URL="/elements2/g.85/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.106" [label="G.106", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.106/", target="_top"];
     "G.13" [label="G.13", style="rounded,filled", fillcolor=orange, URL="/elements2/g.13/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.84" [label="G.84", style="rounded,filled", fillcolor=orange, URL="/elements2/g.84/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.106" -> "G.85";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.8" -> "G.6";
     "G.85" -> "G.15";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.8" -> "G.5";
     "G.106" -> "G.13";
     "G.85" -> "G.18";
     "G.12" -> "G.11";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.11" -> "G.10";
     "G.85" -> "G.84";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
   }
