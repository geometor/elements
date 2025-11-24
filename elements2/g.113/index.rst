:order: 113
:original_id: III.32
:type: prop
:dependencies: g.45, g.99, g.102, g.112

.. _g.113:

G.113
=====

**Heath ID:** :ref:`III.32`

   If a straight line touch a circle, and from the point of contact there be drawn across, in the circle, a straight line cutting the circle, the angles which it makes with the tangent will be equal to the angles in the alternate segments of the circle.

For let a straight line ``EF`` touch the circle ``ABCD`` at the point ``B``, and from the point ``B`` let there be drawn across, in the circle ``ABCD``, a straight line ``BD`` cutting it; I say that the angles which ``BD`` makes with the tangent ``EF`` will be equal to the angles in the alternate segments of the circle, that is, that the angle ``FBD`` is equal to the angle constructed in the segment ``BAD``, and the angle ``EBD`` is equal to the angle constructed in the segment ``DCB``.

For let ``BA`` be drawn from ``B`` at right angles to ``EF``, let a point ``C`` be taken at random on the circumference ``BD``,

and let ``AD``, ``DC``, ``CB`` be joined.

Then, since a straight line ``EF`` touches the circle ``ABCD`` at ``B``, and ``BA`` has been drawn from the point of contact at right angles to the tangent, the centre of the circle ``ABCD`` is on ``BA``. [:ref:`g.99`]

Therefore ``BA`` is a diameter of the circle ``ABCD``;


.. container:: center

   therefore the angle ``ADB``, being an angle in a semicircle, is right. [:ref:`g.112`]


Therefore the remaining angles ``BAD``, ``ABD`` are equal to one right angle. [:ref:`g.45`]

But the angle ``ABF`` is also right; therefore the angle ``ABF`` is equal to the angles ``BAD``, ``ABD``.

Let the angle ``ABD`` be subtracted from each; therefore the angle ``DBF`` which remains is equal to the angle ``BAD`` in the alternate segment of the circle.

Next, since ``ABCD`` is a quadrilateral in a circle, its opposite angles are equal to two right angles. [:ref:`g.102`]

But the angles ``DBF``, ``DBE`` are also equal to two right angles; therefore the angles ``DBF``, ``DBE`` are equal to the angles ``BAD``, ``BCD``,


.. container:: center

   of which the angle ``BAD`` was proved equal to the angle ``DBF``; therefore the angle ``DBE`` which remains is equal to the angle ``DCB`` in the alternate segment ``DCB`` of the circle.


Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.113" [label="G.113", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.113/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.102" [label="G.102", URL="/elements2/g.102/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.101" [label="G.101", URL="/elements2/g.101/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.27" [label="G.27", URL="/elements2/g.27/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.112" [label="G.112", URL="/elements2/g.112/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.45" [label="G.45", URL="/elements2/g.45/", target="_top"];
     "G.44" [label="G.44", URL="/elements2/g.44/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.26" [label="G.26", URL="/elements2/g.26/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.99" [label="G.99", URL="/elements2/g.99/", target="_top"];
     "G.100" [label="G.100", URL="/elements2/g.100/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.98" [label="G.98", URL="/elements2/g.98/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.17" -> "G.16";
     "G.42" -> "G.41";
     "G.112" -> "G.102";
     "G.113" -> "G.102";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.102" -> "G.101";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.28" -> "G.27";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.98" -> "G.28";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.112" -> "G.18";
     "G.24" -> "G.22";
     "G.113" -> "G.112";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.100" -> "G.45";
     "G.102" -> "G.45";
     "G.112" -> "G.45";
     "G.113" -> "G.45";
     "G.45" -> "G.44";
     "G.45" -> "G.42";
     "G.42" -> "G.40";
     "G.98" -> "G.26";
     "G.112" -> "G.26";
     "G.44" -> "G.38";
     "G.113" -> "G.99";
     "G.101" -> "G.100";
     "G.25" -> "G.17";
     "G.24" -> "G.21";
     "G.26" -> "G.21";
     "G.42" -> "G.21";
     "G.45" -> "G.21";
     "G.15" -> "G.14";
     "G.38" -> "G.37";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.99" -> "G.98";
     "G.26" -> "G.25";
     "G.27" -> "G.25";
     "G.38" -> "G.25";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.9" -> "G.8";
     "G.44" -> "G.33";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.26" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
     "G.100" -> "G.12";
     "G.112" -> "G.12";
   }



Required for
------------

:ref:`g.114`, :ref:`g.115`, :ref:`g.131`, :ref:`g.132`, :ref:`g.133`, :ref:`g.120`, :ref:`g.571`, :ref:`g.578`
