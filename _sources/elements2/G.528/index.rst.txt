:order: 528
:number: 528
:canonical_id: G.528
:original_id: XI.23
:title: G.528 construct a solid angle out of three plane
:volume: III
:book: XI
:type: prop
:subtype: problem
:categories: problem, construction, solid-geometry
:category: problem, construction, solid-geometry
:tags: book-xi, point, segment, circle, angle, triangle, solid-angle, plane-angle, right-angle, trilateral, straight-line, centre, parallel-straight-lines, alternando, right-angles-to-plane, square, semicircle, diameter, angle-in-segment, plane, equality, reductio-ad-absurdum, lemma
:dependencies: G.4, G.11, G.12, G.14, G.22, G.24, G.29, G.33, G.50, G.56, G.63, G.79, G.138, G.139, G.147, G.195, G.211, G.213, G.514, G.524, G.527
:excerpt: Construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right angles.

.. _G.528:
.. _XI.23:

G.528 construct a solid angle out of three plane
================================================

.. rubric:: `XI.23 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/23/>`_

.. enunciation::

   Construct a :term:`solid angle <G.524>` out of three :term:`plane angles <G.22>` two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four :term:`right angles <G.33>`.

.. signature:: problem

   | :fn:`construct_solid_angle <G.528>`\ (:g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>`) → :g:`/ O R / <g2:/ O R />`, :g:`/ B C / <g3:/ B C />`
   | **given** :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` be the three given plane angles, let two of these, taken together in any manner, be greater than the remaining one, while, further, the three are less than four right angles
   | **construct** If then we cut off :g:`/ O R / <g2:/ O R />` :eq:`= <g2:/ O R / = g3:/ B C />` to :g:`/ B C / <g3:/ B C />`, the square on :g:`/ A B / <g3:/ A B />` will be greater than the square on :g:`/ L O / <g2:/ L O />` by the square on :g:`/ O R / <g2:/ O R />`

.. picture:: g1.svg
   :alt: Proposition 23, Figure 1

.. picture:: g2.svg
   :alt: Proposition 23, Figure 2

.. picture:: g3.svg
   :alt: Proposition 23, Lemma

.. step:: given

   :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` be the three given plane angles, let two of these, taken together in any manner, be greater than the remaining one, while, further, the three are less than four right angles

.. step:: construct

   Let :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`, :g:`/ G H / <g1:/ G H />`, :g:`/ H K / <g1:/ H K />` be cut off :eq:`equal <g1:/ A B / = g1:/ B C / = g1:/ D E / = g1:/ E F / = g1:/ G H / = g1:/ H K />` to one another

.. step:: construct

   :fn:`segment <G.14>`\ (:g:`A <g1:A>`, :g:`C <g1:C>`) → :g:`/ A C / <g1:/ A C />`, :fn:`segment <G.14>`\ (:g:`D <g1:D>`, :g:`F <g1:F>`) → :g:`/ D F / <g1:/ D F />`, :fn:`segment <G.14>`\ (:g:`G <g1:G>`, :g:`K <g1:K>`) → :g:`/ G K / <g1:/ G K />`

.. step:: assert ∵ there_plane_angles <G.527>

   It is therefore possible to construct a :term:`triangle <G.12>` out of :term:`segments <G.4>` equal to :g:`/ A C / <g1:/ A C />`, :g:`/ D F / <g1:/ D F />`, :g:`/ G K / <g1:/ G K />`

.. step:: construct

   Let :g:`< L M N > <g2:< L M N >>` be so constructed that :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g2:/ L M /; g1:/ D F / = g2:/ M N /; g1:/ G K / = g2:/ N L />` to :g:`/ L M / <g2:/ L M />`, :g:`/ D F / <g1:/ D F />` to :g:`/ M N / <g2:/ M N />`, and further :g:`/ G K / <g1:/ G K />` to :g:`/ N L / <g2:/ N L />`, let :g:`( L M N ) <g2:( L M N )>` be described about :g:`< L M N > <g2:< L M N >>`

.. step:: construct

   Let its :term:`center <G.11>` be taken

.. step:: assert

   Let it be :g:`O <g2:O>`

.. step:: construct

   :fn:`segment <G.14>`\ (:g:`L <g2:L>`, :g:`O <g2:O>`) → :g:`/ L O / <g2:/ L O />`, :fn:`segment <G.14>`\ (:g:`M <g2:M>`, :g:`O <g2:O>`) → :g:`/ M O / <g2:/ M O />`, :fn:`segment <G.14>`\ (:g:`N <g2:N>`, :g:`O <g2:O>`) → :g:`/ N O / <g2:/ N O />`

.. step:: assert

   If not, :g:`/ A B / <g1:/ A B />` is either :eq:`= <g1:/ A B / = g2:/ L O />` to :g:`/ L O / <g2:/ L O />`, or less

.. step:: assert

   First, let it be :eq:`= <g1:/ A B / = g2:/ L O />`

.. step:: assert

   :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g2:/ L O />` :g:`/ L O / <g2:/ L O />`, while :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ B C /; g2:/ O L / = g2:/ O M />` :g:`/ B C / <g1:/ B C />`, and :g:`/ O L / <g2:/ O L />` to :g:`/ O M / <g2:/ O M />`, :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ A B / = g2:/ L O /; g1:/ B C / = g2:/ O M />` :g:`/ L O / <g2:/ L O />`, :g:`/ O M / <g2:/ O M />`; and, by hypothesis, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g2:/ L M />` :g:`/ L M / <g2:/ L M />`

.. step:: assert ∵ sss_congruence <G.29>

   :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g2:< L O M )>` :g:`< L O M ) <g2:< L O M )>`

.. step:: assert

   For the same reason :g:`< D E F ) <g1:< D E F )>` :eq:`= <g1:< D E F ) = g2:< M O N ); g1:< G H K ) = g2:< N O L )>` :g:`< M O N ) <g2:< M O N )>`, and further :g:`< G H K ) <g1:< G H K )>` to :g:`< N O L ) <g2:< N O L )>`

.. step:: assert

   the three angles :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` :eq:`= <g1:< A B C ) = g2:< L O M ); g1:< D E F ) = g2:< M O N ); g1:< G H K ) = g2:< N O L )>` the three angles :g:`< L O M ) <g2:< L O M )>`, :g:`< M O N ) <g2:< M O N )>`, :g:`< N O L ) <g2:< N O L )>`

.. step:: assert

   The three angles :g:`< L O M ) <g2:< L O M )>`, :g:`< M O N ) <g2:< M O N )>`, :g:`< N O L ) <g2:< N O L )>` are equal to four right angles

.. step:: assert

   :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` are equal to four right angles

