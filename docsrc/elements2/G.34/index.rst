:order: 34
:number: 34
:canonical_id: G.34
:original_id: I.23
:volume: I
:book: I
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry
:category: problem, construction, plane-geometry
:tags: book-i, point, segment, line, angle, triangle, equality
:dependencies: G.15, G.33
:excerpt: On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.

.. _G.34:
.. _I.23:

G.34
====

.. rubric:: `I.23 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/23/>`_

.. enunciation::

   On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.

Let :g:`/ A B / <0308.g1:/ A B />` be the given straight line, :g:`A <0308.g1:A>` the point on it, and the angle :g:`< D C E ) <0308.g1:< D C E )>` the given rectilineal angle;

thus it is required to construct on the given straight line :g:`/ A B / <0308.g1:/ A B />`, and at the point :g:`A <0308.g1:A>` on it, a rectilineal angle equal to the given rectilineal angle :g:`< D C E ) <0308.g1:< D C E )>`.

.. picture:: 0308.g1.svg
   :alt: Folio 0308 Figure 1 - Proposition 23

On the straight lines :g:`[ C D ] <0308.g1:[ C D ]>`, :g:`[ C E ] <0308.g1:[ C E ]>` respectively let the points :g:`D <0308.g1:D>`, :g:`E <0308.g1:E>` be taken at random; let :g:`/ D E / <0308.g1:/ D E />` be joined, and out of three straight lines which are equal to the three
straight lines :g:`/ C D / <0308.g1:/ C D />`, :g:`/ D E / <0308.g1:/ D E />`, :g:`/ C E / <0308.g1:/ C E />` let the triangle :g:`< A F G > <0308.g1:< A F G >>` be constructed in such a way that :g:`/ C D / <0308.g1:/ C D />` is :eq:`equal <0308.g1:/ C D / = 0308.g1:/ A F /; 0308.g1:/ C E / = 0308.g1:/ A G /; 0308.g1:/ D E / = 0308.g1:/ F G />` to :g:`/ A F / <0308.g1:/ A F />`, :g:`/ C E / <0308.g1:/ C E />` to :g:`/ A G / <0308.g1:/ A G />`, and further :g:`/ D E / <0308.g1:/ D E />` to :g:`/ F G / <0308.g1:/ F G />`. :just:`[G.33] <G.33>`

Then, since the two sides :g:`/ D C / <0308.g1:/ D C />`, :g:`/ C E / <0308.g1:/ C E />` are :eq:`equal <0308.g1:/ D C / = 0308.g1:/ F A /; 0308.g1:/ C E / = 0308.g1:/ A G />` to the two sides :g:`/ F A / <0308.g1:/ F A />`, :g:`/ A G / <0308.g1:/ A G />` respectively, and the base :g:`/ D E / <0308.g1:/ D E />` is :eq:`equal <0308.g1:/ D E / = 0308.g1:/ F G />` to the base :g:`/ F G / <0308.g1:/ F G />`,

.. assertion:: [G.15] <G.15>

   the angle :g:`< D C E ) <0308.g1:< D C E )>` is :eq:`equal <0308.g1:< D C E ) = 0308.g1:< F A G )>` to the angle :g:`< F A G ) <0308.g1:< F A G )>`.

Therefore on the given straight line :g:`/ A B / <0308.g1:/ A B />`, and at the point :g:`A <0308.g1:A>` on it, the rectilineal angle :g:`< F A G ) <0308.g1:< F A G )>` has been constructed :eq:`equal <0308.g1:< F A G ) = 0308.g1:< D C E )>` to the given rectilineal angle :g:`< D C E ) <0308.g1:< D C E )>`.

