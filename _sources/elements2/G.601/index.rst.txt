:order: 601
:number: 601
:canonical_id: G.601
:original_id: XIII.18
:title: G.601 set out sides
:volume: III
:book: XIII
:type: prop
:subtype: problem
:categories: problem, construction, solid-geometry, regular-solids
:category: problem, construction, solid-geometry, regular-solids
:tags: book-xiii, point, segment, circle, triangle, figure, diameter, sphere, semicircle, right-angle, convertendo, square, trilateral, diameter-of-sphere, pyramid, cube, octahedron, straight-line, icosahedron, inscribed-in-circle, centre, extreme-and-mean-ratio, dodecahedron, parts-non-aliquot, rational, ratio, proportional, invertendo, perpendicular, inscribed, pentagon, hexagon, proportion, irrational, apotome, equality
:dependencies: G.9, G.167, G.213, G.218, G.230, G.232, G.587, G.588, G.592, G.594, G.595, G.597, G.600
:excerpt: To set out the sides of the five figures and to compare them with one another.

.. _G.601:
.. _XIII.18:

G.601 set out sides
===================

.. rubric:: `XIII.18 <https://geometor.github.io/euclid/heath/volume_III/book_xiii/propositions/18/>`_

.. enunciation::

   To set out the sides of the five :term:`figures <G.9>` and to compare them with one another.

.. signature:: problem

   | :fn:`set_out_sides <G.601>`\ () → :g:`/ M B / <g1:/ M B />`, :g:`/ N B / <g1:/ N B />`
   | **construct** :g:`/ M B / <g1:/ M B />`, which is a side of the icosahedron, is by far greater than :g:`/ N B / <g1:/ N B />` which is a side of the dodecahedron

.. picture:: g1.svg
   :alt: Proposition 18 Semicircle Construction Diagram

.. step:: construct

   Let :g:`/ A B / <g1:/ A B />`, the :term:`diameter <G.61>` of the given :term:`sphere <G.575>`, be set out, and let it be cut at :g:`C <g1:C>` so that :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g1:/ C B />` to :g:`/ C B / <g1:/ C B />`, and at :g:`D <g1:D>` so that :g:`/ A D / <g1:/ A D />` is double of :g:`/ D B / <g1:/ D B />`

.. step:: construct

   Let the :term:`semicircle <G.96>` :g:`( A E B ) <g1:( A E B )>` be described on :g:`/ A B / <g1:/ A B />`

.. step:: construct

   From :g:`C <g1:C>`, :g:`D <g1:D>` let :g:`/ C E / <g1:/ C E />`, :g:`/ D F / <g1:/ D F />` be drawn :term:`at right angles <G.32>` to :g:`/ A B / <g1:/ A B />`

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`A <g1:A>`, :g:`F <g1:F>`) → :g:`/ A F / <g1:/ A F />`, :fn:`segment <G.13>`\ (:g:`F <g1:F>`, :g:`B <g1:B>`) → :g:`/ F B / <g1:/ F B />`, :fn:`segment <G.13>`\ (:g:`E <g1:E>`, :g:`B <g1:B>`) → :g:`/ E B / <g1:/ E B />`

.. step:: assert

   Since :g:`/ A D / <g1:/ A D />` is double of :g:`/ D B / <g1:/ D B />`, therefore :g:`/ A B / <g1:/ A B />` is triple of :g:`/ D B / <g1:/ D B />`.

.. step:: assert

   *:term:`Convertendo <G.200>`*, therefore, :g:`/ A B / <g1:/ A B />` is one and a half times :g:`/ A D / <g1:/ A D />`.

.. step:: assert ∵ magnitudes_proportional_said_def, right_angled_triangle <G.230, G.218>

   But, as :g:`/ A B / <g1:/ A B />` is to :g:`/ A D / <g1:/ A D />`, so is the :term:`square <G.63>` on :g:`/ A B / <g1:/ A B />` to the square on :g:`/ A F / <g1:/ A F />`, for :g:`< A F B > <g1:< A F B >>` is equiangular with :g:`< A F D > <g1:< A F D >>`.

.. step:: assert

   Therefore the square on :g:`/ A B / <g1:/ A B />` is one and a half times the square on :g:`/ A F / <g1:/ A F />`.

.. step:: assert ∵ construct_pyramid_comprehend <G.592>

   The square on the :term:`diameter of the sphere <G.576>` is also one and a half times the square on the side of the :term:`pyramid <G.553>`.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is the diameter of the sphere;

.. step:: assert

   Therefore :g:`/ A F / <g1:/ A F />` is equal to the side of the pyramid.

.. step:: assert

   Since :g:`/ A D / <g1:/ A D />` is double of :g:`/ D B / <g1:/ D B />`,

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />` is triple of :g:`/ D B / <g1:/ D B />`.

.. step:: assert ∵ right_angled_triangle, magnitudes_proportional_said_def <G.218, G.230>

   But, as :g:`/ A B / <g1:/ A B />` is to :g:`/ D B / <g1:/ D B />`, so is the square on :g:`/ A B / <g1:/ A B />` to the square on :g:`/ F B / <g1:/ F B />`.

.. step:: assert

   Therefore the square on :g:`/ A B / <g1:/ A B />` is triple of the square on :g:`/ F B / <g1:/ F B />`.

.. step:: assert ∵ construct_cube_comprehend <G.595>

   The square on the diameter of the sphere is also triple of the square on the side of the :term:`cube <G.548>`.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is the diameter of the sphere;

.. step:: assert

   Therefore :g:`/ F B / <g1:/ F B />` is the side of the cube.

.. step:: assert

   And, since :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g1:/ C B />` to :g:`/ C B / <g1:/ C B />`,

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />` is double of :g:`/ C B / <g1:/ C B />`.

.. step:: assert

   But, as :g:`/ A B / <g1:/ A B />` is to :g:`/ C B / <g1:/ C B />`, so is the square on :g:`/ A B / <g1:/ A B />` to the square on :g:`/ E B / <g1:/ E B />`;

.. step:: assert

   Therefore the square on :g:`/ A B / <g1:/ A B />` is double of the square on :g:`/ E B / <g1:/ E B />`.

.. step:: assert ∵ construct_octahedron_comprehend <G.594>

   The square on the diameter of the sphere is also double of the square on the side of the :term:`octahedron <G.593>`.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is the diameter of the given sphere;

.. step:: assert

   Therefore :g:`/ E B / <g1:/ E B />` is the side of the octahedron.

.. step:: construct

   Next, let :g:`/ A G / <g1:/ A G />` be drawn from :g:`A <g1:A>` at right angles to :g:`/ A B / <g1:/ A B />`

.. step:: construct

   :fn:`cut_equal_segment <G.21>`\ (:g:`/ A B / <g1:/ A B />`) → :g:`/ A G / <g1:/ A G />` (:eq:`equal <g1:/ A G / = g1:/ A B />`)

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`G <g1:G>`, :g:`C <g1:C>`) → :g:`/ G C / <g1:/ G C />`

.. step:: construct

   From :g:`H <g1:H>` let :g:`/ H K / <g1:/ H K />` be drawn perpendicular to :g:`/ A B / <g1:/ A B />`.

.. step:: assert

   Since :g:`/ A G / <g1:/ A G />` is double of :g:`/ A C / <g1:/ A C />`, for :g:`/ A G / <g1:/ A G />` is :eq:`equal <g1:/ A G / = g1:/ A B />` to :g:`/ A B / <g1:/ A B />`, and, as :g:`/ A G / <g1:/ A G />` is to :g:`/ A C / <g1:/ A C />`, so is :g:`/ H K / <g1:/ H K />` to :g:`/ C K / <g1:/ C K />`,

.. step:: assert

   Therefore :g:`/ H K / <g1:/ H K />` is also double of :g:`/ C K / <g1:/ C K />`.

.. step:: assert

   Therefore the square on :g:`/ H K / <g1:/ H K />` is quadruple of the square on :g:`/ C K / <g1:/ C K />`; therefore the squares on :g:`/ H K / <g1:/ H K />`, :g:`/ C K / <g1:/ C K />`, that is, the square on :g:`/ H C / <g1:/ H C />`, is five times the square on :g:`/ C K / <g1:/ C K />`.

.. step:: assert

   :g:`/ H C / <g1:/ H C />` is :eq:`equal <g1:/ H C / = g1:/ C B />` to :g:`/ C B / <g1:/ C B />`;

.. step:: assert

   Therefore the square on :g:`/ C B / <g1:/ C B />` is five times the square on :g:`/ C K / <g1:/ C K />`.

.. step:: assert

   And, since :g:`/ A B / <g1:/ A B />` is double of :g:`/ C B / <g1:/ C B />`, and, in them, :g:`/ A D / <g1:/ A D />` is double of :g:`/ D B / <g1:/ D B />`,

.. step:: assert

   Therefore the remainder :g:`/ D B / <g1:/ D B />` is double of the remainder :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   Therefore :g:`/ C B / <g1:/ C B />` is triple of :g:`/ C D / <g1:/ C D />`; therefore the square on :g:`/ C B / <g1:/ C B />` is nine times the square on :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   The square on :g:`/ C B / <g1:/ C B />` is five times the square on :g:`/ C K / <g1:/ C K />`;

.. step:: assert

   Therefore the square on :g:`/ C K / <g1:/ C K />` is greater than the square on :g:`/ C D / <g1:/ C D />`; therefore :g:`/ C K / <g1:/ C K />` is greater than :g:`/ C D / <g1:/ C D />`.

.. step:: construct

   :fn:`cut_equal_segment <G.21>`\ (:g:`/ C K / <g1:/ C K />`) → :g:`/ C L / <g1:/ C L />` (:eq:`equal <g1:/ C L / = g1:/ C K />`)

.. step:: construct

   From :g:`L <g1:L>` let :g:`/ L M / <g1:/ L M />` be drawn at right angles to :g:`/ A B / <g1:/ A B />`

.. step:: construct

   :fn:`segment <G.13>`\ (:g:`M <g1:M>`, :g:`B <g1:B>`) → :g:`/ M B / <g1:/ M B />`

.. step:: assert

   Since the square on :g:`/ C B / <g1:/ C B />` is five times the square on :g:`/ C K / <g1:/ C K />`, and :g:`/ A B / <g1:/ A B />` is double of :g:`/ C B / <g1:/ C B />`, and :g:`/ K L / <g1:/ K L />` double of :g:`/ C K / <g1:/ C K />`,

.. step:: assert

   Therefore the square on :g:`/ A B / <g1:/ A B />` is five times the square on :g:`/ K L / <g1:/ K L />`.

.. step:: assert ∵ construct_icosahedron_comprehend <G.597>

   The square on the diameter of the sphere is also five times the square on the radius of the :term:`circle <G.10>` from which the :term:`icosahedron <G.596>` has been described.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is the diameter of the sphere;

.. step:: assert ∵ inscribe_hexagon_in_circle <G.167>

   Therefore :g:`/ K L / <g1:/ K L />` is the radius of the circle from which the icosahedron has been described; therefore :g:`/ K L / <g1:/ K L />` is a side of the hexagon in the said circle.

.. step:: assert ∵ construct_icosahedron_comprehend <G.597>

   And, since the diameter of the sphere is made up of the side of the hexagon and two of the sides of the decagon inscribed in the same circle, and :g:`/ A B / <g1:/ A B />` is the diameter of the sphere, while :g:`/ K L / <g1:/ K L />` is a side of the hexagon, and :g:`/ A K / <g1:/ A K />` is :eq:`equal <g1:/ A K / = g1:/ L B />` to :g:`/ L B / <g1:/ L B />`.

.. step:: assert

   Therefore each of :g:`/ A K / <g1:/ A K />`, :g:`/ L B / <g1:/ L B />` is a side of the decagon :term:`inscribed in the circle <G.148>` from which the icosahedron has been described.

.. step:: assert

   And, since :g:`/ L B / <g1:/ L B />` belongs to a decagon, and :g:`/ L M / <g1:/ L M />` to a hexagon, for :g:`/ L M / <g1:/ L M />` is :eq:`equal <g1:/ L M / = g1:/ K L />` to :g:`/ K L / <g1:/ K L />`, since it is also :eq:`equal <g1:/ L M / = g1:/ H K />` to :g:`/ H K / <g1:/ H K />`, being the same distance from the :term:`center <G.14>`, and each of :g:`/ H K / <g1:/ H K />`, :g:`/ K L / <g1:/ K L />` is double of :g:`/ C K / <g1:/ C K />`,

.. step:: assert ∵ equilateral_pentagon_inscribed <G.588>

   Therefore :g:`/ M B / <g1:/ M B />` belongs to a pentagon.

.. step:: assert ∵ construct_icosahedron_comprehend <G.597>

   The side of the pentagon is the side of the icosahedron .

.. step:: assert

   Therefore :g:`/ M B / <g1:/ M B />` belongs to the icosahedron.

.. step:: construct

   Since :g:`/ F B / <g1:/ F B />` is a side of the cube, let it be cut in :term:`extreme and mean ratio <G.242>` at :g:`N <g1:N>`, and let :g:`/ N B / <g1:/ N B />` be the greater :term:`segment <G.4>` ;

.. step:: assert ∵ construct_dodecahedron_comprehend <G.600>

   Therefore :g:`/ N B / <g1:/ N B />` is a side of the :term:`dodecahedron <G.599>`.

.. step:: assert

   And, since the square on the diameter of the sphere was proved to be one and a half times the square on the side :g:`/ A F / <g1:/ A F />` of the pyramid, double of the square on the side :g:`/ E B / <g1:/ E B />` of the octahedron and triple of the side :g:`/ F B / <g1:/ F B />` of the cube,

.. step:: assert

   Therefore, of :term:`parts of <G.254>` which the square on the diameter of the sphere contains six, the square on the side of the pyramid contains four, the square on the side of the octahedron three, and the square on the side of the cube two.