.. step:: assert

   They are also, by hypothesis, less than four right angles ⇒⇐

.. step:: assert

   :g:`/ A B / <g1:/ A B />` is not equal to :g:`/ L O / <g2:/ L O />`

.. step:: assert

   I say next that neither is :g:`/ A B / <g1:/ A B />` less than :g:`/ L O / <g2:/ L O />`

.. step:: construct

   If possible, let it be so, and let :g:`/ O P / <g2:/ O P />` be made :eq:`equal <g2:/ O P / = g1:/ A B />` to :g:`/ A B / <g1:/ A B />`, and :g:`/ O Q / <g2:/ O Q />` :eq:`equal <g2:/ O Q / = g1:/ B C />` to :g:`/ B C / <g1:/ B C />`, and let :g:`/ P Q / <g2:/ P Q />` be joined.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ B C />` :g:`/ B C / <g1:/ B C />`, :g:`/ O P / <g2:/ O P />` :eq:`= <g2:/ O P / = g2:/ O Q />` :g:`/ O Q / <g2:/ O Q />`, so that :g:`/ L P / <g2:/ L P />` :eq:`= <g2:/ L P / = g2:/ Q M />` :g:`/ Q M / <g2:/ Q M />`

.. step:: assert ∵ segment_drawn_parallel, parallel_transversal_angles, equiangular_triangles_sides, magnitudes_proportional_proportional <G.211, G.56, G.213, G.195>

   :g:`/ L M / <g2:/ L M />` is parallel to :g:`/ P Q / <g2:/ P Q />`, and :g:`< L M O > <g2:< L M O >>` is equiangular with :g:`< P Q O > <g2:< P Q O >>`; therefore, as :g:`/ O L / <g2:/ O L />` is to :g:`/ L M / <g2:/ L M />`, so is :g:`/ O P / <g2:/ O P />` to :g:`/ P Q / <g2:/ P Q />`; and alternately, as :g:`/ L O / <g2:/ L O />` is to :g:`/ O P / <g2:/ O P />`, so is :g:`/ L M / <g2:/ L M />` to :g:`/ P Q / <g2:/ P Q />`

.. step:: assert

   :g:`/ L O / <g2:/ L O />` > :g:`/ O P / <g2:/ O P />`

.. step:: assert

   :g:`/ L M / <g2:/ L M />` is also greater than :g:`/ P Q / <g2:/ P Q />`

.. step:: assert

   :g:`/ L M / <g2:/ L M />` was made :eq:`= <g2:/ L M / = g1:/ A C />` to :g:`/ A C / <g1:/ A C />`

.. step:: assert

   :g:`/ A C / <g1:/ A C />` is also greater than :g:`/ P Q / <g2:/ P Q />`

.. step:: assert

   Since, then, :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ A B / = g2:/ P O /; g1:/ B C / = g2:/ O Q />` :g:`/ P O / <g2:/ P O />`, :g:`/ O Q / <g2:/ O Q />`, and :g:`/ A C / <g1:/ A C />` > :g:`/ P Q / <g2:/ P Q />`,

.. step:: assert ∵ converse_hinge_theorem <G.50>

   :g:`< A B C ) <g1:< A B C )>` > :g:`< P O Q ) <g2:< P O Q )>`

.. step:: assert

   Similarly we can prove that :g:`< D E F ) <g1:< D E F )>` is also greater than :g:`< M O N ) <g2:< M O N )>`, and :g:`< G H K ) <g1:< G H K )>` greater than :g:`< N O L ) <g2:< N O L )>`

.. step:: assert

   the three angles :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` are greater than the three angles :g:`< L O M ) <g2:< L O M )>`, :g:`< M O N ) <g2:< M O N )>`, :g:`< N O L ) <g2:< N O L )>`

.. step:: assert

   But, by hypothesis, :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` are less than four right angles

.. step:: assert

   :g:`< L O M ) <g2:< L O M )>`, :g:`< M O N ) <g2:< M O N )>`, :g:`< N O L ) <g2:< N O L )>` are much less than four right angles

.. step:: assert

   They are also equal to four right angles:

.. step:: assert

   ⇒⇐ Therefore :g:`/ A B / <g1:/ A B />` is not less than :g:`/ L O / <g2:/ L O />`

.. step:: assert

   It was proved that neither is it equal

.. step:: assert

   :g:`/ A B / <g1:/ A B />` > :g:`/ L O / <g2:/ L O />`

