:canonical_id: G.43
:original_id: I.18
:title: G.43 greater side subtends greater angle
:volume: I
:book: I
:type: prop

G.43 greater side subtends greater angle — Heath
================================================

.. rubric:: `I.18 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/18/>`_

.. enunciation::

   In any :term:`triangle <G.11>` the greater side subtends the greater :term:`angle <G.22>`.

.. picture:: g1.svg
   :alt: Proposition 18 figure

For let :g:`< A B C > <g1:< A B C >>` be a triangle having the side :g:`/ A C / <g1:/ A C />` greater than :g:`/ A B / <g1:/ A B />`;

I say that the angle :g:`< A B C ) <g1:< A B C )>` is also greater than the angle :g:`< B C A ) <g1:< B C A )>`.

For, since :g:`/ A C / <g1:/ A C />` is greater than :g:`/ A B / <g1:/ A B />`, let :g:`/ A D / <g1:/ A D />` be made :eq:`equal <g1:/ A D / = g1:/ A B />` to :g:`/ A B / <g1:/ A B />` :just:`[G.21] <G.21>`, and let :g:`/ B D / <g1:/ B D />` be joined.

Then, since the angle :g:`< A D B ) <g1:< A D B )>` is an exterior angle of the triangle :g:`< B C D > <g1:< B C D >>`,

.. assertion:: [G.41] <G.41>

   it is greater than the interior and opposite angle :g:`< D C B ) <g1:< D C B )>`.

But the angle :g:`< A D B ) <g1:< A D B )>` is :eq:`equal <g1:< A D B ) = g1:< A B D )>` to the angle :g:`< A B D ) <g1:< A B D )>`,

.. subclause::

   since the side :g:`/ A B / <g1:/ A B />` is :eq:`equal <g1:/ A B / = g1:/ A D />` to :g:`/ A D / <g1:/ A D />`;

.. assertion::

   therefore the angle :g:`< A B D ) <g1:< A B D )>` is also greater than the angle :g:`< A C B ) <g1:< A C B )>`;

.. assertion::

   therefore the angle :g:`< A B C ) <g1:< A B C )>` is much greater than the angle :g:`< A C B ) <g1:< A C B )>`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.1" [label="G.1", tooltip="G.1 (I.def.1): A point A is that which has no part.", fillcolor="#224422", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.2): A line [ A B ] is a projection of a relationship of two points A, B.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.def.3): The extremities of a segment / A B / are points A, B.", fillcolor="#224422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.def.4): A segment / A B / is a portion of a line [ A B ] between two points A, B on the line.", fillcolor="#224422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.def.5): A surface is that which has length and breadth only.", fillcolor="#224422", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.def.6): The extremities of a surface are lines or arcs.", fillcolor="#224422", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.def.7): A plane surface lies evenly with the lines on itself.", fillcolor="#224422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.def.15): A circle ( A B ) is a plane figure contained by one arc defined by a center A and a point B establishing its defining radius / A B /, such that all segments / A B /, / A C /, / A D...", fillcolor="#224422", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.13" [label="G.13", tooltip="G.13 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.13/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.post.3): Construct a circle ( A B ) with center A and defining radius point B.", fillcolor="#444422", URL="../G.15/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.cn.1): Things equal to the same thing are equal to one another.", fillcolor="#442222", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.1): Construct an equilateral triangle on a given segment.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.post.2): Extend a segment / A B / continuously along a line [ A B ] to / B C /.", fillcolor="#444422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.cn.3): If equals are subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.19/index.html", target="_top"];
     "G.20" [label="G.20", tooltip="G.20 (I.2): Construct at a given point a segment equal to a given segment.", fillcolor="#222244", URL="../G.20/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.3): Cut off from the greater of two unequal segments a segment equal to the less.", fillcolor="#222244", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.cn.4): Things / A B /, / D E / that coincide with one another are equal to one another.", fillcolor="#442222", URL="../G.23/index.html", target="_top"];
     "G.24" [label="G.24", tooltip="G.24 (I.4): Triangles with two sides and the included angle equal are congruent (SAS).", fillcolor="#222244", URL="../G.24/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.5): In an isosceles triangle, the angles at the base are equal, and if the equal sides are extended, the angles under the base are equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.def.9): A rectilineal angle is contained by two segments or lines.", fillcolor="#224422", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.10): Bisect a given segment.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.32/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.11): Construct a segment at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.35" [label="G.35", tooltip="G.35 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.35/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.13): A segment standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.36/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.37/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.41/index.html", target="_top"];
     "G.43" [label="G.43", tooltip="G.43 (I.18): In any triangle, the greater side subtends the greater angle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.13" -> "G.1";
     "G.14" -> "G.1";
     "G.20" -> "G.1";
     "G.27" -> "G.1";
     "G.33" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.29" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.27" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.13" -> "G.4";
     "G.17" -> "G.4";
     "G.18" -> "G.4";
     "G.20" -> "G.4";
     "G.21" -> "G.4";
     "G.22" -> "G.4";
     "G.24" -> "G.4";
     "G.25" -> "G.4";
     "G.27" -> "G.4";
     "G.28" -> "G.4";
     "G.31" -> "G.4";
     "G.32" -> "G.4";
     "G.33" -> "G.4";
     "G.36" -> "G.4";
     "G.39" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.28" -> "G.11";
     "G.41" -> "G.11";
     "G.43" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.41" -> "G.13";
     "G.15" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.36" -> "G.16";
     "G.39" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.33" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.20" -> "G.19";
     "G.39" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.30" -> "G.21";
     "G.33" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.32" -> "G.22";
     "G.36" -> "G.22";
     "G.39" -> "G.22";
     "G.41" -> "G.22";
     "G.43" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.31" -> "G.24";
     "G.41" -> "G.24";
     "G.27" -> "G.25";
     "G.28" -> "G.27";
     "G.30" -> "G.28";
     "G.33" -> "G.28";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.41" -> "G.31";
     "G.33" -> "G.32";
     "G.36" -> "G.32";
     "G.37" -> "G.32";
     "G.36" -> "G.33";
     "G.36" -> "G.35";
     "G.39" -> "G.36";
     "G.39" -> "G.37";
     "G.41" -> "G.39";
     "G.41" -> "G.40";
     "G.43" -> "G.41";
   }

