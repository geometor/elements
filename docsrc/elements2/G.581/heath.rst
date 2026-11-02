:canonical_id: G.581
:original_id: XIII.3
:title: G.581 segment cut extreme
:volume: III
:book: XIII
:type: prop

G.581 segment cut extreme — Heath
=================================

.. rubric:: `XIII.3 <https://geometor.github.io/euclid/heath/volume_III/book_xiii/propositions/03/>`_

.. enunciation::

   If a :term:`straight line <G.4>` be cut in :term:`extreme and mean ratio <G.242>`, the :term:`square <G.63>` on the lesser segment added to the half of the greater segment is five times the square on the half of the greater segment.

For let any straight line :g:`/ A B / <g1:/ A B />` be cut in extreme and mean ratio at the :term:`point <G.1>` :g:`C <g1:C>`, let :g:`/ A C / <g1:/ A C />` be the greater segment, and let :g:`/ A C / <g1:/ A C />` be :eq:`bisected <g1:/ A D / = g1:/ D C />` at :g:`D <g1:D>` ; I say that the square on :g:`/ B D / <g1:/ B D />` is five times the square on :g:`/ D C / <g1:/ D C />`.

For let the square :g:`< A E > <g1:< A E >>` be described on :g:`/ A B / <g1:/ A B />`, and let the :term:`figure <G.9>` be drawn double.

.. picture:: g1.svg
   :alt: Book XIII, Proposition 3

.. subclause::

   Since :g:`/ A C / <g1:/ A C />` is double of :g:`/ D C / <g1:/ D C />`,

.. assertion::

   therefore the square on :g:`/ A C / <g1:/ A C />` is quadruple of the square on :g:`/ D C / <g1:/ D C />`, that is, :g:`< R S > <g1:< R S >>` is quadruple of :g:`< F G > <g1:< F G >>`.

.. subclause::

   And, since the :term:`rectangle <G.81>` :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` is equal to the square on :g:`/ A C / <g1:/ A C />`, and :g:`< C E > <g1:< C E >>` is the rectangle :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`,

.. assertion::

   therefore :g:`< C E > <g1:< C E >>` is :eq:`equal <g1:< C E > = g1:< R S >>` to :g:`< R S > <g1:< R S >>`.

.. subclause::

   But :g:`< R S > <g1:< R S >>` is quadruple of :g:`< F G > <g1:< F G >>` ;

.. assertion::

   therefore :g:`< C E > <g1:< C E >>` is also quadruple of :g:`< F G > <g1:< F G >>`.

.. subclause::

   Again, since :g:`/ A D / <g1:/ A D />` is :eq:`equal <g1:/ A D / = g1:/ D C />` to :g:`/ D C / <g1:/ D C />`,

.. assertion::

   :g:`/ H K / <g1:/ H K />` is also :eq:`equal <g1:/ H K / = g1:/ K F />` to :g:`/ K F / <g1:/ K F />`.

.. assertion::

   Hence the square :g:`< G F > <g1:< G F >>` is also :eq:`equal <g1:< G F > = g1:< H L >>` to the square :g:`< H L > <g1:< H L >>`.

.. assertion::

   Therefore :g:`/ G K / <g1:/ G K />` is :eq:`equal <g1:/ G K / = g1:/ K L /; g1:/ M N / = g1:/ N E />` to :g:`/ K L / <g1:/ K L />`, that is, :g:`/ M N / <g1:/ M N />` to :g:`/ N E / <g1:/ N E />` ; hence :g:`< M F > <g1:< M F >>` is also :eq:`equal <g1:< M F > = g1:< F E >>` to :g:`< F E > <g1:< F E >>`.

.. subclause::

   But :g:`< M F > <g1:< M F >>` is :eq:`equal <g1:< M F > = g1:< C G >>` to :g:`< C G > <g1:< C G >>` ;

.. assertion::

   therefore :g:`< C G > <g1:< C G >>` is also :eq:`equal <g1:< C G > = g1:< F E >>` to :g:`< F E > <g1:< F E >>`.

.. subclause::

   Let :g:`< C N > <g1:< C N >>` be added to each ;

.. assertion::

   therefore the :term:`gnomon <G.86>` :g:`< O P Q > <g1:< O P Q >>` is :eq:`equal <g1:< O P Q > = g1:< C E >>` to :g:`< C E > <g1:< C E >>`.

.. subclause::

   But :g:`< C E > <g1:< C E >>` was proved quadruple of :g:`< G F > <g1:< G F >>` ;

.. assertion::

   therefore the gnomon :g:`< O P Q > <g1:< O P Q >>` is also quadruple of the square :g:`< F G > <g1:< F G >>`.

.. assertion::

   Therefore the gnomon :g:`< O P Q > <g1:< O P Q >>` and the square :g:`< F G > <g1:< F G >>` are five times :g:`< F G > <g1:< F G >>`.

.. subclause::

   But the gnomon :g:`< O P Q > <g1:< O P Q >>` and the square :g:`< F G > <g1:< F G >>` are the square :g:`< D N > <g1:< D N >>`.

.. subclause::

   And :g:`< D N > <g1:< D N >>` is the square on :g:`/ D B / <g1:/ D B />`, and :g:`< G F > <g1:< G F >>` the square on :g:`/ D C / <g1:/ D C />`.

.. assertion::

   Therefore the square on :g:`/ D B / <g1:/ D B />` is five times the square on :g:`/ D C / <g1:/ D C />`.

.. qed::

   :just:`Q. E. D.`

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
     "G.14" [label="G.14", tooltip="G.14 (I.def.16): The point A within the circle ( A B ) from which all segments / A B /, / A C / to the arc are equal is called the center of the circle.", fillcolor="#224422", URL="../G.14/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.def.8): A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.", fillcolor="#224422", URL="../G.22/index.html", target="_top"];
     "G.32" [label="G.32", tooltip="G.32 (I.def.10): When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.", fillcolor="#224422", URL="../G.32/index.html", target="_top"];
     "G.61" [label="G.61", tooltip="G.61 (I.def.17): A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.", fillcolor="#224422", URL="../G.61/index.html", target="_top"];
     "G.63" [label="G.63", tooltip="G.63 (I.def.22): Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opp...", fillcolor="#224422", URL="../G.63/index.html", target="_top"];
     "G.81" [label="G.81", tooltip="G.81 (II.def.1): Any rectangular parallelogram is said to becontained by the twosegments containing theright angle.", fillcolor="#224422", URL="../G.81/index.html", target="_top"];
     "G.86" [label="G.86", tooltip="G.86 (II.def.2): And in any parallelogrammic area let any one whatever of the parallelograms about itsdiameter with the two complements be called agnomon.", fillcolor="#224422", URL="../G.86/index.html", target="_top"];
     "G.242" [label="G.242", tooltip="G.242 (VI.def.3): A segment is said to have been cut in extreme and mean ratio when, as the wholeline is to the greater segment, so is the greater to the less.", fillcolor="#224422", URL="../G.242/index.html", target="_top"];
     "G.581" [label="G.581", tooltip="G.581 (XIII.3): If a segment be cut in extreme and mean ratio, the square on the lesser segment added to the half of the greater segment is five times the square on the half of the greater segment...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.4" -> "G.1";
     "G.10" -> "G.1";
     "G.14" -> "G.1";
     "G.3" -> "G.2";
     "G.4" -> "G.2";
     "G.6" -> "G.2";
     "G.22" -> "G.2";
     "G.242" -> "G.2";
     "G.4" -> "G.3";
     "G.8" -> "G.3";
     "G.7" -> "G.4";
     "G.10" -> "G.4";
     "G.11" -> "G.4";
     "G.22" -> "G.4";
     "G.32" -> "G.4";
     "G.61" -> "G.4";
     "G.81" -> "G.4";
     "G.581" -> "G.4";
     "G.6" -> "G.5";
     "G.7" -> "G.5";
     "G.10" -> "G.6";
     "G.10" -> "G.7";
     "G.22" -> "G.7";
     "G.9" -> "G.8";
     "G.10" -> "G.9";
     "G.581" -> "G.9";
     "G.14" -> "G.10";
     "G.61" -> "G.10";
     "G.12" -> "G.11";
     "G.63" -> "G.11";
     "G.63" -> "G.12";
     "G.61" -> "G.14";
     "G.32" -> "G.22";
     "G.63" -> "G.22";
     "G.81" -> "G.32";
     "G.86" -> "G.61";
     "G.581" -> "G.63";
     "G.581" -> "G.81";
     "G.581" -> "G.86";
     "G.581" -> "G.242";
   }

Required for
------------

:ref:`G.597 <G.597>`, :ref:`G.601 <G.601>`
