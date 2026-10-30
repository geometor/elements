:order: 482
:number: 482
:canonical_id: G.482
:original_id: XI.35
:volume: III
:book: XI
:type: prop
:subtype: theorem
:categories: theorem, proof, solid-geometry
:category: theorem, proof, solid-geometry
:tags: book-xi, point, segment, angle, triangle, perpendicular, plane, equality, porism
:dependencies: G.11, G.15, G.37, G.60, G.61, G.451
:excerpt: If there be two equal plane angles, and on their vertices there be set up elevated straight lines containing equal angles with the original straight lines respectively, if on the elevated straight lines points be taken at random and perpendiculars be drawn from them to the planes in which the original angles are, and if from the points so arising in the planes straight lines be joined to the vertices of the original angles, they will contain, with the elevated straight lines, equal angles.

.. _G.482:
.. _XI.35:

G.482
=====

.. rubric:: `XI.35 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/35/>`_

.. enunciation::

   If there be two equal plane angles, and on their vertices there be set up elevated straight lines containing equal angles with the original straight lines respectively, if on the elevated straight lines points be taken at random and perpendiculars be drawn from them to the planes in which the original angles are, and if from the points so arising in the planes straight lines be joined to the vertices of the original angles, they will contain, with the elevated straight lines, equal angles.

.. signature:: theorem

   | :fn:`there_equal_plane <G.482>`\ ()
   | **prove** :g:`< G A L ) <g1:< G A L )>` is :eq:`equal <g1:< G A L ) = g1:< M D N )>` to :g:`< M D N ) <g1:< M D N )>`

.. picture:: g1.svg
   :alt: Book XI, Proposition 35

.. step:: construct

   :fn:`segment <G.3>`\ () → :g:`< B A C ) <g1:< B A C )>`, :fn:`segment <G.3>`\ () → :g:`< E D F ) <g1:< E D F )>`, :fn:`segment <G.3>`\ () → :g:`A <g1:A>`, :fn:`segment <G.3>`\ () → :g:`D <g1:D>`, :fn:`segment <G.3>`\ (:g:`A <g1:A>`, :g:`G <g1:G>`) → :g:`/ A G / <g1:/ A G />`, :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`M <g1:M>`) → :g:`/ D M / <g1:/ D M />`, :fn:`segment <G.3>`\ () → :g:`< M D E ) <g1:< M D E )>`, :fn:`segment <G.3>`\ () → :g:`< G A B ) <g1:< G A B )>`, :fn:`segment <G.3>`\ () → :g:`< M D F ) <g1:< M D F )>`, :fn:`segment <G.3>`\ () → :g:`< G A C ) <g1:< G A C )>`, :fn:`segment <G.3>`\ () → :g:`G <g1:G>`, :fn:`segment <G.3>`\ () → :g:`M <g1:M>`, :fn:`segment <G.3>`\ (:g:`A <g1:A>`, :g:`G <g1:G>`) → :g:`/ A G / <g1:/ A G />`, :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`M <g1:M>`) → :g:`/ D M / <g1:/ D M />`, :fn:`segment <G.3>`\ (:g:`G <g1:G>`, :g:`L <g1:L>`) → :g:`/ G L / <g1:/ G L />`, :fn:`segment <G.3>`\ (:g:`M <g1:M>`, :g:`N <g1:N>`) → :g:`/ M N / <g1:/ M N />`, :fn:`segment <G.3>`\ () → :g:`G <g1:G>`, :fn:`segment <G.3>`\ () → :g:`M <g1:M>`, :fn:`segment <G.3>`\ (:g:`B <g1:B>`, :g:`A <g1:A>`) → :g:`/ B A / <g1:/ B A />`, :fn:`segment <G.3>`\ (:g:`A <g1:A>`, :g:`C <g1:C>`) → :g:`/ A C / <g1:/ A C />`, :fn:`segment <G.3>`\ (:g:`E <g1:E>`, :g:`D <g1:D>`) → :g:`/ E D / <g1:/ E D />`, :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`F <g1:F>`) → :g:`/ D F / <g1:/ D F />`, :fn:`segment <G.3>`\ () → :g:`L <g1:L>`, :fn:`segment <G.3>`\ () → :g:`N <g1:N>`, :fn:`segment <G.3>`\ (:g:`L <g1:L>`, :g:`A <g1:A>`) → :g:`/ L A / <g1:/ L A />`, :fn:`segment <G.3>`\ (:g:`N <g1:N>`, :g:`D <g1:D>`) → :g:`/ N D / <g1:/ N D />`

.. step:: construct

   :fn:`cut_equal_segment <G.9>`\ (:g:`/ D M / <g1:/ D M />`) → :g:`/ A H / <g1:/ A H />` (:eq:`equal <g1:/ A H / = g1:/ D M />`)

