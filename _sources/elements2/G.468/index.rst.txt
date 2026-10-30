:order: 468
:number: 468
:canonical_id: G.468
:original_id: XI.23
:volume: III
:book: XI
:type: prop
:subtype: problem
:categories: problem, construction, solid-geometry
:category: problem, construction, solid-geometry
:tags: book-xi, point, segment, circle, angle, triangle, right-angle, plane, solid-angle, equality, reductio-ad-absurdum, lemma
:dependencies: G.11, G.15, G.36, G.42, G.60, G.110, G.117, G.153, G.164, G.166, G.455, G.467
:excerpt: Construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right angles.

.. _G.468:
.. _XI.23:

G.468
=====

.. rubric:: `XI.23 <https://geometor.github.io/euclid/heath/volume_III/book_xi/propositions/23/>`_

.. enunciation::

   Construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right angles.

.. signature:: problem

   | :fn:`construct_solid_angle <G.468>`\ (:g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>`) → :g:`/ O R / <g2:/ O R />`, :g:`/ B C / <g3:/ B C />`
   | **given** :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` be the three given plane angles, let two of these, taken together in any manner, be greater than the remaining one, while, further, the three are less than four right angles
   | **construct** If then we cut off :g:`/ O R / <g2:/ O R />` :eq:`equal <g2:/ O R / = g3:/ B C />` to :g:`/ B C / <g3:/ B C />`, the square on :g:`/ A B / <g3:/ A B />` will be greater than the square on :g:`/ L O / <g2:/ L O />` by the square on :g:`/ O R / <g2:/ O R />`

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

   :fn:`segment <G.3>`\ (:g:`A <g1:A>`, :g:`C <g1:C>`) → :g:`/ A C / <g1:/ A C />`, :fn:`segment <G.3>`\ (:g:`D <g1:D>`, :g:`F <g1:F>`) → :g:`/ D F / <g1:/ D F />`, :fn:`segment <G.3>`\ (:g:`G <g1:G>`, :g:`K <g1:K>`) → :g:`/ G K / <g1:/ G K />`

.. step:: assert ∵ there_plane_angles <G.467>

   It is therefore possible to construct a triangle out of straight lines equal to :g:`/ A C / <g1:/ A C />`, :g:`/ D F / <g1:/ D F />`, :g:`/ G K / <g1:/ G K />`.

.. step:: construct

   Let :g:`< L M N > <g2:< L M N >>` be so constructed that :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g2:/ L M /; g1:/ D F / = g2:/ M N /; g1:/ G K / = g2:/ N L />` to :g:`/ L M / <g2:/ L M />`, :g:`/ D F / <g1:/ D F />` to :g:`/ M N / <g2:/ M N />`, and further :g:`/ G K / <g1:/ G K />` to :g:`/ N L / <g2:/ N L />`, let :g:`( L M N ) <g2:( L M N )>` be described about :g:`< L M N > <g2:< L M N >>`

.. step:: construct

   Let its center be taken

.. step:: assert

   Let it be :g:`O <g2:O>`

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`L <g2:L>`, :g:`O <g2:O>`) → :g:`/ L O / <g2:/ L O />`, :fn:`segment <G.3>`\ (:g:`M <g2:M>`, :g:`O <g2:O>`) → :g:`/ M O / <g2:/ M O />`, :fn:`segment <G.3>`\ (:g:`N <g2:N>`, :g:`O <g2:O>`) → :g:`/ N O / <g2:/ N O />`

.. step:: assert

   If not, :g:`/ A B / <g1:/ A B />` is either :eq:`equal <g1:/ A B / = g2:/ L O />` to :g:`/ L O / <g2:/ L O />`, or less.

.. step:: assert

   First, let it be :eq:`equal <g1:/ A B / = g2:/ L O />`.

.. step:: assert

   Since :g:`/ A B / <g1:/ A B />` is :eq:`equal <g1:/ A B / = g2:/ L O />` to :g:`/ L O / <g2:/ L O />`, while :g:`/ A B / <g1:/ A B />` is :eq:`equal <g1:/ A B / = g1:/ B C /; g2:/ O L / = g2:/ O M />` to :g:`/ B C / <g1:/ B C />`, and :g:`/ O L / <g2:/ O L />` to :g:`/ O M / <g2:/ O M />`, the two sides :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are :eq:`equal <g1:/ A B / = g2:/ L O /; g1:/ B C / = g2:/ O M />` to the two sides :g:`/ L O / <g2:/ L O />`, :g:`/ O M / <g2:/ O M />` respectively; and, by hypothesis, the base :g:`/ A C / <g1:/ A C />` is :eq:`equal <g1:/ A C / = g2:/ L M />` to the base :g:`/ L M / <g2:/ L M />`;

.. step:: assert ∵ sss_congruence <G.15>

   Therefore :g:`< A B C ) <g1:< A B C )>` is :eq:`equal <g1:< A B C ) = g2:< L O M )>` to :g:`< L O M ) <g2:< L O M )>`.

.. step:: assert

   For the same reason :g:`< D E F ) <g1:< D E F )>` is also :eq:`equal <g1:< D E F ) = g2:< M O N ); g1:< G H K ) = g2:< N O L )>` to :g:`< M O N ) <g2:< M O N )>`, and further :g:`< G H K ) <g1:< G H K )>` to :g:`< N O L ) <g2:< N O L )>`;

.. step:: assert

   Therefore the three angles :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` are :eq:`equal <g1:< A B C ) = g2:< L O M ); g1:< D E F ) = g2:< M O N ); g1:< G H K ) = g2:< N O L )>` to the three angles :g:`< L O M ) <g2:< L O M )>`, :g:`< M O N ) <g2:< M O N )>`, :g:`< N O L ) <g2:< N O L )>`.