.. step:: assert

   Therefore the square on the side of the pyramid is four-thirds of the square on the side of the octahedron, and double of the square on the side of the cube ; and the square on the side of the octahedron is one and a half times the square on the side of the cube.

.. step:: assert

   The said sides, therefore, of the three figures, I mean the pyramid, the octahedron and the cube, are to one another in :term:`rational <G.391>` :term:`ratios <G.173>`.

.. step:: assert ∵ construct_icosahedron_comprehend, construct_dodecahedron_comprehend <G.597, G.600>

   The remaining two, I mean the side of the icosahedron and the side of the dodecahedron, are not in rational ratios either to one another or to the aforesaid sides ; for they are irrational, the one being minor and the other an apotome.

.. step:: assert

   That the side :g:`/ M B / <g1:/ M B />` of the icosahedron is greater than the side :g:`/ N B / <g1:/ N B />` of the dodecahedron we can prove thus.

.. step:: assert ∵ right_angled_triangle <G.218>

   Since :g:`< F D B > <g1:< F D B >>` is equiangular with :g:`< A F B > <g1:< A F B >>`.

.. step:: assert ∵ equiangular_triangles_sides <G.213>

   Proportionally, as :g:`/ D B / <g1:/ D B />` is to :g:`/ F B / <g1:/ F B />`, so is :g:`/ F B / <g1:/ F B />` to :g:`/ A B / <g1:/ A B />`.

.. step:: assert ∵ magnitudes_proportional_said_def, similar_polygons_divided <G.230, G.232>

   And, since the three segments are :term:`proportional <G.180>`, as the first is to the third, so is the square on the first to the square on the second .

.. step:: assert

   Therefore, as :g:`/ D B / <g1:/ D B />` is to :g:`/ A B / <g1:/ A B />`, so is the square on :g:`/ D B / <g1:/ D B />` to the square on :g:`/ F B / <g1:/ F B />`;

.. step:: assert

   Therefore, :term:`inversely <G.182>`, as :g:`/ A B / <g1:/ A B />` is to :g:`/ D B / <g1:/ D B />`, so is the square on :g:`/ F B / <g1:/ F B />` to the square on :g:`/ D B / <g1:/ D B />`.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is triple of :g:`/ D B / <g1:/ D B />` ;

.. step:: assert

   Therefore the square on :g:`/ F B / <g1:/ F B />` is triple of the square on :g:`/ D B / <g1:/ D B />`.

.. step:: assert

   The square on :g:`/ A D / <g1:/ A D />` is also quadruple of the square on :g:`/ D B / <g1:/ D B />`, for :g:`/ A D / <g1:/ A D />` is double of :g:`/ D B / <g1:/ D B />` ;

.. step:: assert

   Therefore the square on :g:`/ A D / <g1:/ A D />` is greater than the square on :g:`/ F B / <g1:/ F B />` ; therefore :g:`/ A D / <g1:/ A D />` is greater than :g:`/ F B / <g1:/ F B />` ; therefore :g:`/ A L / <g1:/ A L />` is by far greater than :g:`/ F B / <g1:/ F B />`.

.. step:: assert ∵ side_hexagon_decagon <G.587>

   And, when :g:`/ A L / <g1:/ A L />` is cut in extreme and mean ratio, :g:`/ K L / <g1:/ K L />` is the greater segment, inasmuch as :g:`/ K L / <g1:/ K L />` belongs to a hexagon, and :g:`/ A K / <g1:/ A K />` to a decagon ; and, when :g:`/ F B / <g1:/ F B />` is cut in extreme and mean ratio, :g:`/ N B / <g1:/ N B />` is the greater segment .

.. step:: assert

   Therefore :g:`/ K L / <g1:/ K L />` is greater than :g:`/ N B / <g1:/ N B />`.

.. step:: assert

   :g:`/ K L / <g1:/ K L />` is :eq:`equal <g1:/ K L / = g1:/ L M />` to :g:`/ L M / <g1:/ L M />` ;

.. step:: assert

   Therefore :g:`/ L M / <g1:/ L M />` is greater than :g:`/ N B / <g1:/ N B />`.