.. step:: construct

   :fn:`set_segment_right <G.514>`: Let then :g:`/ O R / <g2:/ O R />` be set up from :g:`O <g2:O>` at right angles to the plane of :g:`( L M N ) <g2:( L M N )>`, and let the square on :g:`/ O R / <g2:/ O R />` be equal to that area by which the square on :g:`/ A B / <g1:/ A B />` is greater than the square on :g:`/ L O / <g2:/ L O />`

.. step:: construct

   :fn:`segment <G.14>`\ (:g:`R <g2:R>`, :g:`L <g2:L>`) → :g:`/ R L / <g2:/ R L />`, :fn:`segment <G.14>`\ (:g:`R <g2:R>`, :g:`M <g2:M>`) → :g:`/ R M / <g2:/ R M />`, :fn:`segment <G.14>`\ (:g:`R <g2:R>`, :g:`N <g2:N>`) → :g:`/ R N / <g2:/ R N />`

.. step:: assert

   :g:`/ R O / <g2:/ R O />` is at right angles to the plane of :g:`( L M N ) <g2:( L M N )>`,

.. step:: assert

   :g:`/ R O / <g2:/ R O />` is also at right angles to each of :g:`/ L O / <g2:/ L O />`, :g:`/ M O / <g2:/ M O />`, :g:`/ N O / <g2:/ N O />`

.. step:: assert

   since :g:`/ L O / <g2:/ L O />` :eq:`= <g2:/ L O / = g2:/ O M />` :g:`/ O M / <g2:/ O M />`, while :g:`/ O R / <g2:/ O R />` is common and at right angles,

.. step:: assert ∵ sas_congruence <G.24>

   :g:`/ R L / <g2:/ R L />` :eq:`= <g2:/ R L / = g2:/ R M />` :g:`/ R M / <g2:/ R M />`

.. step:: assert

   For the same reason :g:`/ R N / <g2:/ R N />` :eq:`= <g2:/ R N / = g2:/ R L / = g2:/ R M />` each of :g:`/ R L / <g2:/ R L />`, :g:`/ R M / <g2:/ R M />`

.. step:: assert

   :g:`/ R L / <g2:/ R L />`, :g:`/ R M / <g2:/ R M />`, :g:`/ R N / <g2:/ R N />` :eq:`= <g2:/ R L / = g2:/ R M / = g2:/ R N />`

.. step:: assert

   Next, since by hypothesis the :term:`square <G.63>` on :g:`/ O R / <g2:/ O R />` is equal to that area by which the square on :g:`/ A B / <g1:/ A B />` > the square on :g:`/ L O / <g2:/ L O />`,

.. step:: assert

   the square on :g:`/ A B / <g1:/ A B />` is equal to the squares on :g:`/ L O / <g2:/ L O />`, :g:`/ O R / <g2:/ O R />`

.. step:: assert ∵ pythagorean_theorem <G.79>

   The square on :g:`/ L R / <g2:/ L R />` is equal to the squares on :g:`/ L O / <g2:/ L O />`, :g:`/ O R / <g2:/ O R />`, for :g:`< L O R ) <g2:< L O R )>` is right

.. step:: assert

   the square on :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g2:/ R L />` the square on :g:`/ R L / <g2:/ R L />`; therefore :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g2:/ R L />` :g:`/ R L / <g2:/ R L />`

.. step:: assert

   Each of :g:`/ B C / <g1:/ B C />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`, :g:`/ G H / <g1:/ G H />`, :g:`/ H K / <g1:/ H K />` :eq:`= <g1:/ B C / = g1:/ D E / = g1:/ E F / = g1:/ G H / = g1:/ H K / = g1:/ A B />` :g:`/ A B / <g1:/ A B />`, while each of :g:`/ R M / <g2:/ R M />`, :g:`/ R N / <g2:/ R N />` :eq:`= <g2:/ R M / = g2:/ R N / = g2:/ R L />` :g:`/ R L / <g2:/ R L />`

.. step:: assert

   each of :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`, :g:`/ G H / <g1:/ G H />`, :g:`/ H K / <g1:/ H K />` :eq:`= <g1:/ A B / = g1:/ B C / = g1:/ D E / = g1:/ E F / = g1:/ G H / = g1:/ H K / = g2:/ R L / = g2:/ R M / = g2:/ R N />` each of :g:`/ R L / <g2:/ R L />`, :g:`/ R M / <g2:/ R M />`, :g:`/ R N / <g2:/ R N />`

.. step:: assert

   since :g:`/ L R / <g2:/ L R />`, :g:`/ R M / <g2:/ R M />` :eq:`= <g2:/ L R / = g1:/ A B /; g2:/ R M / = g1:/ B C />` :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, and :g:`/ L M / <g2:/ L M />` is by hypothesis :eq:`= <g2:/ L M / = g1:/ A C />` to :g:`/ A C / <g1:/ A C />`,

.. step:: assert ∵ sss_congruence <G.29>

   :g:`< L R M ) <g2:< L R M )>` :eq:`= <g2:< L R M ) = g1:< A B C )>` :g:`< A B C ) <g1:< A B C )>`

.. step:: assert

   For the same reason

.. step:: assert

   :g:`< M R N ) <g2:< M R N )>` :eq:`= <g2:< M R N ) = g1:< D E F ); g2:< L R N ) = g1:< G H K )>` :g:`< D E F ) <g1:< D E F )>`, and :g:`< L R N ) <g2:< L R N )>` to :g:`< G H K ) <g1:< G H K )>`

.. step:: assert

   out of the three plane angles :g:`< L R M ) <g2:< L R M )>`, :g:`< M R N ) <g2:< M R N )>`, :g:`< L R N ) <g2:< L R N )>`, which :eq:`= <g2:< L R M ) = g1:< A B C ); g2:< M R N ) = g1:< D E F ); g2:< L R N ) = g1:< G H K )>` the three given angles :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>`, the solid angle at :g:`R <g2:R>` has been constructed, which is contained by :g:`< L R M ) <g2:< L R M )>`, :g:`< M R N ) <g2:< M R N )>`, :g:`< L R N ) <g2:< L R N )>`