.. step:: assert

   The three angles :g:`< L O M ) <g2:< L O M )>`, :g:`< M O N ) <g2:< M O N )>`, :g:`< N O L ) <g2:< N O L )>` are equal to four right angles;

.. step:: assert

   Therefore :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` are equal to four right angles.

.. step:: assert

   They are also, by hypothesis, less than four right angles: which is absurd.

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />` is not equal to :g:`/ L O / <g2:/ L O />`.

.. step:: assert

   I say next that neither is :g:`/ A B / <g1:/ A B />` less than :g:`/ L O / <g2:/ L O />`.

.. step:: construct

   If possible, let it be so, and let :g:`/ O P / <g2:/ O P />` be made :eq:`equal <g2:/ O P / = g1:/ A B />` to :g:`/ A B / <g1:/ A B />`, and :g:`/ O Q / <g2:/ O Q />` :eq:`equal <g2:/ O Q / = g1:/ B C />` to :g:`/ B C / <g1:/ B C />`, and let :g:`/ P Q / <g2:/ P Q />` be joined.

.. step:: assert

   Since :g:`/ A B / <g1:/ A B />` is :eq:`equal <g1:/ A B / = g1:/ B C />` to :g:`/ B C / <g1:/ B C />`, :g:`/ O P / <g2:/ O P />` is also :eq:`equal <g2:/ O P / = g2:/ O Q />` to :g:`/ O Q / <g2:/ O Q />`, so that the remainder :g:`/ L P / <g2:/ L P />` is :eq:`equal <g2:/ L P / = g2:/ Q M />` to :g:`/ Q M / <g2:/ Q M />`.

.. step:: assert ∵ straight_line_drawn_vi_2, parallel_transversal_angles, equiangular_triangles_sides, magnitudes_proportional_proportional <G.164, G.42, G.166, G.153>

   Therefore :g:`/ L M / <g2:/ L M />` is parallel to :g:`/ P Q / <g2:/ P Q />`, and :g:`< L M O > <g2:< L M O >>` is equiangular with :g:`< P Q O > <g2:< P Q O >>`; therefore, as :g:`/ O L / <g2:/ O L />` is to :g:`/ L M / <g2:/ L M />`, so is :g:`/ O P / <g2:/ O P />` to :g:`/ P Q / <g2:/ P Q />`; and alternately, as :g:`/ L O / <g2:/ L O />` is to :g:`/ O P / <g2:/ O P />`, so is :g:`/ L M / <g2:/ L M />` to :g:`/ P Q / <g2:/ P Q />`.

.. step:: assert

   :g:`/ L O / <g2:/ L O />` is greater than :g:`/ O P / <g2:/ O P />`;

.. step:: assert

   Therefore :g:`/ L M / <g2:/ L M />` is also greater than :g:`/ P Q / <g2:/ P Q />`.

.. step:: assert

   :g:`/ L M / <g2:/ L M />` was made :eq:`equal <g2:/ L M / = g1:/ A C />` to :g:`/ A C / <g1:/ A C />`;

.. step:: assert

   Therefore :g:`/ A C / <g1:/ A C />` is also greater than :g:`/ P Q / <g2:/ P Q />`.

.. step:: assert

   Since, then, the two sides :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are :eq:`equal <g1:/ A B / = g2:/ P O /; g1:/ B C / = g2:/ O Q />` to the two sides :g:`/ P O / <g2:/ P O />`, :g:`/ O Q / <g2:/ O Q />`, and the base :g:`/ A C / <g1:/ A C />` is greater than the base :g:`/ P Q / <g2:/ P Q />`,

.. step:: assert ∵ converse_hinge_theorem <G.36>

   Therefore :g:`< A B C ) <g1:< A B C )>` is greater than :g:`< P O Q ) <g2:< P O Q )>`.

.. step:: assert

   Similarly we can prove that :g:`< D E F ) <g1:< D E F )>` is also greater than :g:`< M O N ) <g2:< M O N )>`, and :g:`< G H K ) <g1:< G H K )>` greater than :g:`< N O L ) <g2:< N O L )>`.

.. step:: assert

   Therefore the three angles :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` are greater than the three angles :g:`< L O M ) <g2:< L O M )>`, :g:`< M O N ) <g2:< M O N )>`, :g:`< N O L ) <g2:< N O L )>`.

.. step:: assert

   But, by hypothesis, :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>` are less than four right angles;

.. step:: assert

   Therefore :g:`< L O M ) <g2:< L O M )>`, :g:`< M O N ) <g2:< M O N )>`, :g:`< N O L ) <g2:< N O L )>` are much less than four right angles.

.. step:: assert

   They are also equal to four right angles:

.. step:: assert

   Which is absurd. Therefore :g:`/ A B / <g1:/ A B />` is not less than :g:`/ L O / <g2:/ L O />`.

.. step:: assert

   It was proved that neither is it equal;

.. step:: assert

   Therefore :g:`/ A B / <g1:/ A B />` is greater than :g:`/ L O / <g2:/ L O />`.

.. step:: construct

   :fn:`set_straight_line <G.455>`: Let then :g:`/ O R / <g2:/ O R />` be set up from :g:`O <g2:O>` at right angles to the plane of :g:`( L M N ) <g2:( L M N )>`, and let the square on :g:`/ O R / <g2:/ O R />` be equal to that area by which the square on :g:`/ A B / <g1:/ A B />` is greater than the square on :g:`/ L O / <g2:/ L O />`

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`R <g2:R>`, :g:`L <g2:L>`) → :g:`/ R L / <g2:/ R L />`, :fn:`segment <G.3>`\ (:g:`R <g2:R>`, :g:`M <g2:M>`) → :g:`/ R M / <g2:/ R M />`, :fn:`segment <G.3>`\ (:g:`R <g2:R>`, :g:`N <g2:N>`) → :g:`/ R N / <g2:/ R N />`

.. step:: assert

   Since :g:`/ R O / <g2:/ R O />` is at right angles to the plane of :g:`( L M N ) <g2:( L M N )>`,

.. step:: assert

   Therefore :g:`/ R O / <g2:/ R O />` is also at right angles to each of :g:`/ L O / <g2:/ L O />`, :g:`/ M O / <g2:/ M O />`, :g:`/ N O / <g2:/ N O />`.

.. step:: assert

   And, since :g:`/ L O / <g2:/ L O />` is :eq:`equal <g2:/ L O / = g2:/ O M />` to :g:`/ O M / <g2:/ O M />`, while :g:`/ O R / <g2:/ O R />` is common and at right angles,

.. step:: assert ∵ sas_congruence <G.11>

   Therefore the base :g:`/ R L / <g2:/ R L />` is :eq:`equal <g2:/ R L / = g2:/ R M />` to the base :g:`/ R M / <g2:/ R M />`.

.. step:: assert

   For the same reason :g:`/ R N / <g2:/ R N />` is also :eq:`equal <g2:/ R N / = g2:/ R L / = g2:/ R M />` to each of :g:`/ R L / <g2:/ R L />`, :g:`/ R M / <g2:/ R M />`;

.. step:: assert

   Therefore :g:`/ R L / <g2:/ R L />`, :g:`/ R M / <g2:/ R M />`, :g:`/ R N / <g2:/ R N />` are :eq:`equal <g2:/ R L / = g2:/ R M / = g2:/ R N />` to one another.

.. step:: assert

   Next, since by hypothesis the square on :g:`/ O R / <g2:/ O R />` is equal to that area by which the square on :g:`/ A B / <g1:/ A B />` is greater than the square on :g:`/ L O / <g2:/ L O />`,

.. step:: assert

   Therefore the square on :g:`/ A B / <g1:/ A B />` is equal to the squares on :g:`/ L O / <g2:/ L O />`, :g:`/ O R / <g2:/ O R />`.

.. step:: assert ∵ pythagorean_theorem <G.60>

   The square on :g:`/ L R / <g2:/ L R />` is equal to the squares on :g:`/ L O / <g2:/ L O />`, :g:`/ O R / <g2:/ O R />`, for :g:`< L O R ) <g2:< L O R )>` is right.

.. step:: assert

   Therefore the square on :g:`/ A B / <g1:/ A B />` is :eq:`equal <g1:/ A B / = g2:/ R L />` to the square on :g:`/ R L / <g2:/ R L />`; therefore :g:`/ A B / <g1:/ A B />` is :eq:`equal <g1:/ A B / = g2:/ R L />` to :g:`/ R L / <g2:/ R L />`.

.. step:: assert

   Each of :g:`/ B C / <g1:/ B C />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`, :g:`/ G H / <g1:/ G H />`, :g:`/ H K / <g1:/ H K />` is :eq:`equal <g1:/ B C / = g1:/ D E / = g1:/ E F / = g1:/ G H / = g1:/ H K / = g1:/ A B />` to :g:`/ A B / <g1:/ A B />`, while each of :g:`/ R M / <g2:/ R M />`, :g:`/ R N / <g2:/ R N />` is :eq:`equal <g2:/ R M / = g2:/ R N / = g2:/ R L />` to :g:`/ R L / <g2:/ R L />`;