.. step:: construct

   :fn:`parallel_line <G.44>`\ (:g:`H <g1:H>`, :g:`/ G L / <g1:/ G L />`) → :g:`/ H K / <g1:/ H K />`

.. step:: assert

   :g:`/ G L / <g1:/ G L />` is perpendicular to the plane through :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />`;

.. step:: assert ∵ straight_lines_parallel_xi_8 <G.451>

   Therefore :g:`/ H K / <g1:/ H K />` is also perpendicular to the plane through :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />`.

.. step:: construct

   From :g:`K <g1:K>`, :g:`N <g1:N>` let :g:`/ K C / <g1:/ K C />`, :g:`/ N F / <g1:/ N F />`, :g:`/ K B / <g1:/ K B />`, :g:`/ N E / <g1:/ N E />` be drawn :eq:`perpendicular <g1:/ K C / = g1:/ A C /; g1:/ N F / = g1:/ D F /; g1:/ K B / = g1:/ A B /; g1:/ N E / = g1:/ D E />` to :g:`/ A C / <g1:/ A C />`, :g:`/ D F / <g1:/ D F />`, :g:`/ A B / <g1:/ A B />`, :g:`/ D E / <g1:/ D E />`, and let :g:`/ H C / <g1:/ H C />`, :g:`/ C B / <g1:/ C B />`, :g:`/ M F / <g1:/ M F />`, :g:`/ F E / <g1:/ F E />` be joined.

.. step:: assert ∵ pythagorean_theorem <G.60>

   Since the square on :g:`/ H A / <g1:/ H A />` is equal to the squares on :g:`/ H K / <g1:/ H K />`, :g:`/ K A / <g1:/ K A />`, and the squares on :g:`/ K C / <g1:/ K C />`, :g:`/ C A / <g1:/ C A />` are equal to the square on :g:`/ K A / <g1:/ K A />`.

.. step:: assert

   Therefore the square on :g:`/ H A / <g1:/ H A />` is also equal to the squares on :g:`/ H K / <g1:/ H K />`, :g:`/ K C / <g1:/ K C />`, :g:`/ C A / <g1:/ C A />`.

.. step:: assert ∵ pythagorean_theorem <G.60>

   The square on :g:`/ H C / <g1:/ H C />` is equal to the squares on :g:`/ H K / <g1:/ H K />`, :g:`/ K C / <g1:/ K C />`.

.. step:: assert

   Therefore the square on :g:`/ H A / <g1:/ H A />` is equal to the squares on :g:`/ H C / <g1:/ H C />`, :g:`/ C A / <g1:/ C A />`.

.. step:: assert ∵ converse_pythagorean <G.61>

   Therefore :g:`< H C A ) <g1:< H C A )>` is :eq:`right <g1:< H C A )>`.

.. step:: assert

   For the same reason :g:`< D F M ) <g1:< D F M )>` is also :eq:`right <g1:< D F M )>`.

.. step:: assert

   Therefore :g:`< A C H ) <g1:< A C H )>` is :eq:`equal <g1:< A C H ) = g1:< D F M )>` to :g:`< D F M ) <g1:< D F M )>`.

.. step:: assert

   :g:`< H A C ) <g1:< H A C )>` is also :eq:`equal <g1:< H A C ) = g1:< M D F )>` to :g:`< M D F ) <g1:< M D F )>`.

.. step:: assert ∵ asa_aas_congruence <G.37>

   Therefore :g:`< M D F > <g1:< M D F >>`, :g:`< H A C > <g1:< H A C >>` are two triangles which have two angles equal to two angles respectively, and one side equal to one side, namely, that subtending one of the equal angles, that is, :g:`/ H A / <g1:/ H A />` :eq:`equal <g1:/ H A / = g1:/ M D />` to :g:`/ M D / <g1:/ M D />`; therefore they will also have the remaining sides equal to the remaining sides respectively.

.. step:: assert

   Therefore :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g1:/ D F />` to :g:`/ D F / <g1:/ D F />`.

.. step:: assert

   Similarly we can prove that :g:`/ A B / <g1:/ A B />` is also :eq:`equal <g1:/ A B / = g1:/ D E />` to :g:`/ D E / <g1:/ D E />`.

.. step:: assert

   Since then :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g1:/ D F /; g1:/ A B / = g1:/ D E />` to :g:`/ D F / <g1:/ D F />`, and :g:`/ A B / <g1:/ A B />` to :g:`/ D E / <g1:/ D E />`, the two sides :g:`/ C A / <g1:/ C A />`, :g:`/ A B / <g1:/ A B />` are :eq:`equal <g1:/ C A / = g1:/ F D /; g1:/ A B / = g1:/ D E />` to the two sides :g:`/ F D / <g1:/ F D />`, :g:`/ D E / <g1:/ D E />`.

