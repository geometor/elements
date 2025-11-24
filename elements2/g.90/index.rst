:order: 90
:original_id: III.13
:type: prop
:dependencies: g.87, g.77, g.89

.. _g.90:

G.90
====

**Heath ID:** :ref:`III.13`

   A circle does not touch a circle at more points than one, whether it touch it internally or externally.

For, if possible, let the circle ``ABDC`` touch the circle ``EBFD``, first internally, at more points than one, namely ``D``, ``B``.

Let the centre ``G`` of the circle ``ABDC``, and the centre ``H`` of ``EBFD``, be taken.

Therefore the straight line

joined from ``G`` to ``H`` will fall on ``B``, ``D``. [:ref:`g.87`]

Let it so fall, as ``BGHD``.

Then, since the point ``G`` is the centre of the circle ``ABCD``,


.. container:: center

   ``BG`` is equal to ``GD``;



.. container:: center

   therefore ``BG`` is greater than ``HD``; therefore ``BH`` is much greater than ``HD``.


Again, since the point ``H`` is the centre of the circle ``EBFD``,


.. container:: center

   ``BH`` is equal to ``HD``;



.. container:: center

   but it was also proved much greater than it: which is impossible.


Therefore a circle does not touch a circle internally at more points than one.

I say further that neither does it so touch it externally.

For, if possible, let the circle ``ACK`` touch the circle ``ABDC`` at more points than one, namely ``A``, ``C``, and let ``AC`` be joined.

Then, since on the circumference of each of the circles ``ABDC``, ``ACK`` two points ``A``, ``C`` have been taken at random, the straight line joining the points will fall within each circle; [:ref:`g.77`]


.. container:: center

   but it fell within the circle ``ABCD`` and outside ``ACK`` [:ref:`g.89`]: which is absurd.


Therefore a circle does not touch a circle externally at more points than one.

And it was proved that neither does it so touch it internally.

Therefore etc. Q. E. D.
ABDC. Euclid writes ``ABCD`` (here and in the next proposition), notwithstanding the order in which the points are placed in the figure.
does it so touch it. It is necessary to supply these words which the Greek (ὅτι οὐδὲ ἐκτός and ὅτι οὐδὲ ἐντός) leaves to be understood.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.76" [label="G.76", URL="/elements2/g.76/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.89" [label="G.89", style="rounded,filled", fillcolor=orange, URL="/elements2/g.89/", target="_top"];
     "G.90" [label="G.90", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.90/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.27" [label="G.27", URL="/elements2/g.27/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.87" [label="G.87", style="rounded,filled", fillcolor=orange, URL="/elements2/g.87/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.77" [label="G.77", URL="/elements2/g.77/", target="_top"];
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
     "G.90" -> "G.89";
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
     "G.90" -> "G.87";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.90" -> "G.77";
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
