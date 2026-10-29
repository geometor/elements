:order: 463
:number: 463
:canonical_id: G.463
:original_id: XI.18
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, polygon, right-angle, plane
:dependencies: G.19, G.40, G.446, G.451, G.462
:excerpt: If a straight line be at right angles to any plane, all the planes through it will also be at right angles to the same plane.

.. _G.463:
.. _XI.18:

G.463
=====

.. rubric:: `XI.18 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/18/>`_

.. enunciation::

   If a straight line be at right angles to any plane, all the planes through it will also be at right angles to the same plane.

For let any straight line :g:`/ A B / <0306.g1:/ A B />` be at right angles to the plane of reference; I say that all the planes through :g:`/ A B / <0306.g1:/ A B />` are also at right angles to the plane of reference.

.. picture:: 0306.g1.svg
   :alt: Book XI, Proposition 18

For let the plane :g:`< D E > <0306.g1:< D E >>` be drawn through :g:`/ A B / <0306.g1:/ A B />`, let :g:`/ C E / <0306.g1:/ C E />` be the common section of the plane :g:`< D E > <0306.g1:< D E >>` and the plane of reference, let a point :g:`F <0306.g1:F>` be taken at random on :g:`/ C E / <0306.g1:/ C E />`, and from :g:`F <0306.g1:F>` let :g:`/ F G / <0306.g1:/ F G />` be drawn in the plane :g:`< D E > <0306.g1:< D E >>` at right angles to :g:`/ C E / <0306.g1:/ C E />`. :just:`[G.19] <G.19>`

.. subclause::

   Now, since :g:`/ A B / <0306.g1:/ A B />` is at right angles to the plane of reference,

.. assertion::

   :g:`/ A B / <0306.g1:/ A B />` is also at right angles to all the straight lines which meet it and are in the plane of reference; :just:`[G.446] <G.446>` so that it is also at right angles to :g:`/ C E / <0306.g1:/ C E />`; therefore the angle :g:`< A B F ) <0306.g1:< A B F )>` is right.

.. subclause::

   But the angle :g:`< G F B ) <0306.g1:< G F B )>` is also right;

.. assertion:: [G.40] <G.40>

   therefore :g:`/ A B / <0306.g1:/ A B />` is parallel to :g:`/ F G / <0306.g1:/ F G />`.

.. subclause::

   But :g:`/ A B / <0306.g1:/ A B />` is at right angles to the plane of reference;

.. assertion:: [G.451] <G.451>

   therefore :g:`/ F G / <0306.g1:/ F G />` is also at right angles to the plane of reference.

.. subclause::

   Now a plane is at right angles to a plane, when the straight lines drawn, in one of the planes, at right angles to the common section of the planes are at right angles to the remaining plane. :just:`[G.462] <G.462>`

.. subclause::

   And :g:`/ F G / <0306.g1:/ F G />`, drawn in one of the planes :g:`< D E > <0306.g1:< D E >>` at right angles to :g:`/ C E / <0306.g1:/ C E />`, the common section of the planes, was proved to be at right angles to the plane of reference;

.. assertion::

   therefore the plane :g:`< D E > <0306.g1:< D E >>` is at right angles to the plane of reference.

Similarly also it can be proved that all the planes through :g:`/ A B / <0306.g1:/ A B />` are at right angles to the plane of reference.

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
     "G.37" [label="G.37", tooltip="G.37 (I.26): If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of...", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another in either direction.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.28): If a straight line falling on two straight lines make the exterior angle equal to the interior and opposite angle on the same side, or the interior angles on the same side equal to...", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): That, if a straight line falling on two straight lines make the interior angles on the same side less than two right angles, the two straight lines, if produced indefinitely, meet ...", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior an...", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.443" [label="G.443", tooltip="G.443 (XI.1): A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.443/index.html", target="_top"];
     "G.444" [label="G.444", tooltip="G.444 (XI.2): If two straight lines cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.444/index.html", target="_top"];
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line is at right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.447" [label="G.447", tooltip="G.447 (XI.4): If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it will also be at right angles to the plane through the...", fillcolor="#222244", URL="../G.447/index.html", target="_top"];
     "G.450" [label="G.450", tooltip="G.450 (XI.7): If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.", fillcolor="#222244", URL="../G.450/index.html", target="_top"];
     "G.451" [label="G.451", tooltip="G.451 (XI.8): If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one will also be at right angles to the same plane.", fillcolor="#222244", URL="../G.451/index.html", target="_top"];
     "G.462" [label="G.462", tooltip="G.462 (XI.def.4): A plane is at right angles to a plane when the straight lines drawn, in one of the planes, at right angles to the common section of the planes are at right angles to the remaining ...", fillcolor="#224422", URL="../G.462/index.html", target="_top"];
     "G.463" [label="G.463", tooltip="G.463 (XI.18): If a straight line be at right angles to any plane, all the planes through it will also be at right angles to the same plane.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
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
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.37" -> "G.11";
     "G.447" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.447" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.463" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.25" -> "G.22";
     "G.40" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.40" -> "G.25";
     "G.42" -> "G.25";
     "G.447" -> "G.25";
     "G.27" -> "G.26";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.447" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.39";
     "G.463" -> "G.40";
     "G.42" -> "G.41";
     "G.451" -> "G.42";
     "G.444" -> "G.443";
     "G.451" -> "G.444";
     "G.450" -> "G.445";
     "G.447" -> "G.446";
     "G.451" -> "G.446";
     "G.463" -> "G.446";
     "G.451" -> "G.447";
     "G.451" -> "G.450";
     "G.463" -> "G.451";
     "G.463" -> "G.462";
   }

Required for
------------

:ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`