.. step:: assert

   :g:`< C A B ) <g1:< C A B )>` is also :eq:`equal <g1:< C A B ) = g1:< F D E )>` to :g:`< F D E ) <g1:< F D E )>`;

.. step:: assert ∵ sas_congruence <G.11>

   Therefore the base :g:`/ B C / <g1:/ B C />` is :eq:`equal <g1:/ B C / = g1:/ E F />` to the base :g:`/ E F / <g1:/ E F />`, the triangle to the triangle, and the remaining angles to the remaining angles; therefore :g:`< A C B ) <g1:< A C B )>` is :eq:`equal <g1:< A C B ) = g1:< D F E )>` to :g:`< D F E ) <g1:< D F E )>`.

.. step:: assert

   The right angle :g:`< A C K ) <g1:< A C K )>` is also :eq:`equal <g1:< A C K ) = g1:< D F N )>` to the right angle :g:`< D F N ) <g1:< D F N )>`;

.. step:: assert

   Therefore the remaining angle :g:`< B C K ) <g1:< B C K )>` is also :eq:`equal <g1:< B C K ) = g1:< E F N )>` to the remaining angle :g:`< E F N ) <g1:< E F N )>`.

.. step:: assert

   For the same reason :g:`< C B K ) <g1:< C B K )>` is also :eq:`equal <g1:< C B K ) = g1:< F E N )>` to :g:`< F E N ) <g1:< F E N )>`.

.. step:: assert ∵ asa_aas_congruence <G.37>

   Therefore :g:`< B C K > <g1:< B C K >>`, :g:`< E F N > <g1:< E F N >>` are two triangles which have two angles equal to two angles respectively, and one side equal to one side, namely, that adjacent to the equal angles, that is, :g:`/ B C / <g1:/ B C />` :eq:`equal <g1:/ B C / = g1:/ E F />` to :g:`/ E F / <g1:/ E F />`; therefore they will also have the remaining sides equal to the remaining sides.

.. step:: assert

   Therefore :g:`/ C K / <g1:/ C K />` is :eq:`equal <g1:/ C K / = g1:/ F N />` to :g:`/ F N / <g1:/ F N />`.

.. step:: assert

   :g:`/ A C / <g1:/ A C />` is also :eq:`equal <g1:/ A C / = g1:/ D F />` to :g:`/ D F / <g1:/ D F />`;

.. step:: assert

   Therefore the two sides :g:`/ A C / <g1:/ A C />`, :g:`/ C K / <g1:/ C K />` are :eq:`equal <g1:/ A C / = g1:/ D F /; g1:/ C K / = g1:/ F N />` to the two sides :g:`/ D F / <g1:/ D F />`, :g:`/ F N / <g1:/ F N />`; and they contain right angles.

.. step:: assert ∵ sas_congruence <G.11>

   Therefore the base :g:`/ A K / <g1:/ A K />` is :eq:`equal <g1:/ A K / = g1:/ D N />` to the base :g:`/ D N / <g1:/ D N />`.

.. step:: assert

   And, since :g:`/ A H / <g1:/ A H />` is :eq:`equal <g1:/ A H / = g1:/ D M />` to :g:`/ D M / <g1:/ D M />`,

.. step:: assert

   The square on :g:`/ A H / <g1:/ A H />` is also :eq:`equal <g1:/ A H / = g1:/ D M />` to the square on :g:`/ D M / <g1:/ D M />`.

.. step:: assert ∵ pythagorean_theorem <G.60>

   The squares on :g:`/ A K / <g1:/ A K />`, :g:`/ K H / <g1:/ K H />` are equal to the square on :g:`/ A H / <g1:/ A H />`, for :g:`< A K H ) <g1:< A K H )>` is :eq:`right <g1:< A K H )>`; and the squares on :g:`/ D N / <g1:/ D N />`, :g:`/ N M / <g1:/ N M />` are equal to the square on :g:`/ D M / <g1:/ D M />`, for :g:`< D N M ) <g1:< D N M )>` is :eq:`right <g1:< D N M )>`.

.. step:: assert

   Therefore the squares on :g:`/ A K / <g1:/ A K />`, :g:`/ K H / <g1:/ K H />` are equal to the squares on :g:`/ D N / <g1:/ D N />`, :g:`/ N M / <g1:/ N M />`; and of these the square on :g:`/ A K / <g1:/ A K />` is :eq:`equal <g1:/ A K / = g1:/ D N />` to the square on :g:`/ D N / <g1:/ D N />`; therefore the remaining square on :g:`/ K H / <g1:/ K H />` is :eq:`equal <g1:/ K H / = g1:/ N M />` to the square on :g:`/ N M / <g1:/ N M />`; therefore :g:`/ H K / <g1:/ H K />` is :eq:`equal <g1:/ H K / = g1:/ M N />` to :g:`/ M N / <g1:/ M N />`.