.. step:: assert

   LEMMA. ~~~~~~

.. step:: assert

   How it is possible to take the square on :g:`/ O R / <g2:/ O R />` equal to that area by which the square on :g:`/ A B / <g3:/ A B />` > the square on :g:`/ L O / <g2:/ L O />`, we can show as follows

.. step:: assert

   Let :g:`/ A B / <g3:/ A B />`, :g:`/ L O / <g2:/ L O />` be set out, and let :g:`/ A B / <g3:/ A B />` be the greater

.. step:: construct

   :fn:`fit_chord_in_circle <G.147>`: Let the semicircle :g:`( A B C ) <g3:( A B C )>` be described on :g:`/ A B / <g3:/ A B />`, and into the semicircle :g:`( A B C ) <g3:( A B C )>` let :g:`/ A C / <g3:/ A C />` be fitted :eq:`equal <g3:/ A C / = g2:/ L O />` to :g:`/ L O / <g2:/ L O />`, not being greater than the diameter :g:`/ A B / <g3:/ A B />`

.. step:: construct

   :fn:`segment <G.14>`\ (:g:`C <g3:C>`, :g:`B <g3:B>`) → :g:`/ C B / <g3:/ C B />`

.. step:: assert

   then :g:`< A C B ) <g3:< A C B )>` is an :term:`angle in the semicircle <G.138>` :g:`( A C B ) <g3:( A C B )>`,

.. step:: assert ∵ thales_semicircle_theorem <G.139>

   :g:`< A C B ) <g3:< A C B )>` is right

.. step:: assert ∵ pythagorean_theorem <G.79>

   the square on :g:`/ A B / <g3:/ A B />` is equal to the squares on :g:`/ A C / <g3:/ A C />`, :g:`/ C B / <g3:/ C B />`

.. step:: assert

   the square on :g:`/ A B / <g3:/ A B />` > the square on :g:`/ A C / <g3:/ A C />` by the square on :g:`/ C B / <g3:/ C B />`

.. step:: assert

   :g:`/ A C / <g3:/ A C />` :eq:`= <g3:/ A C / = g2:/ L O />` :g:`/ L O / <g2:/ L O />`

.. step:: assert

   the square on :g:`/ A B / <g3:/ A B />` > the square on :g:`/ L O / <g2:/ L O />` by the square on :g:`/ C B / <g3:/ C B />`

