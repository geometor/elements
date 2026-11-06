:order: 545
:number: 545
:canonical_id: G.545
:original_id: XI.35
:title: G.545 there equal plane
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, triangle, plane-angle, straight-line, perpendicular, plane-surface, rectilineal-angle, parallel-straight-lines, square, trilateral, extremity, plane, equality, porism
:dependencies: G.1, G.4, G.7, G.14, G.21, G.22, G.24, G.29, G.33, G.51, G.58, G.63, G.79, G.80, G.510
:excerpt: If there be two equal plane angles, and on their vertices there be set up elevated segments containing equal angles with the original segments respectively, if on the elevated segments points be taken at random and perpendiculars be drawn from them to the planes in which the original angles are, and if from the points so arising in the planes segments be joined to the vertices of the original angles, they will contain, with the elevated segments, equal angles.

.. _G.545:
.. _XI.35:

G.545 there equal plane
=======================

.. rubric:: `XI.35 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/35/>`_

.. enunciation::

   If there be two equal :term:`plane angles <G.22>`, and on their vertices there be set up elevated :term:`segments <G.4>` containing equal angles with the original segments respectively, if on the elevated segments :term:`points <G.1>` be taken at random and :term:`perpendiculars <G.33>` be drawn from them to the :term:`planes <G.7>` in which the original angles are, and if from the points so arising in the planes segments be joined to the vertices of the original angles, they will contain, with the elevated segments, equal angles.

.. signature:: theorem

   | :fn:`there_equal_plane <G.545>`\ ()
   | **prove** :g:`< G A L ) <g1:< G A L )>` :eq:`= <g1:< G A L ) = g1:< M D N )>` :g:`< M D N ) <g1:< M D N )>`

.. picture:: g1.svg
   :alt: Book XI, Proposition 35

.. step:: construct

   :fn:`segment <G.14>`\ () → :g:`< B A C ) <g1:< B A C )>`, :fn:`segment <G.14>`\ () → :g:`< E D F ) <g1:< E D F )>`, :fn:`segment <G.14>`\ () → :g:`A <g1:A>`, :fn:`segment <G.14>`\ () → :g:`D <g1:D>`, :fn:`segment <G.14>`\ (:g:`A <g1:A>`, :g:`G <g1:G>`) → :g:`/ A G / <g1:/ A G />`, :fn:`segment <G.14>`\ (:g:`D <g1:D>`, :g:`M <g1:M>`) → :g:`/ D M / <g1:/ D M />`, :fn:`segment <G.14>`\ () → :g:`< M D E ) <g1:< M D E )>`, :fn:`segment <G.14>`\ () → :g:`< G A B ) <g1:< G A B )>`, :fn:`segment <G.14>`\ () → :g:`< M D F ) <g1:< M D F )>`, :fn:`segment <G.14>`\ () → :g:`< G A C ) <g1:< G A C )>`, :fn:`segment <G.14>`\ () → :g:`G <g1:G>`, :fn:`segment <G.14>`\ () → :g:`M <g1:M>`, :fn:`segment <G.14>`\ (:g:`A <g1:A>`, :g:`G <g1:G>`) → :g:`/ A G / <g1:/ A G />`, :fn:`segment <G.14>`\ (:g:`D <g1:D>`, :g:`M <g1:M>`) → :g:`/ D M / <g1:/ D M />`, :fn:`segment <G.14>`\ (:g:`G <g1:G>`, :g:`L <g1:L>`) → :g:`/ G L / <g1:/ G L />`, :fn:`segment <G.14>`\ (:g:`M <g1:M>`, :g:`N <g1:N>`) → :g:`/ M N / <g1:/ M N />`, :fn:`segment <G.14>`\ () → :g:`G <g1:G>`, :fn:`segment <G.14>`\ () → :g:`M <g1:M>`, :fn:`segment <G.14>`\ (:g:`B <g1:B>`, :g:`A <g1:A>`) → :g:`/ B A / <g1:/ B A />`, :fn:`segment <G.14>`\ (:g:`A <g1:A>`, :g:`C <g1:C>`) → :g:`/ A C / <g1:/ A C />`, :fn:`segment <G.14>`\ (:g:`E <g1:E>`, :g:`D <g1:D>`) → :g:`/ E D / <g1:/ E D />`, :fn:`segment <G.14>`\ (:g:`D <g1:D>`, :g:`F <g1:F>`) → :g:`/ D F / <g1:/ D F />`, :fn:`segment <G.14>`\ () → :g:`L <g1:L>`, :fn:`segment <G.14>`\ () → :g:`N <g1:N>`, :fn:`segment <G.14>`\ (:g:`L <g1:L>`, :g:`A <g1:A>`) → :g:`/ L A / <g1:/ L A />`, :fn:`segment <G.14>`\ (:g:`N <g1:N>`, :g:`D <g1:D>`) → :g:`/ N D / <g1:/ N D />`