.. qed::

   Q. E. F.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.1" [label="G.1", tooltip="G.1 (I.cn.1): Things which are equal to the same thing are also equal to one another.", fillcolor="#442222", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.15): A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure are equal to one another ;", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.post.1): To draw a straight line from any point to any point.", fillcolor="#444422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.post.3): To describe a circle with any centre and distance.", fillcolor="#444422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.1): On a given finite straight line to construct an equilateral triangle.", fillcolor="#222244", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.cn.3): If equals be subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.post.2): To produce a finite straight line continuously in a straight line.", fillcolor="#444422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.2): To place at a given point (as an extremity) a straight line equal to a given straight line.", fillcolor="#222244", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.3): Given two unequal straight lines, to cut off from the greater a straight line equal to the less.", fillcolor="#222244", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.cn.4): [7] 4. Things which coincide with one another are equal to one another.", fillcolor="#442222", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.4): If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base equal to the base...", fillcolor="#222244", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.5): In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another...", fillcolor="#222244", URL="../G.12/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.7): Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its extremities),...", fillcolor="#222244", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.8): If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal...", fillcolor="#222244", URL="../G.15/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.9): To bisect a given rectilineal angle.", fillcolor="#222244", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.10): To bisect a given finite straight line.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is cal...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.11): To draw a straight line at right angles to a given straight line from a given point on it.", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals be added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): That all right angles are equal to one another.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): If two straight lines cut one another, they make the vertical angles equal to one another.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): [8] 5. The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle two sides taken together in any manner are greater than the remaining one.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manne...", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.27" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.8" -> "G.6";
     "G.25" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.27" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.27" -> "G.9";
     "G.29" -> "G.9";
     "G.33" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.25" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
   }

Required for
------------

:ref:`G.35 <G.35>`, :ref:`G.36 <G.36>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`, :ref:`G.62 <G.62>`, :ref:`G.63 <G.63>`, :ref:`G.64 <G.64>`, :ref:`G.65 <G.65>`, :ref:`G.66 <G.66>`, :ref:`G.67 <G.67>`, :ref:`G.68 <G.68>`, :ref:`G.70 <G.70>`, :ref:`G.71 <G.71>`, :ref:`G.72 <G.72>`, :ref:`G.73 <G.73>`, :ref:`G.74 <G.74>`, :ref:`G.75 <G.75>`, :ref:`G.82 <G.82>`, :ref:`G.83 <G.83>`, :ref:`G.91 <G.91>`, :ref:`G.93 <G.93>`, :ref:`G.98 <G.98>`, :ref:`G.99 <G.99>`, :ref:`G.100 <G.100>`, :ref:`G.106 <G.106>`, :ref:`G.108 <G.108>`, :ref:`G.110 <G.110>`, :ref:`G.111 <G.111>`, :ref:`G.112 <G.112>`, :ref:`G.113 <G.113>`, :ref:`G.114 <G.114>`, :ref:`G.115 <G.115>`, :ref:`G.116 <G.116>`, :ref:`G.118 <G.118>`, :ref:`G.119 <G.119>`, :ref:`G.122 <G.122>`, :ref:`G.124 <G.124>`, :ref:`G.126 <G.126>`, :ref:`G.128 <G.128>`, :ref:`G.129 <G.129>`, :ref:`G.130 <G.130>`, :ref:`G.133 <G.133>`, :ref:`G.163 <G.163>`, :ref:`G.164 <G.164>`, :ref:`G.165 <G.165>`, :ref:`G.166 <G.166>`, :ref:`G.167 <G.167>`, :ref:`G.168 <G.168>`, :ref:`G.169 <G.169>`, :ref:`G.171 <G.171>`, :ref:`G.172 <G.172>`, :ref:`G.173 <G.173>`, :ref:`G.174 <G.174>`, :ref:`G.175 <G.175>`, :ref:`G.176 <G.176>`, :ref:`G.177 <G.177>`, :ref:`G.178 <G.178>`, :ref:`G.179 <G.179>`, :ref:`G.180 <G.180>`, :ref:`G.181 <G.181>`, :ref:`G.184 <G.184>`, :ref:`G.185 <G.185>`, :ref:`G.187 <G.187>`, :ref:`G.188 <G.188>`, :ref:`G.189 <G.189>`, :ref:`G.190 <G.190>`, :ref:`G.191 <G.191>`, :ref:`G.192 <G.192>`, :ref:`G.193 <G.193>`, :ref:`G.194 <G.194>`, :ref:`G.195 <G.195>`, :ref:`G.196 <G.196>`, :ref:`G.197 <G.197>`, :ref:`G.198 <G.198>`, :ref:`G.286 <G.286>`, :ref:`G.319 <G.319>`, :ref:`G.320 <G.320>`, :ref:`G.322 <G.322>`, :ref:`G.323 <G.323>`, :ref:`G.324 <G.324>`, :ref:`G.325 <G.325>`, :ref:`G.326 <G.326>`, :ref:`G.327 <G.327>`, :ref:`G.330 <G.330>`, :ref:`G.331 <G.331>`, :ref:`G.333 <G.333>`, :ref:`G.334 <G.334>`, :ref:`G.335 <G.335>`, :ref:`G.336 <G.336>`, :ref:`G.338 <G.338>`, :ref:`G.339 <G.339>`, :ref:`G.340 <G.340>`, :ref:`G.341 <G.341>`, :ref:`G.342 <G.342>`, :ref:`G.343 <G.343>`, :ref:`G.344 <G.344>`, :ref:`G.345 <G.345>`, :ref:`G.346 <G.346>`, :ref:`G.347 <G.347>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.350 <G.350>`, :ref:`G.351 <G.351>`, :ref:`G.352 <G.352>`, :ref:`G.353 <G.353>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.356 <G.356>`, :ref:`G.357 <G.357>`, :ref:`G.358 <G.358>`, :ref:`G.359 <G.359>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.362 <G.362>`, :ref:`G.363 <G.363>`, :ref:`G.364 <G.364>`, :ref:`G.365 <G.365>`, :ref:`G.366 <G.366>`, :ref:`G.367 <G.367>`, :ref:`G.368 <G.368>`, :ref:`G.370 <G.370>`, :ref:`G.372 <G.372>`, :ref:`G.374 <G.374>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.379 <G.379>`, :ref:`G.380 <G.380>`, :ref:`G.381 <G.381>`, :ref:`G.382 <G.382>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.385 <G.385>`, :ref:`G.387 <G.387>`, :ref:`G.388 <G.388>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.391 <G.391>`, :ref:`G.392 <G.392>`, :ref:`G.393 <G.393>`, :ref:`G.394 <G.394>`, :ref:`G.395 <G.395>`, :ref:`G.396 <G.396>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.399 <G.399>`, :ref:`G.400 <G.400>`, :ref:`G.401 <G.401>`, :ref:`G.402 <G.402>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.405 <G.405>`, :ref:`G.407 <G.407>`, :ref:`G.409 <G.409>`, :ref:`G.411 <G.411>`, :ref:`G.413 <G.413>`, :ref:`G.415 <G.415>`, :ref:`G.417 <G.417>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.424 <G.424>`, :ref:`G.425 <G.425>`, :ref:`G.426 <G.426>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.429 <G.429>`, :ref:`G.430 <G.430>`, :ref:`G.431 <G.431>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.434 <G.434>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.438 <G.438>`, :ref:`G.439 <G.439>`, :ref:`G.440 <G.440>`, :ref:`G.441 <G.441>`, :ref:`G.442 <G.442>`, :ref:`G.454 <G.454>`, :ref:`G.455 <G.455>`, :ref:`G.459 <G.459>`, :ref:`G.461 <G.461>`, :ref:`G.465 <G.465>`, :ref:`G.466 <G.466>`, :ref:`G.467 <G.467>`, :ref:`G.468 <G.468>`, :ref:`G.471 <G.471>`, :ref:`G.473 <G.473>`, :ref:`G.478 <G.478>`, :ref:`G.479 <G.479>`, :ref:`G.480 <G.480>`, :ref:`G.481 <G.481>`, :ref:`G.482 <G.482>`, :ref:`G.483 <G.483>`, :ref:`G.484 <G.484>`, :ref:`G.486 <G.486>`, :ref:`G.487 <G.487>`, :ref:`G.488 <G.488>`, :ref:`G.489 <G.489>`, :ref:`G.490 <G.490>`, :ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.495 <G.495>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`, :ref:`G.508 <G.508>`, :ref:`G.509 <G.509>`, :ref:`G.511 <G.511>`, :ref:`G.512 <G.512>`, :ref:`G.513 <G.513>`, :ref:`G.515 <G.515>`, :ref:`G.516 <G.516>`, :ref:`G.517 <G.517>`, :ref:`G.518 <G.518>`, :ref:`G.519 <G.519>`, :ref:`G.520 <G.520>`, :ref:`G.521 <G.521>`, :ref:`G.522 <G.522>`, :ref:`G.523 <G.523>`, :ref:`G.524 <G.524>`, :ref:`G.525 <G.525>`