.. step:: assert

   Therefore each of :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`, :g:`/ G H / <g1:/ G H />`, :g:`/ H K / <g1:/ H K />` is :eq:`equal <g1:/ A B / = g1:/ B C / = g1:/ D E / = g1:/ E F / = g1:/ G H / = g1:/ H K / = g2:/ R L / = g2:/ R M / = g2:/ R N />` to each of :g:`/ R L / <g2:/ R L />`, :g:`/ R M / <g2:/ R M />`, :g:`/ R N / <g2:/ R N />`.

.. step:: assert

   And, since the two sides :g:`/ L R / <g2:/ L R />`, :g:`/ R M / <g2:/ R M />` are :eq:`equal <g2:/ L R / = g1:/ A B /; g2:/ R M / = g1:/ B C />` to the two sides :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, and the base :g:`/ L M / <g2:/ L M />` is by hypothesis :eq:`equal <g2:/ L M / = g1:/ A C />` to the base :g:`/ A C / <g1:/ A C />`,

.. step:: assert ∵ sss_congruence <G.15>

   Therefore :g:`< L R M ) <g2:< L R M )>` is :eq:`equal <g2:< L R M ) = g1:< A B C )>` to :g:`< A B C ) <g1:< A B C )>`.

.. step:: assert

   For the same reason

.. step:: assert

   :g:`< M R N ) <g2:< M R N )>` is also :eq:`equal <g2:< M R N ) = g1:< D E F ); g2:< L R N ) = g1:< G H K )>` to :g:`< D E F ) <g1:< D E F )>`, and :g:`< L R N ) <g2:< L R N )>` to :g:`< G H K ) <g1:< G H K )>`.

.. step:: assert

   Therefore, out of the three plane angles :g:`< L R M ) <g2:< L R M )>`, :g:`< M R N ) <g2:< M R N )>`, :g:`< L R N ) <g2:< L R N )>`, which are :eq:`equal <g2:< L R M ) = g1:< A B C ); g2:< M R N ) = g1:< D E F ); g2:< L R N ) = g1:< G H K )>` to the three given angles :g:`< A B C ) <g1:< A B C )>`, :g:`< D E F ) <g1:< D E F )>`, :g:`< G H K ) <g1:< G H K )>`, the solid angle at :g:`R <g2:R>` has been constructed, which is contained by :g:`< L R M ) <g2:< L R M )>`, :g:`< M R N ) <g2:< M R N )>`, :g:`< L R N ) <g2:< L R N )>`.

.. step:: assert

   LEMMA. ~~~~~~

.. step:: assert

   How it is possible to take the square on :g:`/ O R / <g2:/ O R />` equal to that area by which the square on :g:`/ A B / <g3:/ A B />` is greater than the square on :g:`/ L O / <g2:/ L O />`, we can show as follows.

.. step:: assert

   Let :g:`/ A B / <g3:/ A B />`, :g:`/ L O / <g2:/ L O />` be set out, and let :g:`/ A B / <g3:/ A B />` be the greater

.. step:: construct

   :fn:`fit_chord_in_circle <G.117>`: Let the semicircle :g:`( A B C ) <g3:( A B C )>` be described on :g:`/ A B / <g3:/ A B />`, and into the semicircle :g:`( A B C ) <g3:( A B C )>` let :g:`/ A C / <g3:/ A C />` be fitted :eq:`equal <g3:/ A C / = g2:/ L O />` to :g:`/ L O / <g2:/ L O />`, not being greater than the diameter :g:`/ A B / <g3:/ A B />`

.. step:: construct

   :fn:`segment <G.3>`\ (:g:`C <g3:C>`, :g:`B <g3:B>`) → :g:`/ C B / <g3:/ C B />`

.. step:: assert

   Since then :g:`< A C B ) <g3:< A C B )>` is an angle in the semicircle :g:`( A C B ) <g3:( A C B )>`,

.. step:: assert ∵ thales_semicircle_theorem <G.110>

   Therefore :g:`< A C B ) <g3:< A C B )>` is right.

.. step:: assert ∵ pythagorean_theorem <G.60>

   Therefore the square on :g:`/ A B / <g3:/ A B />` is equal to the squares on :g:`/ A C / <g3:/ A C />`, :g:`/ C B / <g3:/ C B />`.

.. step:: assert

   Hence the square on :g:`/ A B / <g3:/ A B />` is greater than the square on :g:`/ A C / <g3:/ A C />` by the square on :g:`/ C B / <g3:/ C B />`.

.. step:: assert

   :g:`/ A C / <g3:/ A C />` is :eq:`equal <g3:/ A C / = g2:/ L O />` to :g:`/ L O / <g2:/ L O />`.

.. step:: assert

   Therefore the square on :g:`/ A B / <g3:/ A B />` is greater than the square on :g:`/ L O / <g2:/ L O />` by the square on :g:`/ C B / <g3:/ C B />`.

.. step:: conclude

   If then we cut off :g:`/ O R / <g2:/ O R />` :eq:`equal <g2:/ O R / = g3:/ B C />` to :g:`/ B C / <g3:/ B C />`, the square on :g:`/ A B / <g3:/ A B />` will be greater than the square on :g:`/ L O / <g2:/ L O />` by the square on :g:`/ O R / <g2:/ O R />`.

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
     "G.20" [label="G.20", tooltip="G.20 (I.12): Construct a perpendicular to a given infinite line from a given point not on it.", fillcolor="#222244", URL="../G.20/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2): If equals are added to equals, the wholes are equal.", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13): A ray standing on a line makes either two right angles or adjacent angles summing to two right angles.", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4): All right angles are equal.", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.24" [label="G.24", tooltip="G.24 (I.14): If two rays at a point on a line on opposite sides make adjacent angles summing to two right angles, the two rays are collinear.", fillcolor="#222244", URL="../G.24/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15): Intersecting lines make their vertical angles equal.", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5): The whole is greater than the part.", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16): In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.28" [label="G.28", tooltip="G.28 (I.17): In any triangle, the sum of any two angles is less than two right angles.", fillcolor="#222244", URL="../G.28/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18): In any triangle, the greater side subtends the greater angle.", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19): In any triangle, the greater angle is subtended by the greater side.", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20): In any triangle, the sum of any two sides is greater than the remaining side.", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22): Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23): Construct on a given line at a given point an angle equal to a given angle.", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.35" [label="G.35", tooltip="G.35 (I.24): If two triangles have two sides equal to two sides respectively, the one with the greater included angle has the greater base.", fillcolor="#222244", URL="../G.35/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.25): If two triangles have two sides equal to two sides respectively, the one with the greater base has the greater included angle.", fillcolor="#222244", URL="../G.36/index.html", target="_top"];
     "G.37" [label="G.37", tooltip="G.37 (I.26): Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23): Parallel lines are straight lines in the same plane which, produced indefinitely in both directions, do not meet.", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27): If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.28): If a transversal cutting two lines makes the exterior angle equal to the opposite interior angle, or interior angles on the same side supplementary, the lines are parallel.", fillcolor="#222244", URL="../G.40/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5): Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29): A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31): Construct through a given point a line parallel to a given line.", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.32): In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.", fillcolor="#222244", URL="../G.45/index.html", target="_top"];
     "G.46" [label="G.46", tooltip="G.46 (I.33): Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34): In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35): Parallelograms on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.36): Parallelograms on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37): Triangles on the same base and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.38): Triangles on equal bases and in the same parallels are equal in area.", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.39): Equal triangles on the same base and on the same side lie in the same parallels.", fillcolor="#222244", URL="../G.52/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41): If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.59" [label="G.59", tooltip="G.59 (I.46): Construct a square on a given segment.", fillcolor="#222244", URL="../G.59/index.html", target="_top"];
     "G.60" [label="G.60", tooltip="G.60 (I.47): In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).", fillcolor="#222244", URL="../G.60/index.html", target="_top"];
     "G.98" [label="G.98", tooltip="G.98 (III.20): In a circle the angle at the centre is double of the angle at the circumference, when the angles have the same circumference as base.", fillcolor="#222244", URL="../G.98/index.html", target="_top"];
     "G.99" [label="G.99", tooltip="G.99 (III.21): In a circle the angles in the same segment are equal.", fillcolor="#222244", URL="../G.99/index.html", target="_top"];
     "G.100" [label="G.100", tooltip="G.100 (III.22): The opposite angles of quadrilaterals in circles are equal to two right angles.", fillcolor="#222244", URL="../G.100/index.html", target="_top"];
     "G.110" [label="G.110", tooltip="G.110 (III.31): In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of...", fillcolor="#222244", URL="../G.110/index.html", target="_top"];
     "G.117" [label="G.117", tooltip="G.117 (IV.1): Into a given circle to fit a straight line equal to a given straight line which is not greater than the diameter of the circle.", fillcolor="#222244", URL="../G.117/index.html", target="_top"];
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.136" [label="G.136", tooltip="G.136 (V.2): If a first magnitude be the same multiple of a second that a third is of a fourth, and a fifth also be the same multiple of the second that a sixth is of the fourth, the sum of the...", fillcolor="#222244", URL="../G.136/index.html", target="_top"];
     "G.137" [label="G.137", tooltip="G.137 (V.3): If a first magnitude be the same multiple of a second that a third is of a fourth, and if equimultiples be taken of the first and third, then alsoex aequali the magnitudes taken is...", fillcolor="#222244", URL="../G.137/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equimu...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.139" [label="G.139", tooltip="G.139 (V.4): If a first magnitude have to a second the same ratio as a third to a fourth, any equimultiples whatever of the first and third will also have the same ratio to any equimultiples wh...", fillcolor="#222244", URL="../G.139/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (V.def.7): When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then t...", fillcolor="#224422", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.146" [label="G.146", tooltip="G.146 (V.9): Magnitudes which have the same ratio to the same are equal; and magnitudes to which the same has the same ratio are equal.", fillcolor="#222244", URL="../G.146/index.html", target="_top"];
     "G.147" [label="G.147", tooltip="G.147 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", fillcolor="#222244", URL="../G.147/index.html", target="_top"];
     "G.148" [label="G.148", tooltip="G.148 (V.11): Ratios which are the same with the same ratio are also the same with one another.", fillcolor="#222244", URL="../G.148/index.html", target="_top"];
     "G.149" [label="G.149", tooltip="G.149 (V.12): If any number of magnitudes be proportional, as one of the antecedents is to one of the consequents, so will all the antecedents be to all the consequents.", fillcolor="#222244", URL="../G.149/index.html", target="_top"];
     "G.150" [label="G.150", tooltip="G.150 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.150/index.html", target="_top"];
     "G.151" [label="G.151", tooltip="G.151 (V.14): If a first magnitude have to a second the same ratio as a third has to a fourth, and the first be greater than the third, the second is greater than the fourth; if equal, equal; an...", fillcolor="#222244", URL="../G.151/index.html", target="_top"];
     "G.152" [label="G.152", tooltip="G.152 (V.15): Parts have the same ratio as the same multiples of them taken in corresponding order.", fillcolor="#222244", URL="../G.152/index.html", target="_top"];
     "G.153" [label="G.153", tooltip="G.153 (V.16): If four magnitudes be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.153/index.html", target="_top"];
     "G.157" [label="G.157", tooltip="G.157 (V.20): If there be three magnitudes, and others equal to them in multitude, which taken two and two are in the same ratio, and ifex aequali the first be greater than the third, the fourth...", fillcolor="#222244", URL="../G.157/index.html", target="_top"];
     "G.159" [label="G.159", tooltip="G.159 (V.22): If there be any number of magnitudes whatever, and others equal to them in multitude, which taken two and two together are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.159/index.html", target="_top"];
     "G.163" [label="G.163", tooltip="G.163 (VI.1): Triangles and parallelograms which are under the same height are to one another as their bases.", fillcolor="#222244", URL="../G.163/index.html", target="_top"];
     "G.164" [label="G.164", tooltip="G.164 (VI.2): If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionall...", fillcolor="#222244", URL="../G.164/index.html", target="_top"];
     "G.166" [label="G.166", tooltip="G.166 (VI.4): In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.", fillcolor="#222244", URL="../G.166/index.html", target="_top"];
     "G.443" [label="G.443", tooltip="G.443 (XI.1): A part of a straight line cannot be in the plane of reference and a part in a plane more elevated.", fillcolor="#222244", URL="../G.443/index.html", target="_top"];
     "G.444" [label="G.444", tooltip="G.444 (XI.2): If two straight lines cut one another, they are in one plane, and every triangle is in one plane.", fillcolor="#222244", URL="../G.444/index.html", target="_top"];
     "G.445" [label="G.445", tooltip="G.445 (XI.3): If two planes cut one another, their common section is a straight line.", fillcolor="#222244", URL="../G.445/index.html", target="_top"];
     "G.446" [label="G.446", tooltip="G.446 (XI.def.3): A straight line isat right angles to a plane, when it makes right angles with all the straight lines which meet it and are in the plane.", fillcolor="#224422", URL="../G.446/index.html", target="_top"];
     "G.447" [label="G.447", tooltip="G.447 (XI.4): If a straight line be set up at right angles to two straight lines which cut one another, at their common point of section, it is at right angles to the plane through them.", fillcolor="#222244", URL="../G.447/index.html", target="_top"];
     "G.450" [label="G.450", tooltip="G.450 (XI.7): If two straight lines be parallel and points be taken at random on each of them, the straight line joining the points is in the same plane with the parallel straight lines.", fillcolor="#222244", URL="../G.450/index.html", target="_top"];
     "G.451" [label="G.451", tooltip="G.451 (XI.8): If two straight lines be parallel, and one of them be at right angles to any plane, the remaining one is at right angles to the same plane.", fillcolor="#222244", URL="../G.451/index.html", target="_top"];
     "G.454" [label="G.454", tooltip="G.454 (XI.11): From a given elevated point to draw a straight line perpendicular to a given plane.", fillcolor="#222244", URL="../G.454/index.html", target="_top"];
     "G.455" [label="G.455", tooltip="G.455 (XI.12): To set up a straight line at right angles to a given plane from a given point in it.", fillcolor="#222244", URL="../G.455/index.html", target="_top"];
     "G.467" [label="G.467", tooltip="G.467 (XI.22): If there be three plane angles of which two, taken together in any manner, are greater than the remaining one, and they are contained by equal straight lines, it is possible to con...", fillcolor="#222244", URL="../G.467/index.html", target="_top"];
     "G.468" [label="G.468", tooltip="G.468 (XI.23): Construct a solid angle out of three plane angles two of which, taken together in any manner, are greater than the remaining one: thus the three angles must be less than four right...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.24" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
     "G.52" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.20" -> "G.3";
     "G.27" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.20" -> "G.4";
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
     "G.28" -> "G.7";
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
     "G.35" -> "G.11";
     "G.36" -> "G.11";
     "G.37" -> "G.11";
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.60" -> "G.11";
     "G.447" -> "G.11";
     "G.467" -> "G.11";
     "G.468" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.35" -> "G.12";
     "G.98" -> "G.12";
     "G.110" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.20" -> "G.15";
     "G.34" -> "G.15";
     "G.447" -> "G.15";
     "G.468" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.17";
     "G.27" -> "G.17";
     "G.19" -> "G.18";
     "G.20" -> "G.18";
     "G.22" -> "G.18";
     "G.110" -> "G.18";
     "G.22" -> "G.19";
     "G.59" -> "G.19";
     "G.454" -> "G.19";
     "G.454" -> "G.20";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.60" -> "G.21";
     "G.24" -> "G.22";
     "G.25" -> "G.22";
     "G.28" -> "G.22";
     "G.40" -> "G.22";
     "G.42" -> "G.22";
     "G.45" -> "G.22";
     "G.24" -> "G.23";
     "G.25" -> "G.23";
     "G.60" -> "G.24";
     "G.27" -> "G.25";
     "G.40" -> "G.25";
     "G.42" -> "G.25";
     "G.447" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.110" -> "G.28";
     "G.166" -> "G.28";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.35" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.35" -> "G.34";
     "G.44" -> "G.34";
     "G.36" -> "G.35";
     "G.467" -> "G.35";
     "G.468" -> "G.36";
     "G.47" -> "G.37";
     "G.447" -> "G.37";
     "G.39" -> "G.38";
     "G.40" -> "G.39";
     "G.44" -> "G.39";
     "G.46" -> "G.39";
     "G.166" -> "G.40";
     "G.42" -> "G.41";
     "G.166" -> "G.41";
     "G.45" -> "G.42";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.59" -> "G.42";
     "G.451" -> "G.42";
     "G.468" -> "G.42";
     "G.45" -> "G.44";
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.52" -> "G.44";
     "G.59" -> "G.44";
     "G.454" -> "G.44";
     "G.455" -> "G.44";
     "G.98" -> "G.45";
     "G.100" -> "G.45";
     "G.110" -> "G.45";
     "G.49" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.59" -> "G.47";
     "G.166" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.51" -> "G.49";
     "G.52" -> "G.50";
     "G.54" -> "G.50";
     "G.163" -> "G.51";
     "G.164" -> "G.51";
     "G.164" -> "G.52";
     "G.60" -> "G.54";
     "G.163" -> "G.54";
     "G.60" -> "G.59";
     "G.468" -> "G.60";
     "G.99" -> "G.98";
     "G.100" -> "G.99";
     "G.110" -> "G.100";
     "G.468" -> "G.110";
     "G.468" -> "G.117";
     "G.145" -> "G.135";
     "G.149" -> "G.135";
     "G.137" -> "G.136";
     "G.139" -> "G.137";
     "G.139" -> "G.138";
     "G.142" -> "G.138";
     "G.149" -> "G.138";
     "G.150" -> "G.138";
     "G.153" -> "G.138";
     "G.159" -> "G.138";
     "G.163" -> "G.138";
     "G.159" -> "G.139";
     "G.147" -> "G.142";
     "G.152" -> "G.142";
     "G.164" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.150" -> "G.144";
     "G.146" -> "G.145";
     "G.147" -> "G.145";
     "G.151" -> "G.145";
     "G.157" -> "G.145";
     "G.164" -> "G.146";
     "G.151" -> "G.147";
     "G.157" -> "G.147";
     "G.153" -> "G.148";
     "G.163" -> "G.148";
     "G.164" -> "G.148";
     "G.152" -> "G.149";
     "G.151" -> "G.150";
     "G.157" -> "G.150";
     "G.153" -> "G.151";
     "G.153" -> "G.152";
     "G.163" -> "G.152";
     "G.166" -> "G.153";
     "G.468" -> "G.153";
     "G.159" -> "G.157";
     "G.166" -> "G.159";
     "G.164" -> "G.163";
     "G.166" -> "G.164";
     "G.468" -> "G.164";
     "G.468" -> "G.166";
     "G.444" -> "G.443";
     "G.451" -> "G.444";
     "G.450" -> "G.445";
     "G.447" -> "G.446";
     "G.451" -> "G.446";
     "G.454" -> "G.446";
     "G.451" -> "G.447";
     "G.454" -> "G.447";
     "G.451" -> "G.450";
     "G.454" -> "G.451";
     "G.455" -> "G.451";
     "G.455" -> "G.454";
     "G.468" -> "G.455";
     "G.468" -> "G.467";
   }

.. toctree::
   :hidden:

   code
   heath
