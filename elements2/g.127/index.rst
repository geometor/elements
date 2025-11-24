:order: 127
:original_id: IV.6
:type: prop
:dependencies: g.11, g.126, g.112

.. _g.127:

G.127
=====

**Heath ID:** :ref:`IV.6`

   In a given circle to inscribe a square.

``In a given circle to inscribe a square``.

Let ``ABCD`` be the given circle; thus it is required to inscribe a square in the circle ``ABCD``.

Let two diameters ``AC``, ``BD`` of the circle ``ABCD`` be drawn at right angles to one another, and let ``AB``, ``BC``, ``CD``, ``DA`` be joined.

Then, since ``BE`` is equal to ``ED``, for ``E`` is the centre, and ``EA`` is common and at right angles, therefore the base ``AB`` is equal to the base ``AD``. [:ref:`g.11`]

For the same reason each of the straight lines ``BC``, ``CD`` is also equal to each of the straight lines ``AB``, ``AD``;


.. container:: center

   therefore the quadrilateral ``ABCD`` is equilateral.


I say next that it is also right-angled.

For, since the straight line ``BD`` is a diameter of the circle ``ABCD``, therefore ``BAD`` is a semicircle;


.. container:: center

   therefore the angle ``BAD`` is right. [:ref:`g.112`]


For the same reason each of the angles ``ABC``, ``BCD``, ``CDA`` is also right;


.. container:: center

   therefore the quadrilateral ``ABCD`` is right-angled.


But it was also proved equilateral; therefore it is a square; [:ref:`g.126`] and it has been inscribed in the circle ``ABCD``.

Therefore in the given circle the square ``ABCD`` has been inscribed. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.127" [label="G.127", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.127/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.102" [label="G.102", URL="/elements2/g.102/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.101" [label="G.101", URL="/elements2/g.101/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
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
     "G.100" [label="G.100", URL="/elements2/g.100/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.33" [label="G.33", URL="/elements2/g.33/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.126" [label="G.126", style="rounded,filled", fillcolor=orange, URL="/elements2/g.126/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.17" -> "G.16";
     "G.42" -> "G.41";
     "G.112" -> "G.102";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.102" -> "G.101";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.112" -> "G.18";
     "G.24" -> "G.22";
     "G.127" -> "G.112";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.100" -> "G.45";
     "G.102" -> "G.45";
     "G.112" -> "G.45";
     "G.45" -> "G.44";
     "G.45" -> "G.42";
     "G.42" -> "G.40";
     "G.112" -> "G.26";
     "G.44" -> "G.38";
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
     "G.26" -> "G.25";
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
     "G.127" -> "G.11";
     "G.11" -> "G.10";
     "G.127" -> "G.126";
     "G.14" -> "G.12";
     "G.100" -> "G.12";
     "G.112" -> "G.12";
   }



Required for
------------

:ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`