.. step:: assert

   And, since the two sides :g:`/ H A / <g1:/ H A />`, :g:`/ A K / <g1:/ A K />` are :eq:`equal <g1:/ H A / = g1:/ M D /; g1:/ A K / = g1:/ D N />` to the two sides :g:`/ M D / <g1:/ M D />`, :g:`/ D N / <g1:/ D N />` respectively, and the base :g:`/ H K / <g1:/ H K />` was proved :eq:`equal <g1:/ H K / = g1:/ M N />` to the base :g:`/ M N / <g1:/ M N />`,

.. step:: assert ∵ sss_congruence <G.15>

   Therefore :g:`< H A K ) <g1:< H A K )>` is :eq:`equal <g1:< H A K ) = g1:< M D N )>` to :g:`< M D N ) <g1:< M D N )>`.

.. step:: conclude

   Therefore etc.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.1" [label="G.1", tooltip="G.1 (I.cn.1): Things equal to the same thing are equal to one another.", fillcolor="#442222", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.15): A circle is a plane figure contained by one line such that all segments falling upon it from its center are equal.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.post.1): Construct a segment between any two points.", fillcolor="#444422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.post.3): Construct a circle with any center and radius.", fillcolor="#444422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.1): Construct an equilateral triangle on a given finite segment.", fillcolor="#222244", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.cn.3): If equals are subtracted from equals, the remainders are equal.", fillcolor="#442222", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.post.2): Extend a finite segment continuously in a straight line.", fillcolor="#444422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.2): Construct at a given point a segment equal to a given segment.", fillcolor="#222244", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.3): Cut off from the greater of two unequal segments a segment equal to the less.", fillcolor="#222244", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.cn.4): Things that coincide with one another are equal.", fillcolor="#442222", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.4): Triangles with two sides and the included angle equal are congruent (SAS).", fillcolor="#222244", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.5): In an isosceles triangle, the angles at the base are equal, and if the equal sides are extended, the angles under the base are equal.", fillcolor="#222244", URL="../G.12/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.15/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.10): Bisect a given finite segment.", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10): When a straight line standing on a straight line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing line is perpendicular to that on which...", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.11): Construct a line at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): A ray standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.24" [label="G.24", tooltip="G.24 (I.14): If two rays at a point on a line on opposite sides make adjacent angles summing to two right angles, the two rays are collinear.", fillcolor="#222244", URL="../G.24/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel lines are straight lines in the same plane which, produced indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.48): If the square on one side of a triangle equals the sum of the squares on the other two sides, the angle contained by those two sides is right.", fillcolor="#222244", URL="../G.61/index.html", target="_top"];
     "G.443" [label="G.443", tooltip="G.443 (XI.1): A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.443/index.html", target="_top"];
     "G.444" [label="G.444", tooltip="G.444 (XI.2): If two straight lines cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.444/index.html", target="_top"];
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line isat right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.447" [label="G.447", tooltip="G.447 (XI.4): If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.447/index.html", target="_top"];
     "G.450" [label="G.450", tooltip="G.450 (XI.7): If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.", fillcolor="#222244", URL="../G.450/index.html", target="_top"];
     "G.451" [label="G.451", tooltip="G.451 (XI.8): If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.451/index.html", target="_top"];
     "G.482" [label="G.482", tooltip="G.482 (XI.35): If there be two equal plane angles, and on their vertices there be set up elevated straight lines containing equal angles with the original straight lines respectively, if on the e...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
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
     "G.24" -> "G.6";
     "G.25" -> "G.6";
     "G.48" -> "G.6";
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
     "G.37" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.60" -> "G.11";
     "G.447" -> "G.11";
     "G.482" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
     "G.61" -> "G.15";
     "G.447" -> "G.15";
     "G.482" -> "G.15";
     "G.17" -> "G.16";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.59" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.60" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.23";
     "G.60" -> "G.24";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.447" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.47" -> "G.37";
     "G.447" -> "G.37";
     "G.482" -> "G.37";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.451" -> "G.42";
     "G.50" -> "G.44";
     "G.59" -> "G.44";
     "G.48" -> "G.47";
     "G.50" -> "G.47";
     "G.54" -> "G.47";
     "G.59" -> "G.47";
     "G.50" -> "G.48";
     "G.54" -> "G.50";
     "G.60" -> "G.54";
     "G.60" -> "G.59";
     "G.61" -> "G.60";
     "G.482" -> "G.60";
     "G.482" -> "G.61";
     "G.444" -> "G.443";
     "G.451" -> "G.444";
     "G.450" -> "G.445";
     "G.447" -> "G.446";
     "G.451" -> "G.446";
     "G.451" -> "G.447";
     "G.451" -> "G.450";
     "G.482" -> "G.451";
   }

Required for
------------

:ref:`G.483 <G.483>`

.. toctree::
   :hidden:

   code
   heath