.. step:: conclude

   If then we cut off :g:`/ O R / <g2:/ O R />` :eq:`= <g2:/ O R / = g3:/ B C />` to :g:`/ B C / <g3:/ B C />`, the square on :g:`/ A B / <g3:/ A B />` will be greater than the square on :g:`/ L O / <g2:/ L O />` by the square on :g:`/ O R / <g2:/ O R />`

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
     "G.35" [label="G.35", tooltip="G.35 (I.12): Construct a perpendicular to a given line from a given point not on it.", fillcolor="#222244", URL="../G.35/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.36/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.13): A segment standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.14): If two segments at a point on a line on opposite sides make adjacent angles summing to two right angles, the two segments are collinear.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.17): In any triangle, the sum of any two angles is less than two right angles.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.43" [label="G.43", tooltip="G.43 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.43/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.24): If two triangles have two sides equal to two sides respectively, the one with the greater included angle has the greater base.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.25): If two triangles have two sides equal to two sides respectively, the one with the greater base has the greater included angle.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.def.23): Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.52/index.html", target="_top"];
     "G.53" [label="G.53", tooltip="G.53 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.53/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.28): If a transversal cutting two lines makes the exterior angle equal to the opposite interior angle, or interior angles on the same side supplementary, the lines are parallel.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.55/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.56/index.html", target="_top"];
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
     "G.75" [label="G.75", tooltip="G.75 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.75/index.html", target="_top"];
     "G.76" [label="G.76", tooltip="G.76 (I.def.11): An obtuse angle is greater than a right angle.", fillcolor="#224422", URL="../G.76/index.html", target="_top"];
     "G.77" [label="G.77", tooltip="G.77 (I.def.12): An acute angle is less than a right angle.", fillcolor="#224422", URL="../G.77/index.html", target="_top"];
     "G.78" [label="G.78", tooltip="G.78 (I.def.21): A right-angled triangle has a right angle, an obtuse-angled triangle has an obtuse angle, and an acute-angled triangle has three acute angles.", fillcolor="#224422", URL="../G.78/index.html", target="_top"];
     "G.79" [label="G.79", tooltip="G.79 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.79/index.html", target="_top"];
     "G.96" [label="G.96", tooltip="G.96 (I.def.18): A semicircle is the figure contained by a diameter and the arc cut off by it.", fillcolor="#224422", URL="../G.96/index.html", target="_top"];
     "G.122" [label="G.122", tooltip="G.122 (III.def.10): Asector of a circle is thefigure which, when anangle is constructed at thecenter of thecircle, is contained by thesegments containing the angle and the arc cut off by them.", fillcolor="#224422", URL="../G.122/index.html", target="_top"];
     "G.123" [label="G.123", tooltip="G.123 (III.20): In a circle the angle at the center is double of the angle at the arc, when the angles have the same arc as base.", fillcolor="#222244", URL="../G.123/index.html", target="_top"];
     "G.124" [label="G.124", tooltip="G.124 (III.21): In a circle the angles in the same segment are equal.", fillcolor="#222244", URL="../G.124/index.html", target="_top"];
     "G.125" [label="G.125", tooltip="G.125 (III.22): The opposite angles of quadrilaterals in circles are equal to two right angles.", fillcolor="#222244", URL="../G.125/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (III.def.8): Anangle in a segment is theangle which, when apoint is taken on the arc of the segment andsegments are joined from it to theextremities of the segment which is thebase of the segme...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.139" [label="G.139", tooltip="G.139 (III.31): In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of...", fillcolor="#222244", URL="../G.139/index.html", target="_top"];
     "G.146" [label="G.146", tooltip="G.146 (IV.def.7): Asegment is said to befitted into a circle when itsextremities are on the arc of thecircle.", fillcolor="#224422", URL="../G.146/index.html", target="_top"];
     "G.147" [label="G.147", tooltip="G.147 (IV.1): Into a given circle to fit a segment equal to a given segment which is not greater than the diameter of the circle.", fillcolor="#222244", URL="../G.147/index.html", target="_top"];
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
     "G.202" [label="G.202", tooltip="G.202 (V.20): If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and if ex aequali the first be greater than the third, the fourt...", fillcolor="#222244", URL="../G.202/index.html", target="_top"];
     "G.205" [label="G.205", tooltip="G.205 (V.22): If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.205/index.html", target="_top"];
     "G.209" [label="G.209", tooltip="G.209 (VI.def.4): The height of anyfigure is theperpendicular drawn from the vertex to the base.", fillcolor="#224422", URL="../G.209/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.210/index.html", target="_top"];
     "G.211" [label="G.211", tooltip="G.211 (VI.2): If a segment be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionally, the...", fillcolor="#222244", URL="../G.211/index.html", target="_top"];
     "G.213" [label="G.213", tooltip="G.213 (VI.4): In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.", fillcolor="#222244", URL="../G.213/index.html", target="_top"];
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
     "G.513" [label="G.513", tooltip="G.513 (XI.11): From a given elevated point to draw a segment perpendicular to a given plane.", fillcolor="#222244", URL="../G.513/index.html", target="_top"];
     "G.514" [label="G.514", tooltip="G.514 (XI.12): To set up a segment at right angles to a given plane from a given point in it.", fillcolor="#222244", URL="../G.514/index.html", target="_top"];
     "G.524" [label="G.524", tooltip="G.524 (XI.def.11): Asolid angle is the inclination constituted by more than twolines which meet one another and are not in the samesurface, towards all the lines. Otherwise: Asolid angle is that whic...", fillcolor="#224422", URL="../G.524/index.html", target="_top"];
     "G.527" [label="G.527", tooltip="G.527 (XI.22): If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal segments, it is possible to construct...", fillcolor="#222244", URL="../G.527/index.html", target="_top"];
     "G.528" [label="G.528", tooltip="G.528 (XI.23): Construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.35" -> "G.1";
     "G.37" -> "G.1";
     "G.39" -> "G.1";
     "G.40" -> "G.1";
     "G.45" -> "G.1";
     "G.47" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
     "G.58" -> "G.1";
     "G.59" -> "G.1";
     "G.68" -> "G.1";
     "G.75" -> "G.1";
     "G.79" -> "G.1";
     "G.138" -> "G.1";
     "G.211" -> "G.1";
     "G.506" -> "G.1";
     "G.509" -> "G.1";
     "G.513" -> "G.1";
     "G.514" -> "G.1";
     "G.524" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.7" -> "G.2";
     "G.18" -> "G.2";
     "G.22" -> "G.2";
     "G.30" -> "G.2";
     "G.33" -> "G.2";
     "G.34" -> "G.2";
     "G.35" -> "G.2";
     "G.37" -> "G.2";
     "G.39" -> "G.2";
     "G.40" -> "G.2";
     "G.48" -> "G.2";
     "G.52" -> "G.2";
     "G.53" -> "G.2";
     "G.54" -> "G.2";
     "G.55" -> "G.2";
     "G.56" -> "G.2";
     "G.58" -> "G.2";
     "G.65" -> "G.2";
     "G.211" -> "G.2";
     "G.504" -> "G.2";
     "G.509" -> "G.2";
     "G.524" -> "G.2";
     "G.4" -> "G.3";
     "G.6" -> "G.3";
     "G.8" -> "G.3";
     "G.20" -> "G.3";
     "G.28" -> "G.3";
     "G.29" -> "G.3";
     "G.60" -> "G.3";
     "G.65" -> "G.3";
     "G.138" -> "G.3";
     "G.146" -> "G.3";
     "G.504" -> "G.3";
     "G.527" -> "G.3";
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
     "G.35" -> "G.4";
     "G.37" -> "G.4";
     "G.39" -> "G.4";
     "G.40" -> "G.4";
     "G.41" -> "G.4";
     "G.47" -> "G.4";
     "G.48" -> "G.4";
     "G.49" -> "G.4";
     "G.50" -> "G.4";
     "G.52" -> "G.4";
     "G.53" -> "G.4";
     "G.54" -> "G.4";
     "G.55" -> "G.4";
     "G.56" -> "G.4";
     "G.58" -> "G.4";
     "G.59" -> "G.4";
     "G.60" -> "G.4";
     "G.61" -> "G.4";
     "G.62" -> "G.4";
     "G.65" -> "G.4";
     "G.68" -> "G.4";
     "G.75" -> "G.4";
     "G.79" -> "G.4";
     "G.122" -> "G.4";
     "G.123" -> "G.4";
     "G.124" -> "G.4";
     "G.138" -> "G.4";
     "G.139" -> "G.4";
     "G.146" -> "G.4";
     "G.147" -> "G.4";
     "G.211" -> "G.4";
     "G.213" -> "G.4";
     "G.502" -> "G.4";
     "G.503" -> "G.4";
     "G.504" -> "G.4";
     "G.505" -> "G.4";
     "G.506" -> "G.4";
     "G.509" -> "G.4";
     "G.510" -> "G.4";
     "G.513" -> "G.4";
     "G.514" -> "G.4";
     "G.527" -> "G.4";
     "G.528" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.524" -> "G.5";
     "G.10" -> "G.6";
     "G.138" -> "G.6";
     "G.146" -> "G.6";
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
     "G.513" -> "G.7";
     "G.514" -> "G.7";
     "G.524" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.12" -> "G.9";
     "G.66" -> "G.9";
     "G.67" -> "G.9";
     "G.96" -> "G.9";
     "G.122" -> "G.9";
     "G.187" -> "G.9";
     "G.188" -> "G.9";
     "G.189" -> "G.9";
     "G.209" -> "G.9";
     "G.11" -> "G.10";
     "G.15" -> "G.10";
     "G.17" -> "G.10";
     "G.20" -> "G.10";
     "G.21" -> "G.10";
     "G.35" -> "G.10";
     "G.47" -> "G.10";
     "G.61" -> "G.10";
     "G.96" -> "G.10";
     "G.122" -> "G.10";
     "G.123" -> "G.10";
     "G.124" -> "G.10";
     "G.125" -> "G.10";
     "G.139" -> "G.10";
     "G.146" -> "G.10";
     "G.147" -> "G.10";
     "G.502" -> "G.10";
     "G.15" -> "G.11";
     "G.17" -> "G.11";
     "G.20" -> "G.11";
     "G.21" -> "G.11";
     "G.35" -> "G.11";
     "G.47" -> "G.11";
     "G.61" -> "G.11";
     "G.96" -> "G.11";
     "G.122" -> "G.11";
     "G.123" -> "G.11";
     "G.124" -> "G.11";
     "G.502" -> "G.11";
     "G.528" -> "G.11";
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
     "G.42" -> "G.12";
     "G.43" -> "G.12";
     "G.44" -> "G.12";
     "G.45" -> "G.12";
     "G.47" -> "G.12";
     "G.48" -> "G.12";
     "G.49" -> "G.12";
     "G.50" -> "G.12";
     "G.51" -> "G.12";
     "G.53" -> "G.12";
     "G.59" -> "G.12";
     "G.60" -> "G.12";
     "G.62" -> "G.12";
     "G.63" -> "G.12";
     "G.64" -> "G.12";
     "G.66" -> "G.12";
     "G.67" -> "G.12";
     "G.68" -> "G.12";
     "G.70" -> "G.12";
     "G.78" -> "G.12";
     "G.79" -> "G.12";
     "G.125" -> "G.12";
     "G.139" -> "G.12";
     "G.210" -> "G.12";
     "G.211" -> "G.12";
     "G.213" -> "G.12";
     "G.503" -> "G.12";
     "G.527" -> "G.12";
     "G.528" -> "G.12";
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
     "G.35" -> "G.14";
     "G.41" -> "G.14";
     "G.43" -> "G.14";
     "G.45" -> "G.14";
     "G.47" -> "G.14";
     "G.49" -> "G.14";
     "G.51" -> "G.14";
     "G.58" -> "G.14";
     "G.60" -> "G.14";
     "G.65" -> "G.14";
     "G.68" -> "G.14";
     "G.70" -> "G.14";
     "G.79" -> "G.14";
     "G.123" -> "G.14";
     "G.124" -> "G.14";
     "G.125" -> "G.14";
     "G.139" -> "G.14";
     "G.147" -> "G.14";
     "G.210" -> "G.14";
     "G.211" -> "G.14";
     "G.503" -> "G.14";
     "G.510" -> "G.14";
     "G.527" -> "G.14";
     "G.528" -> "G.14";
     "G.17" -> "G.15";
     "G.20" -> "G.15";
     "G.21" -> "G.15";
     "G.35" -> "G.15";
     "G.47" -> "G.15";
     "G.147" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.16";
     "G.21" -> "G.16";
     "G.37" -> "G.16";
     "G.39" -> "G.16";
     "G.40" -> "G.16";
     "G.56" -> "G.16";
     "G.64" -> "G.16";
     "G.65" -> "G.16";
     "G.68" -> "G.16";
     "G.20" -> "G.17";
     "G.31" -> "G.17";
     "G.32" -> "G.17";
     "G.34" -> "G.17";
     "G.20" -> "G.18";
     "G.25" -> "G.18";
     "G.41" -> "G.18";
     "G.42" -> "G.18";
     "G.45" -> "G.18";
     "G.58" -> "G.18";
     "G.59" -> "G.18";
     "G.66" -> "G.18";
     "G.67" -> "G.18";
     "G.123" -> "G.18";
     "G.210" -> "G.18";
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
     "G.75" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.29" -> "G.22";
     "G.30" -> "G.22";
     "G.31" -> "G.22";
     "G.32" -> "G.22";
     "G.33" -> "G.22";
     "G.34" -> "G.22";
     "G.35" -> "G.22";
     "G.37" -> "G.22";
     "G.39" -> "G.22";
     "G.40" -> "G.22";
     "G.41" -> "G.22";
     "G.42" -> "G.22";
     "G.43" -> "G.22";
     "G.44" -> "G.22";
     "G.45" -> "G.22";
     "G.48" -> "G.22";
     "G.49" -> "G.22";
     "G.50" -> "G.22";
     "G.51" -> "G.22";
     "G.53" -> "G.22";
     "G.54" -> "G.22";
     "G.55" -> "G.22";
     "G.56" -> "G.22";
     "G.58" -> "G.22";
     "G.59" -> "G.22";
     "G.60" -> "G.22";
     "G.62" -> "G.22";
     "G.63" -> "G.22";
     "G.64" -> "G.22";
     "G.75" -> "G.22";
     "G.76" -> "G.22";
     "G.77" -> "G.22";
     "G.78" -> "G.22";
     "G.79" -> "G.22";
     "G.122" -> "G.22";
     "G.123" -> "G.22";
     "G.124" -> "G.22";
     "G.125" -> "G.22";
     "G.138" -> "G.22";
     "G.139" -> "G.22";
     "G.213" -> "G.22";
     "G.524" -> "G.22";
     "G.527" -> "G.22";
     "G.528" -> "G.22";
     "G.24" -> "G.23";
     "G.29" -> "G.23";
     "G.25" -> "G.24";
     "G.32" -> "G.24";
     "G.41" -> "G.24";
     "G.49" -> "G.24";
     "G.50" -> "G.24";
     "G.51" -> "G.24";
     "G.60" -> "G.24";
     "G.62" -> "G.24";
     "G.64" -> "G.24";
     "G.79" -> "G.24";
     "G.506" -> "G.24";
     "G.527" -> "G.24";
     "G.528" -> "G.24";
     "G.28" -> "G.25";
     "G.44" -> "G.25";
     "G.45" -> "G.25";
     "G.49" -> "G.25";
     "G.123" -> "G.25";
     "G.139" -> "G.25";
     "G.28" -> "G.26";
     "G.41" -> "G.26";
     "G.45" -> "G.26";
     "G.29" -> "G.28";
     "G.31" -> "G.29";
     "G.34" -> "G.29";
     "G.35" -> "G.29";
     "G.48" -> "G.29";
     "G.506" -> "G.29";
     "G.528" -> "G.29";
     "G.31" -> "G.30";
     "G.48" -> "G.30";
     "G.32" -> "G.31";
     "G.35" -> "G.32";
     "G.41" -> "G.32";
     "G.34" -> "G.33";
     "G.35" -> "G.33";
     "G.37" -> "G.33";
     "G.38" -> "G.33";
     "G.39" -> "G.33";
     "G.40" -> "G.33";
     "G.42" -> "G.33";
     "G.54" -> "G.33";
     "G.55" -> "G.33";
     "G.56" -> "G.33";
     "G.59" -> "G.33";
     "G.75" -> "G.33";
     "G.76" -> "G.33";
     "G.77" -> "G.33";
     "G.78" -> "G.33";
     "G.79" -> "G.33";
     "G.125" -> "G.33";
     "G.139" -> "G.33";
     "G.209" -> "G.33";
     "G.211" -> "G.33";
     "G.505" -> "G.33";
     "G.506" -> "G.33";
     "G.510" -> "G.33";
     "G.513" -> "G.33";
     "G.514" -> "G.33";
     "G.528" -> "G.33";
     "G.37" -> "G.34";
     "G.75" -> "G.34";
     "G.513" -> "G.34";
     "G.513" -> "G.35";
     "G.37" -> "G.36";
     "G.56" -> "G.36";
     "G.62" -> "G.36";
     "G.64" -> "G.36";
     "G.79" -> "G.36";
     "G.39" -> "G.37";
     "G.40" -> "G.37";
     "G.42" -> "G.37";
     "G.54" -> "G.37";
     "G.56" -> "G.37";
     "G.59" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.38";
     "G.79" -> "G.39";
     "G.41" -> "G.40";
     "G.54" -> "G.40";
     "G.56" -> "G.40";
     "G.506" -> "G.40";
     "G.43" -> "G.41";
     "G.51" -> "G.41";
     "G.53" -> "G.41";
     "G.139" -> "G.42";
     "G.213" -> "G.42";
     "G.44" -> "G.43";
     "G.45" -> "G.44";
     "G.49" -> "G.44";
     "G.47" -> "G.45";
     "G.48" -> "G.47";
     "G.49" -> "G.48";
     "G.58" -> "G.48";
     "G.50" -> "G.49";
     "G.527" -> "G.49";
     "G.528" -> "G.50";
     "G.62" -> "G.51";
     "G.506" -> "G.51";
     "G.53" -> "G.52";
     "G.54" -> "G.52";
     "G.56" -> "G.52";
     "G.58" -> "G.52";
     "G.59" -> "G.52";
     "G.60" -> "G.52";
     "G.62" -> "G.52";
     "G.64" -> "G.52";
     "G.65" -> "G.52";
     "G.66" -> "G.52";
     "G.67" -> "G.52";
     "G.68" -> "G.52";
     "G.70" -> "G.52";
     "G.75" -> "G.52";
     "G.79" -> "G.52";
     "G.211" -> "G.52";
     "G.213" -> "G.52";
     "G.509" -> "G.52";
     "G.510" -> "G.52";
     "G.513" -> "G.52";
     "G.54" -> "G.53";
     "G.58" -> "G.53";
     "G.60" -> "G.53";
     "G.213" -> "G.54";
     "G.56" -> "G.55";
     "G.213" -> "G.55";
     "G.59" -> "G.56";
     "G.60" -> "G.56";
     "G.62" -> "G.56";
     "G.64" -> "G.56";
     "G.75" -> "G.56";
     "G.510" -> "G.56";
     "G.528" -> "G.56";
     "G.59" -> "G.58";
     "G.66" -> "G.58";
     "G.67" -> "G.58";
     "G.68" -> "G.58";
     "G.75" -> "G.58";
     "G.79" -> "G.58";
     "G.513" -> "G.58";
     "G.514" -> "G.58";
     "G.123" -> "G.59";
     "G.125" -> "G.59";
     "G.139" -> "G.59";
     "G.65" -> "G.60";
     "G.62" -> "G.61";
     "G.66" -> "G.61";
     "G.67" -> "G.61";
     "G.70" -> "G.61";
     "G.96" -> "G.61";
     "G.139" -> "G.61";
     "G.147" -> "G.61";
     "G.502" -> "G.61";
     "G.64" -> "G.62";
     "G.65" -> "G.62";
     "G.66" -> "G.62";
     "G.67" -> "G.62";
     "G.70" -> "G.62";
     "G.75" -> "G.62";
     "G.213" -> "G.62";
     "G.64" -> "G.63";
     "G.75" -> "G.63";
     "G.79" -> "G.63";
     "G.528" -> "G.63";
     "G.65" -> "G.64";
     "G.66" -> "G.64";
     "G.67" -> "G.65";
     "G.68" -> "G.66";
     "G.70" -> "G.66";
     "G.210" -> "G.67";
     "G.211" -> "G.67";
     "G.211" -> "G.68";
     "G.79" -> "G.70";
     "G.210" -> "G.70";
     "G.79" -> "G.75";
     "G.78" -> "G.76";
     "G.78" -> "G.77";
     "G.79" -> "G.78";
     "G.528" -> "G.79";
     "G.139" -> "G.96";
     "G.123" -> "G.122";
     "G.124" -> "G.123";
     "G.125" -> "G.124";
     "G.139" -> "G.125";
     "G.139" -> "G.138";
     "G.528" -> "G.138";
     "G.528" -> "G.139";
     "G.147" -> "G.146";
     "G.528" -> "G.147";
     "G.170" -> "G.169";
     "G.253" -> "G.169";
     "G.171" -> "G.170";
     "G.172" -> "G.170";
     "G.175" -> "G.170";
     "G.176" -> "G.170";
     "G.177" -> "G.170";
     "G.183" -> "G.170";
     "G.185" -> "G.170";
     "G.186" -> "G.170";
     "G.189" -> "G.170";
     "G.190" -> "G.170";
     "G.191" -> "G.170";
     "G.193" -> "G.170";
     "G.195" -> "G.170";
     "G.205" -> "G.170";
     "G.210" -> "G.170";
     "G.186" -> "G.171";
     "G.190" -> "G.171";
     "G.175" -> "G.172";
     "G.174" -> "G.173";
     "G.188" -> "G.173";
     "G.189" -> "G.173";
     "G.175" -> "G.174";
     "G.202" -> "G.174";
     "G.205" -> "G.174";
     "G.213" -> "G.174";
     "G.177" -> "G.175";
     "G.177" -> "G.176";
     "G.180" -> "G.176";
     "G.183" -> "G.176";
     "G.187" -> "G.176";
     "G.188" -> "G.176";
     "G.189" -> "G.176";
     "G.190" -> "G.176";
     "G.191" -> "G.176";
     "G.192" -> "G.176";
     "G.193" -> "G.176";
     "G.195" -> "G.176";
     "G.202" -> "G.176";
     "G.205" -> "G.176";
     "G.210" -> "G.176";
     "G.211" -> "G.176";
     "G.205" -> "G.177";
     "G.183" -> "G.180";
     "G.190" -> "G.180";
     "G.195" -> "G.180";
     "G.213" -> "G.180";
     "G.182" -> "G.181";
     "G.190" -> "G.181";
     "G.193" -> "G.181";
     "G.194" -> "G.181";
     "G.183" -> "G.182";
     "G.202" -> "G.182";
     "G.188" -> "G.183";
     "G.193" -> "G.183";
     "G.211" -> "G.183";
     "G.186" -> "G.184";
     "G.188" -> "G.184";
     "G.202" -> "G.184";
     "G.186" -> "G.185";
     "G.188" -> "G.185";
     "G.191" -> "G.185";
     "G.192" -> "G.185";
     "G.202" -> "G.185";
     "G.187" -> "G.186";
     "G.188" -> "G.186";
     "G.192" -> "G.186";
     "G.202" -> "G.186";
     "G.211" -> "G.187";
     "G.192" -> "G.188";
     "G.202" -> "G.188";
     "G.195" -> "G.189";
     "G.210" -> "G.189";
     "G.211" -> "G.189";
     "G.193" -> "G.190";
     "G.192" -> "G.191";
     "G.202" -> "G.191";
     "G.195" -> "G.192";
     "G.195" -> "G.193";
     "G.210" -> "G.193";
     "G.195" -> "G.194";
     "G.213" -> "G.194";
     "G.213" -> "G.195";
     "G.528" -> "G.195";
     "G.205" -> "G.202";
     "G.213" -> "G.205";
     "G.210" -> "G.209";
     "G.211" -> "G.209";
     "G.211" -> "G.210";
     "G.213" -> "G.211";
     "G.528" -> "G.211";
     "G.528" -> "G.213";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.502" -> "G.253";
     "G.503" -> "G.253";
     "G.503" -> "G.502";
     "G.510" -> "G.503";
     "G.509" -> "G.504";
     "G.506" -> "G.505";
     "G.510" -> "G.505";
     "G.513" -> "G.505";
     "G.510" -> "G.506";
     "G.513" -> "G.506";
     "G.510" -> "G.509";
     "G.513" -> "G.510";
     "G.514" -> "G.510";
     "G.514" -> "G.513";
     "G.528" -> "G.514";
     "G.528" -> "G.524";
     "G.528" -> "G.527";
   }

.. toctree::
   :hidden:

   code
   heath