.. step:: conclude

   Therefore :g:`/ M B / <g1:/ M B />`, which is a side of the icosahedron, is by far greater than :g:`/ N B / <g1:/ N B />` which is a side of the dodecahedron.

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
     "G.26" [label="G.26", tooltip="G.26 (I.6): If two angles of a triangle are equal, the sides subtending the equal angles are also equal.", fillcolor="#222244", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.7): On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.8): Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.def.9): A rectilineal angle is contained by two segments or lines.", fillcolor="#224422", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.9): Bisect a given angle.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.10): Bisect a given segment.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.32/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.11): Construct a segment at right angles to a given line from a given point on it.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.12): Construct a perpendicular to a given line from a given point not on it.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.35" [label="G.35", tooltip="G.35 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.35/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.13): A segment standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.36/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.14): If two segments at a point on a line on opposite sides make adjacent angles summing to two right angles, the two segments are collinear.", fillcolor="#222244", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.17): In any triangle, the sum of any two angles is less than two right angles.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.43" [label="G.43", tooltip="G.43 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.43/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.def.23): Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.52/index.html", target="_top"];
     "G.53" [label="G.53", tooltip="G.53 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.53/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.28): If a transversal cutting two lines makes the exterior angle equal to the opposite interior angle, or interior angles on the same side supplementary, the lines are parallel.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
     "G.57" [label="G.57", tooltip="G.57 (I.30): Lines parallel to the same line are parallel to one another.", fillcolor="#222244", URL="../G.57/index.html", target="_top"];
     "G.58" [label="G.58", tooltip="G.58 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.58/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.32): In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.62" [label="G.62", tooltip="G.62 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.62/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.64" [label="G.64", tooltip="G.64 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.64/index.html", target="_top"];
     "G.65" [label="G.65", tooltip="G.65 (I.36): Parallelograms on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.65/index.html", target="_top"];
     "G.66" [label="G.66", tooltip="G.66 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.66/index.html", target="_top"];
     "G.67" [label="G.67", tooltip="G.67 (I.38): Triangles on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.67/index.html", target="_top"];
     "G.68" [label="G.68", tooltip="G.68 (I.39): Equal triangles on the same base and on the same side lie in the same parallels.", fillcolor="#222244", URL="../G.68/index.html", target="_top"];
     "G.70" [label="G.70", tooltip="G.70 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.70/index.html", target="_top"];
     "G.71" [label="G.71", tooltip="G.71 (I.42): Construct, in a given angle, a parallelogram equal in area to a given triangle.", fillcolor="#222244", URL="../G.71/index.html", target="_top"];
     "G.72" [label="G.72", tooltip="G.72 (I.43): In any parallelogram, the complements of the parallelograms about the diagonal are equal in area.", fillcolor="#222244", URL="../G.72/index.html", target="_top"];
     "G.73" [label="G.73", tooltip="G.73 (I.44): Apply to a given segment, in a given angle, a parallelogram equal in area to a given triangle.", fillcolor="#222244", URL="../G.73/index.html", target="_top"];
     "G.74" [label="G.74", tooltip="G.74 (I.45): Construct, in a given angle, a parallelogram equal in area to a given polygon.", fillcolor="#222244", URL="../G.74/index.html", target="_top"];
     "G.75" [label="G.75", tooltip="G.75 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.75/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (I.def.11): An obtuse angle is greater than a right angle.", fillcolor="#224422", URL="../G.76/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.78" [label="G.78", tooltip="G.78 (I.def.21): A right-angled triangle has a right angle, an obtuse-angled triangle has an obtuse angle, and an acute-angled triangle has three acute angles.", fillcolor="#224422", URL="../G.78/index.html", target="_top"];
     "G.79" [label="G.79", tooltip="G.79 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.79/index.html", target="_top"];
     "G.81" [label="G.81", tooltip="G.81 (II.def.1): Any rectangular parallelogram is said to becontained by the twosegments containing theright angle.", fillcolor="#224422", URL="../G.81/index.html", target="_top"];
     "G.83" [label="G.83", tooltip="G.83 (II.2): If a segment be cut at random, the rectangle contained by the whole and both of the segments is equal to the square on the whole.", fillcolor="#222244", URL="../G.83/index.html", target="_top"];
     "G.86" [label="G.86", tooltip="G.86 (II.def.2): And in any parallelogrammic area let any one whatever of the parallelograms about itsdiameter with the two complements be called agnomon.", fillcolor="#224422", URL="../G.86/index.html", target="_top"];
     "G.87" [label="G.87", tooltip="G.87 (II.5): If a segment be cut into equal and unequal segments, the rectangle contained by the unequal segments of the whole together with the square on the segment between the points of sect...", fillcolor="#222244", URL="../G.87/index.html", target="_top"];
     "G.89" [label="G.89", tooltip="G.89 (II.7): If a segment be cut at random, the square on the whole and that on one of the segments both together are equal to twice the rectangle contained by the whole and the said segment an...", fillcolor="#222244", URL="../G.89/index.html", target="_top"];
     "G.96" [label="G.96", tooltip="G.96 (I.def.18): A semicircle is the figure contained by a diameter and the arc cut off by it.", fillcolor="#224422", URL="../G.96/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.1): Find the center of a given circle.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.102" [label="G.102", tooltip="G.102 (III.5): If two circles cut one another, they will not have the same center.", fillcolor="#222244", URL="../G.102/index.html", target="_top"];
     "G.108" [label="G.108", tooltip="G.108 (III.10): A circle does not cut a circle at more points than two.", fillcolor="#222244", URL="../G.108/index.html", target="_top"];
     "G.111" [label="G.111", tooltip="G.111 (III.def.2): Asegment is said totouch a circle which, meeting thecircle and being produced, does not cut the circle.", fillcolor="#224422", URL="../G.111/index.html", target="_top"];
     "G.117" [label="G.117", tooltip="G.117 (III.def.7): Anangle of a segment is that contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.117/index.html", target="_top"];
     "G.118" [label="G.118", tooltip="G.118 (III.16): The segment drawn at right angles to the diameter of a circle from its extremity will fall outside the circle, and into the space between the segment and the arc another segment ca...", fillcolor="#222244", URL="../G.118/index.html", target="_top"];
     "G.120" [label="G.120", tooltip="G.120 (III.18): If a segment touch a circle, and a segment be joined from the center to the point of contact, the segment so joined is perpendicular to the tangent.", fillcolor="#222244", URL="../G.120/index.html", target="_top"];
     "G.121" [label="G.121", tooltip="G.121 (III.19): If a segment touch a circle, and from the point of contact a segment be drawn at right angles to the tangent, the center of the circle is on the segment so drawn.", fillcolor="#222244", URL="../G.121/index.html", target="_top"];
     "G.122" [label="G.122", tooltip="G.122 (III.def.10): Asector of a circle is thefigure which, when anangle is constructed at thecenter of thecircle, is contained by thesegments containing the angle and the arc cut off by them.", fillcolor="#224422", URL="../G.122/index.html", target="_top"];
     "G.123" [label="G.123", tooltip="G.123 (III.20): In a circle the angle at the center is double of the angle at the arc, when the angles have the same arc as base.", fillcolor="#222244", URL="../G.123/index.html", target="_top"];
     "G.124" [label="G.124", tooltip="G.124 (III.21): In a circle the angles in the same segment are equal.", fillcolor="#222244", URL="../G.124/index.html", target="_top"];
     "G.125" [label="G.125", tooltip="G.125 (III.22): The opposite angles of quadrilaterals in circles are equal to two right angles.", fillcolor="#222244", URL="../G.125/index.html", target="_top"];
     "G.126" [label="G.126", tooltip="G.126 (III.def.6): Asegment of a circle is thefigure contained by asegment and a arc of acircle.", fillcolor="#224422", URL="../G.126/index.html", target="_top"];
     "G.127" [label="G.127", tooltip="G.127 (III.def.11): Similar segments of circles are those which admit equalangles, or in which the angles are equal.", fillcolor="#224422", URL="../G.127/index.html", target="_top"];
     "G.129" [label="G.129", tooltip="G.129 (III.24): Similar segments of circles on equal segments are equal.", fillcolor="#222244", URL="../G.129/index.html", target="_top"];
     "G.131" [label="G.131", tooltip="G.131 (III.def.1): Equal circles are those thediameters of which are equal, or the radii of which are equal.", fillcolor="#224422", URL="../G.131/index.html", target="_top"];
     "G.132" [label="G.132", tooltip="G.132 (III.def.9): And, when thesegments containing theangle cut off a arc, the angle is said tostand upon that arc.", fillcolor="#224422", URL="../G.132/index.html", target="_top"];
     "G.133" [label="G.133", tooltip="G.133 (III.26): In equal circles equal angles stand on equal arcs, whether they stand at the centres or at the arcs.", fillcolor="#222244", URL="../G.133/index.html", target="_top"];
     "G.134" [label="G.134", tooltip="G.134 (III.27): In equal circles angles standing on equal arcs are equal, whether they stand at the centres or at the arcs.", fillcolor="#222244", URL="../G.134/index.html", target="_top"];
     "G.135" [label="G.135", tooltip="G.135 (III.28): In equal circles equal segments cut off equal arcs, the greater equal to the greater and the less to the less.", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.136" [label="G.136", tooltip="G.136 (III.29): In equal circles equal arcs are subtended by equal segments.", fillcolor="#222244", URL="../G.136/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (III.def.8): Anangle in a segment is theangle which, when apoint is taken on the arc of the segment andsegments are joined from it to theextremities of the segment which is thebase of the segme...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.139" [label="G.139", tooltip="G.139 (III.31): In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of...", fillcolor="#222244", URL="../G.139/index.html", target="_top"];
     "G.140" [label="G.140", tooltip="G.140 (III.32): If a segment touch a circle, and from the point of contact there be drawn across, in the circle, a segment cutting the circle, the angles which it makes with the tangent will equal...", fillcolor="#222244", URL="../G.140/index.html", target="_top"];
     "G.146" [label="G.146", tooltip="G.146 (IV.def.7): Asegment is said to befitted into a circle when itsextremities are on the arc of thecircle.", fillcolor="#224422", URL="../G.146/index.html", target="_top"];
     "G.147" [label="G.147", tooltip="G.147 (IV.1): Into a given circle to fit a segment equal to a given segment which is not greater than the diameter of the circle.", fillcolor="#222244", URL="../G.147/index.html", target="_top"];
     "G.148" [label="G.148", tooltip="G.148 (IV.def.3): Apolygon is said to beinscribed in a circle when eachangle of the inscribedfigure lies on the arc of thecircle.", fillcolor="#224422", URL="../G.148/index.html", target="_top"];
     "G.149" [label="G.149", tooltip="G.149 (IV.2): Inscribe in a given circle a triangle equiangular with a given triangle.", fillcolor="#222244", URL="../G.149/index.html", target="_top"];
     "G.150" [label="G.150", tooltip="G.150 (IV.def.4): Apolygon is said to becircumscribed about a circle, when each side of the circumscribedfigure touches the arc of thecircle.", fillcolor="#224422", URL="../G.150/index.html", target="_top"];
     "G.153" [label="G.153", tooltip="G.153 (IV.def.5): Similarly acircle is said to beinscribed in a figure when the arc of the circle touches each side of thefigure in which it is inscribed.", fillcolor="#224422", URL="../G.153/index.html", target="_top"];
     "G.155" [label="G.155", tooltip="G.155 (IV.def.2): Similarly afigure is said to becircumscribed about a figure when the respective sides of the circumscribed figure pass through the respectiveangles of that about which it is circum...", fillcolor="#224422", URL="../G.155/index.html", target="_top"];
     "G.156" [label="G.156", tooltip="G.156 (IV.def.6): Acircle is said to becircumscribed about a figure when the arc of the circle passes through eachangle of thefigure about which it is circumscribed.", fillcolor="#224422", URL="../G.156/index.html", target="_top"];
     "G.166" [label="G.166", tooltip="G.166 (IV.14): About a given pentagon, which is equilateral and equiangular, to circumscribe a circle.", fillcolor="#222244", URL="../G.166/index.html", target="_top"];
     "G.167" [label="G.167", tooltip="G.167 (IV.15): Inscribe in a given circle an equilateral and equiangular hexagon.", fillcolor="#222244", URL="../G.167/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.171" [label="G.171", tooltip="G.171 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.171/index.html", target="_top"];
     "G.172" [label="G.172", tooltip="G.172 (V.2): If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the...", fillcolor="#222244", URL="../G.172/index.html", target="_top"];
     "G.173" [label="G.173", tooltip="G.173 (V.def.3): Aratio is a sort of relation in respect of size between two magnitudes of the same kind.", fillcolor="#224422", URL="../G.173/index.html", target="_top"];
     "G.174" [label="G.174", tooltip="G.174 (V.def.17): Aratioex aequali arises when, there being several magnitudes and another set equal to them in multitude which taken two and two are in the same proportion, as the first is to the l...", fillcolor="#224422", URL="../G.174/index.html", target="_top"];
     "G.175" [label="G.175", tooltip="G.175 (V.3): If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then also ex aequali the magnitudes taken i...", fillcolor="#222244", URL="../G.175/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.177" [label="G.177", tooltip="G.177 (V.4): If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples wh...", fillcolor="#222244", URL="../G.177/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.182" [label="G.182", tooltip="G.182 (V.def.13): Inverse ratio means taking theconsequent as antecedent in relation to the antecedent as consequent.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
     "G.183" [label="G.183", tooltip="G.183 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.183/index.html", target="_top"];
     "G.184" [label="G.184", tooltip="G.184 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.184/index.html", target="_top"];
     "G.185" [label="G.185", tooltip="G.185 (V.def.7): When, of theequimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then th...", fillcolor="#224422", URL="../G.185/index.html", target="_top"];
     "G.186" [label="G.186", tooltip="G.186 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.186/index.html", target="_top"];
     "G.187" [label="G.187", tooltip="G.187 (V.9): Magnitudes which have the same ratio to the same are equal; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.187/index.html", target="_top"];
     "G.188" [label="G.188", tooltip="G.188 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", fillcolor="#222244", URL="../G.188/index.html", target="_top"];
     "G.189" [label="G.189", tooltip="G.189 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.189/index.html", target="_top"];
     "G.190" [label="G.190", tooltip="G.190 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.190/index.html", target="_top"];
     "G.191" [label="G.191", tooltip="G.191 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.191/index.html", target="_top"];
     "G.192" [label="G.192", tooltip="G.192 (V.14): If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second is greater than the fourth; if equal, equal; an...", fillcolor="#222244", URL="../G.192/index.html", target="_top"];
     "G.193" [label="G.193", tooltip="G.193 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.193/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (V.def.12): Alternate ratio means taking theantecedent in relation to the antecedent and the consequent in relation to the consequent.", fillcolor="#224422", URL="../G.194/index.html", target="_top"];
     "G.195" [label="G.195", tooltip="G.195 (V.16): If four magnitudes be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.195/index.html", target="_top"];
     "G.196" [label="G.196", tooltip="G.196 (V.def.14): Composition of a ratio means taking theantecedent together with the consequent as one in relation to the consequent by itself.", fillcolor="#224422", URL="../G.196/index.html", target="_top"];
     "G.197" [label="G.197", tooltip="G.197 (V.def.15): Separation of a ratio means taking the excess by which theantecedent exceeds the consequent in relation to the consequent by itself.", fillcolor="#224422", URL="../G.197/index.html", target="_top"];
     "G.198" [label="G.198", tooltip="G.198 (V.17): If magnitudes be proportional componendo, they is proportional separando.", fillcolor="#222244", URL="../G.198/index.html", target="_top"];
     "G.199" [label="G.199", tooltip="G.199 (V.18): If magnitudes be proportional separando, they is proportional componendo.", fillcolor="#222244", URL="../G.199/index.html", target="_top"];
     "G.200" [label="G.200", tooltip="G.200 (V.def.16): Conversion of a ratio means taking theantecedent in relation to the excess by which the antecedent exceeds the consequent.", fillcolor="#224422", URL="../G.200/index.html", target="_top"];
     "G.201" [label="G.201", tooltip="G.201 (V.19): If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder is to the remainder as whole to whole.", fillcolor="#222244", URL="../G.201/index.html", target="_top"];
     "G.202" [label="G.202", tooltip="G.202 (V.20): If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and if ex aequali the first be greater than the third, the fourt...", fillcolor="#222244", URL="../G.202/index.html", target="_top"];
     "G.205" [label="G.205", tooltip="G.205 (V.22): If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.205/index.html", target="_top"];
     "G.209" [label="G.209", tooltip="G.209 (VI.def.4): The height of anyfigure is theperpendicular drawn from the vertex to the base.", fillcolor="#224422", URL="../G.209/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.210/index.html", target="_top"];
     "G.211" [label="G.211", tooltip="G.211 (VI.2): If a segment be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionally, the...", fillcolor="#222244", URL="../G.211/index.html", target="_top"];
     "G.213" [label="G.213", tooltip="G.213 (VI.4): In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.", fillcolor="#222244", URL="../G.213/index.html", target="_top"];
     "G.215" [label="G.215", tooltip="G.215 (VI.6): If two triangles have one angle equal to one angle and the sides about the equal angles proportional, the triangles is equiangular and will have those angles equal which the corres...", fillcolor="#222244", URL="../G.215/index.html", target="_top"];
     "G.217" [label="G.217", tooltip="G.217 (VI.def.1): Similar polygons are such as have theirangles severally equal and the sides about the equal anglesproportional.", fillcolor="#224422", URL="../G.217/index.html", target="_top"];
     "G.218" [label="G.218", tooltip="G.218 (VI.8): If in a right-angled triangle a perpendicular be drawn from the right angle to the base, the triangles adjoining the perpendicular are similar both to the whole and to one another.", fillcolor="#222244", URL="../G.218/index.html", target="_top"];
     "G.221" [label="G.221", tooltip="G.221 (VI.11): To two given segments to find a third proportional.", fillcolor="#222244", URL="../G.221/index.html", target="_top"];
     "G.222" [label="G.222", tooltip="G.222 (VI.12): To three given segments to find a fourth proportional.", fillcolor="#222244", URL="../G.222/index.html", target="_top"];
     "G.223" [label="G.223", tooltip="G.223 (VI.13): To two given segments to find a mean proportional.", fillcolor="#222244", URL="../G.223/index.html", target="_top"];
     "G.224" [label="G.224", tooltip="G.224 (VI.def.2): Reciprocally related figures have their sides about equal angles reciprocally proportional.", fillcolor="#224422", URL="../G.224/index.html", target="_top"];
     "G.225" [label="G.225", tooltip="G.225 (VI.14): In equal and equiangular parallelograms the sides about the equal angles are reciprocally proportional; and equiangular parallelograms in which the sides about the equal angles are...", fillcolor="#222244", URL="../G.225/index.html", target="_top"];
     "G.226" [label="G.226", tooltip="G.226 (VI.15): In equal triangles which have one angle equal to one angle the sides about the equal angles are reciprocally proportional; and those triangles which have one angle equal to one ang...", fillcolor="#222244", URL="../G.226/index.html", target="_top"];
     "G.227" [label="G.227", tooltip="G.227 (VI.16): If four segments be proportional, the rectangle contained by the extremes is equal to the rectangle contained by the means; and, if the rectangle contained by the extremes equals t...", fillcolor="#222244", URL="../G.227/index.html", target="_top"];
     "G.228" [label="G.228", tooltip="G.228 (VI.17): If three segments be proportional, the rectangle contained by the extremes is equal to the square on the mean; and, if the rectangle contained by the extremes equals the square on ...", fillcolor="#222244", URL="../G.228/index.html", target="_top"];
     "G.229" [label="G.229", tooltip="G.229 (VI.18): Describe on a given segment a rectilinear figure similar and similarly situated to a given rectilinear figure.", fillcolor="#222244", URL="../G.229/index.html", target="_top"];
     "G.230" [label="G.230", tooltip="G.230 (V.def.9): When three magnitudes areproportional, the first is said to have to the third theduplicate ratio of that which it has to the second.", fillcolor="#224422", URL="../G.230/index.html", target="_top"];
     "G.231" [label="G.231", tooltip="G.231 (VI.19): Similar triangles are to one another in the duplicate ratio of the corresponding sides.", fillcolor="#222244", URL="../G.231/index.html", target="_top"];
     "G.232" [label="G.232", tooltip="G.232 (VI.20): Similar polygons are divided into similar triangles, and into triangles equal in multitude and in the same ratio as the wholes, and the polygon has to the polygon a ratio duplicate...", fillcolor="#222244", URL="../G.232/index.html", target="_top"];
     "G.233" [label="G.233", tooltip="G.233 (VI.21): Figures which are similar to the same polygon are also similar to one another.", fillcolor="#222244", URL="../G.233/index.html", target="_top"];
     "G.234" [label="G.234", tooltip="G.234 (VI.22): If four segments be proportional, the polygons similar and similarly described upon them is proportional; and, if the polygons similar and similarly described upon them be proporti...", fillcolor="#222244", URL="../G.234/index.html", target="_top"];
     "G.236" [label="G.236", tooltip="G.236 (VI.24): In any parallelogram the parallelograms about the diameter are similar both to the whole and to one another.", fillcolor="#222244", URL="../G.236/index.html", target="_top"];
     "G.237" [label="G.237", tooltip="G.237 (VI.25): Construct one and the same figure similar to a given polygon and equal to another given polygon.", fillcolor="#222244", URL="../G.237/index.html", target="_top"];
     "G.238" [label="G.238", tooltip="G.238 (VI.26): If from a parallelogram there be taken away a parallelogram similar and similarly situated to the whole and having a common angle with it, it is about the same diameter with the wh...", fillcolor="#222244", URL="../G.238/index.html", target="_top"];
     "G.240" [label="G.240", tooltip="G.240 (VI.28): To a given segment to apply a parallelogram equal to a given polygon and deficient by a parallelogrammic figure similar to a given one: thus the given polygon must not be greater t...", fillcolor="#222244", URL="../G.240/index.html", target="_top"];
     "G.242" [label="G.242", tooltip="G.242 (VI.def.3): A segment is said to have been cut in extreme and mean ratio when, as the wholeline is to the greater segment, so is the greater to the less.", fillcolor="#224422", URL="../G.242/index.html", target="_top"];
     "G.245" [label="G.245", tooltip="G.245 (VI.32): If two triangles having two sides proportional to two sides be placed together at one angle so that their corresponding sides are also parallel, the remaining sides of the triangle...", fillcolor="#222244", URL="../G.245/index.html", target="_top"];
     "G.246" [label="G.246", tooltip="G.246 (VI.33): In equal circles angles have the same ratio as the arcs on which they stand, whether they stand at the centres or at the arcs.", fillcolor="#222244", URL="../G.246/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.249" [label="G.249", tooltip="G.249 (VII.def.12): Numbers prime to one another are those which aremeasured by anunit alone as a common measure.", fillcolor="#224422", URL="../G.249/index.html", target="_top"];
     "G.250" [label="G.250", tooltip="G.250 (VII.1): Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is...", fillcolor="#222244", URL="../G.250/index.html", target="_top"];
     "G.251" [label="G.251", tooltip="G.251 (VII.2): Given two numbers not prime to one another, to find their greatest common measure.", fillcolor="#222244", URL="../G.251/index.html", target="_top"];
     "G.252" [label="G.252", tooltip="G.252 (VII.3): Given three numbers not prime to one another, to find their greatest common measure.", fillcolor="#222244", URL="../G.252/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.254" [label="G.254", tooltip="G.254 (VII.def.4): Butparts when it does notmeasure it.", fillcolor="#224422", URL="../G.254/index.html", target="_top"];
     "G.255" [label="G.255", tooltip="G.255 (VII.4): Any number is either a part or parts of any number, the less of the greater.", fillcolor="#222244", URL="../G.255/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.257" [label="G.257", tooltip="G.257 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.257/index.html", target="_top"];
     "G.258" [label="G.258", tooltip="G.258 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.258/index.html", target="_top"];
     "G.261" [label="G.261", tooltip="G.261 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.261/index.html", target="_top"];
     "G.262" [label="G.262", tooltip="G.262 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.262/index.html", target="_top"];
     "G.263" [label="G.263", tooltip="G.263 (VII.def.20): Numbers areproportional when the first is thesame multiple, or thesame part, or thesame parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.263/index.html", target="_top"];
     "G.265" [label="G.265", tooltip="G.265 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.265/index.html", target="_top"];
     "G.266" [label="G.266", tooltip="G.266 (VII.13): If four numbers be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.266/index.html", target="_top"];
     "G.267" [label="G.267", tooltip="G.267 (VII.14): If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.267/index.html", target="_top"];
     "G.268" [label="G.268", tooltip="G.268 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.268/index.html", target="_top"];
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.270" [label="G.270", tooltip="G.270 (VII.16): If two numbers by multiplying one another make certain numbers, the numbers so produced are equal.", fillcolor="#222244", URL="../G.270/index.html", target="_top"];
     "G.271" [label="G.271", tooltip="G.271 (VII.17): If a number by multiplying two numbers make certain numbers, the numbers so produced will have the same ratio as the numbers multiplied.", fillcolor="#222244", URL="../G.271/index.html", target="_top"];
     "G.272" [label="G.272", tooltip="G.272 (VII.18): If two numbers by multiplying any number make certain numbers, the numbers so produced will have the same ratio as the multipliers.", fillcolor="#222244", URL="../G.272/index.html", target="_top"];
     "G.273" [label="G.273", tooltip="G.273 (VII.19): If four numbers be proportional, the number produced from the first and fourth will equals the number produced from the second and third; and, if the number produced from the first...", fillcolor="#222244", URL="../G.273/index.html", target="_top"];
     "G.274" [label="G.274", tooltip="G.274 (VII.20): The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", fillcolor="#222244", URL="../G.274/index.html", target="_top"];
     "G.275" [label="G.275", tooltip="G.275 (VII.21): Numbers prime to one another are the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.275/index.html", target="_top"];
     "G.276" [label="G.276", tooltip="G.276 (VII.22): The least numbers of those which have the same ratio with them are prime to one another.", fillcolor="#222244", URL="../G.276/index.html", target="_top"];
     "G.277" [label="G.277", tooltip="G.277 (VII.23): If two numbers be prime to one another, the number which measures the one of them is prime to the remaining number.", fillcolor="#222244", URL="../G.277/index.html", target="_top"];
     "G.278" [label="G.278", tooltip="G.278 (VII.24): If two numbers be prime to any number, their product also is prime to the same.", fillcolor="#222244", URL="../G.278/index.html", target="_top"];
     "G.279" [label="G.279", tooltip="G.279 (VII.25): If two numbers be prime to one another, the product of one of them into itself is prime to the remaining one.", fillcolor="#222244", URL="../G.279/index.html", target="_top"];
     "G.280" [label="G.280", tooltip="G.280 (VII.26): If two numbers be prime to two numbers, both to each, their products also is prime to one another.", fillcolor="#222244", URL="../G.280/index.html", target="_top"];
     "G.281" [label="G.281", tooltip="G.281 (VII.27): If two numbers be prime to one another, and each by multiplying itself make a certain number, the products is prime to one another; and, if the original numbers by multiplying the ...", fillcolor="#222244", URL="../G.281/index.html", target="_top"];
     "G.283" [label="G.283", tooltip="G.283 (VII.def.11): Aprime number is that which ismeasured by anunit alone.", fillcolor="#224422", URL="../G.283/index.html", target="_top"];
     "G.289" [label="G.289", tooltip="G.289 (VII.33): Given as many numbers as we please, to find the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.289/index.html", target="_top"];
     "G.290" [label="G.290", tooltip="G.290 (VII.34): Given two numbers, to find the least number which they measure.", fillcolor="#222244", URL="../G.290/index.html", target="_top"];
     "G.291" [label="G.291", tooltip="G.291 (VII.35): If two numbers measure any number, the least number measured by them will also measure the same.", fillcolor="#222244", URL="../G.291/index.html", target="_top"];
     "G.296" [label="G.296", tooltip="G.296 (VIII.1): If there be as many numbers as we please in continued proportion, and the extremes of them be prime to one another, the numbers are the least of those which have the same ratio wit...", fillcolor="#222244", URL="../G.296/index.html", target="_top"];
     "G.297" [label="G.297", tooltip="G.297 (VIII.2): Find numbers in continued proportion, as many as may be prescribed, and the least that are in a given ratio.", fillcolor="#222244", URL="../G.297/index.html", target="_top"];
     "G.299" [label="G.299", tooltip="G.299 (VIII.4): Given as many ratios as we please in least numbers, to find numbers in continued proportion which are the least in the given ratios.", fillcolor="#222244", URL="../G.299/index.html", target="_top"];
     "G.300" [label="G.300", tooltip="G.300 (VII.def.16): And, when twonumbers havingmultiplied one another make some number, the number so produced is calledplane, and itssides are the numbers which have multiplied one another.", fillcolor="#224422", URL="../G.300/index.html", target="_top"];
     "G.308" [label="G.308", tooltip="G.308 (VII.def.18): Asquare number is equalmultiplied by equal, or anumber which is contained by two equal numbers.", fillcolor="#224422", URL="../G.308/index.html", target="_top"];
     "G.309" [label="G.309", tooltip="G.309 (VIII.11): Between two square numbers there is one mean proportional number, and the square has to the square the ratio duplicate of that which the side has to the side.", fillcolor="#222244", URL="../G.309/index.html", target="_top"];
     "G.318" [label="G.318", tooltip="G.318 (VII.def.21): Similar plane and solid numbers are those which have their sidesproportional.", fillcolor="#224422", URL="../G.318/index.html", target="_top"];
     "G.319" [label="G.319", tooltip="G.319 (VIII.18): Between two similar plane numbers there is one mean proportional number; and the plane number has to the plane number the ratio duplicate of that which the corresponding side has t...", fillcolor="#222244", URL="../G.319/index.html", target="_top"];
     "G.328" [label="G.328", tooltip="G.328 (VIII.26): Similar plane numbers have to one another the ratio which a square number has to a square number.", fillcolor="#222244", URL="../G.328/index.html", target="_top"];
     "G.372" [label="G.372", tooltip="G.372 (X.def.1): Those magnitudes are said to becommensurable which aremeasured by the same measure, and thoseincommensurable which cannot have any common measure.", fillcolor="#224422", URL="../G.372/index.html", target="_top"];
     "G.376" [label="G.376", tooltip="G.376 (X.5): Commensurable magnitudes have to one another the ratio which a number has to a number.", fillcolor="#222244", URL="../G.376/index.html", target="_top"];
     "G.377" [label="G.377", tooltip="G.377 (X.6): If two magnitudes have to one another the ratio which a number has to a number, the magnitudes is commensurable.", fillcolor="#222244", URL="../G.377/index.html", target="_top"];
     "G.378" [label="G.378", tooltip="G.378 (X.7): Incommensurable magnitudes have not to one another the ratio which a number has to a number.", fillcolor="#222244", URL="../G.378/index.html", target="_top"];
     "G.379" [label="G.379", tooltip="G.379 (X.8): If two magnitudes have not to one another the ratio which a number has to a number, the magnitudes is incommensurable.", fillcolor="#222244", URL="../G.379/index.html", target="_top"];
     "G.380" [label="G.380", tooltip="G.380 (X.def.2): Straight lines arecommensurable in square when thesquares on them aremeasured by the same area, andincommensurable in square when the squares on them cannot possibly have any area ...", fillcolor="#224422", URL="../G.380/index.html", target="_top"];
     "G.381" [label="G.381", tooltip="G.381 (X.9): The squares on segments commensurable in length have to one another the ratio which a square number has to a square number; and squares which have to one another the ratio which a ...", fillcolor="#222244", URL="../G.381/index.html", target="_top"];
     "G.382" [label="G.382", tooltip="G.382 (X.11): If four magnitudes be proportional, and the first be commensurable with the second, the third is commensurable with the fourth; and, if the first be incommensurable with the second...", fillcolor="#222244", URL="../G.382/index.html", target="_top"];
     "G.384" [label="G.384", tooltip="G.384 (X.12): Magnitudes commensurable with the same magnitude are commensurable with one another also.", fillcolor="#222244", URL="../G.384/index.html", target="_top"];
     "G.385" [label="G.385", tooltip="G.385 (X.13): If two magnitudes be commensurable, and the one of them be incommensurable with any magnitude, the remaining one is incommensurable with the same.", fillcolor="#222244", URL="../G.385/index.html", target="_top"];
     "G.387" [label="G.387", tooltip="G.387 (X.15): If two commensurable magnitudes be added together, the whole is commensurable with each of them; and, if the whole be commensurable with one of them, the original magnitudes is com...", fillcolor="#222244", URL="../G.387/index.html", target="_top"];
     "G.388" [label="G.388", tooltip="G.388 (X.16): If two incommensurable magnitudes be added together, the whole is incommensurable with each of them; and, if the whole be incommensurable with one of them, the original magnitudes ...", fillcolor="#222244", URL="../G.388/index.html", target="_top"];
     "G.389" [label="G.389", tooltip="G.389 (X.17): If there be two unequal segments, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, and if it...", fillcolor="#222244", URL="../G.389/index.html", target="_top"];
     "G.390" [label="G.390", tooltip="G.390 (X.18): If there be two unequal segments, and to the greater there be applied a parallelogram equal to the fourth part of the square on the less and deficient by a square figure, and if it...", fillcolor="#222244", URL="../G.390/index.html", target="_top"];
     "G.391" [label="G.391", tooltip="G.391 (X.def.3): With these hypotheses, it is proved that there existsegments infinite in multitude which arecommensurable and incommensurable respectively, some in length only, and others in squar...", fillcolor="#224422", URL="../G.391/index.html", target="_top"];
     "G.392" [label="G.392", tooltip="G.392 (X.def.4): And let thesquare on the assignedsegment be calledrational and those areas which arecommensurable with itrational, but those which are incommensurable with itirrational, and the se...", fillcolor="#224422", URL="../G.392/index.html", target="_top"];
     "G.393" [label="G.393", tooltip="G.393 (X.19): The rectangle contained by rational segments commensurable in length is rational.", fillcolor="#222244", URL="../G.393/index.html", target="_top"];
     "G.394" [label="G.394", tooltip="G.394 (X.20): If a rational area be applied to a rational segment, it produces as breadth a segment rational and commensurable in length with the segment to which it is applied.", fillcolor="#222244", URL="../G.394/index.html", target="_top"];
     "G.395" [label="G.395", tooltip="G.395 (X.21): The rectangle contained by rational segments commensurable in square only is irrational, and the side of the square equal to it is irrational. Let the latter be called medial.", fillcolor="#222244", URL="../G.395/index.html", target="_top"];
     "G.396" [label="G.396", tooltip="G.396 (X.22): The square on a medial segment, if applied to a rational segment, produces as breadth a segment rational and incommensurable in length with that to which it is applied.", fillcolor="#222244", URL="../G.396/index.html", target="_top"];
     "G.397" [label="G.397", tooltip="G.397 (X.23): A segment commensurable with a medial segment is medial.", fillcolor="#222244", URL="../G.397/index.html", target="_top"];
     "G.404" [label="G.404", tooltip="G.404 (X.30): Find two rational segments commensurable in square only and such that the square on the greater is greater than the square on the less by the square on a segment incommensurable in...", fillcolor="#222244", URL="../G.404/index.html", target="_top"];
     "G.407" [label="G.407", tooltip="G.407 (X.33): Find two segments incommensurable in square which make the sum of the squares on them rational but the rectangle contained by them medial.", fillcolor="#222244", URL="../G.407/index.html", target="_top"];
     "G.453" [label="G.453", tooltip="G.453 (X.73): If from a rational segment there be subtracted a rational segment commensurable with the whole in square only, the remainder is irrational; and let it be called an apotome.", fillcolor="#222244", URL="../G.453/index.html", target="_top"];
     "G.454" [label="G.454", tooltip="G.454 (X.def.iii.1): Given arationalsegment and an apotome, if thesquare on the whole be greater than the square on the annex by the square on a segmentcommensurable in length with the whole, and the w...", fillcolor="#224422", URL="../G.454/index.html", target="_top"];
     "G.458" [label="G.458", tooltip="G.458 (X.76): If from a segment there be subtracted a segment which is incommensurable in square with the whole and which with the whole makes the squares on them added together rational, but th...", fillcolor="#222244", URL="../G.458/index.html", target="_top"];
     "G.471" [label="G.471", tooltip="G.471 (X.def.iii.4): Again, if thesquare on the whole be greater than the square on the annex by the square on asegment incommensurable with the whole, then, if the whole becommensurable in length with...", fillcolor="#224422", URL="../G.471/index.html", target="_top"];
     "G.480" [label="G.480", tooltip="G.480 (X.94): If an area be contained by a rational segment and a fourth apotome, the “side” of the area is minor.", fillcolor="#222244", URL="../G.480/index.html", target="_top"];
     "G.483" [label="G.483", tooltip="G.483 (X.97): The square on an apotome applied to a rational segment produces as breadth a first apotome.", fillcolor="#222244", URL="../G.483/index.html", target="_top"];
     "G.502" [label="G.502", tooltip="G.502 (XI.1): A part of a segment cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.502/index.html", target="_top"];
     "G.503" [label="G.503", tooltip="G.503 (XI.2): If two segments cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.503/index.html", target="_top"];
     "G.504" [label="G.504", tooltip="G.504 (XI.3): If two planes cut one another, their common section is a segment.", fillcolor="#222244", URL="../G.504/index.html", target="_top"];
     "G.505" [label="G.505", tooltip="G.505 (XI.def.3): Asegment isat right angles to a plane, when it makesright angles with all the segments which meet it and are in theplane.", fillcolor="#224422", URL="../G.505/index.html", target="_top"];
     "G.506" [label="G.506", tooltip="G.506 (XI.4): If a segment be set up at right angles to two segments which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.506/index.html", target="_top"];
     "G.507" [label="G.507", tooltip="G.507 (XI.5): If a segment be set up at right angles to three segments which meet one another, at their common point of section, the three segments are in one plane.", fillcolor="#222244", URL="../G.507/index.html", target="_top"];
     "G.508" [label="G.508", tooltip="G.508 (XI.6): If two segments be at right angles to the same plane, the segments is parallel.", fillcolor="#222244", URL="../G.508/index.html", target="_top"];
     "G.509" [label="G.509", tooltip="G.509 (XI.7): If two segments be parallel and points be taken at random on each of them, the segment joining the points is in the same plane with the parallel lines.", fillcolor="#222244", URL="../G.509/index.html", target="_top"];
     "G.510" [label="G.510", tooltip="G.510 (XI.8): If two segments be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.510/index.html", target="_top"];
     "G.511" [label="G.511", tooltip="G.511 (XI.9): Straight lines which are parallel to the same segment and are not in the same plane with it are also parallel to one another.", fillcolor="#222244", URL="../G.511/index.html", target="_top"];
     "G.513" [label="G.513", tooltip="G.513 (XI.11): From a given elevated point to draw a segment perpendicular to a given plane.", fillcolor="#222244", URL="../G.513/index.html", target="_top"];
     "G.514" [label="G.514", tooltip="G.514 (XI.12): To set up a segment at right angles to a given plane from a given point in it.", fillcolor="#222244", URL="../G.514/index.html", target="_top"];
     "G.529" [label="G.529", tooltip="G.529 (XI.def.1): Asolid is that which has length, breadth, and depth.", fillcolor="#224422", URL="../G.529/index.html", target="_top"];
     "G.548" [label="G.548", tooltip="G.548 (XI.def.25): Acube is asolid figure contained by six equalsquares.", fillcolor="#224422", URL="../G.548/index.html", target="_top"];
     "G.549" [label="G.549", tooltip="G.549 (XI.38): If the sides of the opposite planes of a cube be bisected, and planes be carried through the points of section, the common section of the planes and the diameter of the cube bisect...", fillcolor="#222244", URL="../G.549/index.html", target="_top"];
     "G.553" [label="G.553", tooltip="G.553 (XI.def.12): Apyramid is asolid figure, contained byplanes, which is constructed from one plane to onepoint.", fillcolor="#224422", URL="../G.553/index.html", target="_top"];
     "G.575" [label="G.575", tooltip="G.575 (XI.def.14): When, thediameter of asemicircle remaining fixed, the semicircle is carried round and restored again to the same position from which it began to be moved, thefigure so comprehended...", fillcolor="#224422", URL="../G.575/index.html", target="_top"];
     "G.576" [label="G.576", tooltip="G.576 (XI.def.17): Adiameter of the sphere is anysegment drawn through thecenter and terminated in both directions by thesurface of thesphere.", fillcolor="#224422", URL="../G.576/index.html", target="_top"];
     "G.579" [label="G.579", tooltip="G.579 (XIII.1): If a segment be cut in extreme and mean ratio, the square on the greater segment added to the half of the whole is five times the square on the half.", fillcolor="#222244", URL="../G.579/index.html", target="_top"];
     "G.581" [label="G.581", tooltip="G.581 (XIII.3): If a segment be cut in extreme and mean ratio, the square on the lesser segment added to the half of the greater segment is five times the square on the half of the greater segment...", fillcolor="#222244", URL="../G.581/index.html", target="_top"];
     "G.582" [label="G.582", tooltip="G.582 (XIII.4): If a segment be cut in extreme and mean ratio, the square on the whole and the square on the lesser segment together are triple of the square on the greater segment.", fillcolor="#222244", URL="../G.582/index.html", target="_top"];
     "G.583" [label="G.583", tooltip="G.583 (XIII.5): If a segment be cut in extreme and mean ratio, and there be added to it a segment equal to the greater segment, the whole segment has been cut in extreme and mean ratio, and the or...", fillcolor="#222244", URL="../G.583/index.html", target="_top"];
     "G.584" [label="G.584", tooltip="G.584 (XIII.6): If a rational segment be cut in extreme and mean ratio, each of the segments is the irrational segment called apotome.", fillcolor="#222244", URL="../G.584/index.html", target="_top"];
     "G.585" [label="G.585", tooltip="G.585 (XIII.7): If three angles of an equilateral pentagon, taken either in order or not in order, be equal, the pentagon is equiangular.", fillcolor="#222244", URL="../G.585/index.html", target="_top"];
     "G.586" [label="G.586", tooltip="G.586 (XIII.8): If in an equilateral and equiangular pentagon segments subtend two angles taken in order, they cut one another in extreme and mean ratio, and their greater segments are equal to th...", fillcolor="#222244", URL="../G.586/index.html", target="_top"];
     "G.587" [label="G.587", tooltip="G.587 (XIII.9): If the side of the hexagon and that of the decagon inscribed in the same circle be added together, the whole segment has been cut in extreme and mean ratio, and its greater segment...", fillcolor="#222244", URL="../G.587/index.html", target="_top"];
     "G.588" [label="G.588", tooltip="G.588 (XIII.10): If an equilateral pentagon be inscribed in a circle, the square on the side of the pentagon is equal to the squares on the side of the hexagon and on that of the decagon inscribed ...", fillcolor="#222244", URL="../G.588/index.html", target="_top"];
     "G.589" [label="G.589", tooltip="G.589 (XIII.11): If in a circle which has its diameter rational an equilateral pentagon be inscribed, the side of the pentagon is the irrational segment called minor.", fillcolor="#222244", URL="../G.589/index.html", target="_top"];
     "G.590" [label="G.590", tooltip="G.590 (XIII.12): If an equilateral triangle be inscribed in a circle, the square on the side of the triangle is triple of the square on the radius of the circle.", fillcolor="#222244", URL="../G.590/index.html", target="_top"];
     "G.591" [label="G.591", tooltip="G.591 (XI.def.15): Theaxis of the sphere is thesegment which remains fixed and about which thesemicircle is turned.", fillcolor="#224422", URL="../G.591/index.html", target="_top"];
     "G.592" [label="G.592", tooltip="G.592 (XIII.13): To construct a pyramid, to comprehend it in a given sphere, and to prove that the square on the diameter of the sphere is one and a half times the square on the side of the pyramid...", fillcolor="#222244", URL="../G.592/index.html", target="_top"];
     "G.593" [label="G.593", tooltip="G.593 (XI.def.26): Anoctahedron is asolid figure contained by eight equal andequilateral triangles.", fillcolor="#224422", URL="../G.593/index.html", target="_top"];
     "G.594" [label="G.594", tooltip="G.594 (XIII.14): Construct an octahedron and comprehend it in a sphere, as in the preceding case; and to prove that the square on the diameter of the sphere is double of the square on the side of t...", fillcolor="#222244", URL="../G.594/index.html", target="_top"];
     "G.595" [label="G.595", tooltip="G.595 (XIII.15): Construct a cube and comprehend it in a sphere, like the pyramid; and to prove that the square on the diameter of the sphere is triple of the square on the side of the cube.", fillcolor="#222244", URL="../G.595/index.html", target="_top"];
     "G.596" [label="G.596", tooltip="G.596 (XI.def.27): Anicosahedron is asolid figure contained by twenty equal andequilateral triangles.", fillcolor="#224422", URL="../G.596/index.html", target="_top"];
     "G.597" [label="G.597", tooltip="G.597 (XIII.16): Construct an icosahedron and comprehend it in a sphere, like the aforesaid figures; and to prove that the side of the icosahedron is the irrational segment called minor.", fillcolor="#222244", URL="../G.597/index.html", target="_top"];
     "G.598" [label="G.598", tooltip="G.598 (XI.def.16): Thecenter of the sphere is the same as that of thesemicircle.", fillcolor="#224422", URL="../G.598/index.html", target="_top"];
     "G.599" [label="G.599", tooltip="G.599 (XI.def.28): Adodecahedron is asolid figure contained by twelve equal,equilateral, and equiangular pentagons.", fillcolor="#224422", URL="../G.599/index.html", target="_top"];
     "G.600" [label="G.600", tooltip="G.600 (XIII.17): Construct a dodecahedron and comprehend it in a sphere, like the aforesaid figures, and to prove that the side of the dodecahedron is the irrational segment called apotome.", fillcolor="#222244", URL="../G.600/index.html", target="_top"];
     "G.601" [label="G.601", tooltip="G.601 (XIII.18): To set out the sides of the five figures and to compare them with one another.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.13" -> "G.1";
     "G.14" -> "G.1";
     "G.20" -> "G.1";
     "G.27" -> "G.1";
     "G.33" -> "G.1";
     "G.34" -> "G.1";
     "G.38" -> "G.1";
     "G.48" -> "G.1";
     "G.58" -> "G.1";
     "G.87" -> "G.1";
     "G.108" -> "G.1";
     "G.120" -> "G.1";
     "G.121" -> "G.1";
     "G.138" -> "G.1";
     "G.140" -> "G.1";
     "G.211" -> "G.1";
     "G.506" -> "G.1";
     "G.507" -> "G.1";
     "G.509" -> "G.1";
     "G.513" -> "G.1";
     "G.514" -> "G.1";
     "G.549" -> "G.1";
     "G.553" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.29" -> "G.2";
     "G.198" -> "G.2";
     "G.211" -> "G.2";
     "G.242" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.27" -> "G.3";
     "G.60" -> "G.3";
     "G.118" -> "G.3";
     "G.138" -> "G.3";
     "G.146" -> "G.3";
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
     "G.34" -> "G.4";
     "G.36" -> "G.4";
     "G.38" -> "G.4";
     "G.39" -> "G.4";
     "G.47" -> "G.4";
     "G.48" -> "G.4";
     "G.52" -> "G.4";
     "G.53" -> "G.4";
     "G.54" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.57" -> "G.4";
     "G.58" -> "G.4";
     "G.60" -> "G.4";
     "G.61" -> "G.4";
     "G.73" -> "G.4";
     "G.75" -> "G.4";
     "G.81" -> "G.4";
     "G.83" -> "G.4";
     "G.87" -> "G.4";
     "G.89" -> "G.4";
     "G.111" -> "G.4";
     "G.117" -> "G.4";
     "G.118" -> "G.4";
     "G.120" -> "G.4";
     "G.121" -> "G.4";
     "G.122" -> "G.4";
     "G.126" -> "G.4";
     "G.129" -> "G.4";
     "G.132" -> "G.4";
     "G.135" -> "G.4";
     "G.136" -> "G.4";
     "G.138" -> "G.4";
     "G.140" -> "G.4";
     "G.146" -> "G.4";
     "G.147" -> "G.4";
     "G.211" -> "G.4";
     "G.221" -> "G.4";
     "G.222" -> "G.4";
     "G.223" -> "G.4";
     "G.227" -> "G.4";
     "G.228" -> "G.4";
     "G.229" -> "G.4";
     "G.234" -> "G.4";
     "G.240" -> "G.4";
     "G.245" -> "G.4";
     "G.380" -> "G.4";
     "G.381" -> "G.4";
     "G.388" -> "G.4";
     "G.389" -> "G.4";
     "G.390" -> "G.4";
     "G.391" -> "G.4";
     "G.392" -> "G.4";
     "G.393" -> "G.4";
     "G.394" -> "G.4";
     "G.395" -> "G.4";
     "G.396" -> "G.4";
     "G.397" -> "G.4";
     "G.404" -> "G.4";
     "G.407" -> "G.4";
     "G.453" -> "G.4";
     "G.454" -> "G.4";
     "G.458" -> "G.4";
     "G.471" -> "G.4";
     "G.480" -> "G.4";
     "G.483" -> "G.4";
     "G.502" -> "G.4";
     "G.503" -> "G.4";
     "G.504" -> "G.4";
     "G.505" -> "G.4";
     "G.506" -> "G.4";
     "G.507" -> "G.4";
     "G.508" -> "G.4";
     "G.509" -> "G.4";
     "G.510" -> "G.4";
     "G.511" -> "G.4";
     "G.513" -> "G.4";
     "G.514" -> "G.4";
     "G.576" -> "G.4";
     "G.579" -> "G.4";
     "G.581" -> "G.4";
     "G.582" -> "G.4";
     "G.583" -> "G.4";
     "G.584" -> "G.4";
     "G.586" -> "G.4";
     "G.587" -> "G.4";
     "G.589" -> "G.4";
     "G.591" -> "G.4";
     "G.597" -> "G.4";
     "G.600" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.576" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.52" -> "G.7";
     "G.319" -> "G.7";
     "G.502" -> "G.7";
     "G.503" -> "G.7";
     "G.504" -> "G.7";
     "G.505" -> "G.7";
     "G.507" -> "G.7";
     "G.509" -> "G.7";
     "G.510" -> "G.7";
     "G.511" -> "G.7";
     "G.513" -> "G.7";
     "G.514" -> "G.7";
     "G.549" -> "G.7";
     "G.553" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.24" -> "G.9";
     "G.26" -> "G.9";
     "G.96" -> "G.9";
     "G.122" -> "G.9";
     "G.126" -> "G.9";
     "G.148" -> "G.9";
     "G.150" -> "G.9";
     "G.153" -> "G.9";
     "G.155" -> "G.9";
     "G.156" -> "G.9";
     "G.187" -> "G.9";
     "G.188" -> "G.9";
     "G.189" -> "G.9";
     "G.209" -> "G.9";
     "G.229" -> "G.9";
     "G.233" -> "G.9";
     "G.237" -> "G.9";
     "G.240" -> "G.9";
     "G.388" -> "G.9";
     "G.389" -> "G.9";
     "G.390" -> "G.9";
     "G.575" -> "G.9";
     "G.581" -> "G.9";
     "G.597" -> "G.9";
     "G.600" -> "G.9";
     "G.601" -> "G.9";
     "G.14" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.21" -> "G.10";
     "G.61" -> "G.10";
     "G.96" -> "G.10";
     "G.98" -> "G.10";
     "G.102" -> "G.10";
     "G.108" -> "G.10";
     "G.111" -> "G.10";
     "G.117" -> "G.10";
     "G.118" -> "G.10";
     "G.121" -> "G.10";
     "G.122" -> "G.10";
     "G.123" -> "G.10";
     "G.124" -> "G.10";
     "G.125" -> "G.10";
     "G.126" -> "G.10";
     "G.139" -> "G.10";
     "G.140" -> "G.10";
     "G.146" -> "G.10";
     "G.147" -> "G.10";
     "G.148" -> "G.10";
     "G.149" -> "G.10";
     "G.150" -> "G.10";
     "G.153" -> "G.10";
     "G.156" -> "G.10";
     "G.166" -> "G.10";
     "G.167" -> "G.10";
     "G.502" -> "G.10";
     "G.587" -> "G.10";
     "G.588" -> "G.10";
     "G.589" -> "G.10";
     "G.590" -> "G.10";
     "G.12" -> "G.11";
     "G.24" -> "G.11";
     "G.26" -> "G.11";
     "G.28" -> "G.11";
     "G.41" -> "G.11";
     "G.42" -> "G.11";
     "G.43" -> "G.11";
     "G.44" -> "G.11";
     "G.45" -> "G.11";
     "G.47" -> "G.11";
     "G.51" -> "G.11";
     "G.59" -> "G.11";
     "G.63" -> "G.11";
     "G.66" -> "G.11";
     "G.67" -> "G.11";
     "G.68" -> "G.11";
     "G.70" -> "G.11";
     "G.71" -> "G.11";
     "G.73" -> "G.11";
     "G.74" -> "G.11";
     "G.78" -> "G.11";
     "G.125" -> "G.11";
     "G.148" -> "G.11";
     "G.149" -> "G.11";
     "G.150" -> "G.11";
     "G.210" -> "G.11";
     "G.211" -> "G.11";
     "G.213" -> "G.11";
     "G.215" -> "G.11";
     "G.218" -> "G.11";
     "G.226" -> "G.11";
     "G.232" -> "G.11";
     "G.233" -> "G.11";
     "G.234" -> "G.11";
     "G.237" -> "G.11";
     "G.240" -> "G.11";
     "G.245" -> "G.11";
     "G.392" -> "G.11";
     "G.503" -> "G.11";
     "G.590" -> "G.11";
     "G.17" -> "G.12";
     "G.25" -> "G.12";
     "G.63" -> "G.12";
     "G.166" -> "G.12";
     "G.167" -> "G.12";
     "G.585" -> "G.12";
     "G.586" -> "G.12";
     "G.588" -> "G.12";
     "G.589" -> "G.12";
     "G.590" -> "G.12";
     "G.593" -> "G.12";
     "G.596" -> "G.12";
     "G.599" -> "G.12";
     "G.17" -> "G.13";
     "G.20" -> "G.13";
     "G.25" -> "G.13";
     "G.27" -> "G.13";
     "G.34" -> "G.13";
     "G.41" -> "G.13";
     "G.15" -> "G.14";
     "G.61" -> "G.14";
     "G.96" -> "G.14";
     "G.98" -> "G.14";
     "G.102" -> "G.14";
     "G.120" -> "G.14";
     "G.121" -> "G.14";
     "G.122" -> "G.14";
     "G.133" -> "G.14";
     "G.134" -> "G.14";
     "G.166" -> "G.14";
     "G.246" -> "G.14";
     "G.502" -> "G.14";
     "G.576" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.34" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.36" -> "G.16";
     "G.38" -> "G.16";
     "G.39" -> "G.16";
     "G.56" -> "G.16";
     "G.57" -> "G.16";
     "G.64" -> "G.16";
     "G.65" -> "G.16";
     "G.68" -> "G.16";
     "G.73" -> "G.16";
     "G.74" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.33" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.42" -> "G.18";
     "G.20" -> "G.19";
     "G.38" -> "G.19";
     "G.39" -> "G.19";
     "G.64" -> "G.19";
     "G.72" -> "G.19";
     "G.21" -> "G.20";
     "G.25" -> "G.21";
     "G.30" -> "G.21";
     "G.33" -> "G.21";
     "G.41" -> "G.21";
     "G.43" -> "G.21";
     "G.47" -> "G.21";
     "G.221" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.26" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.32" -> "G.22";
     "G.36" -> "G.22";
     "G.38" -> "G.22";
     "G.39" -> "G.22";
     "G.41" -> "G.22";
     "G.42" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.51" -> "G.22";
     "G.53" -> "G.22";
     "G.54" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.59" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.76" -> "G.22";
     "G.77" -> "G.22";
     "G.78" -> "G.22";
     "G.118" -> "G.22";
     "G.122" -> "G.22";
     "G.123" -> "G.22";
     "G.124" -> "G.22";
     "G.125" -> "G.22";
     "G.127" -> "G.22";
     "G.132" -> "G.22";
     "G.133" -> "G.22";
     "G.134" -> "G.22";
     "G.138" -> "G.22";
     "G.139" -> "G.22";
     "G.140" -> "G.22";
     "G.148" -> "G.22";
     "G.155" -> "G.22";
     "G.156" -> "G.22";
     "G.213" -> "G.22";
     "G.215" -> "G.22";
     "G.217" -> "G.22";
     "G.225" -> "G.22";
     "G.226" -> "G.22";
     "G.238" -> "G.22";
     "G.245" -> "G.22";
     "G.246" -> "G.22";
     "G.585" -> "G.22";
     "G.586" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.24";
     "G.31" -> "G.24";
     "G.41" -> "G.24";
     "G.51" -> "G.24";
     "G.60" -> "G.24";
     "G.62" -> "G.24";
     "G.64" -> "G.24";
     "G.79" -> "G.24";
     "G.133" -> "G.24";
     "G.136" -> "G.24";
     "G.215" -> "G.24";
     "G.506" -> "G.24";
     "G.508" -> "G.24";
     "G.549" -> "G.24";
     "G.585" -> "G.24";
     "G.586" -> "G.24";
     "G.588" -> "G.24";
     "G.592" -> "G.24";
     "G.594" -> "G.24";
     "G.27" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.118" -> "G.25";
     "G.123" -> "G.25";
     "G.139" -> "G.25";
     "G.167" -> "G.25";
     "G.585" -> "G.25";
     "G.586" -> "G.25";
     "G.587" -> "G.25";
     "G.588" -> "G.25";
     "G.166" -> "G.26";
     "G.585" -> "G.26";
     "G.586" -> "G.26";
     "G.28" -> "G.27";
     "G.30" -> "G.28";
     "G.33" -> "G.28";
     "G.34" -> "G.28";
     "G.48" -> "G.28";
     "G.98" -> "G.28";
     "G.135" -> "G.28";
     "G.506" -> "G.28";
     "G.508" -> "G.28";
     "G.585" -> "G.28";
     "G.600" -> "G.28";
     "G.30" -> "G.29";
     "G.48" -> "G.29";
     "G.71" -> "G.29";
     "G.73" -> "G.29";
     "G.74" -> "G.29";
     "G.118" -> "G.29";
     "G.31" -> "G.30";
     "G.34" -> "G.31";
     "G.41" -> "G.31";
     "G.33" -> "G.32";
     "G.34" -> "G.32";
     "G.36" -> "G.32";
     "G.37" -> "G.32";
     "G.38" -> "G.32";
     "G.42" -> "G.32";
     "G.54" -> "G.32";
     "G.55" -> "G.32";
     "G.56" -> "G.32";
     "G.59" -> "G.32";
     "G.76" -> "G.32";
     "G.77" -> "G.32";
     "G.78" -> "G.32";
     "G.79" -> "G.32";
     "G.81" -> "G.32";
     "G.98" -> "G.32";
     "G.118" -> "G.32";
     "G.120" -> "G.32";
     "G.121" -> "G.32";
     "G.125" -> "G.32";
     "G.139" -> "G.32";
     "G.209" -> "G.32";
     "G.218" -> "G.32";
     "G.505" -> "G.32";
     "G.506" -> "G.32";
     "G.507" -> "G.32";
     "G.510" -> "G.32";
     "G.513" -> "G.32";
     "G.514" -> "G.32";
     "G.36" -> "G.33";
     "G.75" -> "G.33";
     "G.513" -> "G.33";
     "G.513" -> "G.34";
     "G.36" -> "G.35";
     "G.56" -> "G.35";
     "G.62" -> "G.35";
     "G.64" -> "G.35";
     "G.72" -> "G.35";
     "G.74" -> "G.35";
     "G.79" -> "G.35";
     "G.38" -> "G.36";
     "G.39" -> "G.36";
     "G.42" -> "G.36";
     "G.54" -> "G.36";
     "G.56" -> "G.36";
     "G.59" -> "G.36";
     "G.38" -> "G.37";
     "G.39" -> "G.37";
     "G.74" -> "G.38";
     "G.79" -> "G.38";
     "G.225" -> "G.38";
     "G.226" -> "G.38";
     "G.245" -> "G.38";
     "G.549" -> "G.38";
     "G.41" -> "G.39";
     "G.54" -> "G.39";
     "G.56" -> "G.39";
     "G.73" -> "G.39";
     "G.167" -> "G.39";
     "G.506" -> "G.39";
     "G.549" -> "G.39";
     "G.41" -> "G.40";
     "G.45" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.118" -> "G.42";
     "G.120" -> "G.42";
     "G.139" -> "G.42";
     "G.213" -> "G.42";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.118" -> "G.44";
     "G.120" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.58" -> "G.48";
     "G.71" -> "G.48";
     "G.134" -> "G.48";
     "G.149" -> "G.48";
     "G.215" -> "G.48";
     "G.229" -> "G.48";
     "G.62" -> "G.51";
     "G.506" -> "G.51";
     "G.549" -> "G.51";
     "G.588" -> "G.51";
     "G.53" -> "G.52";
     "G.54" -> "G.52";
     "G.56" -> "G.52";
     "G.57" -> "G.52";
     "G.58" -> "G.52";
     "G.60" -> "G.52";
     "G.64" -> "G.52";
     "G.65" -> "G.52";
     "G.66" -> "G.52";
     "G.67" -> "G.52";
     "G.68" -> "G.52";
     "G.70" -> "G.52";
     "G.211" -> "G.52";
     "G.245" -> "G.52";
     "G.508" -> "G.52";
     "G.509" -> "G.52";
     "G.510" -> "G.52";
     "G.511" -> "G.52";
     "G.54" -> "G.53";
     "G.58" -> "G.53";
     "G.60" -> "G.53";
     "G.213" -> "G.54";
     "G.508" -> "G.54";
     "G.56" -> "G.55";
     "G.73" -> "G.55";
     "G.213" -> "G.55";
     "G.57" -> "G.56";
     "G.59" -> "G.56";
     "G.60" -> "G.56";
     "G.62" -> "G.56";
     "G.64" -> "G.56";
     "G.73" -> "G.56";
     "G.74" -> "G.56";
     "G.75" -> "G.56";
     "G.245" -> "G.56";
     "G.510" -> "G.56";
     "G.549" -> "G.56";
     "G.74" -> "G.57";
     "G.59" -> "G.58";
     "G.66" -> "G.58";
     "G.67" -> "G.58";
     "G.68" -> "G.58";
     "G.71" -> "G.58";
     "G.73" -> "G.58";
     "G.75" -> "G.58";
     "G.83" -> "G.58";
     "G.87" -> "G.58";
     "G.221" -> "G.58";
     "G.222" -> "G.58";
     "G.238" -> "G.58";
     "G.513" -> "G.58";
     "G.514" -> "G.58";
     "G.123" -> "G.59";
     "G.125" -> "G.59";
     "G.139" -> "G.59";
     "G.140" -> "G.59";
     "G.149" -> "G.59";
     "G.167" -> "G.59";
     "G.215" -> "G.59";
     "G.218" -> "G.59";
     "G.229" -> "G.59";
     "G.232" -> "G.59";
     "G.245" -> "G.59";
     "G.586" -> "G.59";
     "G.587" -> "G.59";
     "G.588" -> "G.59";
     "G.589" -> "G.59";
     "G.65" -> "G.60";
     "G.74" -> "G.60";
     "G.549" -> "G.60";
     "G.597" -> "G.60";
     "G.62" -> "G.61";
     "G.72" -> "G.61";
     "G.86" -> "G.61";
     "G.96" -> "G.61";
     "G.118" -> "G.61";
     "G.131" -> "G.61";
     "G.139" -> "G.61";
     "G.147" -> "G.61";
     "G.236" -> "G.61";
     "G.238" -> "G.61";
     "G.502" -> "G.61";
     "G.549" -> "G.61";
     "G.575" -> "G.61";
     "G.589" -> "G.61";
     "G.64" -> "G.62";
     "G.65" -> "G.62";
     "G.66" -> "G.62";
     "G.67" -> "G.62";
     "G.70" -> "G.62";
     "G.72" -> "G.62";
     "G.74" -> "G.62";
     "G.75" -> "G.62";
     "G.213" -> "G.62";
     "G.64" -> "G.63";
     "G.75" -> "G.63";
     "G.79" -> "G.63";
     "G.83" -> "G.63";
     "G.87" -> "G.63";
     "G.89" -> "G.63";
     "G.228" -> "G.63";
     "G.297" -> "G.63";
     "G.309" -> "G.63";
     "G.380" -> "G.63";
     "G.381" -> "G.63";
     "G.388" -> "G.63";
     "G.389" -> "G.63";
     "G.390" -> "G.63";
     "G.392" -> "G.63";
     "G.395" -> "G.63";
     "G.396" -> "G.63";
     "G.404" -> "G.63";
     "G.407" -> "G.63";
     "G.454" -> "G.63";
     "G.458" -> "G.63";
     "G.471" -> "G.63";
     "G.483" -> "G.63";
     "G.548" -> "G.63";
     "G.579" -> "G.63";
     "G.581" -> "G.63";
     "G.582" -> "G.63";
     "G.588" -> "G.63";
     "G.590" -> "G.63";
     "G.592" -> "G.63";
     "G.594" -> "G.63";
     "G.595" -> "G.63";
     "G.65" -> "G.64";
     "G.66" -> "G.64";
     "G.67" -> "G.65";
     "G.87" -> "G.65";
     "G.240" -> "G.65";
     "G.68" -> "G.66";
     "G.70" -> "G.66";
     "G.71" -> "G.67";
     "G.210" -> "G.67";
     "G.211" -> "G.67";
     "G.211" -> "G.68";
     "G.71" -> "G.70";
     "G.79" -> "G.70";
     "G.210" -> "G.70";
     "G.73" -> "G.71";
     "G.74" -> "G.71";
     "G.73" -> "G.72";
     "G.87" -> "G.72";
     "G.89" -> "G.72";
     "G.74" -> "G.73";
     "G.237" -> "G.73";
     "G.237" -> "G.74";
     "G.79" -> "G.75";
     "G.83" -> "G.75";
     "G.87" -> "G.75";
     "G.89" -> "G.75";
     "G.78" -> "G.76";
     "G.78" -> "G.77";
     "G.118" -> "G.77";
     "G.120" -> "G.77";
     "G.79" -> "G.78";
     "G.218" -> "G.78";
     "G.385" -> "G.79";
     "G.404" -> "G.79";
     "G.407" -> "G.79";
     "G.590" -> "G.79";
     "G.594" -> "G.79";
     "G.595" -> "G.79";
     "G.600" -> "G.79";
     "G.83" -> "G.81";
     "G.87" -> "G.81";
     "G.89" -> "G.81";
     "G.227" -> "G.81";
     "G.228" -> "G.81";
     "G.388" -> "G.81";
     "G.393" -> "G.81";
     "G.395" -> "G.81";
     "G.407" -> "G.81";
     "G.458" -> "G.81";
     "G.581" -> "G.81";
     "G.588" -> "G.83";
     "G.87" -> "G.86";
     "G.89" -> "G.86";
     "G.240" -> "G.86";
     "G.579" -> "G.86";
     "G.581" -> "G.86";
     "G.582" -> "G.86";
     "G.389" -> "G.87";
     "G.453" -> "G.89";
     "G.458" -> "G.89";
     "G.483" -> "G.89";
     "G.139" -> "G.96";
     "G.575" -> "G.96";
     "G.591" -> "G.96";
     "G.598" -> "G.96";
     "G.108" -> "G.98";
     "G.592" -> "G.98";
     "G.108" -> "G.102";
     "G.129" -> "G.108";
     "G.118" -> "G.111";
     "G.120" -> "G.111";
     "G.121" -> "G.111";
     "G.140" -> "G.111";
     "G.118" -> "G.117";
     "G.149" -> "G.118";
     "G.121" -> "G.120";
     "G.140" -> "G.121";
     "G.123" -> "G.122";
     "G.124" -> "G.123";
     "G.134" -> "G.123";
     "G.125" -> "G.124";
     "G.139" -> "G.125";
     "G.140" -> "G.125";
     "G.140" -> "G.126";
     "G.129" -> "G.127";
     "G.133" -> "G.127";
     "G.133" -> "G.129";
     "G.133" -> "G.131";
     "G.134" -> "G.131";
     "G.135" -> "G.131";
     "G.136" -> "G.131";
     "G.246" -> "G.131";
     "G.133" -> "G.132";
     "G.134" -> "G.132";
     "G.246" -> "G.132";
     "G.134" -> "G.133";
     "G.135" -> "G.133";
     "G.167" -> "G.133";
     "G.588" -> "G.133";
     "G.136" -> "G.134";
     "G.167" -> "G.134";
     "G.246" -> "G.134";
     "G.586" -> "G.135";
     "G.167" -> "G.136";
     "G.139" -> "G.138";
     "G.140" -> "G.139";
     "G.223" -> "G.139";
     "G.385" -> "G.139";
     "G.404" -> "G.139";
     "G.590" -> "G.139";
     "G.592" -> "G.139";
     "G.594" -> "G.139";
     "G.597" -> "G.139";
     "G.149" -> "G.140";
     "G.147" -> "G.146";
     "G.385" -> "G.147";
     "G.149" -> "G.148";
     "G.167" -> "G.148";
     "G.588" -> "G.148";
     "G.590" -> "G.148";
     "G.592" -> "G.149";
     "G.167" -> "G.150";
     "G.167" -> "G.153";
     "G.586" -> "G.155";
     "G.166" -> "G.156";
     "G.586" -> "G.166";
     "G.587" -> "G.167";
     "G.588" -> "G.167";
     "G.590" -> "G.167";
     "G.597" -> "G.167";
     "G.601" -> "G.167";
     "G.170" -> "G.169";
     "G.249" -> "G.169";
     "G.250" -> "G.169";
     "G.251" -> "G.169";
     "G.252" -> "G.169";
     "G.253" -> "G.169";
     "G.254" -> "G.169";
     "G.256" -> "G.169";
     "G.268" -> "G.169";
     "G.274" -> "G.169";
     "G.277" -> "G.169";
     "G.283" -> "G.169";
     "G.290" -> "G.169";
     "G.291" -> "G.169";
     "G.372" -> "G.169";
     "G.380" -> "G.169";
     "G.171" -> "G.170";
     "G.172" -> "G.170";
     "G.175" -> "G.170";
     "G.176" -> "G.170";
     "G.177" -> "G.170";
     "G.185" -> "G.170";
     "G.193" -> "G.170";
     "G.257" -> "G.170";
     "G.186" -> "G.171";
     "G.190" -> "G.171";
     "G.198" -> "G.171";
     "G.175" -> "G.172";
     "G.198" -> "G.172";
     "G.174" -> "G.173";
     "G.188" -> "G.173";
     "G.189" -> "G.173";
     "G.232" -> "G.173";
     "G.289" -> "G.173";
     "G.297" -> "G.173";
     "G.299" -> "G.173";
     "G.309" -> "G.173";
     "G.319" -> "G.173";
     "G.328" -> "G.173";
     "G.376" -> "G.173";
     "G.377" -> "G.173";
     "G.378" -> "G.173";
     "G.379" -> "G.173";
     "G.381" -> "G.173";
     "G.175" -> "G.174";
     "G.202" -> "G.174";
     "G.205" -> "G.174";
     "G.267" -> "G.174";
     "G.177" -> "G.175";
     "G.177" -> "G.176";
     "G.180" -> "G.176";
     "G.183" -> "G.176";
     "G.187" -> "G.176";
     "G.189" -> "G.176";
     "G.190" -> "G.176";
     "G.191" -> "G.176";
     "G.192" -> "G.176";
     "G.193" -> "G.176";
     "G.195" -> "G.176";
     "G.202" -> "G.176";
     "G.205" -> "G.176";
     "G.210" -> "G.176";
     "G.232" -> "G.176";
     "G.246" -> "G.176";
     "G.267" -> "G.176";
     "G.271" -> "G.176";
     "G.272" -> "G.176";
     "G.274" -> "G.176";
     "G.275" -> "G.176";
     "G.276" -> "G.176";
     "G.289" -> "G.176";
     "G.296" -> "G.176";
     "G.205" -> "G.177";
     "G.183" -> "G.180";
     "G.190" -> "G.180";
     "G.195" -> "G.180";
     "G.198" -> "G.180";
     "G.199" -> "G.180";
     "G.213" -> "G.180";
     "G.215" -> "G.180";
     "G.217" -> "G.180";
     "G.221" -> "G.180";
     "G.222" -> "G.180";
     "G.223" -> "G.180";
     "G.227" -> "G.180";
     "G.228" -> "G.180";
     "G.230" -> "G.180";
     "G.234" -> "G.180";
     "G.245" -> "G.180";
     "G.266" -> "G.180";
     "G.273" -> "G.180";
     "G.296" -> "G.180";
     "G.297" -> "G.180";
     "G.299" -> "G.180";
     "G.309" -> "G.180";
     "G.318" -> "G.180";
     "G.319" -> "G.180";
     "G.382" -> "G.180";
     "G.182" -> "G.181";
     "G.190" -> "G.181";
     "G.194" -> "G.181";
     "G.196" -> "G.181";
     "G.197" -> "G.181";
     "G.200" -> "G.181";
     "G.231" -> "G.181";
     "G.265" -> "G.181";
     "G.183" -> "G.182";
     "G.188" -> "G.183";
     "G.193" -> "G.183";
     "G.211" -> "G.183";
     "G.225" -> "G.183";
     "G.226" -> "G.183";
     "G.273" -> "G.183";
     "G.376" -> "G.183";
     "G.377" -> "G.183";
     "G.186" -> "G.184";
     "G.188" -> "G.184";
     "G.186" -> "G.185";
     "G.188" -> "G.185";
     "G.191" -> "G.185";
     "G.187" -> "G.186";
     "G.188" -> "G.186";
     "G.192" -> "G.186";
     "G.202" -> "G.186";
     "G.211" -> "G.187";
     "G.215" -> "G.187";
     "G.225" -> "G.187";
     "G.226" -> "G.187";
     "G.234" -> "G.187";
     "G.238" -> "G.187";
     "G.273" -> "G.187";
     "G.377" -> "G.187";
     "G.192" -> "G.188";
     "G.202" -> "G.188";
     "G.195" -> "G.189";
     "G.199" -> "G.189";
     "G.201" -> "G.189";
     "G.210" -> "G.189";
     "G.211" -> "G.189";
     "G.215" -> "G.189";
     "G.225" -> "G.189";
     "G.226" -> "G.189";
     "G.231" -> "G.189";
     "G.234" -> "G.189";
     "G.238" -> "G.189";
     "G.377" -> "G.189";
     "G.384" -> "G.189";
     "G.480" -> "G.189";
     "G.193" -> "G.190";
     "G.232" -> "G.190";
     "G.192" -> "G.191";
     "G.202" -> "G.191";
     "G.195" -> "G.192";
     "G.199" -> "G.192";
     "G.583" -> "G.192";
     "G.586" -> "G.192";
     "G.195" -> "G.193";
     "G.210" -> "G.193";
     "G.600" -> "G.193";
     "G.195" -> "G.194";
     "G.261" -> "G.194";
     "G.262" -> "G.194";
     "G.266" -> "G.194";
     "G.268" -> "G.194";
     "G.201" -> "G.195";
     "G.213" -> "G.195";
     "G.231" -> "G.195";
     "G.236" -> "G.195";
     "G.237" -> "G.195";
     "G.198" -> "G.196";
     "G.199" -> "G.196";
     "G.198" -> "G.197";
     "G.199" -> "G.197";
     "G.389" -> "G.197";
     "G.590" -> "G.197";
     "G.199" -> "G.198";
     "G.201" -> "G.198";
     "G.236" -> "G.199";
     "G.589" -> "G.199";
     "G.201" -> "G.200";
     "G.592" -> "G.200";
     "G.404" -> "G.201";
     "G.589" -> "G.201";
     "G.205" -> "G.202";
     "G.213" -> "G.205";
     "G.232" -> "G.205";
     "G.234" -> "G.205";
     "G.236" -> "G.205";
     "G.376" -> "G.205";
     "G.377" -> "G.205";
     "G.384" -> "G.205";
     "G.210" -> "G.209";
     "G.211" -> "G.210";
     "G.225" -> "G.210";
     "G.226" -> "G.210";
     "G.231" -> "G.210";
     "G.232" -> "G.210";
     "G.237" -> "G.210";
     "G.393" -> "G.210";
     "G.394" -> "G.210";
     "G.395" -> "G.210";
     "G.397" -> "G.210";
     "G.480" -> "G.210";
     "G.483" -> "G.210";
     "G.579" -> "G.210";
     "G.213" -> "G.211";
     "G.221" -> "G.211";
     "G.222" -> "G.211";
     "G.236" -> "G.211";
     "G.215" -> "G.213";
     "G.218" -> "G.213";
     "G.229" -> "G.213";
     "G.232" -> "G.213";
     "G.586" -> "G.213";
     "G.587" -> "G.213";
     "G.588" -> "G.213";
     "G.601" -> "G.213";
     "G.232" -> "G.215";
     "G.245" -> "G.215";
     "G.218" -> "G.217";
     "G.229" -> "G.217";
     "G.231" -> "G.217";
     "G.232" -> "G.217";
     "G.233" -> "G.217";
     "G.234" -> "G.217";
     "G.236" -> "G.217";
     "G.223" -> "G.218";
     "G.592" -> "G.218";
     "G.597" -> "G.218";
     "G.601" -> "G.218";
     "G.231" -> "G.221";
     "G.234" -> "G.221";
     "G.234" -> "G.222";
     "G.237" -> "G.223";
     "G.225" -> "G.224";
     "G.226" -> "G.224";
     "G.227" -> "G.225";
     "G.396" -> "G.225";
     "G.231" -> "G.226";
     "G.228" -> "G.227";
     "G.480" -> "G.228";
     "G.483" -> "G.228";
     "G.579" -> "G.228";
     "G.582" -> "G.228";
     "G.583" -> "G.228";
     "G.584" -> "G.228";
     "G.588" -> "G.228";
     "G.592" -> "G.228";
     "G.234" -> "G.229";
     "G.237" -> "G.229";
     "G.240" -> "G.229";
     "G.231" -> "G.230";
     "G.309" -> "G.230";
     "G.319" -> "G.230";
     "G.597" -> "G.230";
     "G.601" -> "G.230";
     "G.232" -> "G.231";
     "G.234" -> "G.231";
     "G.237" -> "G.231";
     "G.377" -> "G.231";
     "G.381" -> "G.232";
     "G.601" -> "G.232";
     "G.236" -> "G.233";
     "G.240" -> "G.233";
     "G.396" -> "G.234";
     "G.238" -> "G.236";
     "G.240" -> "G.237";
     "G.240" -> "G.238";
     "G.480" -> "G.238";
     "G.407" -> "G.240";
     "G.579" -> "G.242";
     "G.581" -> "G.242";
     "G.582" -> "G.242";
     "G.583" -> "G.242";
     "G.584" -> "G.242";
     "G.586" -> "G.242";
     "G.587" -> "G.242";
     "G.600" -> "G.245";
     "G.586" -> "G.246";
     "G.587" -> "G.246";
     "G.588" -> "G.246";
     "G.248" -> "G.247";
     "G.249" -> "G.247";
     "G.250" -> "G.247";
     "G.268" -> "G.247";
     "G.269" -> "G.247";
     "G.283" -> "G.247";
     "G.250" -> "G.248";
     "G.251" -> "G.248";
     "G.252" -> "G.248";
     "G.253" -> "G.248";
     "G.255" -> "G.248";
     "G.256" -> "G.248";
     "G.257" -> "G.248";
     "G.258" -> "G.248";
     "G.261" -> "G.248";
     "G.262" -> "G.248";
     "G.265" -> "G.248";
     "G.266" -> "G.248";
     "G.267" -> "G.248";
     "G.268" -> "G.248";
     "G.269" -> "G.248";
     "G.270" -> "G.248";
     "G.271" -> "G.248";
     "G.272" -> "G.248";
     "G.273" -> "G.248";
     "G.274" -> "G.248";
     "G.275" -> "G.248";
     "G.276" -> "G.248";
     "G.277" -> "G.248";
     "G.278" -> "G.248";
     "G.279" -> "G.248";
     "G.280" -> "G.248";
     "G.281" -> "G.248";
     "G.289" -> "G.248";
     "G.290" -> "G.248";
     "G.291" -> "G.248";
     "G.296" -> "G.248";
     "G.297" -> "G.248";
     "G.299" -> "G.248";
     "G.300" -> "G.248";
     "G.308" -> "G.248";
     "G.309" -> "G.248";
     "G.319" -> "G.248";
     "G.376" -> "G.248";
     "G.377" -> "G.248";
     "G.378" -> "G.248";
     "G.379" -> "G.248";
     "G.250" -> "G.249";
     "G.251" -> "G.249";
     "G.252" -> "G.249";
     "G.275" -> "G.249";
     "G.276" -> "G.249";
     "G.277" -> "G.249";
     "G.278" -> "G.249";
     "G.279" -> "G.249";
     "G.280" -> "G.249";
     "G.281" -> "G.249";
     "G.296" -> "G.249";
     "G.251" -> "G.250";
     "G.252" -> "G.251";
     "G.255" -> "G.251";
     "G.289" -> "G.252";
     "G.255" -> "G.253";
     "G.257" -> "G.253";
     "G.261" -> "G.253";
     "G.262" -> "G.253";
     "G.263" -> "G.253";
     "G.389" -> "G.253";
     "G.390" -> "G.253";
     "G.502" -> "G.253";
     "G.590" -> "G.253";
     "G.255" -> "G.254";
     "G.258" -> "G.254";
     "G.261" -> "G.254";
     "G.262" -> "G.254";
     "G.263" -> "G.254";
     "G.274" -> "G.255";
     "G.257" -> "G.256";
     "G.263" -> "G.256";
     "G.258" -> "G.257";
     "G.261" -> "G.257";
     "G.262" -> "G.257";
     "G.265" -> "G.257";
     "G.261" -> "G.258";
     "G.262" -> "G.258";
     "G.265" -> "G.258";
     "G.262" -> "G.261";
     "G.266" -> "G.262";
     "G.265" -> "G.263";
     "G.266" -> "G.263";
     "G.271" -> "G.263";
     "G.274" -> "G.263";
     "G.289" -> "G.263";
     "G.299" -> "G.263";
     "G.376" -> "G.263";
     "G.377" -> "G.263";
     "G.268" -> "G.265";
     "G.274" -> "G.265";
     "G.267" -> "G.266";
     "G.271" -> "G.266";
     "G.274" -> "G.266";
     "G.299" -> "G.266";
     "G.319" -> "G.266";
     "G.296" -> "G.267";
     "G.270" -> "G.268";
     "G.270" -> "G.269";
     "G.271" -> "G.269";
     "G.272" -> "G.269";
     "G.276" -> "G.269";
     "G.278" -> "G.269";
     "G.281" -> "G.269";
     "G.289" -> "G.269";
     "G.290" -> "G.269";
     "G.300" -> "G.269";
     "G.308" -> "G.269";
     "G.272" -> "G.270";
     "G.275" -> "G.270";
     "G.278" -> "G.270";
     "G.289" -> "G.270";
     "G.290" -> "G.270";
     "G.272" -> "G.271";
     "G.273" -> "G.271";
     "G.276" -> "G.271";
     "G.290" -> "G.271";
     "G.297" -> "G.271";
     "G.309" -> "G.271";
     "G.319" -> "G.271";
     "G.273" -> "G.272";
     "G.297" -> "G.272";
     "G.309" -> "G.272";
     "G.278" -> "G.273";
     "G.289" -> "G.273";
     "G.290" -> "G.273";
     "G.275" -> "G.274";
     "G.278" -> "G.274";
     "G.290" -> "G.274";
     "G.296" -> "G.274";
     "G.299" -> "G.274";
     "G.278" -> "G.275";
     "G.289" -> "G.275";
     "G.290" -> "G.275";
     "G.296" -> "G.275";
     "G.297" -> "G.276";
     "G.278" -> "G.277";
     "G.279" -> "G.278";
     "G.280" -> "G.278";
     "G.281" -> "G.279";
     "G.281" -> "G.280";
     "G.297" -> "G.281";
     "G.290" -> "G.283";
     "G.296" -> "G.283";
     "G.290" -> "G.289";
     "G.328" -> "G.289";
     "G.299" -> "G.290";
     "G.299" -> "G.291";
     "G.297" -> "G.296";
     "G.328" -> "G.297";
     "G.384" -> "G.299";
     "G.319" -> "G.300";
     "G.309" -> "G.308";
     "G.328" -> "G.308";
     "G.381" -> "G.308";
     "G.381" -> "G.309";
     "G.319" -> "G.318";
     "G.328" -> "G.318";
     "G.328" -> "G.319";
     "G.381" -> "G.328";
     "G.376" -> "G.372";
     "G.377" -> "G.372";
     "G.378" -> "G.372";
     "G.379" -> "G.372";
     "G.381" -> "G.372";
     "G.382" -> "G.372";
     "G.384" -> "G.372";
     "G.385" -> "G.372";
     "G.387" -> "G.372";
     "G.388" -> "G.372";
     "G.389" -> "G.372";
     "G.390" -> "G.372";
     "G.391" -> "G.372";
     "G.392" -> "G.372";
     "G.393" -> "G.372";
     "G.394" -> "G.372";
     "G.396" -> "G.372";
     "G.397" -> "G.372";
     "G.404" -> "G.372";
     "G.453" -> "G.372";
     "G.454" -> "G.372";
     "G.471" -> "G.372";
     "G.379" -> "G.376";
     "G.381" -> "G.376";
     "G.382" -> "G.376";
     "G.384" -> "G.376";
     "G.378" -> "G.377";
     "G.381" -> "G.377";
     "G.382" -> "G.377";
     "G.384" -> "G.377";
     "G.389" -> "G.377";
     "G.390" -> "G.377";
     "G.404" -> "G.377";
     "G.453" -> "G.377";
     "G.584" -> "G.377";
     "G.382" -> "G.378";
     "G.382" -> "G.379";
     "G.381" -> "G.380";
     "G.395" -> "G.380";
     "G.404" -> "G.380";
     "G.407" -> "G.380";
     "G.458" -> "G.380";
     "G.404" -> "G.381";
     "G.584" -> "G.381";
     "G.589" -> "G.381";
     "G.393" -> "G.382";
     "G.394" -> "G.382";
     "G.395" -> "G.382";
     "G.396" -> "G.382";
     "G.397" -> "G.382";
     "G.453" -> "G.382";
     "G.480" -> "G.382";
     "G.483" -> "G.382";
     "G.385" -> "G.384";
     "G.389" -> "G.384";
     "G.589" -> "G.384";
     "G.390" -> "G.385";
     "G.396" -> "G.385";
     "G.397" -> "G.385";
     "G.453" -> "G.385";
     "G.389" -> "G.387";
     "G.453" -> "G.387";
     "G.589" -> "G.387";
     "G.390" -> "G.388";
     "G.453" -> "G.388";
     "G.458" -> "G.388";
     "G.390" -> "G.389";
     "G.483" -> "G.389";
     "G.407" -> "G.390";
     "G.480" -> "G.390";
     "G.393" -> "G.391";
     "G.394" -> "G.391";
     "G.395" -> "G.391";
     "G.396" -> "G.391";
     "G.397" -> "G.391";
     "G.404" -> "G.391";
     "G.407" -> "G.391";
     "G.453" -> "G.391";
     "G.454" -> "G.391";
     "G.458" -> "G.391";
     "G.471" -> "G.391";
     "G.480" -> "G.391";
     "G.483" -> "G.391";
     "G.584" -> "G.391";
     "G.589" -> "G.391";
     "G.597" -> "G.391";
     "G.600" -> "G.391";
     "G.393" -> "G.392";
     "G.394" -> "G.392";
     "G.395" -> "G.392";
     "G.396" -> "G.392";
     "G.453" -> "G.392";
     "G.584" -> "G.392";
     "G.480" -> "G.393";
     "G.483" -> "G.394";
     "G.396" -> "G.395";
     "G.397" -> "G.395";
     "G.407" -> "G.395";
     "G.480" -> "G.395";
     "G.397" -> "G.396";
     "G.483" -> "G.396";
     "G.407" -> "G.397";
     "G.407" -> "G.404";
     "G.458" -> "G.407";
     "G.483" -> "G.453";
     "G.584" -> "G.453";
     "G.589" -> "G.453";
     "G.483" -> "G.454";
     "G.480" -> "G.458";
     "G.480" -> "G.471";
     "G.589" -> "G.471";
     "G.589" -> "G.480";
     "G.584" -> "G.483";
     "G.503" -> "G.502";
     "G.600" -> "G.502";
     "G.508" -> "G.503";
     "G.510" -> "G.503";
     "G.507" -> "G.504";
     "G.509" -> "G.504";
     "G.506" -> "G.505";
     "G.507" -> "G.505";
     "G.508" -> "G.505";
     "G.510" -> "G.505";
     "G.513" -> "G.505";
     "G.592" -> "G.505";
     "G.595" -> "G.505";
     "G.507" -> "G.506";
     "G.510" -> "G.506";
     "G.511" -> "G.506";
     "G.513" -> "G.506";
     "G.508" -> "G.507";
     "G.511" -> "G.508";
     "G.597" -> "G.508";
     "G.600" -> "G.508";
     "G.510" -> "G.509";
     "G.511" -> "G.510";
     "G.513" -> "G.510";
     "G.514" -> "G.510";
     "G.549" -> "G.511";
     "G.514" -> "G.513";
     "G.592" -> "G.514";
     "G.594" -> "G.514";
     "G.548" -> "G.529";
     "G.553" -> "G.529";
     "G.593" -> "G.529";
     "G.596" -> "G.529";
     "G.599" -> "G.529";
     "G.549" -> "G.548";
     "G.595" -> "G.548";
     "G.600" -> "G.549";
     "G.592" -> "G.553";
     "G.595" -> "G.553";
     "G.576" -> "G.575";
     "G.592" -> "G.575";
     "G.594" -> "G.575";
     "G.595" -> "G.575";
     "G.597" -> "G.575";
     "G.600" -> "G.575";
     "G.592" -> "G.576";
     "G.594" -> "G.576";
     "G.595" -> "G.576";
     "G.597" -> "G.576";
     "G.584" -> "G.579";
     "G.589" -> "G.579";
     "G.597" -> "G.581";
     "G.600" -> "G.582";
     "G.600" -> "G.583";
     "G.600" -> "G.584";
     "G.600" -> "G.585";
     "G.589" -> "G.586";
     "G.597" -> "G.587";
     "G.601" -> "G.587";
     "G.597" -> "G.588";
     "G.601" -> "G.588";
     "G.597" -> "G.589";
     "G.592" -> "G.590";
     "G.592" -> "G.591";
     "G.594" -> "G.591";
     "G.595" -> "G.591";
     "G.597" -> "G.591";
     "G.601" -> "G.592";
     "G.594" -> "G.593";
     "G.601" -> "G.594";
     "G.600" -> "G.595";
     "G.601" -> "G.595";
     "G.597" -> "G.596";
     "G.601" -> "G.597";
     "G.600" -> "G.598";
     "G.600" -> "G.599";
     "G.601" -> "G.600";
   }

.. toctree::
   :hidden:

   code
   heath
