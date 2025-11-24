:order: 112
:original_id: III.31
:type: prop
:dependencies: g.26, g.45, g.12, g.18, g.102

.. _g.112:

G.112
=====

**Heath ID:** :ref:`III.31`

   In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of the greater segment is greater than a right angle, and the angle of the less segment less than a right angle.

Let ``ABCD`` be a circle, let ``BC`` be its diameter, and ``E`` its centre, and let ``BA``, ``AC``, ``AD``, ``DC`` be joined; I say that the angle ``BAC`` in the semicircle ``BAC`` is right, the angle ``ABC`` in the segment ``ABC`` greater than the semicircle is less

than a right angle, and the angle ``ADC`` in the segment ``ADC`` less than the semicircle is greater than a right angle.

Let ``AE`` be joined, and let ``BA`` be carried through to ``F``.

Then, since ``BE`` is equal to ``EA``,


.. container:: center

   the angle ``ABE`` is also equal to the angle ``BAE``. [:ref:`g.12`]


Again, since ``CE`` is equal to ``EA``,


.. container:: center

   the angle ``ACE`` is also equal to the angle ``CAE``. [:ref:`g.12`]


Therefore the whole angle ``BAC`` is equal to the two angles ``ABC``, ``ACB``.

But the angle ``FAC`` exterior to the triangle ``ABC`` is also equal to the two angles ``ABC``, ``ACB``; [:ref:`g.45`]


.. container:: center

   therefore the angle ``BAC`` is also equal to the angle ``FAC``; therefore each is right; [:ref:`g.18`] therefore the angle ``BAC`` in the semicircle ``BAC`` is right.


Next, since in the triangle ``ABC`` the two angles ``ABC``, ``BAC`` are less than two right angles, [:ref:`g.26`] and the angle ``BAC`` is a right angle,


.. container:: center

   the angle ``ABC`` is less than a right angle;


and it is the angle in the segment ``ABC`` greater than the semicircle.

Next, since ``ABCD`` is a quadrilateral in a circle, and the opposite angles of quadrilaterals in circles are equal to two right angles, [:ref:`g.102`] while the angle ``ABC`` is less than a right angle, therefore the angle ``ADC`` which remains is greater than a right angle; and it is the angle in the segment ``ADC`` less than the semicircle.

I say further that the angle of the greater segment, namely that contained by the circumference ``ABC`` and the straight line ``AC``, is greater than a right angle; and the angle of the less segment, namely that contained by the circumference ``ADC`` and the straight line ``AC``, is less than a right angle.

This is at once manifest. For, since the angle contained by the straight lines ``BA``, ``AC`` is right,


.. container:: center

   the angle contained by the circumference ``ABC`` and the straight line ``AC`` is greater than a right angle.


Again, since the angle contained by the straight lines ``AC``, ``AF`` is right,


.. container:: center

   the angle contained by the straight line ``CA`` and the circumference ``ADC`` is less than a right angle.


Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
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
     "G.112" [label="G.112", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.112/", target="_top"];
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
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.100" -> "G.12";
     "G.112" -> "G.12";
   }



Required for
------------

:ref:`g.113`, :ref:`g.114`, :ref:`g.115`, :ref:`g.131`, :ref:`g.132`, :ref:`g.133`, :ref:`g.120`, :ref:`g.125`, :ref:`g.127`, :ref:`g.181`, :ref:`g.197`, :ref:`g.200`, :ref:`g.201`, :ref:`g.202`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.347`, :ref:`g.353`, :ref:`g.358`, :ref:`g.361`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.371`, :ref:`g.373`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.381`, :ref:`g.382`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.395`, :ref:`g.396`, :ref:`g.397`, :ref:`g.399`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.509`, :ref:`g.530`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.553`, :ref:`g.555`, :ref:`g.531`, :ref:`g.569`, :ref:`g.570`, :ref:`g.571`, :ref:`g.572`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.563`