Required for
------------

:ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.47 <G.47>`, :ref:`G.48 <G.48>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.66 <G.66>`, :ref:`G.67 <G.67>`, :ref:`G.68 <G.68>`, :ref:`G.69 <G.69>`, :ref:`G.70 <G.70>`, :ref:`G.71 <G.71>`, :ref:`G.73 <G.73>`, :ref:`G.74 <G.74>`, :ref:`G.75 <G.75>`, :ref:`G.79 <G.79>`, :ref:`G.80 <G.80>`, :ref:`G.82 <G.82>`, :ref:`G.83 <G.83>`, :ref:`G.84 <G.84>`, :ref:`G.85 <G.85>`, :ref:`G.87 <G.87>`, :ref:`G.88 <G.88>`, :ref:`G.89 <G.89>`, :ref:`G.91 <G.91>`, :ref:`G.92 <G.92>`, :ref:`G.93 <G.93>`, :ref:`G.94 <G.94>`, :ref:`G.95 <G.95>`, :ref:`G.97 <G.97>`, :ref:`G.99 <G.99>`, :ref:`G.105 <G.105>`, :ref:`G.106 <G.106>`, :ref:`G.110 <G.110>`, :ref:`G.112 <G.112>`, :ref:`G.114 <G.114>`, :ref:`G.116 <G.116>`, :ref:`G.118 <G.118>`, :ref:`G.119 <G.119>`, :ref:`G.120 <G.120>`, :ref:`G.121 <G.121>`, :ref:`G.123 <G.123>`, :ref:`G.124 <G.124>`, :ref:`G.125 <G.125>`, :ref:`G.134 <G.134>`, :ref:`G.136 <G.136>`, :ref:`G.139 <G.139>`, :ref:`G.140 <G.140>`, :ref:`G.141 <G.141>`, :ref:`G.142 <G.142>`, :ref:`G.143 <G.143>`, :ref:`G.144 <G.144>`, :ref:`G.145 <G.145>`, :ref:`G.149 <G.149>`, :ref:`G.151 <G.151>`, :ref:`G.154 <G.154>`, :ref:`G.157 <G.157>`, :ref:`G.158 <G.158>`, :ref:`G.159 <G.159>`, :ref:`G.160 <G.160>`, :ref:`G.162 <G.162>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.165 <G.165>`, :ref:`G.167 <G.167>`, :ref:`G.210 <G.210>`, :ref:`G.211 <G.211>`, :ref:`G.212 <G.212>`, :ref:`G.213 <G.213>`, :ref:`G.214 <G.214>`, :ref:`G.215 <G.215>`, :ref:`G.216 <G.216>`, :ref:`G.218 <G.218>`, :ref:`G.219 <G.219>`, :ref:`G.220 <G.220>`, :ref:`G.221 <G.221>`, :ref:`G.222 <G.222>`, :ref:`G.223 <G.223>`, :ref:`G.225 <G.225>`, :ref:`G.226 <G.226>`, :ref:`G.227 <G.227>`, :ref:`G.228 <G.228>`, :ref:`G.229 <G.229>`, :ref:`G.231 <G.231>`, :ref:`G.232 <G.232>`, :ref:`G.234 <G.234>`, :ref:`G.235 <G.235>`, :ref:`G.236 <G.236>`, :ref:`G.237 <G.237>`, :ref:`G.238 <G.238>`, :ref:`G.239 <G.239>`, :ref:`G.240 <G.240>`, :ref:`G.241 <G.241>`, :ref:`G.243 <G.243>`, :ref:`G.244 <G.244>`, :ref:`G.245 <G.245>`, :ref:`G.246 <G.246>`, :ref:`G.345 <G.345>`, :ref:`G.377 <G.377>`, :ref:`G.378 <G.378>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.386 <G.386>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.393 <G.393>`, :ref:`G.394 <G.394>`, :ref:`G.395 <G.395>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.406 <G.406>`, :ref:`G.407 <G.407>`, :ref:`G.408 <G.408>`, :ref:`G.409 <G.409>`, :ref:`G.410 <G.410>`, :ref:`G.411 <G.411>`, :ref:`G.412 <G.412>`, :ref:`G.413 <G.413>`, :ref:`G.414 <G.414>`, :ref:`G.415 <G.415>`, :ref:`G.416 <G.416>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.423 <G.423>`, :ref:`G.425 <G.425>`, :ref:`G.427 <G.427>`, :ref:`G.429 <G.429>`, :ref:`G.431 <G.431>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.443 <G.443>`, :ref:`G.444 <G.444>`, :ref:`G.445 <G.445>`, :ref:`G.446 <G.446>`, :ref:`G.447 <G.447>`, :ref:`G.448 <G.448>`, :ref:`G.449 <G.449>`, :ref:`G.450 <G.450>`, :ref:`G.451 <G.451>`, :ref:`G.452 <G.452>`, :ref:`G.453 <G.453>`, :ref:`G.455 <G.455>`, :ref:`G.457 <G.457>`, :ref:`G.458 <G.458>`, :ref:`G.459 <G.459>`, :ref:`G.460 <G.460>`, :ref:`G.461 <G.461>`, :ref:`G.462 <G.462>`, :ref:`G.463 <G.463>`, :ref:`G.464 <G.464>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.470 <G.470>`, :ref:`G.472 <G.472>`, :ref:`G.474 <G.474>`, :ref:`G.476 <G.476>`, :ref:`G.477 <G.477>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.485 <G.485>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.498 <G.498>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.513 <G.513>`, :ref:`G.514 <G.514>`, :ref:`G.518 <G.518>`, :ref:`G.520 <G.520>`, :ref:`G.525 <G.525>`, :ref:`G.526 <G.526>`, :ref:`G.527 <G.527>`, :ref:`G.528 <G.528>`, :ref:`G.532 <G.532>`, :ref:`G.536 <G.536>`, :ref:`G.541 <G.541>`, :ref:`G.542 <G.542>`, :ref:`G.543 <G.543>`, :ref:`G.544 <G.544>`, :ref:`G.545 <G.545>`, :ref:`G.546 <G.546>`, :ref:`G.547 <G.547>`, :ref:`G.550 <G.550>`, :ref:`G.551 <G.551>`, :ref:`G.552 <G.552>`, :ref:`G.554 <G.554>`, :ref:`G.555 <G.555>`, :ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.560 <G.560>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.574 <G.574>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`, :ref:`G.579 <G.579>`, :ref:`G.580 <G.580>`, :ref:`G.582 <G.582>`, :ref:`G.583 <G.583>`, :ref:`G.584 <G.584>`, :ref:`G.586 <G.586>`, :ref:`G.587 <G.587>`, :ref:`G.588 <G.588>`, :ref:`G.589 <G.589>`, :ref:`G.590 <G.590>`, :ref:`G.592 <G.592>`, :ref:`G.594 <G.594>`, :ref:`G.595 <G.595>`, :ref:`G.597 <G.597>`, :ref:`G.600 <G.600>`, :ref:`G.601 <G.601>`