.. step:: construct

   :fn:`cut_equal_segment <G.21>`\ (:g:`/ D M / <g1:/ D M />`) → :g:`/ A H / <g1:/ A H />` (:eq:`equal <g1:/ A H / = g1:/ D M />`)

.. step:: construct

   :fn:`parallel_line <G.58>`\ (:g:`H <g1:H>`, :g:`/ G L / <g1:/ G L />`) → :g:`/ H K / <g1:/ H K />`

.. step:: assert

   :g:`/ G L / <g1:/ G L />` is perpendicular to the plane through :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />`

.. step:: assert ∵ segments_parallel_right <G.510>

   :g:`/ H K / <g1:/ H K />` is also perpendicular to the plane through :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />`

.. step:: construct

   From :g:`K <g1:K>`, :g:`N <g1:N>` let :g:`/ K C / <g1:/ K C />`, :g:`/ N F / <g1:/ N F />`, :g:`/ K B / <g1:/ K B />`, :g:`/ N E / <g1:/ N E />` be drawn :eq:`perpendicular <g1:/ K C / = g1:/ A C /; g1:/ N F / = g1:/ D F /; g1:/ K B / = g1:/ A B /; g1:/ N E / = g1:/ D E />` to :g:`/ A C / <g1:/ A C />`, :g:`/ D F / <g1:/ D F />`, :g:`/ A B / <g1:/ A B />`, :g:`/ D E / <g1:/ D E />`, and let :g:`/ H C / <g1:/ H C />`, :g:`/ C B / <g1:/ C B />`, :g:`/ M F / <g1:/ M F />`, :g:`/ F E / <g1:/ F E />` be joined.

.. step:: assert ∵ pythagorean_theorem <G.79>

   the :term:`square <G.63>` on :g:`/ H A / <g1:/ H A />` is equal to the squares on :g:`/ H K / <g1:/ H K />`, :g:`/ K A / <g1:/ K A />`, and the squares on :g:`/ K C / <g1:/ K C />`, :g:`/ C A / <g1:/ C A />` are equal to the square on :g:`/ K A / <g1:/ K A />`

.. step:: assert

   the square on :g:`/ H A / <g1:/ H A />` is also equal to the squares on :g:`/ H K / <g1:/ H K />`, :g:`/ K C / <g1:/ K C />`, :g:`/ C A / <g1:/ C A />`

.. step:: assert ∵ pythagorean_theorem <G.79>

   The square on :g:`/ H C / <g1:/ H C />` is equal to the squares on :g:`/ H K / <g1:/ H K />`, :g:`/ K C / <g1:/ K C />`

.. step:: assert

   the square on :g:`/ H A / <g1:/ H A />` is equal to the squares on :g:`/ H C / <g1:/ H C />`, :g:`/ C A / <g1:/ C A />`

.. step:: assert ∵ converse_pythagorean <G.80>

   :g:`< H C A ) <g1:< H C A )>` is :eq:`right <g1:< H C A )>`

.. step:: assert

   For the same reason :g:`< D F M ) <g1:< D F M )>` is also :eq:`right <g1:< D F M )>`

.. step:: assert

   :g:`< A C H ) <g1:< A C H )>` :eq:`= <g1:< A C H ) = g1:< D F M )>` :g:`< D F M ) <g1:< D F M )>`

