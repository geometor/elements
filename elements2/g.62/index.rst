:order: 62
:original_id: II.1
:type: prop
:dependencies: g.19, g.9, g.44, g.47

.. _g.62:

G.62
====

**Heath ID:** :ref:`II.1`

   If there be two straight lines, and one of them be cut into any number of segments whatever, the rectangle contained by the two straight lines is equal to the rectangles contained by the uncut straight line and each of the segments.

Let ``A``, ``BC`` be two straight lines, and let ``BC`` be cut at random at the points ``D``, ``E``; I say that the rectangle contained by ``A``, ``BC`` is equal to the rectangle contained by ``A``, ``BD``, that contained by ``A``, ``DE`` and that contained by ``A``, ``EC``.

For let ``BF`` be drawn from ``B`` at right angles to ``BC``; [:ref:`g.19`] let ``BG`` be made equal to ``A``, [:ref:`g.9`] through ``G`` let ``GH`` be drawn parallel to ``BC``, [:ref:`g.44`] and through ``D``, ``E``, ``C`` let ``DK``, ``EL``, ``CH`` be drawn parallel to ``BG``.

Then ``BH`` is equal to ``BK``, ``DL``, ``EH``.

Now ``BH`` is the rectangle ``A``, ``BC``, for it is contained by ``GB``, ``BC``, and ``BG`` is equal to ``A``;

``BK`` is the rectangle ``A``, ``BD``, for it is contained by ``GB``, ``BD``, and ``BG`` is equal to ``A``;


.. container:: center

   and ``DL`` is the rectangle ``A``, ``DE``, for ``DK``, that is ``BG`` [:ref:`g.47`], is equal to ``A``.


Similarly also ``EH`` is the rectangle ``A``, ``EC``.

Therefore the rectangle ``A``, ``BC`` is equal to the rectangle ``A``, ``BD``, the rectangle ``A``, ``DE`` and the rectangle ``A``, ``EC``.

Therefore etc. Q. E. D.
the rectangle A, BC. From this point onward I shall translate thus in cases where Euclid leaves out the word ``contained`` (περιεχόμενον). Though the word rectangle
is also omitted in the Greek (the neuter article being sufficient to show that the rectangle is meant), it cannot be dispensed with in English. De Morgan advises the use of the expression the rectangle ``under`` two lines.
This does not seem to me a very good expression, and, if used in a translation from the Greek, it might suggest that ὑπό in τὸ ὑπό meant ``under``, which it does not.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.44" [label="G.44", URL="/elements2/g.44/", target="_top"];
     "G.62" [label="G.62", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.62/", target="_top"];
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
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.47" [label="G.47", URL="/elements2/g.47/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.17" -> "G.16";
     "G.62" -> "G.44";
     "G.42" -> "G.41";
     "G.47" -> "G.42";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.44" -> "G.38";
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
     "G.62" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.38" -> "G.37";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.62" -> "G.19";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.47" -> "G.36";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.62" -> "G.47";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.44" -> "G.33";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.24" -> "G.22";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }
