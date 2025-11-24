:order: 128
:original_id: IV.7
:type: prop
:dependencies: g.39, g.43, g.47, g.98, g.96

.. _g.128:

G.128
=====

**Heath ID:** :ref:`IV.7`

   About a given circle to circumscribe a square.

Let ``ABCD`` be the given circle; thus it is required to circumscribe a square about the circle ``ABCD``.

Let two diameters ``AC``, ``BD`` of the circle ``ABCD`` be drawn at right angles to one another, and through the points ``A``, ``B``, ``C``, ``D`` let ``FG``, ``GH``, ``HK``, ``KF`` be drawn touching the circle ``ABCD``. [:ref:`g.96`]

Then, since ``FG`` touches the circle ``ABCD``, and ``EA`` has been joined from the centre ``E`` to the point of contact at ``A``,


.. container:: center

   therefore the angles at ``A`` are right. [:ref:`g.98`]


For the same reason


.. container:: center

   the angles at the points ``B``, ``C``, ``D`` are also right.


Now, since the angle ``AEB`` is right, and the angle ``EBG`` is also right,


.. container:: center

   therefore ``GH`` is parailel to ``AC``. [:ref:`g.39`]


For the same reason


.. container:: center

   ``AC`` is also parallel to ``FK``, so that ``GH`` is also parallel to ``FK``. [:ref:`g.43`]


Similarly we can prove that


.. container:: center

   each of the straight lines ``GF``, ``HK`` is parallel to ``BED``.


Therefore ``GK``, ``GC``, ``AK``, ``FB``, ``BK`` are parallelograms; therefore ``GF`` is equal to ``HK``, and ``GH`` to ``FK``. [:ref:`g.47`]

And, since ``AC`` is equal to ``BD``, and ``AC`` is also equal to each of the straight lines ``GH``, ``FK``,


.. container:: center

   while ``BD`` is equal to each of the straight lines ``GF``, ``HK``, [:ref:`g.47`] therefore the quadrilateral ``FGHK`` is equilateral.


I say next that it is also right-angled.

For, since ``GBEA`` is a parallelogram, and the angle ``AEB`` is right, therefore the angle ``AGB`` is also right. [:ref:`g.47`]

Similarly we can prove that


.. container:: center

   the angles at ``H``, ``K``, ``F`` are also right.


Therefore ``FGHK`` is right-angled.

But it was also proved equilateral;


.. container:: center

   therefore it is a square;


and it has been circumscribed about the circle ``ABCD``.

Therefore about the given circle a square has been circumscribed. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.43" [label="G.43", URL="/elements2/g.43/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.41" [label="G.41", style="rounded,filled", fillcolor=orange, URL="/elements2/g.41/", target="_top"];
     "G.128" [label="G.128", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.128/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.27" [label="G.27", URL="/elements2/g.27/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.96" [label="G.96", style="rounded,filled", fillcolor=orange, URL="/elements2/g.96/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.42" [label="G.42", URL="/elements2/g.42/", target="_top"];
     "G.40" [label="G.40", style="rounded,filled", fillcolor=orange, URL="/elements2/g.40/", target="_top"];
     "G.38" [label="G.38", URL="/elements2/g.38/", target="_top"];
     "G.26" [label="G.26", URL="/elements2/g.26/", target="_top"];
     "G.39" [label="G.39", URL="/elements2/g.39/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.37" [label="G.37", style="rounded,filled", fillcolor=orange, URL="/elements2/g.37/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.36" [label="G.36", URL="/elements2/g.36/", target="_top"];
     "G.98" [label="G.98", URL="/elements2/g.98/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.47" [label="G.47", URL="/elements2/g.47/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.128" -> "G.43";
     "G.17" -> "G.16";
     "G.42" -> "G.41";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.24";
     "G.39" -> "G.24";
     "G.42" -> "G.24";
     "G.28" -> "G.27";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.128" -> "G.96";
     "G.98" -> "G.28";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.24" -> "G.22";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.43" -> "G.42";
     "G.47" -> "G.42";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.39" -> "G.38";
     "G.98" -> "G.26";
     "G.128" -> "G.39";
     "G.25" -> "G.17";
     "G.24" -> "G.21";
     "G.26" -> "G.21";
     "G.39" -> "G.21";
     "G.42" -> "G.21";
     "G.15" -> "G.14";
     "G.38" -> "G.37";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.47" -> "G.36";
     "G.128" -> "G.98";
     "G.21" -> "G.19";
     "G.26" -> "G.25";
     "G.27" -> "G.25";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.128" -> "G.47";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.43" -> "G.1";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.26" -> "G.7";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
   }



Required for
------------

:ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`