.. step:: assert

   :g:`< H A C ) <g1:< H A C )>` :eq:`= <g1:< H A C ) = g1:< M D F )>` :g:`< M D F ) <g1:< M D F )>`

.. step:: assert ∵ asa_aas_congruence <G.51>

   :g:`< M D F > <g1:< M D F >>`, :g:`< H A C > <g1:< H A C >>` are two triangles which have two angles equal to two angles, and one side equal to one side, namely, that subtending one of the equal angles, that is, :g:`/ H A / <g1:/ H A />` :eq:`= <g1:/ H A / = g1:/ M D />` to :g:`/ M D / <g1:/ M D />`; therefore they will also have the remaining sides equal to the remaining sides

.. step:: assert

   :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`

.. step:: assert

   Similarly we can prove that :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />`

.. step:: assert

   then :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ D F /; g1:/ A B / = g1:/ D E />` :g:`/ D F / <g1:/ D F />`, and :g:`/ A B / <g1:/ A B />` to :g:`/ D E / <g1:/ D E />`, :g:`/ C A / <g1:/ C A />`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ C A / = g1:/ F D /; g1:/ A B / = g1:/ D E />` :g:`/ F D / <g1:/ F D />`, :g:`/ D E / <g1:/ D E />`

.. step:: assert

   :g:`< C A B ) <g1:< C A B )>` :eq:`= <g1:< C A B ) = g1:< F D E )>` :g:`< F D E ) <g1:< F D E )>`

.. step:: assert ∵ sas_congruence <G.24>

   :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`, the triangle to the triangle, and the remaining angles to the remaining angles; therefore :g:`< A C B ) <g1:< A C B )>` :eq:`= <g1:< A C B ) = g1:< D F E )>` :g:`< D F E ) <g1:< D F E )>`

.. step:: assert

   The right angle :g:`< A C K ) <g1:< A C K )>` :eq:`= <g1:< A C K ) = g1:< D F N )>` the right angle :g:`< D F N ) <g1:< D F N )>`

.. step:: assert

   :g:`< B C K ) <g1:< B C K )>` :eq:`= <g1:< B C K ) = g1:< E F N )>` :g:`< E F N ) <g1:< E F N )>`

.. step:: assert

   For the same reason :g:`< C B K ) <g1:< C B K )>` :eq:`= <g1:< C B K ) = g1:< F E N )>` :g:`< F E N ) <g1:< F E N )>`

.. step:: assert ∵ asa_aas_congruence <G.51>

   :g:`< B C K > <g1:< B C K >>`, :g:`< E F N > <g1:< E F N >>` are two triangles which have two angles equal to two angles, and one side equal to one side, namely, that adjacent to the equal angles, that is, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` to :g:`/ E F / <g1:/ E F />`; therefore they will also have the remaining sides equal to the remaining sides

.. step:: assert

   :g:`/ C K / <g1:/ C K />` :eq:`= <g1:/ C K / = g1:/ F N />` :g:`/ F N / <g1:/ F N />`

.. step:: assert

   :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`

.. step:: assert

   :g:`/ A C / <g1:/ A C />`, :g:`/ C K / <g1:/ C K />` :eq:`= <g1:/ A C / = g1:/ D F /; g1:/ C K / = g1:/ F N />` :g:`/ D F / <g1:/ D F />`, :g:`/ F N / <g1:/ F N />`; and they contain right angles

.. step:: assert ∵ sas_congruence <G.24>

   :g:`/ A K / <g1:/ A K />` :eq:`= <g1:/ A K / = g1:/ D N />` :g:`/ D N / <g1:/ D N />`

.. step:: assert

   since :g:`/ A H / <g1:/ A H />` :eq:`= <g1:/ A H / = g1:/ D M />` :g:`/ D M / <g1:/ D M />`,

.. step:: assert

   The square on :g:`/ A H / <g1:/ A H />` :eq:`= <g1:/ A H / = g1:/ D M />` the square on :g:`/ D M / <g1:/ D M />`

.. step:: assert ∵ pythagorean_theorem <G.79>

   The squares on :g:`/ A K / <g1:/ A K />`, :g:`/ K H / <g1:/ K H />` are equal to the square on :g:`/ A H / <g1:/ A H />`, for :g:`< A K H ) <g1:< A K H )>` is :eq:`right <g1:< A K H )>`; and the squares on :g:`/ D N / <g1:/ D N />`, :g:`/ N M / <g1:/ N M />` are equal to the square on :g:`/ D M / <g1:/ D M />`, for :g:`< D N M ) <g1:< D N M )>` is :eq:`right <g1:< D N M )>`

.. step:: assert

   the squares on :g:`/ A K / <g1:/ A K />`, :g:`/ K H / <g1:/ K H />` are equal to the squares on :g:`/ D N / <g1:/ D N />`, :g:`/ N M / <g1:/ N M />`; and of these the square on :g:`/ A K / <g1:/ A K />` :eq:`= <g1:/ A K / = g1:/ D N />` the square on :g:`/ D N / <g1:/ D N />`; therefore the remaining square on :g:`/ K H / <g1:/ K H />` :eq:`= <g1:/ K H / = g1:/ N M />` the square on :g:`/ N M / <g1:/ N M />`; therefore :g:`/ H K / <g1:/ H K />` :eq:`= <g1:/ H K / = g1:/ M N />` :g:`/ M N / <g1:/ M N />`

.. step:: assert

   since :g:`/ H A / <g1:/ H A />`, :g:`/ A K / <g1:/ A K />` :eq:`= <g1:/ H A / = g1:/ M D /; g1:/ A K / = g1:/ D N />` :g:`/ M D / <g1:/ M D />`, :g:`/ D N / <g1:/ D N />`, and :g:`/ H K / <g1:/ H K />` :eq:`= <g1:/ H K / = g1:/ M N />` :g:`/ M N / <g1:/ M N />`,

.. step:: assert ∵ sss_congruence <G.29>

   :g:`< H A K ) <g1:< H A K )>` :eq:`= <g1:< H A K ) = g1:< M D N )>` :g:`< M D N ) <g1:< M D N )>`

.. step:: conclude

   etc

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
     "G.11" [label="G.11", tooltip="G.11 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.def.19): Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.", fillcolor="#224422", URL="../G.12/index.html", target="_top"];
     "G.13" [label="G.13", tooltip="G.13 (I.def.20): Of trilateral figures, an equilateral triangle < A B C > has three equal sides, an isosceles triangle < D E F > has two equal sides, and a scalene triangle < G H K > has three uneq...", fillcolor="#224422", URL="../G.13/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.post.1): Construct a segment / A B / between any two points A, B.", fillcolor="#444422", URL="../G.14/index.html", target="_top"];
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
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.def.9): A rectilineal angle is contained by two segments or lines.", fillcolor="#224422", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.10): Bisect a given segment.", fillcolor="#222244", URL="../G.32/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.11): Construct a segment at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.36/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.13): A segment standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.14): If two segments at a point on a line on opposite sides make adjacent angles summing to two right angles, the two segments are collinear.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.41/index.html", target="_top"];
     "G.43" [label="G.43", tooltip="G.43 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.43/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.def.23): Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.52/index.html", target="_top"];
     "G.53" [label="G.53", tooltip="G.53 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.53/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.58" [label="G.58", tooltip="G.58 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.58/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.62" [label="G.62", tooltip="G.62 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.62/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.64" [label="G.64", tooltip="G.64 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.64/index.html", target="_top"];
     "G.66" [label="G.66", tooltip="G.66 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.66/index.html", target="_top"];
     "G.70" [label="G.70", tooltip="G.70 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.70/index.html", target="_top"];
     "G.75" [label="G.75", tooltip="G.75 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.75/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (I.def.11): An obtuse angle is greater than a right angle.", fillcolor="#224422", URL="../G.76/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.78" [label="G.78", tooltip="G.78 (I.def.21): A right-angled triangle has a right angle, an obtuse-angled triangle has an obtuse angle, and an acute-angled triangle has three acute angles.", fillcolor="#224422", URL="../G.78/index.html", target="_top"];
     "G.79" [label="G.79", tooltip="G.79 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.79/index.html", target="_top"];
     "G.80" [label="G.80", tooltip="G.80 (I.48): If the square on one side of a triangle equals the sum of the squares on the other two sides, the angle contained by those two sides is right.", fillcolor="#222244", URL="../G.80/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.502" [label="G.502", tooltip="G.502 (XI.1): A part of a segment cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.502/index.html", target="_top"];
     "G.503" [label="G.503", tooltip="G.503 (XI.2): If two segments cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.503/index.html", target="_top"];
     "G.504" [label="G.504", tooltip="G.504 (XI.3): If two planes cut one another, their common section is a segment.", fillcolor="#222244", URL="../G.504/index.html", target="_top"];
     "G.505" [label="G.505", tooltip="G.505 (XI.def.3): Asegment isat right angles to a plane, when it makesright angles with all the segments which meet it and are in theplane.", fillcolor="#224422", URL="../G.505/index.html", target="_top"];
     "G.506" [label="G.506", tooltip="G.506 (XI.4): If a segment be set up at right angles to two segments which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.506/index.html", target="_top"];
     "G.509" [label="G.509", tooltip="G.509 (XI.7): If two segments be parallel and points be taken at random on each of them, the segment joining the points is in the same plane with the parallel lines.", fillcolor="#222244", URL="../G.509/index.html", target="_top"];
     "G.510" [label="G.510", tooltip="G.510 (XI.8): If two segments be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.510/index.html", target="_top"];
     "G.545" [label="G.545", tooltip="G.545 (XI.35): If there be two equal plane angles, and on their vertices there be set up elevated segments containing equal angles with the original segments respectively, if on the elevated segm...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.11" -> "G.1";
     "G.14" -> "G.1";
     "G.15" -> "G.1";
     "G.17" -> "G.1";
     "G.20" -> "G.1";
     "G.21" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.28" -> "G.1";
     "G.29" -> "G.1";
     "G.31" -> "G.1";
     "G.32" -> "G.1";
     "G.34" -> "G.1";
     "G.37" -> "G.1";
     "G.39" -> "G.1";
     "G.40" -> "G.1";
     "G.45" -> "G.1";
     "G.47" -> "G.1";
     "G.48" -> "G.1";
     "G.58" -> "G.1";
     "G.75" -> "G.1";
     "G.79" -> "G.1";
     "G.80" -> "G.1";
     "G.506" -> "G.1";
     "G.509" -> "G.1";
     "G.545" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.7" -> "G.2";
     "G.18" -> "G.2";
     "G.22" -> "G.2";
     "G.30" -> "G.2";
     "G.33" -> "G.2";
     "G.34" -> "G.2";
     "G.37" -> "G.2";
     "G.39" -> "G.2";
     "G.40" -> "G.2";
     "G.48" -> "G.2";
     "G.52" -> "G.2";
     "G.53" -> "G.2";
     "G.55" -> "G.2";
     "G.56" -> "G.2";
     "G.58" -> "G.2";
     "G.504" -> "G.2";
     "G.509" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.504" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.12" -> "G.4";
     "G.14" -> "G.4";
     "G.17" -> "G.4";
     "G.18" -> "G.4";
     "G.20" -> "G.4";
     "G.21" -> "G.4";
     "G.22" -> "G.4";
     "G.24" -> "G.4";
     "G.25" -> "G.4";
     "G.28" -> "G.4";
     "G.29" -> "G.4";
     "G.30" -> "G.4";
     "G.31" -> "G.4";
     "G.32" -> "G.4";
     "G.33" -> "G.4";
     "G.34" -> "G.4";
     "G.37" -> "G.4";
     "G.39" -> "G.4";
     "G.40" -> "G.4";
     "G.41" -> "G.4";
     "G.47" -> "G.4";
     "G.48" -> "G.4";
     "G.52" -> "G.4";
     "G.53" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.58" -> "G.4";
     "G.61" -> "G.4";
     "G.62" -> "G.4";
     "G.75" -> "G.4";
     "G.79" -> "G.4";
     "G.80" -> "G.4";
     "G.502" -> "G.4";
     "G.503" -> "G.4";
     "G.504" -> "G.4";
     "G.505" -> "G.4";
     "G.506" -> "G.4";
     "G.509" -> "G.4";
     "G.510" -> "G.4";
     "G.545" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.502" -> "G.7";
     "G.503" -> "G.7";
     "G.504" -> "G.7";
     "G.505" -> "G.7";
     "G.506" -> "G.7";
     "G.509" -> "G.7";
     "G.510" -> "G.7";
     "G.545" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.66" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.47" -> "G.10";
     "G.61" -> "G.10";
     "G.502" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.47" -> "G.11";
     "G.61" -> "G.11";
     "G.502" -> "G.11";
     "G.13" -> "G.12";
     "G.17" -> "G.12";
     "G.20" -> "G.12";
     "G.24" -> "G.12";
     "G.25" -> "G.12";
     "G.28" -> "G.12";
     "G.29" -> "G.12";
     "G.31" -> "G.12";
     "G.32" -> "G.12";
     "G.34" -> "G.12";
     "G.41" -> "G.12";
     "G.43" -> "G.12";
     "G.44" -> "G.12";
     "G.45" -> "G.12";
     "G.47" -> "G.12";
     "G.48" -> "G.12";
     "G.51" -> "G.12";
     "G.53" -> "G.12";
     "G.62" -> "G.12";
     "G.63" -> "G.12";
     "G.64" -> "G.12";
     "G.66" -> "G.12";
     "G.70" -> "G.12";
     "G.78" -> "G.12";
     "G.79" -> "G.12";
     "G.80" -> "G.12";
     "G.503" -> "G.12";
     "G.17" -> "G.13";
     "G.25" -> "G.13";
     "G.63" -> "G.13";
     "G.75" -> "G.13";
     "G.17" -> "G.14";
     "G.20" -> "G.14";
     "G.25" -> "G.14";
     "G.28" -> "G.14";
     "G.31" -> "G.14";
     "G.34" -> "G.14";
     "G.41" -> "G.14";
     "G.43" -> "G.14";
     "G.45" -> "G.14";
     "G.47" -> "G.14";
     "G.48" -> "G.14";
     "G.51" -> "G.14";
     "G.58" -> "G.14";
     "G.70" -> "G.14";
     "G.79" -> "G.14";
     "G.80" -> "G.14";
     "G.503" -> "G.14";
     "G.510" -> "G.14";
     "G.545" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.47" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.37" -> "G.16";
     "G.39" -> "G.16";
     "G.40" -> "G.16";
     "G.47" -> "G.16";
     "G.56" -> "G.16";
     "G.64" -> "G.16";
     "G.66" -> "G.16";
     "G.70" -> "G.16";
     "G.75" -> "G.16";
     "G.80" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.34" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.39" -> "G.18";
     "G.41" -> "G.18";
     "G.45" -> "G.18";
     "G.53" -> "G.18";
     "G.58" -> "G.18";
     "G.66" -> "G.18";
     "G.20" -> "G.19";
     "G.25" -> "G.19";
     "G.39" -> "G.19";
     "G.40" -> "G.19";
     "G.64" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.31" -> "G.21";
     "G.34" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
     "G.45" -> "G.21";
     "G.47" -> "G.21";
     "G.51" -> "G.21";
     "G.75" -> "G.21";
     "G.80" -> "G.21";
     "G.545" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.30" -> "G.22";
     "G.31" -> "G.22";
     "G.32" -> "G.22";
     "G.33" -> "G.22";
     "G.34" -> "G.22";
     "G.37" -> "G.22";
     "G.39" -> "G.22";
     "G.40" -> "G.22";
     "G.41" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.45" -> "G.22";
     "G.48" -> "G.22";
     "G.51" -> "G.22";
     "G.53" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.58" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.64" -> "G.22";
     "G.75" -> "G.22";
     "G.76" -> "G.22";
     "G.77" -> "G.22";
     "G.78" -> "G.22";
     "G.79" -> "G.22";
     "G.80" -> "G.22";
     "G.545" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.62" -> "G.24";
     "G.64" -> "G.24";
     "G.79" -> "G.24";
     "G.506" -> "G.24";
     "G.545" -> "G.24";
     "G.28" -> "G.25";
     "G.43" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.28" -> "G.26";
     "G.39" -> "G.26";
     "G.41" -> "G.26";
     "G.43" -> "G.26";
     "G.45" -> "G.26";
     "G.51" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.48" -> "G.29";
     "G.80" -> "G.29";
     "G.506" -> "G.29";
     "G.545" -> "G.29";
     "G.31" -> "G.30";
     "G.48" -> "G.30";
     "G.32" -> "G.31";
     "G.41" -> "G.32";
     "G.34" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.39" -> "G.33";
     "G.40" -> "G.33";
     "G.55" -> "G.33";
     "G.56" -> "G.33";
     "G.75" -> "G.33";
     "G.76" -> "G.33";
     "G.77" -> "G.33";
     "G.78" -> "G.33";
     "G.79" -> "G.33";
     "G.80" -> "G.33";
     "G.505" -> "G.33";
     "G.506" -> "G.33";
     "G.510" -> "G.33";
     "G.545" -> "G.33";
     "G.37" -> "G.34";
     "G.75" -> "G.34";
     "G.80" -> "G.34";
     "G.37" -> "G.36";
     "G.56" -> "G.36";
     "G.62" -> "G.36";
     "G.64" -> "G.36";
     "G.79" -> "G.36";
     "G.80" -> "G.36";
     "G.39" -> "G.37";
     "G.40" -> "G.37";
     "G.56" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.38";
     "G.79" -> "G.39";
     "G.41" -> "G.40";
     "G.56" -> "G.40";
     "G.506" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.58" -> "G.48";
     "G.62" -> "G.51";
     "G.506" -> "G.51";
     "G.545" -> "G.51";
     "G.53" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.62" -> "G.52";
     "G.64" -> "G.52";
     "G.66" -> "G.52";
     "G.70" -> "G.52";
     "G.75" -> "G.52";
     "G.79" -> "G.52";
     "G.509" -> "G.52";
     "G.510" -> "G.52";
     "G.58" -> "G.53";
     "G.56" -> "G.55";
     "G.62" -> "G.56";
     "G.64" -> "G.56";
     "G.75" -> "G.56";
     "G.510" -> "G.56";
     "G.66" -> "G.58";
     "G.75" -> "G.58";
     "G.79" -> "G.58";
     "G.545" -> "G.58";
     "G.62" -> "G.61";
     "G.66" -> "G.61";
     "G.70" -> "G.61";
     "G.502" -> "G.61";
     "G.64" -> "G.62";
     "G.66" -> "G.62";
     "G.70" -> "G.62";
     "G.75" -> "G.62";
     "G.64" -> "G.63";
     "G.75" -> "G.63";
     "G.79" -> "G.63";
     "G.80" -> "G.63";
     "G.545" -> "G.63";
     "G.66" -> "G.64";
     "G.70" -> "G.66";
     "G.79" -> "G.70";
     "G.79" -> "G.75";
     "G.80" -> "G.75";
     "G.78" -> "G.76";
     "G.78" -> "G.77";
     "G.79" -> "G.78";
     "G.80" -> "G.79";
     "G.545" -> "G.79";
     "G.545" -> "G.80";
     "G.253" -> "G.169";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.502" -> "G.253";
     "G.503" -> "G.253";
     "G.503" -> "G.502";
     "G.510" -> "G.503";
     "G.509" -> "G.504";
     "G.506" -> "G.505";
     "G.510" -> "G.505";
     "G.510" -> "G.506";
     "G.510" -> "G.509";
     "G.545" -> "G.510";
   }

Required for
------------

:ref:`G.546 <G.546>`

.. toctree::
   :hidden:

   code
   heath
