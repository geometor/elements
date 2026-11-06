"""
Pseudocode, formal signature, and tightened enunciation generator for GEOMETOR Elements 2.0.

Transforms classical Heath RST propositions and statements into:
- Tightened, fact-oriented enunciations (``.. enunciation::``)
- Formal proposition/rule signatures (``.. signature::``) with ``given`` and ``construct`` / ``prove`` contracts
- Composable function invocations (``:fn:`name <G.x>`(...) → ...``) for ``construct`` steps
- Symbolic intersection steps (``... ∩ ... → ...``) for ``intersect`` steps
- Semantic rule justifications (``∵ rule_name``) for ``assert`` / ``conclude`` steps
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Tuple


# Curated fact-oriented enunciations for foundational Elements (keyed by canonical Euclid ID)
CURATED_ENUNCIATIONS: Dict[str, str] = {
    # Book I Definitions
    "I.def.1": "A point :g:`A <g1:A>` is that which has no part.",
    "I.def.2": "A line :g:`[ A B ] <g1:[ A B ]>` is a projection of a relationship of two points :g:`A <g1:A>`, :g:`B <g1:B>`.",
    "I.def.3": "The extremities of a segment :g:`/ A B / <g1:/ A B />` are points :g:`A <g1:A>`, :g:`B <g1:B>`.",
    "I.def.4": "A segment :g:`/ A B / <g1:/ A B />` is a portion of a line :g:`[ A B ] <g1:[ A B ]>` between two points :g:`A <g1:A>`, :g:`B <g1:B>` on the line.",
    "I.def.5": "A surface is that which has length and breadth only.",
    "I.def.6": "The extremities of a surface are lines or arcs.",
    "I.def.7": "A plane surface lies evenly with the lines on itself.",
    "I.def.8": "A plane angle is the inclination to one another of two lines or arcs in a plane that meet and do not lie on the same line.",
    "I.def.9": "A rectilineal angle is contained by two segments or lines.",
    "I.def.10": "When a segment standing on a line makes the adjacent angles equal, each of the equal angles is a right angle, and the standing segment is perpendicular to the line.",
    "I.def.11": "An obtuse angle is greater than a right angle.",
    "I.def.12": "An acute angle is less than a right angle.",
    "I.def.13": "A boundary is the extremity of anything.",
    "I.def.14": "A figure is that which is contained by any boundary or boundaries.",
    "I.def.15": "A circle :g:`( A B ) <g1:( B C D )>` is a plane figure contained by one arc defined by a center :g:`A <g1:A>` and a point :g:`B <g1:B>` establishing its defining radius :g:`/ A B / <g1:/ A B />`, such that all segments :g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />`, :g:`/ A D / <g1:/ A D />` falling upon the arc from :g:`A <g1:A>` are :eq:`equal <g1:/ A B / = g1:/ A C / = g1:/ A D />`.",
    "I.def.16": "The point :g:`A <g1:A>` within the circle :g:`( A B ) <g1:( B C D )>` from which all segments :g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />` to the arc are :eq:`equal <g1:/ A B / = g1:/ A C />` is called the center of the circle.",
    "I.def.17": "A diameter of a circle is any segment drawn through the center and terminated in both directions by the arc of the circle; it bisects the circle.",
    "I.def.18": "A semicircle is the figure contained by a diameter and the arc cut off by it.",
    "I.def.19": "Rectilineal figures are contained by segments: trilateral by three, quadrilateral by four, and multilateral by more than four.",
    "I.def.20": "Of trilateral figures, an equilateral triangle :g:`< A B C > <g1:< A B C >>` has three :eq:`equal <g1:/ A B / = g1:/ B C / = g1:/ C A />` sides, an isosceles triangle :g:`< D E F > <g1:< D E F >>` has two :eq:`equal <g1:/ F D / = g1:/ E F />` sides, and a scalene triangle :g:`< G H K > <g1:< G H K >>` has three unequal sides.",
    "I.def.21": "A right-angled triangle has a right angle, an obtuse-angled triangle has an obtuse angle, and an acute-angled triangle has three acute angles.",
    "I.def.22": "Of quadrilateral figures, a square is equilateral and right-angled; an oblong is right-angled but not equilateral; a rhombus is equilateral but not right-angled; a rhomboid has opposite sides and angles equal but is neither equilateral nor right-angled.",
    "I.def.23": "Parallel lines are lines in the same plane which, extended indefinitely in both directions, do not meet.",
    # Book I Postulates
    "I.post.1": "Construct a segment :g:`/ A B / <g1:/ A B />` between any two points :g:`A <g1:A>`, :g:`B <g1:B>`.",
    "I.post.2": "Extend a segment :g:`/ A B / <g1:/ A B />` continuously along a line :g:`[ A B ] <g1:[ A B ]>` to :g:`/ B C / <g1:/ B C />`.",
    "I.post.3": "Construct a circle :g:`( A B ) <g1:( B C D )>` with center :g:`A <g1:A>` and defining radius point :g:`B <g1:B>`.",
    "I.post.4": "All right angles are equal.",
    "I.post.5": "Two lines intersected by a transversal with interior angles on one side summing to less than two right angles meet on that side.",
    # Book I Common Notions
    "I.cn.1": "Things equal to the same thing are equal to one another.",
    "I.cn.2": "If equals are added to equals, the wholes are equal.",
    "I.cn.3": "If equals are subtracted from equals, the remainders are equal.",
    "I.cn.4": "Things :g:`/ A B / <g1:/ A B />`, :g:`/ D E / <g1:/ D E />` that :coincide:`coincide <g1:/ A B / ≡ g1:/ D E /, g1:A ≡ g1:D, g1:B ≡ g1:E>` with one another are :eq:`equal <g1:/ A B / = g1:/ D E />` to one another.",
    "I.cn.5": "The whole is greater than the part.",
    # Book I Propositions
    "I.1": "Construct an equilateral triangle on a given segment.",
    "I.2": "Construct at a given point a segment equal to a given segment.",
    "I.3": "Cut off from the greater of two unequal segments a segment equal to the less.",
    "I.4": "Triangles with two sides and the included angle equal are congruent (SAS).",
    "I.5": "In an isosceles triangle, the angles at the base are equal, and if the equal sides are extended, the angles under the base are equal.",
    "I.6": "If two angles of a triangle are equal, the sides subtending the equal angles are also equal.",
    "I.7": "On the same segment and on the same side, there cannot be constructed two distinct triangles with both pairs of conterminous sides equal.",
    "I.8": "Triangles with all three corresponding sides equal have their corresponding angles equal (SSS).",
    "I.9": "Bisect a given angle.",
    "I.10": "Bisect a given segment.",
    "I.11": "Construct a segment at right angles to a given line from a given point on it.",
    "I.12": "Construct a perpendicular to a given line from a given point not on it.",
    "I.13": "A segment standing on a line makes either two right angles or adjacent angles summing to two right angles.",
    "I.14": "If two segments at a point on a line on opposite sides make adjacent angles summing to two right angles, the two segments are collinear.",
    "I.15": "Intersecting lines make their vertical angles equal.",
    "I.16": "In any triangle, if one side is extended, the exterior angle is greater than either opposite interior angle.",
    "I.17": "In any triangle, the sum of any two angles is less than two right angles.",
    "I.18": "In any triangle, the greater side subtends the greater angle.",
    "I.19": "In any triangle, the greater angle is subtended by the greater side.",
    "I.20": "In any triangle, the sum of any two sides is greater than the remaining side.",
    "I.21": "Segments constructed from the endpoints of one side of a triangle to an interior point have a lesser sum but contain a greater angle than the other two sides.",
    "I.22": "Construct a triangle from three segments equal to three given segments satisfying the triangle inequality.",
    "I.23": "Construct on a given line at a given point an angle equal to a given angle.",
    "I.24": "If two triangles have two sides equal to two sides respectively, the one with the greater included angle has the greater base.",
    "I.25": "If two triangles have two sides equal to two sides respectively, the one with the greater base has the greater included angle.",
    "I.26": "Triangles with two angles and one corresponding side equal are congruent (ASA / AAS).",
    "I.27": "If a transversal cutting two lines makes the alternate interior angles equal, the lines are parallel.",
    "I.28": "If a transversal cutting two lines makes the exterior angle equal to the opposite interior angle, or interior angles on the same side supplementary, the lines are parallel.",
    "I.29": "A transversal cutting parallel lines makes alternate interior angles equal, exterior and opposite interior angles equal, and same-side interior angles supplementary.",
    "I.30": "Lines parallel to the same line are parallel to one another.",
    "I.31": "Construct through a given point a line parallel to a given line.",
    "I.32": "In any triangle, an exterior angle equals the sum of the two opposite interior angles, and the three interior angles sum to two right angles.",
    "I.33": "Segments joining the endpoints of equal and parallel segments in the same directions are themselves equal and parallel.",
    "I.34": "In a parallelogram, opposite sides and opposite angles are equal, and the diagonal bisects the area.",
    "I.35": "Parallelograms on the same base and in the same parallels are equal in area.",
    "I.36": "Parallelograms on equal bases and in the same parallels are equal in area.",
    "I.37": "Triangles on the same base and in the same parallels are equal in area.",
    "I.38": "Triangles on equal bases and in the same parallels are equal in area.",
    "I.39": "Equal triangles on the same base and on the same side lie in the same parallels.",
    "I.40": "Equal triangles on equal bases and on the same side lie in the same parallels.",
    "I.41": "If a parallelogram shares the same base with a triangle and lies in the same parallels, the parallelogram is double the triangle.",
    "I.42": "Construct, in a given angle, a parallelogram equal in area to a given triangle.",
    "I.43": "In any parallelogram, the complements of the parallelograms about the diagonal are equal in area.",
    "I.44": "Apply to a given segment, in a given angle, a parallelogram equal in area to a given triangle.",
    "I.45": "Construct, in a given angle, a parallelogram equal in area to a given polygon.",
    "I.46": "Construct a square on a given segment.",
    "I.47": "In a right-angled triangle, the square on the hypotenuse equals the sum of the squares on the two legs (Pythagorean Theorem).",
    "I.48": "If the square on one side of a triangle equals the sum of the squares on the other two sides, the angle contained by those two sides is right.",
    # Book II Propositions
    "II.1": "If one of two segments is cut into any number of parts, the rectangle contained by the two segments equals the sum of the rectangles contained by the uncut segment and each of the parts.",
    "II.2": "If a segment is cut at random, the sum of the rectangles contained by the whole and each of the parts equals the square on the whole.",
    "II.3": "If a segment is cut at random, the rectangle contained by the whole and one of the parts equals the rectangle contained by the parts together with the square on that part.",
    "II.4": "If a segment is cut at random, the square on the whole equals the squares on the parts together with twice the rectangle contained by the parts.",
    "II.5": "If a segment is cut into equal and unequal parts, the rectangle contained by the unequal parts together with the square on the segment between the points of section equals the square on the half.",
    "II.6": "If a segment is bisected and a segment is added to it in a line, the rectangle contained by the whole with the added segment and the added segment together with the square on the half equals the square on the segment made up of the half and the added segment.",
    "II.7": "If a segment is cut at random, the sum of the squares on the whole and on one of the parts equals twice the rectangle contained by the whole and that part together with the square on the remaining part.",
    "II.8": "If a segment is cut at random, four times the rectangle contained by the whole and one of the parts together with the square on the remaining part equals the square on the whole and the first part as one segment.",
    "II.9": "If a segment is cut into equal and unequal parts, the sum of the squares on the unequal parts is double the sum of the square on the half and the square on the segment between the points of section.",
    "II.10": "If a segment is bisected and a segment is added to it in a line, the sum of the squares on the whole with the added segment and on the added segment is double the sum of the square on the half and the square on the half with the added segment.",
    "II.11": "Cut a given segment so that the rectangle contained by the whole and one of the segments equals the square on the remaining segment.",
    "II.12": "In obtuse-angled triangles, the square on the side subtending the obtuse angle is greater than the sum of the squares on the sides containing the obtuse angle by twice the rectangle contained by one of those sides and the projection of the other upon it.",
    "II.13": "In acute-angled triangles, the square on the side subtending an acute angle is less than the sum of the squares on the sides containing the acute angle by twice the rectangle contained by one of those sides and the projection of the other upon it.",
    "II.14": "Construct a square equal in area to a given rectilineal figure.",
    # Book III Propositions
    "III.1": "Find the center of a given circle.",
    "III.2": "The segment joining any two points on the arc of a circle falls within the circle.",
    "III.3": "A segment through the center of a circle bisects a chord not through the center if and only if it cuts the chord at right angles.",
    "III.4": "In a circle, two intersecting chords that do not both pass through the center do not bisect one another.",
    "III.5": "Two intersecting circles do not have the same center.",
    "III.6": "Two circles that touch one another do not have the same center.",
    "III.7": "From an eccentric point on the diameter of a circle, the greatest segment to the arc passes through the center, the least is the remainder of the diameter, and segments nearer the center are greater than those more remote, with at most two equal segments on opposite sides.",
    "III.8": "From a point outside a circle, of segments falling on the concave arc the greatest passes through the center and nearer ones are greater, while on the convex arc the least lies between the point and the diameter and nearer ones are less, with at most two equal segments.",
    "III.9": "A point within a circle from which more than two equal segments fall on the circle is the center of the circle.",
    "III.10": "A circle does not intersect another circle at more than two points.",
    "III.11": "If two circles touch one another internally, the line joining their centers passes through the point of contact.",
    "III.12": "If two circles touch one another externally, the segment joining their centers passes through the point of contact.",
    "III.13": "A circle does not touch another circle at more than one point, whether internally or externally.",
    "III.14": "In a circle, chords are equal if and only if they are equally distant from the center.",
    "III.15": "Of chords in a circle, the diameter is the greatest, and a chord nearer the center is always greater than one more remote.",
    "III.16": "The line drawn at right angles to the diameter of a circle from its extremity falls outside the circle, no other line can be interposed between it and the arc, and the angle of the semicircle is greater than any acute rectilineal angle.",
    "III.17": "From a given point, construct a line tangent to a given circle.",
    "III.18": "If a line touches a circle, the segment joined from the center to the point of contact is perpendicular to the tangent.",
    "III.19": "If a line touches a circle, the line drawn at right angles to the tangent from the point of contact passes through the center of the circle.",
    "III.20": "In a circle, the angle at the center is double the angle at the circumference when the angles have the same arc as base.",
    "III.21": "In a circle, angles in the same segment are equal to one another.",
    "III.22": "The opposite angles of any quadrilateral inscribed in a circle sum to two right angles.",
    "III.23": "On the same segment and on the same side of it, there cannot be constructed two similar and unequal segments of circles.",
    "III.24": "Similar segments of circles on equal segments are equal to one another.",
    "III.25": "Given a segment of a circle, complete the full circle of which it is a segment.",
    "III.26": "In equal circles, equal angles stand on equal arcs, whether they stand at the centers or at the circumferences.",
    "III.27": "In equal circles, angles standing on equal arcs are equal to one another, whether they stand at the centers or at the circumferences.",
    "III.28": "In equal circles, equal chords cut off equal arcs, the greater equal to the greater and the less to the less.",
    "III.29": "In equal circles, equal arcs are subtended by equal chords.",
    "III.30": "Bisect a given arc of a circle.",
    "III.31": "In a circle, the angle in a semicircle is right, the angle in a greater segment is acute, and the angle in a lesser segment is obtuse.",
    "III.32": "If a line touches a circle and a chord is drawn from the point of contact, the angles which the chord makes with the tangent equal the angles in the alternate segments of the circle.",
    "III.33": "On a given segment, construct a segment of a circle admitting an angle equal to a given rectilineal angle.",
    "III.34": "From a given circle, cut off a segment admitting an angle equal to a given rectilineal angle.",
    "III.35": "If two chords in a circle intersect one another, the rectangle contained by the segments of one equals the rectangle contained by the segments of the other.",
    "III.36": "If from a point outside a circle a secant and a tangent are drawn, the rectangle contained by the whole secant and its external segment equals the square on the tangent.",
    "III.37": "If from a point outside a circle a secant and a segment to the circle are drawn such that the rectangle on the whole secant and its external part equals the square on the segment, the segment is tangent to the circle.",
    # Book IV Propositions
    "IV.1": "Fit into a given circle a chord equal to a given segment not greater than the diameter of the circle.",
    "IV.2": "Inscribe in a given circle a triangle equiangular with a given triangle.",
    "IV.3": "Circumscribe about a given circle a triangle equiangular with a given triangle.",
    "IV.4": "Inscribe a circle in a given triangle.",
    "IV.5": "Circumscribe a circle about a given triangle.",
    "IV.6": "Inscribe a square in a given circle.",
    "IV.7": "Circumscribe a square about a given circle.",
    "IV.8": "Inscribe a circle in a given square.",
    "IV.9": "Circumscribe a circle about a given square.",
    "IV.10": "Construct an isosceles triangle having each of the angles at the base double the remaining angle.",
    "IV.11": "Inscribe an equilateral and equiangular pentagon in a given circle.",
    "IV.12": "Circumscribe an equilateral and equiangular pentagon about a given circle.",
    "IV.13": "Inscribe a circle in a given equilateral and equiangular pentagon.",
    "IV.14": "Circumscribe a circle about a given equilateral and equiangular pentagon.",
    "IV.15": "Inscribe an equilateral and equiangular hexagon in a given circle.",
    "IV.16": "Inscribe an equilateral and equiangular fifteen-angled figure in a given circle.",
    "VI.def.2": "Reciprocally related figures have their sides about equal angles reciprocally proportional.",
    "VI.def.5": "A ratio is said to be compounded of ratios when the sizes of the ratios multiplied together make some ratio.",
}


# Concise short titles for G-Index headings ("G.<n> <short_title>")
SHORT_TITLES: Dict[str, str] = {
    # Book I Definitions (bare nouns)
    "I.def.1": "point",
    "I.def.2": "line",
    "I.def.3": "extremities of a segment",
    "I.def.4": "segment",
    "I.def.5": "surface",
    "I.def.6": "extremities of a surface",
    "I.def.7": "plane surface",
    "I.def.8": "plane angle",
    "I.def.9": "rectilineal angle",
    "I.def.10": "right angle and perpendicular",
    "I.def.11": "obtuse angle",
    "I.def.12": "acute angle",
    "I.def.13": "boundary",
    "I.def.14": "figure",
    "I.def.15": "circle",
    "I.def.16": "center of a circle",
    "I.def.17": "diameter of a circle",
    "I.def.18": "semicircle",
    "I.def.19": "rectilineal figures",
    "I.def.20": "equilateral, isosceles, and scalene triangles",
    "I.def.21": "right, obtuse, and acute-angled triangles",
    "I.def.22": "square, oblong, rhombus, and rhomboid",
    "I.def.23": "parallel lines",
    # Book II Definitions
    "II.def.1": "contained rectangle",
    "II.def.2": "gnomon",
    # Book III Definitions
    "III.def.1": "equal circles",
    "III.def.2": "line tangent to a circle",
    "III.def.3": "tangent circles",
    "III.def.4": "chords equally distant from the center",
    "III.def.5": "chord at greater distance from the center",
    "III.def.6": "segment of a circle",
    "III.def.7": "angle of a circle segment",
    "III.def.8": "angle in a circle segment",
    "III.def.9": "angle standing on an arc",
    "III.def.10": "sector of a circle",
    "III.def.11": "similar circle segments",
    # Book IV Definitions
    "IV.def.1": "polygon inscribed in a polygon",
    "IV.def.2": "polygon circumscribed about a polygon",
    "IV.def.3": "polygon inscribed in a circle",
    "IV.def.4": "polygon circumscribed about a circle",
    "IV.def.5": "circle inscribed in a polygon",
    "IV.def.6": "circle circumscribed about a polygon",
    "IV.def.7": "segment fitted into a circle",
    # Book V Definitions
    "V.def.1": "part (measure) of a magnitude",
    "V.def.2": "multiple of a magnitude",
    "V.def.3": "ratio",
    "V.def.4": "magnitudes having a ratio",
    "V.def.5": "magnitudes in the same ratio",
    "V.def.6": "proportional magnitudes",
    "V.def.7": "greater ratio",
    "V.def.8": "proportion in three terms",
    "V.def.9": "duplicate ratio",
    "V.def.10": "triplicate ratio",
    "V.def.11": "corresponding magnitudes",
    "V.def.12": "alternando (alternate ratio)",
    "V.def.13": "invertendo (inverse ratio)",
    "V.def.14": "componendo (composition of ratio)",
    "V.def.15": "separando (separation of ratio)",
    "V.def.16": "convertendo (conversion of ratio)",
    "V.def.17": "ex aequali (equality of ratios)",
    "V.def.18": "perturbed proportion",
    # Book VI Definitions
    "VI.def.1": "similar rectilineal figures",
    "VI.def.2": "reciprocally related figures",
    "VI.def.3": "extreme and mean ratio",
    "VI.def.4": "height of a figure",
    # Book VII Definitions
    "VII.def.1": "unit",
    "VII.def.2": "number",
    "VII.def.3": "part of a number",
    "VII.def.4": "parts of a number",
    "VII.def.5": "multiple of a number",
    "VII.def.6": "even number",
    "VII.def.7": "odd number",
    "VII.def.8": "even-times even number",
    "VII.def.9": "even-times odd number",
    "VII.def.10": "odd-times odd number",
    "VII.def.11": "prime number",
    "VII.def.12": "numbers prime to one another",
    "VII.def.13": "composite number",
    "VII.def.14": "numbers composite to one another",
    "VII.def.15": "multiplication of numbers",
    "VII.def.16": "plane and solid numbers",
    "VII.def.17": "square and cube numbers",
    "VII.def.18": "cube number",
    "VII.def.19": "square number",
    "VII.def.20": "proportional numbers",
    "VII.def.21": "similar plane and solid numbers",
    "VII.def.22": "perfect number",
    # Book X Definitions
    "X.def.1": "commensurable and incommensurable magnitudes",
    "X.def.2": "commensurable in square",
    "X.def.3": "rational and irrational segments",
    "X.def.4": "rational and irrational areas",
    "X.def.ii.1": "first binomial",
    "X.def.ii.2": "second binomial",
    "X.def.ii.3": "third binomial",
    "X.def.ii.4": "fourth binomial",
    "X.def.ii.5": "fifth binomial",
    "X.def.ii.6": "sixth binomial",
    "X.def.iii.1": "first apotome",
    "X.def.iii.2": "second apotome",
    "X.def.iii.3": "third apotome",
    "X.def.iii.4": "fourth apotome",
    "X.def.iii.5": "fifth apotome",
    "X.def.iii.6": "sixth apotome",
    # Book XI Definitions
    "XI.def.1": "solid",
    "XI.def.2": "extremity of a solid",
    "XI.def.3": "line at right angles to a plane",
    "XI.def.4": "plane at right angles to a plane",
    "XI.def.5": "inclination of a line to a plane",
    "XI.def.6": "inclination of a plane to a plane",
    "XI.def.7": "similarly inclined planes",
    "XI.def.8": "parallel planes",
    "XI.def.9": "similar solid figures",
    "XI.def.10": "equal and similar solid figures",
    "XI.def.11": "solid angle",
    "XI.def.12": "pyramid",
    "XI.def.13": "prism",
    "XI.def.14": "sphere",
    "XI.def.15": "axis of a sphere",
    "XI.def.16": "center of a sphere",
    "XI.def.17": "diameter of a sphere",
    "XI.def.18": "cone",
    "XI.def.19": "axis of a cone",
    "XI.def.20": "base of a cone",
    "XI.def.21": "cylinder",
    "XI.def.22": "axis of a cylinder",
    "XI.def.23": "bases of a cylinder",
    "XI.def.24": "similar cones and cylinders",
    "XI.def.25": "cube",
    "XI.def.26": "octahedron",
    "XI.def.27": "icosahedron",
    "XI.def.28": "dodecahedron",
    # Book I Postulates
    "I.post.1": "construct a segment",
    "I.post.2": "extend a segment",
    "I.post.3": "construct a circle",
    "I.post.4": "right angles are equal",
    "I.post.5": "parallel postulate",
    # Book I Common Notions
    "I.cn.1": "equals to the same are equal",
    "I.cn.2": "equals added to equals are equal",
    "I.cn.3": "equals subtracted from equals are equal",
    "I.cn.4": "coinciding things are equal",
    "I.cn.5": "the whole is greater than the part",
    # Book I Propositions
    "I.1": "construct an equilateral triangle",
    "I.2": "transfer a segment to a point",
    "I.3": "cut off an equal segment",
    "I.4": "congruent triangles by SAS",
    "I.5": "base angles of an isosceles triangle",
    "I.6": "triangle with equal base angles is isosceles",
    "I.7": "uniqueness of triangle sides on a base",
    "I.8": "congruent triangles by SSS",
    "I.9": "bisect an angle",
    "I.10": "bisect a segment",
    "I.11": "construct a perpendicular at a point on a line",
    "I.12": "construct a perpendicular from a point to a line",
    "I.13": "adjacent angles on a line sum to two right angles",
    "I.14": "supplementary adjacent angles form a line",
    "I.15": "vertical angles are equal",
    "I.16": "exterior angle of a triangle is greater than interior",
    "I.17": "two angles of a triangle are less than two right angles",
    "I.18": "greater side subtends greater angle",
    "I.19": "greater angle is subtended by greater side",
    "I.20": "triangle inequality",
    "I.21": "interior segments of a triangle",
    "I.22": "construct a triangle from three segments",
    "I.23": "construct an angle equal to a given angle",
    "I.24": "hinge theorem",
    "I.25": "converse hinge theorem",
    "I.26": "congruent triangles by ASA and AAS",
    "I.27": "equal alternate interior angles imply parallel lines",
    "I.28": "equal corresponding angles imply parallel lines",
    "I.29": "transversal angles of parallel lines",
    "I.30": "lines parallel to the same line are parallel",
    "I.31": "construct a line parallel to a given line",
    "I.32": "exterior angle and angle sum of a triangle",
    "I.33": "segments joining equal and parallel segments",
    "I.34": "opposite sides, angles, and diagonal of a parallelogram",
    "I.35": "parallelograms on the same base in the same parallels",
    "I.36": "parallelograms on equal bases in the same parallels",
    "I.37": "triangles on the same base in the same parallels",
    "I.38": "triangles on equal bases in the same parallels",
    "I.39": "equal triangles on the same base are in the same parallels",
    "I.40": "equal triangles on equal bases are in the same parallels",
    "I.41": "parallelogram is double a triangle on the same base",
    "I.42": "construct a parallelogram equal to a triangle",
    "I.43": "complements of parallelograms about the diagonal are equal",
    "I.44": "apply a parallelogram equal to a triangle on a segment",
    "I.45": "construct a parallelogram equal to a polygon",
    "I.46": "construct a square on a segment",
    "I.47": "Pythagorean theorem",
    "I.48": "converse of the Pythagorean theorem",
    # Book II Propositions
    "II.1": "distributive law of rectangles",
    "II.2": "square equals sum of rectangles on parts",
    "II.3": "rectangle on whole and part",
    "II.4": "square of a sum",
    "II.5": "rectangle on unequal parts plus square on difference",
    "II.6": "rectangle on bisected and extended segment",
    "II.7": "square of a difference",
    "II.8": "four rectangles plus square on difference",
    "II.9": "sum of squares on unequal parts",
    "II.10": "sum of squares on bisected and extended segment",
    "II.11": "cut a segment in extreme and mean ratio",
    "II.12": "law of cosines for obtuse triangles",
    "II.13": "law of cosines for acute triangles",
    "II.14": "construct a square equal to a polygon",
    # Book III Propositions
    "III.1": "find the center of a circle",
    "III.2": "chord of a circle lies within the circle",
    "III.3": "diameter bisects chord iff perpendicular",
    "III.4": "intersecting chords not through the center do not bisect",
    "III.5": "intersecting circles have distinct centers",
    "III.6": "touching circles have distinct centers",
    "III.7": "distances to a circle from an eccentric diameter point",
    "III.8": "distances to a circle from an exterior point",
    "III.9": "point with three equal segments to a circle is the center",
    "III.10": "two circles intersect in at most two points",
    "III.11": "line of centers of internally touching circles",
    "III.12": "line of centers of externally touching circles",
    "III.13": "two circles touch at most at one point",
    "III.14": "equal chords are equidistant from the center",
    "III.15": "diameter is the greatest chord",
    "III.16": "perpendicular at extremity of a diameter is tangent",
    "III.17": "draw a tangent to a circle from a point",
    "III.18": "radius to point of contact is perpendicular to tangent",
    "III.19": "perpendicular to tangent at contact passes through center",
    "III.20": "inscribed angle theorem",
    "III.21": "angles in the same circle segment are equal",
    "III.22": "opposite angles of a cyclic quadrilateral are supplementary",
    "III.23": "no two similar unequal circle segments on the same chord",
    "III.24": "similar circle segments on equal chords are equal",
    "III.25": "complete a circle from a given segment",
    "III.26": "equal angles stand on equal arcs",
    "III.27": "angles standing on equal arcs are equal",
    "III.28": "equal chords cut off equal arcs",
    "III.29": "equal arcs are subtended by equal chords",
    "III.30": "bisect an arc",
    "III.31": "Thales' theorem and angles in circle segments",
    "III.32": "alternate segment theorem",
    "III.33": "construct a circle segment on a chord admitting a given angle",
    "III.34": "cut off a circle segment admitting a given angle",
    "III.35": "intersecting chords theorem",
    "III.36": "tangent-secant theorem",
    "III.37": "converse of the tangent-secant theorem",
    # Book IV Propositions
    "IV.1": "fit a chord in a circle equal to a segment",
    "IV.2": "inscribe a triangle in a circle equiangular with a triangle",
    "IV.3": "circumscribe a triangle about a circle equiangular with a triangle",
    "IV.4": "inscribe a circle in a triangle",
    "IV.5": "circumscribe a circle about a triangle",
    "IV.6": "inscribe a square in a circle",
    "IV.7": "circumscribe a square about a circle",
    "IV.8": "inscribe a circle in a square",
    "IV.9": "circumscribe a circle about a square",
    "IV.10": "construct a golden isosceles triangle",
    "IV.11": "inscribe a regular pentagon in a circle",
    "IV.12": "circumscribe a regular pentagon about a circle",
    "IV.13": "inscribe a circle in a regular pentagon",
    "IV.14": "circumscribe a circle about a regular pentagon",
    "IV.15": "inscribe a regular hexagon in a circle",
    "IV.16": "inscribe a regular pentadecagon in a circle",
}


# Canonical semantic function & rule names keyed by Euclid ID
SEMANTIC_NAMES: Dict[str, str] = {
    # Book I Postulates
    "I.post.1": "segment",
    "I.post.2": "extend",
    "I.post.3": "circle",
    "I.post.4": "right_angles_equal",
    "I.post.5": "parallel_postulate",
    # Book I Common Notions
    "I.cn.1": "equal_transitive",
    "I.cn.2": "add_equals",
    "I.cn.3": "subtract_equals",
    "I.cn.4": "coinciding_equal",
    "I.cn.5": "whole_greater_than_part",
    # Book I Definitions
    "I.def.1": "point_def",
    "I.def.2": "line_def",
    "I.def.3": "segment_extremities",
    "I.def.4": "segment_def",
    "I.def.5": "surface_def",
    "I.def.6": "surface_extremities",
    "I.def.7": "plane_surface_def",
    "I.def.8": "plane_angle_def",
    "I.def.9": "rectilineal_angle_def",
    "I.def.10": "right_angle_perpendicular",
    "I.def.11": "obtuse_angle_def",
    "I.def.12": "acute_angle_def",
    "I.def.13": "boundary_def",
    "I.def.14": "figure_def",
    "I.def.15": "circle_radii",
    "I.def.16": "circle_center",
    "I.def.17": "circle_diameter",
    "I.def.18": "semicircle_def",
    "I.def.19": "polygon_def",
    "I.def.20": "triangle_sides_def",
    "I.def.21": "triangle_angles_def",
    "I.def.22": "quadrilateral_def",
    "I.def.23": "parallel_lines_def",
    # Book I Propositions
    "I.1": "equilateral_triangle",
    "I.2": "transfer_segment",
    "I.3": "cut_equal_segment",
    "I.4": "sas_congruence",
    "I.5": "isosceles_base_angles",
    "I.6": "equal_angles_isosceles",
    "I.7": "unique_triangle_sides",
    "I.8": "sss_congruence",
    "I.9": "bisect_angle",
    "I.10": "bisect_segment",
    "I.11": "perpendicular_at",
    "I.12": "perpendicular_from",
    "I.13": "adjacent_angles_supplementary",
    "I.14": "supplementary_angles_collinear",
    "I.15": "vertical_angles_equal",
    "I.16": "exterior_angle_greater",
    "I.17": "two_angles_less_than_two_right",
    "I.18": "greater_side_greater_angle",
    "I.19": "greater_angle_greater_side",
    "I.20": "triangle_inequality",
    "I.21": "interior_triangle_bounds",
    "I.22": "triangle_from_segments",
    "I.23": "copy_angle",
    "I.24": "hinge_theorem",
    "I.25": "converse_hinge_theorem",
    "I.26": "asa_aas_congruence",
    "I.27": "alternate_angles_parallel",
    "I.28": "corresponding_angles_parallel",
    "I.29": "parallel_transversal_angles",
    "I.30": "parallel_transitive",
    "I.31": "parallel_line",
    "I.32": "triangle_angle_sum",
    "I.33": "join_equal_parallels",
    "I.34": "parallelogram_properties",
    "I.35": "parallelograms_same_base",
    "I.36": "parallelograms_equal_bases",
    "I.37": "triangles_same_base",
    "I.38": "triangles_equal_bases",
    "I.39": "equal_triangles_same_base_parallel",
    "I.40": "equal_triangles_equal_bases_parallel",
    "I.41": "parallelogram_double_triangle",
    "I.42": "parallelogram_from_triangle",
    "I.43": "parallelogram_complements",
    "I.44": "apply_parallelogram_on_segment",
    "I.45": "parallelogram_from_polygon",
    "I.46": "square_on_segment",
    "I.47": "pythagorean_theorem",
    "I.48": "converse_pythagorean",
    # Book II–VI Propositions
    "II.1": "distribute_rectangle",
    "II.2": "square_sum_rectangles",
    "II.3": "rectangle_whole_and_part",
    "II.4": "square_of_sum",
    "II.5": "difference_of_squares_equal_unequal",
    "II.6": "bisected_and_extended_segment",
    "II.7": "square_of_difference",
    "II.8": "four_rectangles_plus_square",
    "II.9": "sum_of_squares_equal_unequal",
    "II.10": "sum_of_squares_bisected_extended",
    "II.11": "cut_extreme_and_mean_ratio",
    "II.12": "law_of_cosines_obtuse",
    "II.13": "law_of_cosines_acute",
    "II.14": "square_from_polygon",
    "III.1": "find_circle_center",
    "III.2": "chord_inside_circle",
    "III.3": "diameter_bisects_chord_perpendicular",
    "III.4": "chords_not_bisecting",
    "III.5": "intersecting_circles_distinct_centers",
    "III.6": "touching_circles_distinct_centers",
    "III.7": "eccentric_diameter_distances",
    "III.8": "exterior_point_circle_distances",
    "III.9": "three_equal_radii_center",
    "III.10": "circles_intersect_at_most_two_points",
    "III.11": "internally_touching_circles_centers",
    "III.12": "externally_touching_circles_centers",
    "III.13": "circles_touch_at_most_one_point",
    "III.14": "equal_chords_equidistant",
    "III.15": "diameter_greatest_chord",
    "III.16": "perpendicular_at_diameter_extremity_tangent",
    "III.17": "tangent_to_circle",
    "III.18": "radius_perpendicular_to_tangent",
    "III.19": "perpendicular_to_tangent_through_center",
    "III.20": "inscribed_angle_theorem",
    "III.21": "angles_in_same_segment_equal",
    "III.22": "cyclic_quadrilateral_opposite_angles",
    "III.23": "unique_similar_circle_segment",
    "III.24": "similar_circle_segments_equal",
    "III.25": "complete_circle_from_segment",
    "III.26": "equal_angles_equal_arcs",
    "III.27": "equal_arcs_equal_angles",
    "III.28": "equal_chords_equal_arcs",
    "III.29": "equal_arcs_equal_chords",
    "III.30": "bisect_arc",
    "III.31": "thales_semicircle_theorem",
    "III.32": "alternate_segment_theorem",
    "III.33": "circle_segment_with_angle",
    "III.34": "cut_circle_segment_with_angle",
    "III.35": "intersecting_chords_theorem",
    "III.36": "tangent_secant_theorem",
    "III.37": "converse_tangent_secant_theorem",
    "IV.1": "fit_chord_in_circle",
    "IV.2": "inscribe_triangle_in_circle",
    "IV.3": "circumscribe_triangle_about_circle",
    "IV.4": "inscribe_circle_in_triangle",
    "IV.5": "circumscribe_circle_about_triangle",
    "IV.6": "inscribe_square_in_circle",
    "IV.7": "circumscribe_square_about_circle",
    "IV.8": "inscribe_circle_in_square",
    "IV.9": "circumscribe_circle_about_square",
    "IV.10": "golden_isosceles_triangle",
    "IV.11": "inscribe_pentagon_in_circle",
    "IV.12": "circumscribe_pentagon_about_circle",
    "IV.13": "inscribe_circle_in_pentagon",
    "IV.14": "circumscribe_circle_about_pentagon",
    "IV.15": "inscribe_hexagon_in_circle",
    "IV.16": "inscribe_pentadecagon_in_circle",
    "VI.9": "cut_nth_part",
    "VI.10": "cut_similarly",
    "VI.11": "third_proportional",
    "VI.12": "fourth_proportional",
    "VI.13": "mean_proportional",
    "VI.30": "extreme_and_mean_ratio",
}

_STOP_WORDS = {
    "a", "an", "the", "of", "to", "in", "on", "from", "with", "by", "for",
    "at", "into", "unto", "upon", "about", "between", "through", "under",
    "over", "after", "before", "be", "is", "are", "was", "were", "been",
    "being", "have", "has", "had", "having", "do", "does", "did", "will",
    "shall", "may", "can", "cannot", "must", "let", "if", "then", "than",
    "that", "which", "who", "whom", "whose", "this", "these", "those",
    "it", "its", "they", "them", "their", "one", "another", "other",
    "each", "either", "neither", "both", "any", "all", "some", "no", "not",
    "nor", "or", "and", "but", "so", "as", "such", "same", "given",
    "two", "three", "four", "first", "second", "third", "fourth",
    "things", "thing", "also", "respectively", "whenever", "when", "where",
}


def get_semantic_name(
    canonical_ref: str,
    node_type: str = "prop",
    subtype: Optional[str] = None,
    enun_text: str = "",
) -> str:
    """Return a concise snake_case function or rule name for any G-node."""
    if canonical_ref in SEMANTIC_NAMES:
        return SEMANTIC_NAMES[canonical_ref]

    cleaned = re.sub(r":[A-Za-z0-9_.-]+:`([^`]+)`", r"\1", enun_text)
    cleaned = re.sub(r"<[^>]+>", "", cleaned)
    words = [
        w.lower()
        for w in re.findall(r"[A-Za-z]{3,}", cleaned)
        if w.lower() not in _STOP_WORDS
    ]
    if words:
        selected = words[:3]
        base = "_".join(selected)
        if node_type == "def" and not base.endswith("_def"):
            base = f"{base}_def"
        return base

    return re.sub(r"[^a-z0-9]+", "_", canonical_ref.lower()).strip("_")


def get_short_title(
    canonical_ref: str,
    node_type: str = "prop",
    subtype: Optional[str] = None,
    enun_text: str = "",
) -> str:
    """Return a concise short title for a G-Index node (e.g. 'point', 'construct an equilateral triangle')."""
    if canonical_ref in SHORT_TITLES:
        return SHORT_TITLES[canonical_ref]
    if canonical_ref in SEMANTIC_NAMES:
        sem = SEMANTIC_NAMES[canonical_ref]
        if sem.endswith("_def"):
            sem = sem[:-4]
        return sem.replace("_", " ")

    # Derive a concise lower-case phrase from enunciation text
    cleaned = re.sub(r":[A-Za-z0-9_.-]+:`([^`<]+?)\s*<[^>]+>`", r"\1", enun_text)
    cleaned = re.sub(r":[A-Za-z0-9_.-]+:`([^`]+)`", r"\1", cleaned)
    cleaned = cleaned.replace("**", "").replace("*", "").strip()
    cleaned = re.sub(r"\.\s*$", "", cleaned)

    # Condense "If ..., then ..." or long clauses into a concise 4-7 word summary
    m_imp = re.match(
        r"^((?:construct|bisect|find|cut(?:\s+off)?|inscribe|circumscribe|apply|divide|draw|describe)\b[^,.;:]+)",
        cleaned,
        re.IGNORECASE,
    )
    if m_imp:
        phrase = m_imp.group(1).strip()
        words = phrase.split()
        if len(words) > 8:
            phrase = " ".join(words[:8])
        return phrase[0].lower() + phrase[1:] if phrase else canonical_ref

    sem = get_semantic_name(canonical_ref, node_type, subtype, enun_text)
    if sem.endswith("_def"):
        sem = sem[:-4]
    return sem.replace("_", " ")


def tighten_enunciation_text(text: str, canonical_ref: str = "") -> str:
    """Return a concise, fact-oriented enunciation string using Elements 2.0 terminology (segment, line, arc)."""
    if canonical_ref in CURATED_ENUNCIATIONS:
        return CURATED_ENUNCIATIONS[canonical_ref]

    s = re.sub(r"^(?:\[\d+\]\s*)*(?:\*\*\d+\.\*\*|\d+\.)?\s*", "", text.strip())
    s = " ".join(line.strip() for line in s.splitlines() if line.strip())

    # Clean archaic constructions into direct imperative / declarative facts and Elements 2.0 terminology
    replacements = [
        (r"^On a given finite straight line to (construct|describe)\b", r"\1 on a given segment"),
        (r"^On a given straight line to (construct|describe)\b", r"\1 on a given segment"),
        (r"^To bisect a given\b", "Bisect a given"),
        (r"^To construct\b", "Construct"),
        (r"^To describe\b", "Construct"),
        (r"^To draw\b", "Construct"),
        (r"^To find\b", "Find"),
        (r"^To cut off\b", "Cut off"),
        (r"^To cut\b", "Cut"),
        (r"^From a given\b", "From a given"),
        (r"^In a given circle to inscribe\b", "Inscribe in a given circle"),
        (r"^About a given circle to circumscribe\b", "Circumscribe about a given circle"),
        (r"^In a given triangle to inscribe\b", "Inscribe in a given triangle"),
        (r"^About a given triangle to circumscribe\b", "Circumscribe about a given triangle"),
        (r"\brectilineal angle\b", "angle"),
        (r"\brectilineal angles\b", "angles"),
        (r"\brectilineal figure\b", "polygon"),
        (r"\brectilineal figures\b", "polygons"),
        (r"\bfinite straight lines\b", "segments"),
        (r"\bfinite straight line\b", "segment"),
        (r"\binfinite straight lines\b", "lines"),
        (r"\binfinite straight line\b", "line"),
        (r"\bparallel straight lines\b", "parallel lines"),
        (r"\bstraight lines\b", "segments"),
        (r"\bstraight line\b", "segment"),
        (r"\bcircumferences\b", "arcs"),
        (r"\bcircumference\b", "arc"),
        (r"\bcentre\b", "center"),
        (r"\bare equal to one another\b", "are equal"),
        (r"\bwill be equal to one another\b", "are equal"),
        (r"\bbe equal to\b", "equals"),
        (r"\bwill also be\b", "is"),
        (r"\bwill be\b", "is"),
        (r"\s+;", ";"),
        (r"\s+:", ":"),
    ]
    for pat, repl in replacements:
        s = re.sub(pat, repl, s)

    if s and s[0].islower():
        s = s[0].upper() + s[1:]
    return s


_ROLE_PROTECT_RE = re.compile(r":[A-Za-z0-9_.-]+:`[^`]+`")


def _split_clauses_preserving_roles(paragraph_text: str) -> List[str]:
    """Split a paragraph on ';' and sentence/construction boundaries outside RST roles."""
    placeholders: Dict[str, str] = {}
    counter = 0

    def _protect(m: re.Match) -> str:
        nonlocal counter
        counter += 1
        tok = f"__ROLE_{counter}__"
        placeholders[tok] = m.group(0)
        return tok

    protected = _ROLE_PROTECT_RE.sub(_protect, paragraph_text)
    # Keep '; and it has been ...' attached to the preceding conclusion clause
    protected = re.sub(
        r";\s+and\s+it\s+has\s+been\b",
        ", and it has been",
        protected,
        flags=re.IGNORECASE,
    )
    # Attach trailing :just:`...` after a semicolon or period to the preceding clause
    protected = re.sub(
        r"([;.])\s*(__ROLE_\d+__)",
        lambda m: f" {m.group(2)}{m.group(1)}"
        if placeholders.get(m.group(2), "").startswith(":just:")
        else m.group(0),
        protected,
    )
    # Split sentence boundaries before transition/proof keywords
    protected = re.sub(
        r"\.\s+(?=(?:Now|Then|And|But|For|Therefore|Since|Again|If|Let|I\s+say|Thus|Through|From|At|On|With)\b)",
        "; ",
        protected,
    )
    # Split compound construction clauses where the first clause already has a construction verb ("be joined, and on DE let...")
    protected = re.sub(
        r"(\bbe\s+(?:joined|drawn(?:\s+through)?|described|constructed|produced|made|cut(?:\s+off)?|taken(?:\s+at\s+random)?|placed|applied|bisected)\b[^,;]*),\s+(?:and\s+)?((?:on|from|with|at|through|in)\s+[^;]+?\blet\b|\blet\b)",
        r"\1; \2",
        protected,
        flags=re.IGNORECASE,
    )

    parts = [p.strip() for p in protected.split(";") if p.strip()]
    restored_parts: List[str] = []
    for p in parts:
        for tok, orig in placeholders.items():
            p = p.replace(tok, orig)
        restored_parts.append(p)
    return restored_parts


def _extract_inline_justifications(clause: str) -> Tuple[str, Optional[str]]:
    """Extract any `:just:`[G.x] <G.x>`` roles from a clause and return (cleaned_clause, combined_targets_str)."""
    just_matches = list(re.finditer(r":just:`([^`]+)`", clause))
    if not just_matches:
        return clause.strip(), None

    targets: List[str] = []
    for m in just_matches:
        raw = m.group(1).strip()
        m_t = re.search(r"<([^>]+)>", raw)
        t_str = m_t.group(1) if m_t else raw.strip("[]")
        for part in t_str.split(","):
            p = part.strip()
            if p and p not in targets:
                targets.append(p)

    cleaned = re.sub(r"\s*:just:`[^`]+`", "", clause).strip()
    cleaned = re.sub(r"[;,]\s*$", ".", cleaned)
    if targets:
        return cleaned, ", ".join(targets)
    return cleaned, None


def _parse_just_targets(just_str: Optional[str]) -> List[str]:
    """Extract list of G.<n> target IDs from a justification string like `[G.4] <G.4>` or `G.4`."""
    if not just_str:
        return []
    m = re.search(r"<([^>]+)>", just_str)
    raw = m.group(1) if m else just_str.strip("[] ")
    return [p.strip() for p in raw.split(",") if p.strip()]


def _fn_tag(fn_name: str, g_target: Optional[str]) -> str:
    """Format a `:fn:` role linking `fn_name` to `g_target` (or plain `**fn_name**` if no target) followed by `\\ ` for `(`."""
    if g_target:
        return f":fn:`{fn_name} <{g_target}>`\\ "
    return f"**{fn_name}**\\ "


def _endpoints_of_seg_role(seg_role: str) -> Optional[Tuple[str, str]]:
    """Given a segment role like `:g:`/ C A / <g1:/ C A />``, return point roles `(:g:`C <g1:C>`, :g:`A <g1:A>`)`."""
    m = re.match(r"^:g:`/\s*([A-Za-z0-9_]+)\s+([A-Za-z0-9_]+)\s*/\s*<(?:([^:>]+):)?[^>]+>`$", seg_role.strip())
    if not m:
        return None
    p1, p2, gid = m.group(1), m.group(2), m.group(3) or "g1"
    return (f":g:`{p1} <{gid}:{p1}>`", f":g:`{p2} <{gid}:{p2}>`")


def _two_point_circle_from_center_radius(
    center_role: str,
    radius_role: str,
    circle_role: str,
    circle_aliases: Optional[Dict[frozenset[str], str]] = None,
) -> Tuple[str, str]:
    """Given center `:g:`A <g1:A>``, radius `:g:`/ A B / <g1:/ A B />``, and circle `:g:`( B C D ) <g1:( B C D )>``,
    return `(radius_point_role, two_point_circle_role)` where circle is displayed as `( A B )`.
    """
    m_c = re.match(r"^:g:`([A-Za-z0-9_]+)\s*<(?:([^:>]+):)?[^>]+>`$", center_role.strip())
    m_r = re.match(
        r"^:g:`/\s*([A-Za-z0-9_]+)\s+([A-Za-z0-9_]+)\s*/\s*<(?:([^:>]+):)?[^>]+>`$",
        radius_role.strip(),
    )
    m_cir = re.match(r"^:g:`\(\s*([^`<]+?)\s*\)\s*<([^>]+)>`$", circle_role.strip())
    if not (m_c and m_cir):
        return radius_role, circle_role

    c_pt = m_c.group(1)
    gid = m_c.group(2) or "g1"
    cir_pts = [tok for tok in m_cir.group(1).split() if tok]
    cir_target = m_cir.group(2).strip()

    r_pt: Optional[str] = None
    if m_r:
        p1, p2 = m_r.group(1), m_r.group(2)
        r_pt = p2 if p1 == c_pt else (p1 if p2 == c_pt else p2)
    elif cir_pts:
        r_pt = cir_pts[0] if cir_pts[0] != c_pt else (cir_pts[1] if len(cir_pts) > 1 else cir_pts[0])

    if not r_pt:
        return radius_role, circle_role

    two_pt_disp = f"( {c_pt} {r_pt} )"
    if circle_aliases is not None and cir_pts:
        circle_aliases[frozenset(cir_pts)] = two_pt_disp

    rad_pt_role = f":g:`{r_pt} <{gid}:{r_pt}>`"
    two_pt_circle_role = f":g:`{two_pt_disp} <{cir_target}>`"
    return rad_pt_role, two_pt_circle_role


def _apply_circle_aliases(
    text: str, circle_aliases: Optional[Dict[frozenset[str], str]]
) -> str:
    """Rewrite any 3-point circle role `:g:`( B C D ) <target>`` to its 2-point `( A B )` display."""
    if not circle_aliases:
        return text

    def _repl(m: re.Match[str]) -> str:
        pts = [tok for tok in m.group(1).split() if tok]
        target = m.group(2).strip()
        alias = circle_aliases.get(frozenset(pts))
        if alias:
            return f":g:`{alias} <{target}>`"
        return m.group(0)

    return re.sub(r":g:`\(\s*([^`<]+?)\s*\)\s*<([^>]+)>`", _repl, text)


def _rewrite_clause_to_pseudocode(
    clause: str,
    is_first_step: bool = False,
    id_map: Optional[Dict[str, str]] = None,
    last_constructed_seg: Optional[str] = None,
    constructed_circles: Optional[List[str]] = None,
    circle_aliases: Optional[Dict[frozenset[str], str]] = None,
) -> Optional[Tuple[str, str, Optional[str]]]:
    """Rewrite a single Heath clause into (step_kind, concise_pseudocode_text, used_fn_target) or None."""
    s = " ".join(line.strip() for line in clause.strip().splitlines() if line.strip())
    if not s:
        return None

    id_map = id_map or {}
    g_segment = id_map.get("I.post.1", "G.3")
    g_extend = id_map.get("I.post.2", "G.7")
    g_circle = id_map.get("I.post.3", "G.4")
    g_equi = id_map.get("I.1", "G.5")
    g_transfer = id_map.get("I.2", "G.8")
    g_cut = id_map.get("I.3", "G.9")
    g_bisect_ang = id_map.get("I.9", "G.16")
    g_bisect_seg = id_map.get("I.10", "G.17")
    g_perp_at = id_map.get("I.11", "G.19")
    g_perp_from = id_map.get("I.12", "G.20")
    g_tri_segs = id_map.get("I.22", "G.33")
    g_copy_ang = id_map.get("I.23", "G.34")
    g_parallel = id_map.get("I.31", "G.44")
    g_pgram_tri = id_map.get("I.42", "G.55")
    g_apply_pgram = id_map.get("I.44", "G.57")
    g_square = id_map.get("I.46", "G.59")

    # Strip bracketed editorial interpolations like `[I say that they are also in the same parallels.]`
    s = re.sub(r"^\[I say that[^\]]*\]\s*(?:And\s*\[For\]\s*|And\s+|For\s+)?", "", s, flags=re.IGNORECASE).strip()

    # 0. Check for Diorismos ("Thus it is required..." or "I say that...") -> return ("goal", goal_text, None)
    m_req = re.match(r"^Thus it is required\s+to\s+(.+?)\.?$", s, re.IGNORECASE)
    if m_req:
        return ("goal", _strip_redundant_type_nouns(m_req.group(1).strip()), None)

    # If "Thus it is required..." is appended to the first sentence, strip it
    s = re.sub(r"\s*Thus it is required\b.*$", "", s, flags=re.IGNORECASE).strip()
    if not s:
        return None

    m_isay = re.match(r"^(?:Therefore\s+etc\.|I\s+say\s+that\s+(.+?)\.?)$", s, re.IGNORECASE)
    if m_isay:
        if m_isay.group(1):
            return ("goal", _strip_redundant_type_nouns(m_isay.group(1).strip()), None)
        return None

    if re.match(r"^(?:\(Being\)\s+what\s+it\s+was\s+required\b|Q\.\s*E\.\s*[DF]\.?$)", s, re.IGNORECASE):
        return None

    # 1. Check for "Given" step (including I.7 "For, if possible, given two straight lines...")
    m_i7 = re.match(
        r"^For,\s*if\s+possible,\s*given\s+(?:two\s+straight\s+lines\s+|two\s+segments\s+)?(.+?)\s+constructed\s+on\s+(?:the\s+straight\s+line\s+|the\s+segment\s+)?(:g:`[^`]+`)\s+and\s+meeting\s+at\s+(?:the\s+point\s+)?(:g:`[^`]+`),\s*let\s+two\s+other\s+(?:straight\s+lines|segments)\s+(.+?)\s+be\s+constructed\s+on\s+the\s+same\s+(?:straight\s+line|segment)\s+(:g:`[^`]+`),\s*on\s+the\s+same\s+side\s+of\s+it,\s*meeting\s+in\s+another\s+(?:point\s+)?(:g:`[^`]+`).*?\bso\s+that\s+(.+?)\.?$",
        s,
        re.IGNORECASE,
    )
    if m_i7:
        segs1 = _strip_redundant_type_nouns(m_i7.group(1))
        base = m_i7.group(2)
        pt_c = m_i7.group(3)
        segs2 = _strip_redundant_type_nouns(m_i7.group(4))
        pt_d = m_i7.group(6)
        sothat = _strip_redundant_type_nouns(m_i7.group(7))
        sothat = re.sub(r"\s+which\s+has\s+the\s+same\s+extremity\s+:g:`[^`]+`\s+with\s+it", "", sothat, flags=re.IGNORECASE)
        given_part = f"{segs1} on {base} meeting at {pt_c}"
        hyp_part = f"Suppose {segs2} on {base} meet at {pt_d} with {sothat}"
        return ("given_and_construct", f"{given_part}|||{hyp_part}", None)

    if re.match(r"^Let\b.*\bbe (?:the )?(?:two |three )?given\b", s, re.IGNORECASE) or (
        is_first_step
        and re.match(r"^Let\b", s, re.IGNORECASE)
        and not re.search(
            r"\bbe\s+(?:described|joined|drawn|constructed|cut|taken|produced|bisected|placed|made|applied)\b",
            s,
            re.IGNORECASE,
        )
    ):
        body = s
        body = re.sub(r"^Let\s+", "", body, flags=re.IGNORECASE)
        body = _strip_redundant_type_nouns(body)
        body = re.sub(
            r"\s+be\s+(?:the\s+)?(?:two\s+|three\s+)?given\s+(?:unequal\s+|infinite\s+|finite\s+)?(?:straight\s+lines?|segments?|rectilineal\s+angles?|angles?|points?|triangles?|circles?|figures?)(?:\s+which\s+is\s+not\s+on\s+it)?\.?$",
            "",
            body,
            flags=re.IGNORECASE,
        )
        body = re.sub(
            r"\bbe\s+(?:the\s+)?(?:two\s+|three\s+)?given\s+(?:unequal\s+|infinite\s+|finite\s+)?(?:straight\s+lines?|segments?|rectilineal\s+angles?|angles?|points?|triangles?|circles?|figures?)\b",
            "",
            body,
            flags=re.IGNORECASE,
        )
        body = re.sub(
            r"\b(?:the\s+)?given\s+(?:unequal\s+|infinite\s+|finite\s+)?(?:straight\s+lines?|segments?|rectilineal\s+angles?|angles?|points?|triangles?|circles?|figures?)\b",
            "",
            body,
            flags=re.IGNORECASE,
        )
        body = re.sub(
            r"\bbe\s+(?:a\s+|two\s+|three\s+)?(?:triangles?|segments?|lines?|circles?|angles?|figures?|parallelograms?)\s+having\s+(?:the\s+two\s+sides\s+|the\s+side\s+|the\s+angle\s+|the\s+angles\s+)?",
            ", ",
            body,
            flags=re.IGNORECASE,
        )
        body = re.sub(r"\bwhich\s+is\s+(not\s+on\s+it|on\s+it)\b", r"\1", body, flags=re.IGNORECASE)
        body = re.sub(r",\s*let\s+(:g:`[^`]+`)\s+be\s+the\s+greater(?:\s+of\s+them)?", r" (\1 >)", body, flags=re.IGNORECASE)
        body = re.sub(r"\s*,\s*and\s+", ", ", body, flags=re.IGNORECASE)
        body = re.sub(r"\s{2,}", " ", body).strip(" ,.")
        return ("given", body, None)

    # Normalize leading conjunctions and strip redundant type nouns for construction matching
    s_norm = _strip_redundant_type_nouns(s)
    s_norm = re.sub(
        r"^(?:For\s+|And\s+again,\s*|Again,\s*|And\s+|Then\s+|Now\s+|But,\s*if\s+not,\s*|If\s+not,\s*)",
        "",
        s_norm,
        flags=re.IGNORECASE,
    ).strip()

    # 2. Circle construction: "with centre A and distance AB let the circle BCD be described"
    m_circle = re.match(
        r"^with\s+(?:centre|center)\s+(:g:`[^`]+`)\s+and\s+(?:distance|radius)\s+(:g:`[^`]+`)\s+let\s+(?:the\s+)?(?:circle\s+)?(:g:`[^`]+`)\s+be\s+described\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_circle:
        center, radius, circle = m_circle.group(1), m_circle.group(2), m_circle.group(3)
        rad_pt_role, two_pt_circle = _two_point_circle_from_center_radius(
            center, radius, circle, circle_aliases
        )
        if constructed_circles is not None:
            constructed_circles.append(two_pt_circle)
        cir_call = f"{_fn_tag('circle', g_circle)}({center}, {rad_pt_role}) → {two_pt_circle}"
        # Emit explicit circle-line intersection steps for I.2, I.3, I.12
        if "( B C )" in two_pt_circle and "<g1:( B C )>" in two_pt_circle:
            int_step = f"{two_pt_circle} ∩ :g:`/ B F / <g1:/ B F />` → :g:`G <g1:G>`"
            return ("construct_and_intersect", f"{cir_call}|||{int_step}", g_circle)
        if "( D G )" in two_pt_circle and "<g1:( D G )>" in two_pt_circle:
            int_step = f"{two_pt_circle} ∩ :g:`/ A E / <g1:/ A E />` → :g:`L <g1:L>`"
            return ("construct_and_intersect", f"{cir_call}|||{int_step}", g_circle)
        if "( A D )" in two_pt_circle and "<g1:( D E F )>" in two_pt_circle:
            int_step = f"{two_pt_circle} ∩ :g:`/ A B / <g1:/ A B />` → :g:`E <g1:E>`"
            return ("construct_and_intersect", f"{cir_call}|||{int_step}", g_circle)
        if "( C D )" in two_pt_circle and "<g1:( C D )>" in two_pt_circle:
            int_step = f"{two_pt_circle} ∩ :g:`[ A B ] <g1:[ A B ]>` → :g:`E <g1:E>`, :g:`G <g1:G>`"
            return ("construct_and_intersect", f"{cir_call}|||{int_step}", g_circle)
        return (
            "construct",
            cir_call,
            g_circle,
        )

    # 3. Intersection + Join: "from the point C, in which the circles cut one another, to the points A, B let the straight lines CA, CB be joined"
    m_int_join = re.match(
        r"^from\s+(?:the\s+point\s+)?(:g:`[^`]+`),\s*in\s+which\s+the\s+circles\s+cut\s+one\s+another,\s*to\s+(?:the\s+points\s+)?(.+?)\s+let\s+(?:the\s+straight\s+lines\s+)?(.+?)\s+be\s+joined\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_int_join:
        pt_c, pts_to, segs_str = m_int_join.group(1), m_int_join.group(2), m_int_join.group(3)
        if constructed_circles and len(constructed_circles) >= 2:
            c1, c2 = constructed_circles[-2], constructed_circles[-1]
            int_expr = f"{c1} ∩ {c2} → {pt_c}"
        else:
            int_expr = f"circles ∩ → {pt_c}"

        seg_roles = re.findall(r":g:`[^`]+`", segs_str)
        pt_roles = re.findall(r":g:`[^`]+`", pts_to)
        if len(seg_roles) == len(pt_roles) and len(seg_roles) > 1:
            calls = [
                f"{_fn_tag('segment', g_segment)}({pt_c}, {pt_r}) → {seg_r}"
                for pt_r, seg_r in zip(pt_roles, seg_roles)
            ]
            join_expr = ", ".join(calls)
        else:
            join_expr = f"{_fn_tag('segment', g_segment)}({pt_c}, {pts_to}) → {segs_str}"
        return ("intersect_and_join", f"{int_expr}|||{join_expr}", g_segment)

    # 4. Simple Segment Join: "from A to B let AB be joined" or "let AB be joined"
    m_from_join = re.match(
        r"^from\s+(?:the\s+point\s+)?(:g:`[^`]+`)\s+to\s+(?:the\s+point\s+)?(:g:`[^`]+`)\s+let\s+(?:the\s+straight\s+line\s+)?(:g:`[^`]+`)\s+be\s+joined\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_from_join:
        p1, p2, seg = m_from_join.group(1), m_from_join.group(2), m_from_join.group(3)
        return (
            "construct",
            f"{_fn_tag('segment', g_segment)}({p1}, {p2}) → {seg}",
            g_segment,
        )

    m_let_join = re.match(
        r"^let\s+(?:the\s+straight\s+lines?\s+)?(.+?)\s+be\s+joined\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_let_join:
        segs_raw = _strip_redundant_type_nouns(m_let_join.group(1))
        seg_roles = re.findall(r":g:`[^`]+`", segs_raw)
        if seg_roles:
            calls: List[str] = []
            for sr in seg_roles:
                eps = _endpoints_of_seg_role(sr)
                if eps:
                    calls.append(f"{_fn_tag('segment', g_segment)}({eps[0]}, {eps[1]}) → {sr}")
                else:
                    calls.append(f"{_fn_tag('segment', g_segment)}() → {sr}")
            return ("construct", ", ".join(calls), g_segment)
        return ("construct", f"{_fn_tag('segment', g_segment)}() → {segs_raw}", g_segment)

    # 5. Join and produce: "let BE be joined and produced in a straight line to F"
    m_join_prod = re.match(
        r"^let\s+(?:the\s+straight\s+line\s+)?(:g:`[^`]+`)\s+be\s+joined\s+and\s+produced\s+(?:in\s+a\s+(?:straight\s+line|segment)\s+)?to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_join_prod:
        seg, pt_to = m_join_prod.group(1), m_join_prod.group(2)
        eps = _endpoints_of_seg_role(seg)
        seg_call = (
            f"{_fn_tag('segment', g_segment)}({eps[0]}, {eps[1]}) → {seg}"
            if eps
            else f"{_fn_tag('segment', g_segment)}() → {seg}"
        )
        ext_call = f"{_fn_tag('extend', g_extend)}({seg}) → {pt_to}"
        return ("construct", f"{seg_call}, {ext_call}", g_extend)

    # 6. Equilateral Triangle construction:
    # "on it / on AB let the equilateral triangle DAB be constructed" OR "let the equilateral triangle ABC be constructed on it"
    m_equi1 = re.match(
        r"^on\s+(.+?)\s+let\s+the\s+(.+?)\s+triangle\s+(:g:`[^`]+`)\s+be\s+constructed\.?$",
        s_norm,
        re.IGNORECASE,
    )
    m_equi2 = re.match(
        r"^let\s+the\s+(.+?)\s+triangle\s+(:g:`[^`]+`)\s+be\s+constructed\s+on\s+(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_equi1 or m_equi2:
        if m_equi1:
            base_raw, eq_role, tri = m_equi1.group(1), m_equi1.group(2), m_equi1.group(3)
        else:
            eq_role, tri, base_raw = m_equi2.group(1), m_equi2.group(2), m_equi2.group(3)
        base = _strip_redundant_type_nouns(base_raw).strip()
        if base.lower() == "it" and last_constructed_seg:
            base = last_constructed_seg
        return (
            "construct",
            f"{_fn_tag('equilateral_triangle', g_equi)}({base}) → {tri} ({eq_role})",
            g_equi,
        )

    # 7. Line Extension (produced):
    # "let AE, BF be produced (further) in a straight line with DA, DB"
    m_prod = re.match(
        r"^let\s+(?:the\s+(?:straight\s+lines?|segments?)\s+)?(.+?)\s+be\s+produced\s+(?:further\s+)?in\s+a\s+(?:straight\s+line|segment)\s+with\s+(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_prod:
        ext, orig = _strip_redundant_type_nouns(m_prod.group(1)), _strip_redundant_type_nouns(m_prod.group(2))
        orig_roles = re.findall(r":g:`[^`]+`", orig)
        ext_roles = re.findall(r":g:`[^`]+`", ext)
        if len(orig_roles) == len(ext_roles) and len(orig_roles) > 1:
            calls = [
                f"{_fn_tag('extend', g_extend)}({o_r}) → {e_r}"
                for o_r, e_r in zip(orig_roles, ext_roles)
            ]
            return ("construct", ", ".join(calls), g_extend)
        return ("construct", f"{_fn_tag('extend', g_extend)}({orig}) → {ext}", g_extend)

    # "let (one side of it) BC be produced / drawn through (in both directions) to D"
    m_prod_to = re.match(
        r"^let\s+(?:one\s+side\s+of\s+it\s+)?(?:the\s+(?:straight\s+lines?|segments?)\s+)?(.+?)\s+be\s+(?:produced|drawn\s+through)(?:\s+in\s+both\s+directions)?\s+to\s+(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_prod_to:
        orig, ext = _strip_redundant_type_nouns(m_prod_to.group(1)), _strip_redundant_type_nouns(m_prod_to.group(2))
        return ("construct", f"{_fn_tag('extend', g_extend)}({orig}) → {ext}", g_extend)

    # 8. Transfer segment: "at A let AD be placed equal to C"
    m_transfer = re.match(
        r"^at\s+(?:the\s+point\s+)?(:g:`[^`]+`)\s+let\s+(?:the\s+straight\s+line\s+)?(:g:`[^`]+`)\s+be\s+placed\s+(.+?)\s+to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_transfer:
        pt, seg, eq_part, src = (
            m_transfer.group(1),
            m_transfer.group(2),
            m_transfer.group(3),
            m_transfer.group(4),
        )
        return (
            "construct",
            f"{_fn_tag('transfer_segment', g_transfer)}({pt}, {src}) → {seg} ({eq_part})",
            g_transfer,
        )

    # 9. Cut off / make equal segment (G.9):
    # "from AE the greater let AG be cut off equal to AF the less" OR "let AE be cut off from AC equal to AD"
    m_cut1 = re.match(
        r"^from\s+(:g:`[^`]+`)(?:\s+the\s+greater)?\s+let\s+(:g:`[^`]+`)\s+be\s+cut\s+off\s+(.+?)\s+to\s+(:g:`[^`]+`)(?:\s+the\s+less)?\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_cut1:
        greater, seg, eq_part, less = m_cut1.group(1), m_cut1.group(2), m_cut1.group(3), m_cut1.group(4)
        return (
            "construct",
            f"{_fn_tag('cut_equal_segment', g_cut)}({greater}, {less}) → {seg} ({eq_part})",
            g_cut,
        )

    m_cut2 = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+cut\s+off\s+from\s+(:g:`[^`]+`)\s+(.+?)\s+to\s+(:g:`[^`]+`)(?:\s+the\s+less)?\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_cut2:
        seg, greater, eq_part, less = m_cut2.group(1), m_cut2.group(2), m_cut2.group(3), m_cut2.group(4)
        return (
            "construct",
            f"{_fn_tag('cut_equal_segment', g_cut)}({greater}, {less}) → {seg} ({eq_part})",
            g_cut,
        )

    m_made_eq = re.match(
        r"^(?:since\s+[^,]+,\s*)?let\s+(:g:`[^`]+`)\s+be\s+made\s+(:eq:`[^`]+`|equal)\s+to\s+(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_made_eq:
        seg, eq_part, target = m_made_eq.group(1), m_made_eq.group(2), _strip_redundant_type_nouns(m_made_eq.group(3))
        return (
            "construct",
            f"{_fn_tag('cut_equal_segment', g_cut)}({target}) → {seg} ({eq_part})",
            g_cut,
        )

    # 10. Bisect angle (G.16): "let < ACB ) be bisected by / CD /"
    m_bis_ang = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+(:eq:`bisected[^`]*`|bisected)\s+by\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_bis_ang:
        ang, eq_part, seg = m_bis_ang.group(1), m_bis_ang.group(2), m_bis_ang.group(3)
        return (
            "construct",
            f"{_fn_tag('bisect_angle', g_bisect_ang)}({ang}) → {seg} ({eq_part})",
            g_bisect_ang,
        )

    # 11. Bisect segment (G.17): "let / EG / be bisected at H"
    m_bis_seg = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+(:eq:`bisected[^`]*`|bisected)\s+at\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_bis_seg:
        seg, eq_part, pt = m_bis_seg.group(1), m_bis_seg.group(2), m_bis_seg.group(3)
        return (
            "construct",
            f"{_fn_tag('bisect_segment', g_bisect_seg)}({seg}) → {pt} ({eq_part})",
            g_bisect_seg,
        )

    # 12. Perpendicular at point on line (G.19): "let / AC / be drawn (from A) at right angles to / AB / (from A on it)"
    m_perp_at = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+drawn\s+(?:from\s+(:g:`[^`]+`)\s+)?at\s+(:eq:`right\s+angles[^`]*`|right\s+angles)\s+to\s+(:g:`[^`]+`)(?:\s+from\s+(:g:`[^`]+`)(?:\s+on\s+it)?)?\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_perp_at:
        perp = m_perp_at.group(1)
        pt = m_perp_at.group(2) or m_perp_at.group(5) or ""
        line = m_perp_at.group(4)
        args = f"{line}, {pt}" if pt else line
        return (
            "construct",
            f"{_fn_tag('perpendicular_at', g_perp_at)}({args}) → {perp}",
            g_perp_at,
        )

    # 13. Perpendicular from point to line (G.20):
    m_perp_from = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+drawn\s+(:eq:`perpendicular[^`]*`|perpendicular)\s+to\s+(:g:`[^`]+`)\s+from\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_perp_from:
        perp, line, pt = m_perp_from.group(1), m_perp_from.group(3), m_perp_from.group(4)
        return (
            "construct",
            f"{_fn_tag('perpendicular_from', g_perp_from)}({line}, {pt}) → {perp}",
            g_perp_from,
        )

    # 14. Copy angle (G.34):
    # "at A on it, let < DAE ) be constructed equal to < ADC )" or "let there be constructed, on / DE /, and at D on it, < EDG ) equal to < BAC )"
    m_copy_ang1 = re.match(
        r"^(?:since\s+[^,]+,\s*)?(?:on\s+(:g:`[^`]+`),\s*and\s+)?at\s+(:g:`[^`]+`)(?:\s+on\s+(?:it|:g:`[^`]+`))?,?\s*let\s+(:g:`[^`]+`)\s+be\s+constructed\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    m_copy_ang2 = re.match(
        r"^(?:since\s+[^,]+,\s*)?let\s+there\s+be\s+constructed,\s*on\s+(:g:`[^`]+`),\s*and\s+at\s+(:g:`[^`]+`)\s+on\s+it,\s*(:g:`[^`]+`)\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_copy_ang1 or m_copy_ang2:
        m_ca = m_copy_ang1 or m_copy_ang2
        assert m_ca is not None
        line_opt, pt, new_ang, eq_part, src_ang = (
            m_ca.group(1),
            m_ca.group(2),
            m_ca.group(3),
            m_ca.group(4),
            m_ca.group(5),
        )
        args = f"{line_opt}, {pt}, {src_ang}" if line_opt else f"{pt}, {src_ang}"
        return (
            "construct",
            f"{_fn_tag('copy_angle', g_copy_ang)}({args}) → {new_ang} ({eq_part})",
            g_copy_ang,
        )

    # 15. Parallel line through point (G.44):
    # "through B let / BE / be drawn parallel to / CA /" OR "let / CE / be drawn through C parallel to / AB /"
    m_par1 = re.match(
        r"^through\s+(:g:`[^`]+`)\s+let\s+(:g:`[^`]+`)\s+be\s+drawn\s+parallel\s+to\s+(?:either\s+)?(.+?)(?:,\s*and)?\.?$",
        s_norm,
        re.IGNORECASE,
    )
    m_par2 = re.match(
        r"^let\s+(:g:`[^`]+`)\s+be\s+drawn\s+through\s+(:g:`[^`]+`)\s+parallel\s+to\s+(?:either\s+)?(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_par1 or m_par2:
        if m_par1:
            pt, new_line, target_line = m_par1.group(1), m_par1.group(2), _strip_redundant_type_nouns(m_par1.group(3))
        else:
            new_line, pt, target_line = m_par2.group(1), m_par2.group(2), _strip_redundant_type_nouns(m_par2.group(3))
        return (
            "construct",
            f"{_fn_tag('parallel_line', g_parallel)}({pt}, {target_line}) → {new_line}",
            g_parallel,
        )

    # 16. Square on segment (G.59):
    m_sq = re.match(
        r"^let\s+there\s+be\s+(?:described|constructed)\s+on\s+(:g:`[^`]+`)\s+the\s+square\s+(:g:`[^`]+`)(?:,\s*and\s+on\s+(:g:`[^`]+`),\s*(:g:`[^`]+`)\s+the\s+squares\s+(:g:`[^`]+`),\s*(:g:`[^`]+`))?\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_sq:
        s1, sq1 = m_sq.group(1), m_sq.group(2)
        calls = [f"{_fn_tag('square_on_segment', g_square)}({s1}) → {sq1}"]
        if m_sq.group(3) and m_sq.group(5):
            calls.append(f"{_fn_tag('square_on_segment', g_square)}({m_sq.group(3)}) → {m_sq.group(5)}")
        if m_sq.group(4) and m_sq.group(6):
            calls.append(f"{_fn_tag('square_on_segment', g_square)}({m_sq.group(4)}) → {m_sq.group(6)}")
        return ("construct", ", ".join(calls), g_square)

    # 17. Parallelogram from triangle (G.55) and Apply parallelogram (G.57):
    m_pg55 = re.match(
        r"^let\s+the\s+parallelogram\s+(:g:`[^`]+`)\s+be\s+constructed\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`),\s*in\s+(:g:`[^`]+`)\s+which\s+is\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_pg55:
        pg, eq1, tri, ang, eq2, given_ang = m_pg55.groups()
        return (
            "construct",
            f"{_fn_tag('parallelogram_from_triangle', g_pgram_tri)}({tri}, {given_ang}) → {pg} ({eq1}, {ang} {eq2})",
            g_pgram_tri,
        )

    m_pg57 = re.match(
        r"^let\s+the\s+parallelogram\s+(:g:`[^`]+`)\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`)\s+be\s+applied\s+to\s+(:g:`[^`]+`),\s*in\s+(:g:`[^`]+`)\s+which\s+is\s+(:eq:`[^`]+`|equal)\s+to\s+(:g:`[^`]+`)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_pg57:
        pg, eq1, tri, seg, ang, eq2, given_ang = m_pg57.groups()
        return (
            "construct",
            f"{_fn_tag('apply_parallelogram_on_segment', g_apply_pgram)}({seg}, {tri}, {given_ang}) → {pg} ({eq1}, {ang} {eq2})",
            g_apply_pgram,
        )

    # 18. Point taken at random: "let a point D be taken at random on AB" or "on CD, CE respectively let D, E be taken at random"
    m_pt1 = re.match(
        r"^let\s+(?:a\s+point\s+)?(:g:`[^`]+`)\s+be\s+taken\s+(?:at\s+random\s+)?on\s+(?:the\s+other\s+side\s+of\s+)?(.+?)\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_pt1:
        pt, target = m_pt1.group(1), _strip_redundant_type_nouns(m_pt1.group(2))
        return ("construct", f"**point**\\ ({target}) → {pt}", None)

    m_pt2 = re.match(
        r"^on\s+(.+?)\s+(?:respectively\s+)?let\s+(.+?)\s+be\s+taken\s+at\s+random\.?$",
        s_norm,
        re.IGNORECASE,
    )
    if m_pt2:
        target, pts = _strip_redundant_type_nouns(m_pt2.group(1)), _strip_redundant_type_nouns(m_pt2.group(2))
        return ("construct", f"**point**\\ ({target}) → {pts}", None)

    # 19. General construction vs assertion classification
    cleaned = _strip_redundant_type_nouns(s)
    cleaned = re.sub(r"^(?:Now,\s*|Again,\s*|Then,\s*|And\s+|But\s+|For,\s*|For\s+)", "", cleaned)
    if cleaned and cleaned[0].islower():
        cleaned = cleaned[0].upper() + cleaned[1:]

    if re.search(
        r"\blet\b.+\bbe\s+(?:described|constructed|drawn|joined|produced|bisected|cut|placed|applied|made|taken|set\s+up|inscribed|circumscribed|added|subtracted|measured|found)\b",
        s,
        re.IGNORECASE,
    ):
        return ("construct", cleaned, None)
    if re.search(r"\bcut\s+one\s+another\s+at\b|\bmeet\s+(?:one\s+another\s+)?at\b", s, re.IGNORECASE):
        return ("intersect", cleaned, None)
    inferred_rule = None
    if re.search(r"\bis\s+the\s+(?:centre|center)\s+of\b", cleaned, re.IGNORECASE):
        inferred_rule = id_map.get("I.def.15", "G.2")
    return ("assert", cleaned, inferred_rule)


def _strip_redundant_type_nouns(text: str) -> str:
    """Strip verbose Euclidean type prefixes immediately preceding symbolic :g: indications and normalize segment/line/arc."""
    s = text
    patterns = [
        (r"\bthe\s+given\s+finite\s+straight\s+line\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+given\s+infinite\s+straight\s+line\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+given\s+straight\s+line\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+given\s+rectilineal\s+angle\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+given\s+point\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+finite\s+straight\s+line\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+three\s+straight\s+lines\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+two\s+straight\s+lines\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+straight\s+lines\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+straight\s+line\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+points\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+point\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+circles\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+circle\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+rectilineal\s+angles\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+rectilineal\s+angle\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+angles\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+angle\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+triangles\s+(:g:`[^`]+`)", r"\1"),
        (r"\bthe\s+triangle\s+(:g:`[^`]+`)", r"\1"),
        (r"\bfinite\s+straight\s+lines\b", "segments"),
        (r"\bfinite\s+straight\s+line\b", "segment"),
        (r"\binfinite\s+straight\s+lines\b", "lines"),
        (r"\binfinite\s+straight\s+line\b", "line"),
        (r"\bparallel\s+straight\s+lines\b", "parallel lines"),
        (r"\bstraight\s+lines\b", "segments"),
        (r"\bstraight\s+line\b", "segment"),
        (r"\bcircumferences\b", "arcs"),
        (r"\bcircumference\b", "arc"),
        (r"\bcentre\b", "center"),
    ]
    for pat, repl in patterns:
        s = re.sub(pat, repl, s, flags=re.IGNORECASE)
    return s


def _format_rule_justification(
    just_targets: List[str],
    g_to_sem_name: Dict[str, str],
) -> Optional[str]:
    """Format a list of G.<n> targets into a `∵ rule_name <G.n>` justification argument."""
    if not just_targets:
        return None
    rule_names = [g_to_sem_name.get(t, t) for t in just_targets]
    rules_str = ", ".join(rule_names)
    targets_str = ", ".join(just_targets)
    return f"∵ {rules_str} <{targets_str}>"


def _build_signature_block(
    canonical_ref: str,
    node_type: str,
    subtype: Optional[str],
    g_name: str,
    sem_name: str,
    given_steps: List[str],
    goal_clauses: List[str],
    conclude_body: Optional[str],
    construct_steps: List[str],
) -> str:
    """Build a `.. signature::` RST block for a G-node."""
    fn_self = f":fn:`{sem_name} <{g_name}>`" if g_name else f"**{sem_name}**"

    # Special foundational definitions, postulates, and common notions with interactive :g: symbols
    if canonical_ref == "I.def.1":
        return f".. signature:: def\n\n   | {fn_self}\\ (:g:`A <g1:A>`)"
    if canonical_ref == "I.def.2":
        return f".. signature:: def\n\n   | {fn_self}\\ (:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`[ A B ] <g1:[ A B ]>`"
    if canonical_ref == "I.def.3":
        return f".. signature:: def\n\n   | {fn_self}\\ (:g:`/ A B / <g1:/ A B />`) → :g:`A <g1:A>`, :g:`B <g1:B>`"
    if canonical_ref == "I.def.4":
        return f".. signature:: def\n\n   | {fn_self}\\ (:g:`[ A B ] <g1:[ A B ]>`, :g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ A B / <g1:/ A B />`"
    if canonical_ref == "I.def.15":
        return f".. signature:: def\n\n   | {fn_self}\\ (:g:`( A B ) <g1:( B C D )>`) → :eq:`/ A B / = / A C / = / A D / <g1:/ A B / = g1:/ A C / = g1:/ A D />`"
    if canonical_ref == "I.def.16":
        return f".. signature:: def\n\n   | {fn_self}\\ (:g:`( A B ) <g1:( B C D )>`) → :g:`A <g1:A>`"
    if canonical_ref == "I.def.20":
        return f".. signature:: def\n\n   | {fn_self}\\ (:g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>`, :g:`< G H K > <g1:< G H K >>`)"
    if canonical_ref == "I.post.1":
        return (
            f".. signature:: postulate\n\n"
            f"   | {fn_self}\\ (:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ A B / <g1:/ A B />`\n"
            f"   | **given** :g:`A <g1:A>`, :g:`B <g1:B>`\n"
            f"   | **construct** :g:`/ A B / <g1:/ A B />`"
        )
    if canonical_ref == "I.post.2":
        return (
            f".. signature:: postulate\n\n"
            f"   | {fn_self}\\ (:g:`/ A B / <g1:/ A B />`) → :g:`/ B C / <g1:/ B C />`\n"
            f"   | **given** :g:`/ A B / <g1:/ A B />` on :g:`[ A B ] <g1:[ A B ]>`\n"
            f"   | **construct** :g:`/ B C / <g1:/ B C />`"
        )
    if canonical_ref == "I.post.3":
        return (
            f".. signature:: postulate\n\n"
            f"   | {fn_self}\\ (:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`( A B ) <g1:( B C D )>`\n"
            f"   | **given** :g:`A <g1:A>`, :g:`B <g1:B>`\n"
            f"   | **construct** :g:`( A B ) <g1:( B C D )>`"
        )
    if canonical_ref == "I.cn.4":
        return (
            f".. signature:: rule\n\n"
            f"   | {fn_self}\\ (:g:`/ A B / <g1:/ A B />`, :g:`/ D E / <g1:/ D E />`)"
        )

    if node_type in ("def", "post", "cn"):
        sig_kind = "rule" if node_type in ("cn", "post") else "def"
        return f".. signature:: {sig_kind}\n\n   | {fn_self}"

    sig_kind = subtype if subtype in ("problem", "theorem") else "prop"
    given_text = "; ".join(given_steps).strip()

    # Extract distinct :g: roles from given_text
    given_roles: List[str] = []
    given_targets: set[str] = set()
    for m in re.finditer(r":g:`([^`]+?)\s+<([^`]+)>`", given_text):
        t = m.group(2).strip()
        if t not in given_targets:
            given_targets.add(t)
            given_roles.append(m.group(0))

    cleaned_conclude = ""
    if conclude_body:
        cleaned_conclude = re.sub(
            r"^(?:Therefore,?\s*(?:given\s+.+?,\s*(?=from\b|at\b|on\b|in\b|to\b))?|Thus\s+|Hence\s+|So\s+that\s+)",
            "",
            conclude_body.strip(),
            flags=re.IGNORECASE,
        ).strip()
        cleaned_conclude = re.sub(
            r",?\s*and\s+it\s+has\s+been\s+constructed.*$",
            "",
            cleaned_conclude,
            flags=re.IGNORECASE,
        ).rstrip(".")

    # Determine return symbol(s) and goal text for problems vs theorems
    ret_roles: List[str] = []
    if sig_kind == "problem":
        # Prefer conclude_body (or goal_clauses with :eq:) for extracting constructed return symbols
        sources = [cleaned_conclude, "; ".join(goal_clauses)]
        seen_ret: set[str] = set()
        for src in sources:
            if not src:
                continue
            for m in re.finditer(r":g:`([^`]+?)\s+<([^`]+)>`", src):
                t = m.group(2).strip()
                if t not in given_targets and t not in seen_ret:
                    seen_ret.add(t)
                    ret_roles.append(m.group(0))
            if ret_roles:
                break
        if not ret_roles and construct_steps:
            m_arrow = re.search(r"→\s*(:g:`[^`]+`)", construct_steps[-1])
            if m_arrow:
                ret_roles.append(m_arrow.group(1))

        # Prefer a goal_clause that already has :eq: or constructed symbols, else cleaned_conclude
        eq_goals = [g for g in goal_clauses if ":eq:`" in g]
        if eq_goals:
            goal_text = "; ".join(eq_goals).strip()
        elif cleaned_conclude:
            goal_text = cleaned_conclude
        else:
            goal_text = "; ".join(goal_clauses).strip()
    else:
        goal_text = "; ".join(goal_clauses).strip() or cleaned_conclude

    args_str = ", ".join(given_roles[:4]) if given_roles else ""
    if sig_kind == "problem" and ret_roles:
        header_line = f"{fn_self}\\ ({args_str}) → {', '.join(ret_roles[:2])}"
    else:
        header_line = f"{fn_self}\\ ({args_str})"

    lines = [f".. signature:: {sig_kind}", "", f"   | {header_line}"]
    if given_text:
        lines.append(f"   | **given** {_symbolize_step_text(given_text)}")
    if goal_text:
        contract_kw = "construct" if sig_kind == "problem" else "prove"
        lines.append(f"   | **{contract_kw}** {_symbolize_step_text(goal_text)}")
    return "\n".join(lines)


def _symbolize_step_text(text: str) -> str:
    """Convert verbose English assertion/conclusion phrases into symbolic operators (=, ≃, >, <, ≠, ⇒⇐)."""
    s = text.strip()
    if not s:
        return s

    # Normalize center-of-circle premise into compact circle -> radii form
    s = re.sub(
        r"^(?:Since\s+)?(:g:`[^`]+`)\s+is\s+the\s+(?:centre|center|:term:`center\s*<[^>]+>`)\s+of\s+(:g:`\(\s*[^`]+`)\s*→\s*",
        r"\2 → ",
        s,
        flags=re.IGNORECASE,
    )

    # Convert :eq:`equal <spec>` phrases to :eq:`= <spec>`
    s = re.sub(
        r"\b(?:(?:is|are|was|were|will\s+be|be)\s+)?(?:also\s+)?(?:proved\s+)?(:eq:`equal\s*<[^>]+>`)\s+to(?:\s+one\s+another|\s+it)?\b",
        r"\1",
        s,
        flags=re.IGNORECASE,
    )
    s = re.sub(r":eq:`equal\s*(<[^>]+>)`", r":eq:`= \1`", s)

    # Convert :coincide:`... <spec>` phrases to :coincide:`≃ <spec>`
    s = re.sub(
        r"\b(?:(?:will|does|do|did|be)\s+)?(?:also\s+)?(:coincide:`(?:coincide[ds]?|coinciding|applied|placed(?:\s+on)?)\s*<[^>]+>`)(?:\s+(?:with|to|on))?\b",
        r"\1",
        s,
        flags=re.IGNORECASE,
    )
    s = re.sub(
        r":coincide:`(?:coincide[ds]?|coinciding|applied|placed(?:\s+on)?)\s*(<[^>]+>)`",
        r":coincide:`≃ \1`",
        s,
    )

    # Convert inequalities and contradictions
    s = re.sub(r"\bis\s+not\s+unequal\s+to\b", "=", s, flags=re.IGNORECASE)
    s = re.sub(r"\bis\s+unequal\s+to\b", "≠", s, flags=re.IGNORECASE)
    s = re.sub(r"\bis\s+much\s+greater\s+than\b", "≫", s, flags=re.IGNORECASE)
    s = re.sub(r"\bis\s+greater\s+than\b", ">", s, flags=re.IGNORECASE)
    s = re.sub(r"\bis\s+less\s+than\b", "<", s, flags=re.IGNORECASE)
    s = re.sub(
        r"\bthe\s+less\s+to\s+the\s+greater:\s*which\s+is\s+(?:absurd|impossible)\.?",
        "< > ⇒⇐",
        s,
        flags=re.IGNORECASE,
    )
    s = re.sub(
        r":?\s*which\s+is\s+(?:absurd|impossible)\.?",
        " ⇒⇐",
        s,
        flags=re.IGNORECASE,
    )

    # Strip leading discourse markers and redundant Euclidean nouns
    s = re.sub(
        r"^(?:Therefore,?\s+|Hence,?\s+|Thus,?\s+|Accordingly,?\s+|Since\s+|In\s+these\s+|And,?\s+)",
        "",
        s,
        flags=re.IGNORECASE,
    )
    s = re.sub(
        r"\b(?:the\s+remainder|the\s+whole\s+angle|the\s+remaining\s+angle|the\s+whole\s+triangle|the\s+whole|the\s+base|the\s+side|the\s+two\s+sides)\s+(?=:g:`)",
        "",
        s,
        flags=re.IGNORECASE,
    )
    s = re.sub(r"\s+respectively\b", "", s, flags=re.IGNORECASE)
    s = re.sub(r"\s{2,}", " ", s).strip(" .;")
    return s


CURATED_PROPOSITIONS: Dict[str, Dict[str, object]] = {
    "I.1": {
        "subtype": "problem",
        "args": [":g:`/ A B / <g1:/ A B />`"],
        "returns": [":g:`< A B C > <g1:< A B C >>`"],
        "given": ":g:`/ A B / <g1:/ A B />`",
        "contract": ":g:`< A B C > <g1:< A B C >>` : :g:`/ C A / <g1:/ C A />` :eq:`= <g1:/ C A / = g1:/ A B / = g1:/ B C />` :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ C A / = g1:/ A B / = g1:/ B C />` :g:`/ B C / <g1:/ B C />`",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />`"),
            ("construct", [], "@fn(I.post.3)(:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`( A B ) <g1:( B C D )>`"),
            ("construct", [], "@fn(I.post.3)(:g:`B <g1:B>`, :g:`A <g1:A>`) → :g:`( B A ) <g1:( A C E )>`"),
            ("intersect", [], ":g:`( A B ) <g1:( B C D )>` ∩ :g:`( B A ) <g1:( A C E )>` → :g:`C <g1:C>`"),
            ("construct", [], "@fn(I.post.1)(:g:`C <g1:C>`, :g:`A <g1:A>`) → :g:`/ C A / <g1:/ C A />`, @fn(I.post.1)(:g:`C <g1:C>`, :g:`B <g1:B>`) → :g:`/ C B / <g1:/ C B />`"),
            ("assert", ["I.def.15"], ":g:`( A B ) <g1:( C D B )>` → :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ A B />` :g:`/ A B / <g1:/ A B />`"),
            ("assert", ["I.def.15"], ":g:`( B A ) <g1:( C A E )>` → :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ B A />` :g:`/ B A / <g1:/ B A />`"),
            ("assert", ["I.cn.1"], ":g:`/ C A / <g1:/ C A />` :eq:`= <g1:/ C A / = g1:/ A B />` :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ A B />` :g:`/ A B / <g1:/ A B />` → :g:`/ C A / <g1:/ C A />` :eq:`= <g1:/ C A / = g1:/ B C />` :g:`/ B C / <g1:/ B C />`"),
            ("conclude", ["I.def.20"], ":g:`/ C A / <g1:/ C A />` :eq:`= <g1:/ C A / = g1:/ A B / = g1:/ B C />` :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ C A / = g1:/ A B / = g1:/ B C />` :g:`/ B C / <g1:/ B C />` → :g:`< A B C > <g1:< A B C >>`"),
        ],
    },
    "I.2": {
        "subtype": "problem",
        "args": [":g:`A <g1:A>`", ":g:`/ B C / <g1:/ B C />`"],
        "returns": [":g:`/ A L / <g1:/ A L />`"],
        "given": ":g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />`",
        "contract": ":g:`/ A L / <g1:/ A L />` :eq:`= <g1:/ A L / = g1:/ B C />` :g:`/ B C / <g1:/ B C />`",
        "steps": [
            ("given", [], ":g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />`"),
            ("construct", [], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ A B / <g1:/ A B />`"),
            ("construct", [], "@fn(I.1)(:g:`/ A B / <g1:/ A B />`) → :g:`< D A B > <g1:< D A B >>` (:g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ D B / = g1:/ A B />` :g:`/ D B / <g1:/ D B />` :eq:`= <g1:/ D A / = g1:/ D B / = g1:/ A B />` :g:`/ A B / <g1:/ A B />`)"),
            ("construct", [], "@fn(I.post.2)(:g:`/ D A / <g1:/ D A />`) → :g:`/ A E / <g1:/ A E />`, @fn(I.post.2)(:g:`/ D B / <g1:/ D B />`) → :g:`/ B F / <g1:/ B F />`"),
            ("construct", [], "@fn(I.post.3)(:g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`( B C ) <g1:( B C )>`"),
            ("intersect", [], ":g:`( B C ) <g1:( B C )>` ∩ :g:`/ B F / <g1:/ B F />` → :g:`G <g1:G>`"),
            ("construct", [], "@fn(I.post.3)(:g:`D <g1:D>`, :g:`G <g1:G>`) → :g:`( D G ) <g1:( D G )>`"),
            ("intersect", [], ":g:`( D G ) <g1:( D G )>` ∩ :g:`/ A E / <g1:/ A E />` → :g:`L <g1:L>`"),
            ("assert", ["I.def.15"], ":g:`( B C ) <g1:( B C )>` → :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ B G />` :g:`/ B G / <g1:/ B G />`"),
            ("assert", ["I.def.15"], ":g:`( D G ) <g1:( D G )>` → :g:`/ D L / <g1:/ D L />` :eq:`= <g1:/ D L / = g1:/ D G />` :g:`/ D G / <g1:/ D G />`"),
            ("assert", ["I.cn.3"], ":g:`/ D L / <g1:/ D L />` :eq:`= <g1:/ D L / = g1:/ D G />` :g:`/ D G / <g1:/ D G />`, :g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ D B />` :g:`/ D B / <g1:/ D B />` → :g:`/ A L / <g1:/ A L />` :eq:`= <g1:/ A L / = g1:/ B G />` :g:`/ B G / <g1:/ B G />`"),
            ("conclude", ["I.cn.1"], ":g:`/ A L / <g1:/ A L />` :eq:`= <g1:/ A L / = g1:/ B G />` :g:`/ B G / <g1:/ B G />`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ B G />` :g:`/ B G / <g1:/ B G />` → :g:`/ A L / <g1:/ A L />` :eq:`= <g1:/ A L / = g1:/ B C />` :g:`/ B C / <g1:/ B C />`"),
        ],
    },
    "I.3": {
        "subtype": "problem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`/ C / <g1:/ C />`"],
        "returns": [":g:`/ A E / <g1:/ A E />`"],
        "given": ":g:`/ A B / <g1:/ A B />` > :g:`/ C / <g1:/ C />`",
        "contract": ":g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ C />` :g:`/ C / <g1:/ C />`",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` > :g:`/ C / <g1:/ C />`"),
            ("construct", [], "@fn(I.2)(:g:`A <g1:A>`, :g:`/ C / <g1:/ C />`) → :g:`/ A D / <g1:/ A D />` (:eq:`= <g1:/ A D / = g1:/ C />` :g:`/ C / <g1:/ C />`)"),
            ("construct", [], "@fn(I.post.3)(:g:`A <g1:A>`, :g:`D <g1:D>`) → :g:`( A D ) <g1:( D E F )>`"),
            ("intersect", [], ":g:`( A D ) <g1:( D E F )>` ∩ :g:`/ A B / <g1:/ A B />` → :g:`E <g1:E>`"),
            ("assert", ["I.def.15"], ":g:`( A D ) <g1:( D E F )>` → :g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ A D />` :g:`/ A D / <g1:/ A D />`"),
            ("conclude", ["I.cn.1"], ":g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ A D />` :g:`/ A D / <g1:/ A D />`, :g:`/ C / <g1:/ C />` :eq:`= <g1:/ C / = g1:/ A D />` :g:`/ A D / <g1:/ A D />` → :g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ C />` :g:`/ C / <g1:/ C />`"),
        ],
    },
    "I.4": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< D E F > <g1:< D E F >>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`, :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`",
        "contract": ":g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`, :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D E F >>` :g:`< D E F > <g1:< D E F >>`, :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< D E F )>` :g:`< D E F ) <g1:< D E F )>`, :g:`< A C B ) <g1:< A C B )>` :eq:`= <g1:< A C B ) = g1:< D F E )>` :g:`< D F E ) <g1:< D F E )>`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`, :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`"),
            ("assert", [], ":g:`A <g1:A>` :coincide:`≃ <g1:A ≡ g1:D; g1:/ A B / ≡ g1:/ D E />` :g:`D <g1:D>`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />` → :g:`B <g1:B>` :coincide:`≃ <g1:B ≡ g1:E>` :g:`E <g1:E>`"),
            ("assert", [], ":g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ D F />` :g:`/ D F / <g1:/ D F />` → :g:`/ A C / <g1:/ A C />` :coincide:`≃ <g1:/ A C / ≡ g1:/ D F />` :g:`/ D F / <g1:/ D F />`, :g:`C <g1:C>` :coincide:`≃ <g1:C ≡ g1:F>` :g:`F <g1:F>`"),
            ("assert", ["I.cn.4"], ":g:`B <g1:B>` :coincide:`≃ <g1:B ≡ g1:E>` :g:`E <g1:E>`, :g:`C <g1:C>` :coincide:`≃ <g1:C ≡ g1:F>` :g:`F <g1:F>` → :g:`/ B C / <g1:/ B C />` :coincide:`≃ <g1:/ B C / ≡ g1:/ E F />` :g:`/ E F / <g1:/ E F />` → :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`"),
            ("conclude", ["I.cn.4"], ":g:`< A B C > <g1:< A B C >>` :coincide:`≃ <g1:< A B C > ≡ g1:< D E F >>` :g:`< D E F > <g1:< D E F >>` → :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D E F >>` :g:`< D E F > <g1:< D E F >>`, :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< D E F )>` :g:`< D E F ) <g1:< D E F )>`, :g:`< A C B ) <g1:< A C B )>` :eq:`= <g1:< A C B ) = g1:< D F E )>` :g:`< D F E ) <g1:< D F E )>`"),
        ],
    },
    "I.5": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`/ A B / <g1:/ A B />`", ":g:`/ A C / <g1:/ A C />`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ A C />` :g:`/ A C / <g1:/ A C />`",
        "contract": ":g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< A C B )>` :g:`< A C B ) <g1:< A C B )>`, :g:`< C B D ) <g1:< C B D )>` :eq:`= <g1:< C B D ) = g1:< B C E )>` :g:`< B C E ) <g1:< B C E )>`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ A C />` :g:`/ A C / <g1:/ A C />`"),
            ("construct", [], "@fn(I.post.2)(:g:`/ A B / <g1:/ A B />`) → :g:`/ B D / <g1:/ B D />`, @fn(I.post.2)(:g:`/ A C / <g1:/ A C />`) → :g:`/ C E / <g1:/ C E />`"),
            ("construct", [], "**point**\\ (:g:`/ B D / <g1:/ B D />`) → :g:`F <g1:F>`"),
            ("construct", [], "@fn(I.3)(:g:`/ A E / <g1:/ A E />`, :g:`/ A F / <g1:/ A F />`) → :g:`/ A G / <g1:/ A G />` (:eq:`= <g1:/ A G / = g1:/ A F />` :g:`/ A F / <g1:/ A F />`)"),
            ("construct", [], "@fn(I.post.1)(:g:`F <g1:F>`, :g:`C <g1:C>`) → :g:`/ F C / <g1:/ F C />`, @fn(I.post.1)(:g:`G <g1:G>`, :g:`B <g1:B>`) → :g:`/ G B / <g1:/ G B />`"),
            ("assert", ["I.4"], ":g:`/ F A / <g1:/ F A />` :eq:`= <g1:/ F A / = g1:/ G A />` :g:`/ G A / <g1:/ G A />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ A B />` :g:`/ A B / <g1:/ A B />`, :g:`< F A G ) <g1:< F A G )>` → :g:`/ F C / <g1:/ F C />` :eq:`= <g1:/ F C / = g1:/ G B />` :g:`/ G B / <g1:/ G B />`, :g:`< A C F ) <g1:< A C F )>` :eq:`= <g1:< A C F ) = g1:< A B G )>` :g:`< A B G ) <g1:< A B G )>`, :g:`< A F C ) <g1:< A F C )>` :eq:`= <g1:< A F C ) = g1:< A G B )>` :g:`< A G B ) <g1:< A G B )>`"),
            ("assert", ["I.cn.3"], ":g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ A G />` :g:`/ A G / <g1:/ A G />`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ A C />` :g:`/ A C / <g1:/ A C />` → :g:`/ B F / <g1:/ B F />` :eq:`= <g1:/ B F / = g1:/ C G />` :g:`/ C G / <g1:/ C G />`"),
            ("assert", ["I.4"], ":g:`/ B F / <g1:/ B F />` :eq:`= <g1:/ B F / = g1:/ C G />` :g:`/ C G / <g1:/ C G />`, :g:`/ F C / <g1:/ F C />` :eq:`= <g1:/ F C / = g1:/ G B />` :g:`/ G B / <g1:/ G B />`, :g:`< B F C ) <g1:< B F C )>` :eq:`= <g1:< B F C ) = g1:< C G B )>` :g:`< C G B ) <g1:< C G B )>` → :g:`< F B C ) <g1:< F B C )>` :eq:`= <g1:< F B C ) = g1:< G C B )>` :g:`< G C B ) <g1:< G C B )>`, :g:`< B C F ) <g1:< B C F )>` :eq:`= <g1:< B C F ) = g1:< C B G )>` :g:`< C B G ) <g1:< C B G )>`"),
            ("conclude", ["I.cn.3"], ":g:`< A B G ) <g1:< A B G )>` :eq:`= <g1:< A B G ) = g1:< A C F )>` :g:`< A C F ) <g1:< A C F )>`, :g:`< C B G ) <g1:< C B G )>` :eq:`= <g1:< C B G ) = g1:< B C F )>` :g:`< B C F ) <g1:< B C F )>` → :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< A C B )>` :g:`< A C B ) <g1:< A C B )>`"),
        ],
    },
    "I.6": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< A B C ) <g1:< A B C )>`", ":g:`< A C B ) <g1:< A C B )>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< A C B )>` :g:`< A C B ) <g1:< A C B )>`",
        "contract": ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ A C />` :g:`/ A C / <g1:/ A C />`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< A C B )>` :g:`< A C B ) <g1:< A C B )>`"),
            ("assert", [], "? :g:`/ A B / <g1:/ A B />` ≠ :g:`/ A C / <g1:/ A C />` → :g:`/ A B / <g1:/ A B />` > :g:`/ A C / <g1:/ A C />`"),
            ("construct", [], "@fn(I.3)(:g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />`) → :g:`/ D B / <g1:/ D B />` (:eq:`= <g1:/ D B / = g1:/ A C />` :g:`/ A C / <g1:/ A C />`)"),
            ("construct", [], "@fn(I.post.1)(:g:`D <g1:D>`, :g:`C <g1:C>`) → :g:`/ D C / <g1:/ D C />`"),
            ("assert", ["I.4"], ":g:`/ D B / <g1:/ D B />` :eq:`= <g1:/ D B / = g1:/ A C />` :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`, :g:`< D B C ) <g1:< D B C )>` :eq:`= <g1:< D B C ) = g1:< A C B )>` :g:`< A C B ) <g1:< A C B )>` → :g:`< D B C > <g1:< D B C >>` :eq:`= <g1:< D B C > = g1:< A C B >>` :g:`< A C B > <g1:< A C B >>`"),
            ("assert", ["I.cn.5"], ":g:`< D B C > <g1:< D B C >>` < :g:`< A C B > <g1:< A C B >>` ⇒⇐"),
            ("conclude", [], ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ A C />` :g:`/ A C / <g1:/ A C />`"),
        ],
    },
    "I.7": {
        "subtype": "theorem",
        "args": [":g:`/ A C / <g1:/ A C />`", ":g:`/ C B / <g1:/ C B />`", ":g:`/ A B / <g1:/ A B />`", ":g:`C <g1:C>`"],
        "returns": [],
        "given": ":g:`/ A C / <g1:/ A C />`, :g:`/ C B / <g1:/ C B />` on :g:`/ A B / <g1:/ A B />` at :g:`C <g1:C>`",
        "contract": "¬∃ :g:`D <g1:D>` ≠ :g:`C <g1:C>` : :g:`/ C A / <g1:/ C A />` :eq:`= <g1:/ C A / = g1:/ D A />` :g:`/ D A / <g1:/ D A />`, :g:`/ C B / <g1:/ C B />` :eq:`= <g1:/ C B / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`",
        "steps": [
            ("given", [], ":g:`/ A C / <g1:/ A C />`, :g:`/ C B / <g1:/ C B />` on :g:`/ A B / <g1:/ A B />` at :g:`C <g1:C>`"),
            ("assert", [], "? :g:`/ A D / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />` on :g:`/ A B / <g1:/ A B />` at :g:`D <g1:D>` : :g:`/ C A / <g1:/ C A />` :eq:`= <g1:/ C A / = g1:/ D A />` :g:`/ D A / <g1:/ D A />`, :g:`/ C B / <g1:/ C B />` :eq:`= <g1:/ C B / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`"),
            ("construct", [], "@fn(I.post.1)(:g:`C <g1:C>`, :g:`D <g1:D>`) → :g:`/ C D / <g1:/ C D />`"),
            ("assert", ["I.5"], ":g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ A D />` :g:`/ A D / <g1:/ A D />` → :g:`< A C D ) <g1:< A C D )>` :eq:`= <g1:< A C D ) = g1:< A D C )>` :g:`< A D C ) <g1:< A D C )>`"),
            ("assert", ["I.cn.5"], ":g:`< A C D ) <g1:< A C D )>` > :g:`< D C B ) <g1:< D C B )>` → :g:`< A D C ) <g1:< A D C )>` > :g:`< D C B ) <g1:< D C B )>` → :g:`< C D B ) <g1:< C D B )>` ≫ :g:`< D C B ) <g1:< D C B )>`"),
            ("assert", ["I.5"], ":g:`/ C B / <g1:/ C B />` :eq:`= <g1:/ C B / = g1:/ D B />` :g:`/ D B / <g1:/ D B />` → :g:`< C D B ) <g1:< C D B )>` :eq:`= <g1:< C D B ) = g1:< D C B )>` :g:`< D C B ) <g1:< D C B )>` ⇒⇐"),
            ("conclude", [], "¬∃ :g:`D <g1:D>` ≠ :g:`C <g1:C>` : :g:`/ C A / <g1:/ C A />` :eq:`= <g1:/ C A / = g1:/ D A />` :g:`/ D A / <g1:/ D A />`, :g:`/ C B / <g1:/ C B />` :eq:`= <g1:/ C B / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`"),
        ],
    },
    "I.8": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< D E F > <g1:< D E F >>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`",
        "contract": ":g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`"),
            ("assert", [], ":g:`B <g1:B>` :coincide:`≃ <g1:B ≡ g1:E; g1:/ B C / ≡ g1:/ E F />` :g:`E <g1:E>`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />` → :g:`C <g1:C>` :coincide:`≃ <g1:C ≡ g1:F>` :g:`F <g1:F>`, :g:`/ B C / <g1:/ B C />` :coincide:`≃ <g1:/ B C / ≡ g1:/ E F />` :g:`/ E F / <g1:/ E F />`"),
            ("assert", ["I.7"], "? ¬(:g:`/ B A / <g1:/ B A />` :coincide:`≃ <g1:/ B A / ≡ g1:/ E D />; g1:/ A C / ≡ g1:/ D F />` :g:`/ E D / <g1:/ E D />`, :g:`/ A C / <g1:/ A C />` :coincide:`≃ <g1:/ B A / ≡ g1:/ E D />; g1:/ A C / ≡ g1:/ D F />` :g:`/ D F / <g1:/ D F />`) → :g:`/ E G / <g1:/ E G />` :eq:`= <g1:/ E D / = g1:/ E G />; g1:/ D F / = g1:/ G F />` :g:`/ E D / <g1:/ E D />`, :g:`/ G F / <g1:/ G F />` :eq:`= <g1:/ E D / = g1:/ E G />; g1:/ D F / = g1:/ G F />` :g:`/ D F / <g1:/ D F />` ⇒⇐"),
            ("assert", [], ":g:`/ B A / <g1:/ B A />` :coincide:`≃ <g1:/ B A / ≡ g1:/ E D />; g1:/ A C / ≡ g1:/ D F />` :g:`/ E D / <g1:/ E D />`, :g:`/ A C / <g1:/ A C />` :coincide:`≃ <g1:/ B A / ≡ g1:/ E D />; g1:/ A C / ≡ g1:/ D F />` :g:`/ D F / <g1:/ D F />`"),
            ("conclude", ["I.cn.4"], ":g:`< B A C ) <g1:< B A C )>` :coincide:`≃ <g1:< B A C ) ≡ g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>` → :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`"),
        ],
    },
    "I.9": {
        "subtype": "problem",
        "args": [":g:`< B A C ) <g1:< B A C )>`"],
        "returns": [":g:`/ A F / <g1:/ A F />`"],
        "given": ":g:`< B A C ) <g1:< B A C )>`",
        "contract": ":g:`/ A F / <g1:/ A F />` : :g:`< D A F ) <g1:< D A F )>` :eq:`= <g1:< D A F ) = g1:< E A F )>` :g:`< E A F ) <g1:< E A F )>`",
        "steps": [
            ("given", [], ":g:`< B A C ) <g1:< B A C )>`"),
            ("construct", [], "**point**\\ (:g:`/ A B / <g1:/ A B />`) → :g:`D <g1:D>`"),
            ("construct", [], "@fn(I.3)(:g:`/ A C / <g1:/ A C />`, :g:`/ A D / <g1:/ A D />`) → :g:`/ A E / <g1:/ A E />` (:eq:`= <g1:/ A E / = g1:/ A D />` :g:`/ A D / <g1:/ A D />`)"),
            ("construct", [], "@fn(I.post.1)(:g:`D <g1:D>`, :g:`E <g1:E>`) → :g:`/ D E / <g1:/ D E />`"),
            ("construct", [], "@fn(I.1)(:g:`/ D E / <g1:/ D E />`) → :g:`< D E F > <g1:< D E F >>` (:g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ D E / = g1:/ D F / = g1:/ E F />` :g:`/ D F / <g1:/ D F />` :eq:`= <g1:/ D E / = g1:/ D F / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`)"),
            ("construct", [], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`F <g1:F>`) → :g:`/ A F / <g1:/ A F />`"),
            ("conclude", ["I.8"], ":g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ E A />` :g:`/ E A / <g1:/ E A />`, :g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ A F />` :g:`/ A F / <g1:/ A F />`, :g:`/ D F / <g1:/ D F />` :eq:`= <g1:/ D F / = g1:/ E F />` :g:`/ E F / <g1:/ E F />` → :g:`< D A F ) <g1:< D A F )>` :eq:`= <g1:< D A F ) = g1:< E A F )>` :g:`< E A F ) <g1:< E A F )>`"),
        ],
    },
    "I.10": {
        "subtype": "problem",
        "args": [":g:`/ A B / <g1:/ A B />`"],
        "returns": [":g:`D <g1:D>`"],
        "given": ":g:`/ A B / <g1:/ A B />`",
        "contract": ":g:`D <g1:D>` ∈ :g:`/ A B / <g1:/ A B />` : :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ B D />` :g:`/ B D / <g1:/ B D />`",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />`"),
            ("construct", [], "@fn(I.1)(:g:`/ A B / <g1:/ A B />`) → :g:`< A B C > <g1:< A B C >>` (:g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ A C / = g1:/ B C />` :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A B / = g1:/ A C / = g1:/ B C />` :g:`/ B C / <g1:/ B C />`)"),
            ("construct", [], "@fn(I.9)(:g:`< A C B ) <g1:< A C B )>`) → :g:`/ C D / <g1:/ C D />` (:g:`< A C D ) <g1:< A C D )>` :eq:`= <g1:< A C D ) = g1:< B C D )>` :g:`< B C D ) <g1:< B C D )>`)"),
            ("conclude", ["I.4"], ":g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ B C />` :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />` :eq:`= <g1:/ C D / = g1:/ C D />` :g:`/ C D / <g1:/ C D />`, :g:`< A C D ) <g1:< A C D )>` :eq:`= <g1:< A C D ) = g1:< B C D )>` :g:`< B C D ) <g1:< B C D )>` → :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ B D />` :g:`/ B D / <g1:/ B D />`"),
        ],
    },
    "I.11": {
        "subtype": "problem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`C <g1:C>`"],
        "returns": [":g:`/ C F / <g1:/ C F />`"],
        "given": ":g:`/ A B / <g1:/ A B />`, :g:`C <g1:C>` ∈ :g:`/ A B / <g1:/ A B />`",
        "contract": ":g:`/ C F / <g1:/ C F />` ⊥ :g:`/ A B / <g1:/ A B />` (:g:`< D C F ) <g1:< D C F )>` :eq:`= <g1:< D C F ) = g1:< F C E )>` :g:`< F C E ) <g1:< F C E )>`)",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />`, :g:`C <g1:C>` ∈ :g:`/ A B / <g1:/ A B />`"),
            ("construct", [], "**point**\\ (:g:`/ A C / <g1:/ A C />`) → :g:`D <g1:D>`"),
            ("construct", [], "@fn(I.3)(:g:`/ C B / <g1:/ C B />`, :g:`/ C D / <g1:/ C D />`) → :g:`/ C E / <g1:/ C E />` (:eq:`= <g1:/ C E / = g1:/ C D />` :g:`/ C D / <g1:/ C D />`)"),
            ("construct", [], "@fn(I.1)(:g:`/ D E / <g1:/ D E />`) → :g:`< F D E > <g1:< F D E >>` (:g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ D E / = g1:/ D F / = g1:/ F E />` :g:`/ D F / <g1:/ D F />` :eq:`= <g1:/ D E / = g1:/ D F / = g1:/ F E />` :g:`/ F E / <g1:/ F E />`)"),
            ("construct", [], "@fn(I.post.1)(:g:`F <g1:F>`, :g:`C <g1:C>`) → :g:`/ F C / <g1:/ F C />`"),
            ("assert", ["I.8"], ":g:`/ D C / <g1:/ D C />` :eq:`= <g1:/ D C / = g1:/ E C />` :g:`/ E C / <g1:/ E C />`, :g:`/ C F / <g1:/ C F />` :eq:`= <g1:/ C F / = g1:/ C F />` :g:`/ C F / <g1:/ C F />`, :g:`/ D F / <g1:/ D F />` :eq:`= <g1:/ D F / = g1:/ F E />` :g:`/ F E / <g1:/ F E />` → :g:`< D C F ) <g1:< D C F )>` :eq:`= <g1:< D C F ) = g1:< E C F )>` :g:`< E C F ) <g1:< E C F )>`"),
            ("conclude", ["I.def.10"], ":g:`< D C F ) <g1:< D C F )>` :eq:`= <g1:< D C F ) = g1:< F C E )>` :g:`< F C E ) <g1:< F C E )>` → :g:`/ C F / <g1:/ C F />` ⊥ :g:`/ A B / <g1:/ A B />`"),
        ],
    },
    "I.12": {
        "subtype": "problem",
        "args": [":g:`[ A B ] <g1:[ A B ]>`", ":g:`C <g1:C>`"],
        "returns": [":g:`/ C H / <g1:/ C H />`"],
        "given": ":g:`[ A B ] <g1:[ A B ]>`, :g:`C <g1:C>` ∉ :g:`[ A B ] <g1:[ A B ]>`",
        "contract": ":g:`/ C H / <g1:/ C H />` ⊥ :g:`[ A B ] <g1:[ A B ]>` (:g:`< C H G ) <g1:< C H G )>` :eq:`= <g1:< C H G ) = g1:< E H C )>` :g:`< E H C ) <g1:< E H C )>`)",
        "steps": [
            ("given", [], ":g:`[ A B ] <g1:[ A B ]>`, :g:`C <g1:C>` ∉ :g:`[ A B ] <g1:[ A B ]>`"),
            ("construct", [], "**point**\\ (:g:`[ A B ] <g1:[ A B ]>`) → :g:`D <g1:D>`"),
            ("construct", [], "@fn(I.post.3)(:g:`C <g1:C>`, :g:`D <g1:D>`) → :g:`( C D ) <g1:( C D )>`"),
            ("intersect", [], ":g:`( C D ) <g1:( C D )>` ∩ :g:`[ A B ] <g1:[ A B ]>` → :g:`E <g1:E>`, :g:`G <g1:G>`"),
            ("construct", [], "@fn(I.10)(:g:`/ E G / <g1:/ E G />`) → :g:`H <g1:H>` (:g:`/ G H / <g1:/ G H />` :eq:`= <g1:/ G H / = g1:/ H E />` :g:`/ H E / <g1:/ H E />`)"),
            ("construct", [], "@fn(I.post.1)(:g:`C <g1:C>`, :g:`G <g1:G>`) → :g:`/ C G / <g1:/ C G />`, @fn(I.post.1)(:g:`C <g1:C>`, :g:`H <g1:H>`) → :g:`/ C H / <g1:/ C H />`, @fn(I.post.1)(:g:`C <g1:C>`, :g:`E <g1:E>`) → :g:`/ C E / <g1:/ C E />`"),
            ("assert", ["I.def.15"], ":g:`( C D ) <g1:( C D )>` → :g:`/ C G / <g1:/ C G />` :eq:`= <g1:/ C G / = g1:/ C E />` :g:`/ C E / <g1:/ C E />`"),
            ("assert", ["I.8"], ":g:`/ G H / <g1:/ G H />` :eq:`= <g1:/ G H / = g1:/ E H />` :g:`/ E H / <g1:/ E H />`, :g:`/ H C / <g1:/ H C />` :eq:`= <g1:/ H C / = g1:/ H C />` :g:`/ H C / <g1:/ H C />`, :g:`/ C G / <g1:/ C G />` :eq:`= <g1:/ C G / = g1:/ C E />` :g:`/ C E / <g1:/ C E />` → :g:`< C H G ) <g1:< C H G )>` :eq:`= <g1:< C H G ) = g1:< E H C )>` :g:`< E H C ) <g1:< E H C )>`"),
            ("conclude", ["I.def.10"], ":g:`< C H G ) <g1:< C H G )>` :eq:`= <g1:< C H G ) = g1:< E H C )>` :g:`< E H C ) <g1:< E H C )>` → :g:`/ C H / <g1:/ C H />` ⊥ :g:`[ A B ] <g1:[ A B ]>`"),
        ],
    },
    "I.13": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`/ C D / <g1:/ C D />`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` on :g:`/ C D / <g1:/ C D />` → :g:`< C B A ) <g1:< C B A )>`, :g:`< A B D ) <g1:< A B D )>`",
        "contract": ":g:`< C B A ) <g1:< C B A )>` + :g:`< A B D ) <g1:< A B D )>` :eq:`= <g1:< C B E ) = g1:< E B D )>` :g:`< C B E ) <g1:< C B E )>` + :g:`< E B D ) <g1:< E B D )>`",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` on :g:`/ C D / <g1:/ C D />` → :g:`< C B A ) <g1:< C B A )>`, :g:`< A B D ) <g1:< A B D )>`"),
            ("assert", ["I.def.10"], "? :g:`< C B A ) <g1:< C B A )>` :eq:`= <g1:< C B A ) = g1:< A B D )>` :g:`< A B D ) <g1:< A B D )>` → :g:`/ A B / <g1:/ A B />` ⊥ :g:`/ C D / <g1:/ C D />`"),
            ("construct", [], "@fn(I.11)(:g:`/ C D / <g1:/ C D />`, :g:`B <g1:B>`) → :g:`/ B E / <g1:/ B E />` ⊥ :g:`/ C D / <g1:/ C D />` (:g:`< C B E ) <g1:< C B E )>` :eq:`= <g1:< C B E ) = g1:< E B D )>` :g:`< E B D ) <g1:< E B D )>`)"),
            ("assert", ["I.cn.2"], ":g:`< C B E ) <g1:< C B E )>` = :g:`< C B A ) <g1:< C B A )>` + :g:`< A B E ) <g1:< A B E )>` → :g:`< C B E ) <g1:< C B E )>` + :g:`< E B D ) <g1:< E B D )>` = :g:`< C B A ) <g1:< C B A )>` + :g:`< A B E ) <g1:< A B E )>` + :g:`< E B D ) <g1:< E B D )>`"),
            ("assert", ["I.cn.2"], ":g:`< D B A ) <g1:< D B A )>` = :g:`< D B E ) <g1:< D B E )>` + :g:`< E B A ) <g1:< E B A )>` → :g:`< D B A ) <g1:< D B A )>` + :g:`< A B C ) <g1:< A B C )>` = :g:`< D B E ) <g1:< D B E )>` + :g:`< E B A ) <g1:< E B A )>` + :g:`< A B C ) <g1:< A B C )>`"),
            ("conclude", ["I.cn.1"], ":g:`< C B A ) <g1:< C B A )>` + :g:`< A B D ) <g1:< A B D )>` :eq:`= <g1:< C B E ) = g1:< E B D )>` :g:`< C B E ) <g1:< C B E )>` + :g:`< E B D ) <g1:< E B D )>`"),
        ],
    },
    "I.14": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`/ B C / <g1:/ B C />`", ":g:`/ B D / <g1:/ B D />`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ B D / <g1:/ B D />` (:g:`< A B C ) <g1:< A B C )>` + :g:`< A B D ) <g1:< A B D )>` = 2∟)",
        "contract": ":g:`/ C B / <g1:/ C B />`, :g:`/ B D / <g1:/ B D />` ∈ :g:`[ C D ] <g1:[ C D ]>`",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ B D / <g1:/ B D />` (:g:`< A B C ) <g1:< A B C )>` + :g:`< A B D ) <g1:< A B D )>` = 2∟)"),
            ("construct", [], "? :g:`/ B D / <g1:/ B D />` ∉ :g:`[ C B ] <g1:[ C B ]>` → @fn(I.post.2)(:g:`/ C B / <g1:/ C B />`) → :g:`/ B E / <g1:/ B E />` ∈ :g:`[ C B ] <g1:[ C B ]>`"),
            ("assert", ["I.13"], ":g:`/ A B / <g1:/ A B />` on :g:`/ C B E / <g1:/ C B E />` → :g:`< A B C ) <g1:< A B C )>` + :g:`< A B E ) <g1:< A B E )>` = 2∟"),
            ("assert", ["I.post.4", "I.cn.1"], ":g:`< C B A ) <g1:< C B A )>` + :g:`< A B E ) <g1:< A B E )>` :eq:`= <g1:< A B E ) = g1:< A B D )>` :g:`< C B A ) <g1:< C B A )>` + :g:`< A B D ) <g1:< A B D )>`"),
            ("assert", ["I.cn.3"], "(:g:`< C B A ) <g1:< C B A )>` + :g:`< A B E ) <g1:< A B E )>`) − :g:`< C B A ) <g1:< C B A )>` = (:g:`< C B A ) <g1:< C B A )>` + :g:`< A B D ) <g1:< A B D )>`) − :g:`< C B A ) <g1:< C B A )>` → :g:`< A B E ) <g1:< A B E )>` :eq:`= <g1:< A B E ) = g1:< A B D )>` :g:`< A B D ) <g1:< A B D )>`"),
            ("assert", ["I.cn.5"], ":g:`< A B E ) <g1:< A B E )>` < :g:`< A B D ) <g1:< A B D )>` ∧ :g:`< A B E ) <g1:< A B E )>` :eq:`= <g1:< A B E ) = g1:< A B D )>` :g:`< A B D ) <g1:< A B D )>` ⇒⇐ → :g:`/ B E / <g1:/ B E />` ∉ :g:`[ C B ] <g1:[ C B ]>`"),
            ("conclude", ["I.post.2"], ":g:`/ C B / <g1:/ C B />`, :g:`/ B D / <g1:/ B D />` ∈ :g:`[ C D ] <g1:[ C D ]>`"),
        ],
    },
    "I.15": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`/ C D / <g1:/ C D />`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` ∩ :g:`/ C D / <g1:/ C D />` → :g:`E <g1:E>`",
        "contract": ":g:`< A E C ) <g1:< A E C )>` :eq:`= <g1:< A E C ) = g1:< D E B )>` :g:`< D E B ) <g1:< D E B )>`, :g:`< C E B ) <g1:< C E B )>` :eq:`= <g1:< C E B ) = g1:< A E D )>` :g:`< A E D ) <g1:< A E D )>`",
        "steps": [
            ("intersect", [], ":g:`/ A B / <g1:/ A B />` ∩ :g:`/ C D / <g1:/ C D />` → :g:`E <g1:E>`"),
            ("assert", ["I.13"], ":g:`/ A E / <g1:/ A E />` on :g:`/ C D / <g1:/ C D />` → :g:`< C E A ) <g1:< C E A )>` + :g:`< A E D ) <g1:< A E D )>` = 2∟"),
            ("assert", ["I.13"], ":g:`/ D E / <g1:/ D E />` on :g:`/ A B / <g1:/ A B />` → :g:`< A E D ) <g1:< A E D )>` + :g:`< D E B ) <g1:< D E B )>` = 2∟"),
            ("assert", ["I.post.4", "I.cn.1"], ":g:`< C E A ) <g1:< C E A )>` + :g:`< A E D ) <g1:< A E D )>` = :g:`< A E D ) <g1:< A E D )>` + :g:`< D E B ) <g1:< D E B )>`"),
            ("assert", ["I.cn.3"], "(:g:`< C E A ) <g1:< C E A )>` + :g:`< A E D ) <g1:< A E D )>`) − :g:`< A E D ) <g1:< A E D )>` = (:g:`< A E D ) <g1:< A E D )>` + :g:`< D E B ) <g1:< D E B )>`) − :g:`< A E D ) <g1:< A E D )>` → :g:`< C E A ) <g1:< C E A )>` :eq:`= <g1:< C E A ) = g1:< B E D )>` :g:`< B E D ) <g1:< B E D )>`"),
            ("conclude", ["I.cn.3"], ":g:`< A E C ) <g1:< A E C )>` :eq:`= <g1:< A E C ) = g1:< D E B )>` :g:`< D E B ) <g1:< D E B )>`, :g:`< C E B ) <g1:< C E B )>` :eq:`= <g1:< C E B ) = g1:< A E D )>` :g:`< A E D ) <g1:< A E D )>`"),
        ],
    },
    "I.16": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`/ B C / <g1:/ B C />`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, @fn(I.post.2)(:g:`/ B C / <g1:/ B C />`) → :g:`/ C D / <g1:/ C D />`",
        "contract": ":g:`< A C D ) <g1:< A C D )>` > :g:`< B A C ) <g1:< B A C )>`, :g:`< A C D ) <g1:< A C D )>` > :g:`< C B A ) <g1:< C B A )>`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, @fn(I.post.2)(:g:`/ B C / <g1:/ B C />`) → :g:`/ C D / <g1:/ C D />`"),
            ("construct", [], "@fn(I.10)(:g:`/ A C / <g1:/ A C />`) → :g:`E <g1:E>` (:g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E C />` :g:`/ E C / <g1:/ E C />`)"),
            ("construct", [], "@fn(I.post.1)(:g:`B <g1:B>`, :g:`E <g1:E>`) → :g:`/ B E / <g1:/ B E />`, @fn(I.post.2)(:g:`/ B E / <g1:/ B E />`), @fn(I.3)(:g:`/ B E / <g1:/ B E />`) → :g:`/ E F / <g1:/ E F />` (:eq:`= <g1:/ E F / = g1:/ B E />` :g:`/ B E / <g1:/ B E />`), @fn(I.post.1)(:g:`F <g1:F>`, :g:`C <g1:C>`) → :g:`/ F C / <g1:/ F C />`, @fn(I.post.2)(:g:`/ A C / <g1:/ A C />`) → :g:`/ C G / <g1:/ C G />`"),
            ("assert", ["I.15"], ":g:`/ A C / <g1:/ A C />` ∩ :g:`/ B F / <g1:/ B F />` → :g:`< A E B ) <g1:< A E B )>` :eq:`= <g1:< A E B ) = g1:< F E C )>` :g:`< F E C ) <g1:< F E C )>`"),
            ("assert", ["I.4"], ":g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E C />` :g:`/ E C / <g1:/ E C />`, :g:`/ E B / <g1:/ E B />` :eq:`= <g1:/ E B / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`, :g:`< A E B ) <g1:< A E B )>` :eq:`= <g1:< A E B ) = g1:< F E C )>` :g:`< F E C ) <g1:< F E C )>` → :g:`< A B E > <g1:< A B E >>` :eq:`= <g1:< A B E > = g1:< C F E >>` :g:`< C F E > <g1:< C F E >>`, :g:`< B A E ) <g1:< B A E )>` :eq:`= <g1:< B A E ) = g1:< E C F )>` :g:`< E C F ) <g1:< E C F )>`"),
            ("assert", ["I.cn.5"], ":g:`< E C D ) <g1:< E C D )>` > :g:`< E C F ) <g1:< E C F )>` → :g:`< A C D ) <g1:< A C D )>` > :g:`< B A E ) <g1:< B A E )>`"),
            ("conclude", ["I.10", "I.15"], ":g:`< A C D ) <g1:< A C D )>` > :g:`< B A C ) <g1:< B A C )>`, :g:`< A C D ) <g1:< A C D )>` :eq:`= <g1:< A C D ) = g1:< B C G )>` :g:`< B C G ) <g1:< B C G )>` > :g:`< C B A ) <g1:< C B A )>`"),
        ],
    },
    "I.17": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`",
        "contract": ":g:`< A B C ) <g1:< A B C )>` + :g:`< B C A ) <g1:< B C A )>` < 2∟, :g:`< B A C ) <g1:< B A C )>` + :g:`< A C B ) <g1:< A C B )>` < 2∟, :g:`< C A B ) <g1:< C A B )>` + :g:`< A B C ) <g1:< A B C )>` < 2∟",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`"),
            ("construct", [], "@fn(I.post.2)(:g:`/ B C / <g1:/ B C />`) → :g:`/ C D / <g1:/ C D />`"),
            ("assert", ["I.16"], ":g:`< A C D ) <g1:< A C D )>` > :g:`< A B C ) <g1:< A B C )>`"),
            ("assert", ["I.cn.2"], ":g:`< A C D ) <g1:< A C D )>` > :g:`< A B C ) <g1:< A B C )>` → :g:`< A C D ) <g1:< A C D )>` + :g:`< A C B ) <g1:< A C B )>` > :g:`< A B C ) <g1:< A B C )>` + :g:`< B C A ) <g1:< B C A )>`"),
            ("assert", ["I.13"], ":g:`/ A C / <g1:/ A C />` on :g:`/ B D / <g1:/ B D />` → :g:`< A C D ) <g1:< A C D )>` + :g:`< A C B ) <g1:< A C B )>` = 2∟"),
            ("conclude", ["I.13"], ":g:`< A B C ) <g1:< A B C )>` + :g:`< B C A ) <g1:< B C A )>` < 2∟, :g:`< B A C ) <g1:< B A C )>` + :g:`< A C B ) <g1:< A C B )>` < 2∟, :g:`< C A B ) <g1:< C A B )>` + :g:`< A B C ) <g1:< A B C )>` < 2∟"),
        ],
    },
    "I.18": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>` (:g:`/ A C / <g1:/ A C />` > :g:`/ A B / <g1:/ A B />`)",
        "contract": ":g:`< A B C ) <g1:< A B C )>` > :g:`< B C A ) <g1:< B C A )>`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>` (:g:`/ A C / <g1:/ A C />` > :g:`/ A B / <g1:/ A B />`)"),
            ("construct", [], "@fn(I.3)(:g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`) → :g:`/ A D / <g1:/ A D />` (:eq:`= <g1:/ A D / = g1:/ A B />` :g:`/ A B / <g1:/ A B />`)"),
            ("construct", [], "@fn(I.post.1)(:g:`B <g1:B>`, :g:`D <g1:D>`) → :g:`/ B D / <g1:/ B D />`"),
            ("assert", ["I.16"], ":g:`< A D B ) <g1:< A D B )>` > :g:`< D C B ) <g1:< D C B )>`"),
            ("assert", ["I.5"], ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ A D />` :g:`/ A D / <g1:/ A D />` → :g:`< A D B ) <g1:< A D B )>` :eq:`= <g1:< A D B ) = g1:< A B D )>` :g:`< A B D ) <g1:< A B D )>` → :g:`< A B D ) <g1:< A B D )>` > :g:`< A C B ) <g1:< A C B )>`"),
            ("conclude", ["I.cn.5"], ":g:`< A B C ) <g1:< A B C )>` > :g:`< A B D ) <g1:< A B D )>` → :g:`< A B C ) <g1:< A B C )>` > :g:`< B C A ) <g1:< B C A )>`"),
        ],
    },
    "I.19": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>` (:g:`< A B C ) <g1:< A B C )>` > :g:`< B C A ) <g1:< B C A )>`)",
        "contract": ":g:`/ A C / <g1:/ A C />` > :g:`/ A B / <g1:/ A B />`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>` (:g:`< A B C ) <g1:< A B C )>` > :g:`< B C A ) <g1:< B C A )>`)"),
            ("construct", [], "? :g:`/ A C / <g1:/ A C />` ≤ :g:`/ A B / <g1:/ A B />` → :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ A B />` :g:`/ A B / <g1:/ A B />` ∨ :g:`/ A C / <g1:/ A C />` < :g:`/ A B / <g1:/ A B />`"),
            ("assert", ["I.5"], "? :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ A B />` :g:`/ A B / <g1:/ A B />` → :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< A C B )>` :g:`< A C B ) <g1:< A C B )>` ⇒⇐ → :g:`/ A C / <g1:/ A C />` ≠ :g:`/ A B / <g1:/ A B />`"),
            ("assert", ["I.18"], "? :g:`/ A C / <g1:/ A C />` < :g:`/ A B / <g1:/ A B />` → :g:`< A B C ) <g1:< A B C )>` < :g:`< A C B ) <g1:< A C B )>` ⇒⇐ → :g:`/ A C / <g1:/ A C />` ≮ :g:`/ A B / <g1:/ A B />`"),
            ("conclude", ["I.5", "I.18"], ":g:`/ A C / <g1:/ A C />` > :g:`/ A B / <g1:/ A B />`"),
        ],
    },
    "I.20": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`",
        "contract": ":g:`/ B A / <g1:/ B A />` + :g:`/ A C / <g1:/ A C />` > :g:`/ B C / <g1:/ B C />`, :g:`/ A B / <g1:/ A B />` + :g:`/ B C / <g1:/ B C />` > :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />` + :g:`/ C A / <g1:/ C A />` > :g:`/ A B / <g1:/ A B />`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`"),
            ("construct", [], "@fn(I.post.2)(:g:`/ B A / <g1:/ B A />`), @fn(I.3)(:g:`/ C A / <g1:/ C A />`) → :g:`/ A D / <g1:/ A D />` (:eq:`= <g1:/ A D / = g1:/ A C />` :g:`/ A C / <g1:/ A C />`), @fn(I.post.1)(:g:`D <g1:D>`, :g:`C <g1:C>`) → :g:`/ D C / <g1:/ D C />`"),
            ("assert", ["I.5"], ":g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ A C />` :g:`/ A C / <g1:/ A C />` → :g:`< A D C ) <g1:< A D C )>` :eq:`= <g1:< A D C ) = g1:< A C D )>` :g:`< A C D ) <g1:< A C D )>`"),
            ("assert", ["I.cn.5"], ":g:`< B C D ) <g1:< B C D )>` > :g:`< A C D ) <g1:< A C D )>` → :g:`< B C D ) <g1:< B C D )>` > :g:`< A D C ) <g1:< A D C )>`"),
            ("assert", ["I.19"], ":g:`< B C D ) <g1:< B C D )>` > :g:`< B D C ) <g1:< B D C )>` → :g:`/ D B / <g1:/ D B />` > :g:`/ B C / <g1:/ B C />`"),
            ("conclude", ["I.19"], ":g:`/ B A / <g1:/ B A />` + :g:`/ A C / <g1:/ A C />` > :g:`/ B C / <g1:/ B C />`, :g:`/ A B / <g1:/ A B />` + :g:`/ B C / <g1:/ B C />` > :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />` + :g:`/ C A / <g1:/ C A />` > :g:`/ A B / <g1:/ A B />`"),
        ],
    },
    "I.21": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`/ B D / <g1:/ B D />`", ":g:`/ D C / <g1:/ D C />`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, :g:`/ B D / <g1:/ B D />`, :g:`/ D C / <g1:/ D C />` (:g:`D <g1:D>` ∈ :g:`< A B C > <g1:< A B C >>`)",
        "contract": ":g:`/ B D / <g1:/ B D />` + :g:`/ D C / <g1:/ D C />` < :g:`/ B A / <g1:/ B A />` + :g:`/ A C / <g1:/ A C />`, :g:`< B D C ) <g1:< B D C )>` > :g:`< B A C ) <g1:< B A C )>`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, :g:`/ B D / <g1:/ B D />`, :g:`/ D C / <g1:/ D C />` (:g:`D <g1:D>` ∈ :g:`< A B C > <g1:< A B C >>`)"),
            ("construct", [], "@fn(I.post.2)(:g:`/ B D / <g1:/ B D />`) → :g:`/ D E / <g1:/ D E />`"),
            ("assert", ["I.20"], ":g:`< A B E > <g1:< A B E >>` → :g:`/ B A / <g1:/ B A />` + :g:`/ A E / <g1:/ A E />` > :g:`/ B E / <g1:/ B E />` → :g:`/ B A / <g1:/ B A />` + :g:`/ A C / <g1:/ A C />` > :g:`/ B E / <g1:/ B E />` + :g:`/ E C / <g1:/ E C />`"),
            ("assert", ["I.20"], ":g:`< C E D > <g1:< C E D >>` → :g:`/ C E / <g1:/ C E />` + :g:`/ E D / <g1:/ E D />` > :g:`/ C D / <g1:/ C D />` → :g:`/ B E / <g1:/ B E />` + :g:`/ E C / <g1:/ E C />` > :g:`/ B D / <g1:/ B D />` + :g:`/ D C / <g1:/ D C />`"),
            ("assert", ["I.16"], ":g:`< C D E > <g1:< C D E >>` → :g:`< B D C ) <g1:< B D C )>` > :g:`< C E D ) <g1:< C E D )>`, :g:`< A B E > <g1:< A B E >>` → :g:`< C E B ) <g1:< C E B )>` > :g:`< B A C ) <g1:< B A C )>`"),
            ("conclude", ["I.16", "I.20"], ":g:`/ B D / <g1:/ B D />` + :g:`/ D C / <g1:/ D C />` < :g:`/ B A / <g1:/ B A />` + :g:`/ A C / <g1:/ A C />`, :g:`< B D C ) <g1:< B D C )>` > :g:`< B A C ) <g1:< B A C )>`"),
        ],
    },
    "I.22": {
        "subtype": "problem",
        "args": [":g:`A <g1:A>`", ":g:`B <g1:B>`", ":g:`C <g1:C>`"],
        "returns": [":g:`< K F G > <g1:< K F G >>`"],
        "given": ":g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` (:g:`A <g1:A>` + :g:`B <g1:B>` > :g:`C <g1:C>`, :g:`A <g1:A>` + :g:`C <g1:C>` > :g:`B <g1:B>`, :g:`B <g1:B>` + :g:`C <g1:C>` > :g:`A <g1:A>`)",
        "contract": ":g:`< K F G > <g1:< K F G >>` (:g:`/ K F / <g1:/ K F />` :eq:`= <g1:/ K F / = g1:A; g1:/ F G / = g1:B; g1:/ K G / = g1:C>` :g:`A <g1:A>`, :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ K F / = g1:A; g1:/ F G / = g1:B; g1:/ K G / = g1:C>` :g:`B <g1:B>`, :g:`/ K G / <g1:/ K G />` :eq:`= <g1:/ K F / = g1:A; g1:/ F G / = g1:B; g1:/ K G / = g1:C>` :g:`C <g1:C>`)",
        "steps": [
            ("given", [], ":g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` (:g:`A <g1:A>` + :g:`B <g1:B>` > :g:`C <g1:C>`, :g:`A <g1:A>` + :g:`C <g1:C>` > :g:`B <g1:B>`, :g:`B <g1:B>` + :g:`C <g1:C>` > :g:`A <g1:A>`)"),
            ("construct", [], "@fn(I.3)(:g:`[ D E ] <g1:[ D E ]>`, :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`/ D F / <g1:/ D F />` :eq:`= <g1:/ D F / = g1:A>` :g:`A <g1:A>`, :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ F G / = g1:B>` :g:`B <g1:B>`, :g:`/ G H / <g1:/ G H />` :eq:`= <g1:/ G H / = g1:C>` :g:`C <g1:C>`"),
            ("construct", [], "@fn(I.post.3)(:g:`F <g1:F>`, :g:`D <g1:D>`) → :g:`( F D ) <g1:( D K L )>`, @fn(I.post.3)(:g:`G <g1:G>`, :g:`H <g1:H>`) → :g:`( G H ) <g1:( K L H )>`"),
            ("intersect", [], ":g:`( F D ) <g1:( D K L )>` ∩ :g:`( G H ) <g1:( K L H )>` → :g:`K <g1:K>`, @fn(I.post.1)(:g:`K <g1:K>`, :g:`F <g1:F>`) → :g:`/ K F / <g1:/ K F />`, @fn(I.post.1)(:g:`K <g1:K>`, :g:`G <g1:G>`) → :g:`/ K G / <g1:/ K G />`"),
            ("assert", ["I.def.15", "I.cn.1"], ":g:`( F D ) <g1:( D K L )>` → :g:`/ F D / <g1:/ F D />` :eq:`= <g1:/ F D / = g1:/ F K />` :g:`/ F K / <g1:/ F K />` → :g:`/ K F / <g1:/ K F />` :eq:`= <g1:/ K F / = g1:A>` :g:`A <g1:A>`"),
            ("assert", ["I.def.15", "I.cn.1"], ":g:`( G H ) <g1:( L K H )>` → :g:`/ G H / <g1:/ G H />` :eq:`= <g1:/ G H / = g1:/ G K />` :g:`/ G K / <g1:/ G K />` → :g:`/ K G / <g1:/ K G />` :eq:`= <g1:/ K G / = g1:C>` :g:`C <g1:C>`"),
            ("conclude", ["I.cn.1"], ":g:`/ K F / <g1:/ K F />` :eq:`= <g1:/ K F / = g1:A; g1:/ F G / = g1:B; g1:/ K G / = g1:C>` :g:`A <g1:A>`, :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ K F / = g1:A; g1:/ F G / = g1:B; g1:/ K G / = g1:C>` :g:`B <g1:B>`, :g:`/ K G / <g1:/ K G />` :eq:`= <g1:/ K F / = g1:A; g1:/ F G / = g1:B; g1:/ K G / = g1:C>` :g:`C <g1:C>` → :g:`< K F G > <g1:< K F G >>`"),
        ],
    },
    "I.23": {
        "subtype": "problem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`A <g1:A>`", ":g:`< D C E ) <g1:< D C E )>`"],
        "returns": [":g:`< F A G ) <g1:< F A G )>`"],
        "given": ":g:`/ A B / <g1:/ A B />`, :g:`A <g1:A>` ∈ :g:`/ A B / <g1:/ A B />`, :g:`< D C E ) <g1:< D C E )>`",
        "contract": ":g:`< F A G ) <g1:< F A G )>` :eq:`= <g1:< F A G ) = g1:< D C E )>` :g:`< D C E ) <g1:< D C E )>`",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />`, :g:`A <g1:A>` ∈ :g:`/ A B / <g1:/ A B />`, :g:`< D C E ) <g1:< D C E )>`"),
            ("construct", [], "**point**\\ (:g:`[ C D ] <g1:[ C D ]>`, :g:`[ C E ] <g1:[ C E ]>`) → :g:`D <g1:D>`, :g:`E <g1:E>`, @fn(I.post.1)(:g:`D <g1:D>`, :g:`E <g1:E>`) → :g:`/ D E / <g1:/ D E />`"),
            ("construct", [], "@fn(I.22)(:g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />`, :g:`/ C E / <g1:/ C E />`) → :g:`< A F G > <g1:< A F G >>` (:g:`/ C D / <g1:/ C D />` :eq:`= <g1:/ C D / = g1:/ A F /; g1:/ C E / = g1:/ A G /; g1:/ D E / = g1:/ F G />` :g:`/ A F / <g1:/ A F />`, :g:`/ C E / <g1:/ C E />` :eq:`= <g1:/ C D / = g1:/ A F /; g1:/ C E / = g1:/ A G /; g1:/ D E / = g1:/ F G />` :g:`/ A G / <g1:/ A G />`, :g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ C D / = g1:/ A F /; g1:/ C E / = g1:/ A G /; g1:/ D E / = g1:/ F G />` :g:`/ F G / <g1:/ F G />`)"),
            ("assert", ["I.8"], ":g:`/ D C / <g1:/ D C />` :eq:`= <g1:/ D C / = g1:/ F A /; g1:/ C E / = g1:/ A G />` :g:`/ F A / <g1:/ F A />`, :g:`/ C E / <g1:/ C E />` :eq:`= <g1:/ D C / = g1:/ F A /; g1:/ C E / = g1:/ A G />` :g:`/ A G / <g1:/ A G />`, :g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ D E / = g1:/ F G />` :g:`/ F G / <g1:/ F G />` → :g:`< D C E ) <g1:< D C E )>` :eq:`= <g1:< D C E ) = g1:< F A G )>` :g:`< F A G ) <g1:< F A G )>`"),
            ("conclude", ["I.8"], ":g:`< F A G ) <g1:< F A G )>` :eq:`= <g1:< F A G ) = g1:< D C E )>` :g:`< D C E ) <g1:< D C E )>`"),
        ],
    },
    "I.24": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< D E F > <g1:< D E F >>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>` (:g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F />` :g:`/ D E / <g1:/ D E />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`, :g:`< B A C ) <g1:< B A C )>` > :g:`< E D F ) <g1:< E D F )>`)",
        "contract": ":g:`/ B C / <g1:/ B C />` > :g:`/ E F / <g1:/ E F />`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>` (:g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F />` :g:`/ D E / <g1:/ D E />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`, :g:`< B A C ) <g1:< B A C )>` > :g:`< E D F ) <g1:< E D F )>`)"),
            ("construct", [], "@fn(I.23)(:g:`/ D E / <g1:/ D E />`, :g:`D <g1:D>`, :g:`< B A C ) <g1:< B A C )>`) → :g:`< E D G ) <g1:< E D G )>` (:eq:`= <g1:< E D G ) = g1:< B A C )>` :g:`< B A C ) <g1:< B A C )>`), @fn(I.3)(:g:`/ A C / <g1:/ A C />`) → :g:`/ D G / <g1:/ D G />` (:eq:`= <g1:/ D G / = g1:/ A C />; g1:/ D G / = g1:/ D F />` :g:`/ A C / <g1:/ A C />`), @fn(I.post.1)(:g:`E <g1:E>`, :g:`G <g1:G>`) → :g:`/ E G / <g1:/ E G />`, @fn(I.post.1)(:g:`F <g1:F>`, :g:`G <g1:G>`) → :g:`/ F G / <g1:/ F G />`"),
            ("assert", ["I.4"], ":g:`/ B A / <g1:/ B A />` :eq:`= <g1:/ B A / = g1:/ E D />; g1:/ A C / = g1:/ D G />` :g:`/ E D / <g1:/ E D />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ B A / = g1:/ E D />; g1:/ A C / = g1:/ D G />` :g:`/ D G / <g1:/ D G />`, :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D G )>` :g:`< E D G ) <g1:< E D G )>` → :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E G />` :g:`/ E G / <g1:/ E G />`"),
            ("assert", ["I.5", "I.cn.5"], ":g:`/ D F / <g1:/ D F />` :eq:`= <g1:/ D F / = g1:/ D G />` :g:`/ D G / <g1:/ D G />` → :g:`< D G F ) <g1:< D G F )>` :eq:`= <g1:< D G F ) = g1:< D F G )>` :g:`< D F G ) <g1:< D F G )>` → :g:`< E F G ) <g1:< E F G )>` ≫ :g:`< E G F ) <g1:< E G F )>`"),
            ("assert", ["I.19"], ":g:`< E F G > <g1:< E F G >>` (:g:`< E F G ) <g1:< E F G )>` > :g:`< E G F ) <g1:< E G F )>`) → :g:`/ E G / <g1:/ E G />` > :g:`/ E F / <g1:/ E F />`"),
            ("conclude", ["I.4", "I.19"], ":g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E G />` :g:`/ E G / <g1:/ E G />`, :g:`/ E G / <g1:/ E G />` > :g:`/ E F / <g1:/ E F />` → :g:`/ B C / <g1:/ B C />` > :g:`/ E F / <g1:/ E F />`"),
        ],
    },
    "I.25": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< D E F > <g1:< D E F >>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>` (:g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F />` :g:`/ D E / <g1:/ D E />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`, :g:`/ B C / <g1:/ B C />` > :g:`/ E F / <g1:/ E F />`)",
        "contract": ":g:`< B A C ) <g1:< B A C )>` > :g:`< E D F ) <g1:< E D F )>`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>` (:g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F />` :g:`/ D E / <g1:/ D E />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`, :g:`/ B C / <g1:/ B C />` > :g:`/ E F / <g1:/ E F />`)"),
            ("construct", [], "? :g:`< B A C ) <g1:< B A C )>` ≤ :g:`< E D F ) <g1:< E D F )>` → :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>` ∨ :g:`< B A C ) <g1:< B A C )>` < :g:`< E D F ) <g1:< E D F )>`"),
            ("assert", ["I.4"], "? :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>` → :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />` ⇒⇐ → :g:`< B A C ) <g1:< B A C )>` ≠ :g:`< E D F ) <g1:< E D F )>`"),
            ("assert", ["I.24"], "? :g:`< B A C ) <g1:< B A C )>` < :g:`< E D F ) <g1:< E D F )>` → :g:`/ B C / <g1:/ B C />` < :g:`/ E F / <g1:/ E F />` ⇒⇐ → :g:`< B A C ) <g1:< B A C )>` ≮ :g:`< E D F ) <g1:< E D F )>`"),
            ("conclude", ["I.4", "I.24"], ":g:`< B A C ) <g1:< B A C )>` > :g:`< E D F ) <g1:< E D F )>`"),
        ],
    },
    "I.26": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< D E F > <g1:< D E F >>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>` (:g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< D E F ); g1:< B C A ) = g1:< E F D )>` :g:`< D E F ) <g1:< D E F )>`, :g:`< B C A ) <g1:< B C A )>` :eq:`= <g1:< A B C ) = g1:< D E F ); g1:< B C A ) = g1:< E F D )>` :g:`< E F D ) <g1:< E F D )>`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />` ∨ :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />`)",
        "contract": ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F /; g1:< B A C ) = g1:< E D F )>` :g:`/ D E / <g1:/ D E />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F /; g1:< B A C ) = g1:< E D F )>` :g:`/ D F / <g1:/ D F />`, :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F /; g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>` (:g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< D E F ); g1:< B C A ) = g1:< E F D )>` :g:`< D E F ) <g1:< D E F )>`, :g:`< B C A ) <g1:< B C A )>` :eq:`= <g1:< A B C ) = g1:< D E F ); g1:< B C A ) = g1:< E F D )>` :g:`< E F D ) <g1:< E F D )>`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`)"),
            ("construct", [], "? :g:`/ A B / <g1:/ A B />` > :g:`/ D E / <g1:/ D E />` → @fn(I.3)(:g:`/ A B / <g1:/ A B />`, :g:`/ D E / <g1:/ D E />`) → :g:`/ B G / <g1:/ B G />` (:eq:`= <g1:/ B G / = g1:/ D E />` :g:`/ D E / <g1:/ D E />`), @fn(I.post.1)(:g:`G <g1:G>`, :g:`C <g1:C>`) → :g:`/ G C / <g1:/ G C />`"),
            ("assert", ["I.4", "I.cn.5"], ":g:`< G B C > <g1:< G B C >>` :eq:`= <g1:< G B C > = g1:< D E F >>` :g:`< D E F > <g1:< D E F >>` → :g:`< G C B ) <g1:< G C B )>` :eq:`= <g1:< G C B ) = g1:< D F E )>` :g:`< D F E ) <g1:< D F E )>` :eq:`= <g1:< D F E ) = g1:< B C A )>` :g:`< B C A ) <g1:< B C A )>` ⇒⇐ → :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />`"),
            ("construct", [], "? :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />` ∧ :g:`/ B C / <g1:/ B C />` > :g:`/ E F / <g1:/ E F />` → @fn(I.3)(:g:`/ B C / <g1:/ B C />`, :g:`/ E F / <g1:/ E F />`) → :g:`/ B H / <g1:/ B H />` (:eq:`= <g1:/ B H / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`), @fn(I.post.1)(:g:`A <g1:A>`, :g:`H <g1:H>`) → :g:`/ A H / <g1:/ A H />`"),
            ("assert", ["I.4", "I.16"], ":g:`< A B H > <g1:< A B H >>` :eq:`= <g1:< A B H > = g1:< D E F >>` :g:`< D E F > <g1:< D E F >>` → :g:`< B H A ) <g1:< B H A )>` :eq:`= <g1:< B H A ) = g1:< E F D )>` :g:`< E F D ) <g1:< E F D )>` :eq:`= <g1:< E F D ) = g1:< B C A )>` :g:`< B C A ) <g1:< B C A )>` ⇒⇐ → :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`"),
            ("conclude", ["I.4"], ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F /; g1:< B A C ) = g1:< E D F )>` :g:`/ D E / <g1:/ D E />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F /; g1:< B A C ) = g1:< E D F )>` :g:`/ D F / <g1:/ D F />`, :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A C / = g1:/ D F /; g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`"),
        ],
    },
    "I.27": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`/ C D / <g1:/ C D />`", ":g:`/ E F / <g1:/ E F />`"],
        "returns": [],
        "given": ":g:`/ E F / <g1:/ E F />` ∩ :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` (:g:`< A E F ) <g1:< A E F )>` :eq:`= <g1:< A E F ) = g1:< E F D )>` :g:`< E F D ) <g1:< E F D )>`)",
        "contract": ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`",
        "steps": [
            ("given", [], ":g:`/ E F / <g1:/ E F />` ∩ :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` (:g:`< A E F ) <g1:< A E F )>` :eq:`= <g1:< A E F ) = g1:< E F D )>` :g:`< E F D ) <g1:< E F D )>`)"),
            ("construct", [], "? ¬(:g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`) → @fn(I.post.2)(:g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`) → :g:`[ A B ] <g1:[ A B ]>` ∩ :g:`[ C D ] <g1:[ C D ]>` → :g:`G <g1:G>`"),
            ("assert", [], ":g:`< G E F > <g1:< G E F >>` → :g:`< A E F ) <g1:< A E F )>` :eq:`= <g1:< A E F ) = g1:< E F G )>` :g:`< E F G ) <g1:< E F G )>`"),
            ("assert", ["I.16"], ":g:`< G E F > <g1:< G E F >>` → :g:`< A E F ) <g1:< A E F )>` > :g:`< E F G ) <g1:< E F G )>` ⇒⇐ → :g:`[ A B ] <g1:[ A B ]>` ∩ :g:`[ C D ] <g1:[ C D ]>` = ∅"),
            ("conclude", ["I.def.23"], ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`"),
        ],
    },
    "I.28": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`/ C D / <g1:/ C D />`", ":g:`/ E F / <g1:/ E F />`"],
        "returns": [],
        "given": ":g:`/ E F / <g1:/ E F />` ∩ :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` (:g:`< E G B ) <g1:< E G B )>` :eq:`= <g1:< E G B ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>` ∨ :g:`< B G H ) <g1:< B G H )>` + :g:`< G H D ) <g1:< G H D )>` = 2∟)",
        "contract": ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`",
        "steps": [
            ("given", [], ":g:`/ E F / <g1:/ E F />` ∩ :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` (:g:`< E G B ) <g1:< E G B )>` :eq:`= <g1:< E G B ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>` ∨ :g:`< B G H ) <g1:< B G H )>` + :g:`< G H D ) <g1:< G H D )>` = 2∟)"),
            ("assert", ["I.15", "I.cn.1"], ":g:`< E G B ) <g1:< E G B )>` :eq:`= <g1:< E G B ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>`, :g:`< E G B ) <g1:< E G B )>` :eq:`= <g1:< E G B ) = g1:< A G H )>` :g:`< A G H ) <g1:< A G H )>` → :g:`< A G H ) <g1:< A G H )>` :eq:`= <g1:< A G H ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>`"),
            ("assert", ["I.27"], ":g:`< A G H ) <g1:< A G H )>` :eq:`= <g1:< A G H ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>` → :g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`"),
            ("assert", ["I.13", "I.cn.3"], ":g:`< B G H ) <g1:< B G H )>` + :g:`< G H D ) <g1:< G H D )>` = 2∟ = :g:`< A G H ) <g1:< A G H )>` + :g:`< B G H ) <g1:< B G H )>` → :g:`< A G H ) <g1:< A G H )>` :eq:`= <g1:< A G H ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>`"),
            ("conclude", ["I.27"], ":g:`< A G H ) <g1:< A G H )>` :eq:`= <g1:< A G H ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>` → :g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`"),
        ],
    },
    "I.29": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`/ C D / <g1:/ C D />`", ":g:`/ E F / <g1:/ E F />`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`, :g:`/ E F / <g1:/ E F />` ∩ :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` → :g:`G <g1:G>`, :g:`H <g1:H>`",
        "contract": ":g:`< A G H ) <g1:< A G H )>` :eq:`= <g1:< A G H ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>`, :g:`< E G B ) <g1:< E G B )>` :eq:`= <g1:< E G B ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>`, :g:`< B G H ) <g1:< B G H )>` + :g:`< G H D ) <g1:< G H D )>` = 2∟",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`, :g:`/ E F / <g1:/ E F />` ∩ :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` → :g:`G <g1:G>`, :g:`H <g1:H>`"),
            ("assert", ["I.13", "I.cn.2"], "? :g:`< A G H ) <g1:< A G H )>` > :g:`< G H D ) <g1:< G H D )>` → :g:`< A G H ) <g1:< A G H )>` + :g:`< B G H ) <g1:< B G H )>` = 2∟ > :g:`< B G H ) <g1:< B G H )>` + :g:`< G H D ) <g1:< G H D )>`"),
            ("assert", ["I.post.5", "I.def.23"], ":g:`< B G H ) <g1:< B G H )>` + :g:`< G H D ) <g1:< G H D )>` < 2∟ → :g:`[ A B ] <g1:[ A B ]>` ∩ :g:`[ C D ] <g1:[ C D ]>` ≠ ∅ ⇒⇐ → :g:`< A G H ) <g1:< A G H )>` :eq:`= <g1:< A G H ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>`"),
            ("assert", ["I.15", "I.cn.1"], ":g:`< A G H ) <g1:< A G H )>` :eq:`= <g1:< A G H ) = g1:< E G B )>` :g:`< E G B ) <g1:< E G B )>`, :g:`< A G H ) <g1:< A G H )>` :eq:`= <g1:< A G H ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>` → :g:`< E G B ) <g1:< E G B )>` :eq:`= <g1:< E G B ) = g1:< G H D )>` :g:`< G H D ) <g1:< G H D )>`"),
            ("conclude", ["I.cn.2", "I.13"], ":g:`< E G B ) <g1:< E G B )>` + :g:`< B G H ) <g1:< B G H )>` = 2∟ → :g:`< B G H ) <g1:< B G H )>` + :g:`< G H D ) <g1:< G H D )>` = 2∟"),
        ],
    },
    "I.30": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`/ C D / <g1:/ C D />`", ":g:`/ E F / <g1:/ E F />`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ E F / <g1:/ E F />`, :g:`/ C D / <g1:/ C D />` ∥ :g:`/ E F / <g1:/ E F />`",
        "contract": ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ E F / <g1:/ E F />`, :g:`/ C D / <g1:/ C D />` ∥ :g:`/ E F / <g1:/ E F />`"),
            ("construct", [], ":g:`/ G K / <g1:/ G K />` ∩ :g:`/ A B / <g1:/ A B />`, :g:`/ E F / <g1:/ E F />`, :g:`/ C D / <g1:/ C D />` → :g:`G <g1:G>`, :g:`H <g1:H>`, :g:`K <g1:K>`"),
            ("assert", ["I.29"], ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ E F / <g1:/ E F />` → :g:`< A G K ) <g1:< A G K )>` :eq:`= <g1:< A G K ) = g1:< G H F )>` :g:`< G H F ) <g1:< G H F )>`"),
            ("assert", ["I.29", "I.cn.1"], ":g:`/ E F / <g1:/ E F />` ∥ :g:`/ C D / <g1:/ C D />` → :g:`< G H F ) <g1:< G H F )>` :eq:`= <g1:< G H F ) = g1:< G K D )>` :g:`< G K D ) <g1:< G K D )>` → :g:`< A G K ) <g1:< A G K )>` :eq:`= <g1:< A G K ) = g1:< G K D )>` :g:`< G K D ) <g1:< G K D )>`"),
            ("conclude", ["I.27"], ":g:`< A G K ) <g1:< A G K )>` :eq:`= <g1:< A G K ) = g1:< G K D )>` :g:`< G K D ) <g1:< G K D )>` → :g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`"),
        ],
    },
    "I.31": {
        "subtype": "problem",
        "args": [":g:`A <g1:A>`", ":g:`/ B C / <g1:/ B C />`"],
        "returns": [":g:`/ E F / <g1:/ E F />`"],
        "given": ":g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />`",
        "contract": ":g:`A <g1:A>` ∈ :g:`/ E F / <g1:/ E F />`, :g:`/ E F / <g1:/ E F />` ∥ :g:`/ B C / <g1:/ B C />`",
        "steps": [
            ("given", [], ":g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />`"),
            ("construct", [], "**point**\\ (:g:`/ B C / <g1:/ B C />`) → :g:`D <g1:D>`, @fn(I.post.1)(:g:`A <g1:A>`, :g:`D <g1:D>`) → :g:`/ A D / <g1:/ A D />`"),
            ("construct", [], "@fn(I.23)(:g:`/ D A / <g1:/ D A />`, :g:`A <g1:A>`, :g:`< A D C ) <g1:< A D C )>`) → :g:`< D A E ) <g1:< D A E )>` (:g:`< D A E ) <g1:< D A E )>` :eq:`= <g1:< D A E ) = g1:< A D C )>` :g:`< A D C ) <g1:< A D C )>`)"),
            ("construct", [], "@fn(I.post.2)(:g:`/ E A / <g1:/ E A />`) → :g:`/ A F / <g1:/ A F />`"),
            ("assert", ["I.27"], ":g:`/ A D / <g1:/ A D />` ∩ :g:`/ B C / <g1:/ B C />`, :g:`/ E F / <g1:/ E F />` (:g:`< D A E ) <g1:< D A E )>` :eq:`= <g1:< D A E ) = g1:< A D C )>` :g:`< A D C ) <g1:< A D C )>`) → :g:`/ E F / <g1:/ E F />` ∥ :g:`/ B C / <g1:/ B C />`"),
            ("conclude", ["I.27"], ":g:`A <g1:A>` ∈ :g:`/ E F / <g1:/ E F />`, :g:`/ E F / <g1:/ E F />` ∥ :g:`/ B C / <g1:/ B C />`"),
        ],
    },
    "I.32": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`/ C D / <g1:/ C D />`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, @fn(I.post.2)(:g:`/ B C / <g1:/ B C />`) → :g:`/ C D / <g1:/ C D />`",
        "contract": ":g:`< A C D ) <g1:< A C D )>` = :g:`< C A B ) <g1:< C A B )>` + :g:`< A B C ) <g1:< A B C )>`, :g:`< A B C ) <g1:< A B C )>` + :g:`< B C A ) <g1:< B C A )>` + :g:`< C A B ) <g1:< C A B )>` = 2∟",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, @fn(I.post.2)(:g:`/ B C / <g1:/ B C />`) → :g:`/ C D / <g1:/ C D />`"),
            ("construct", [], "@fn(I.31)(:g:`C <g1:C>`, :g:`/ A B / <g1:/ A B />`) → :g:`/ C E / <g1:/ C E />` (:g:`/ C E / <g1:/ C E />` ∥ :g:`/ A B / <g1:/ A B />`)"),
            ("assert", ["I.29"], ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ C E / <g1:/ C E />`, :g:`/ A C / <g1:/ A C />` ∩ :g:`/ A B / <g1:/ A B />`, :g:`/ C E / <g1:/ C E />` → :g:`< C A B ) <g1:< C A B )>` :eq:`= <g1:< C A B ) = g1:< A C E )>` :g:`< A C E ) <g1:< A C E )>`"),
            ("assert", ["I.29"], ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ C E / <g1:/ C E />`, :g:`/ B D / <g1:/ B D />` ∩ :g:`/ A B / <g1:/ A B />`, :g:`/ C E / <g1:/ C E />` → :g:`< E C D ) <g1:< E C D )>` :eq:`= <g1:< E C D ) = g1:< A B C )>` :g:`< A B C ) <g1:< A B C )>`"),
            ("assert", ["I.cn.2"], ":g:`< A C E ) <g1:< A C E )>` :eq:`= <g1:< A C E ) = g1:< C A B )>` :g:`< C A B ) <g1:< C A B )>`, :g:`< E C D ) <g1:< E C D )>` :eq:`= <g1:< E C D ) = g1:< A B C )>` :g:`< A B C ) <g1:< A B C )>` → :g:`< A C D ) <g1:< A C D )>` = :g:`< C A B ) <g1:< C A B )>` + :g:`< A B C ) <g1:< A B C )>`"),
            ("assert", ["I.cn.2"], ":g:`< A C D ) <g1:< A C D )>` + :g:`< B C A ) <g1:< B C A )>` = :g:`< A B C ) <g1:< A B C )>` + :g:`< B C A ) <g1:< B C A )>` + :g:`< C A B ) <g1:< C A B )>`"),
            ("conclude", ["I.13", "I.cn.1"], ":g:`< A C D ) <g1:< A C D )>` + :g:`< B C A ) <g1:< B C A )>` = 2∟ → :g:`< A B C ) <g1:< A B C )>` + :g:`< B C A ) <g1:< B C A )>` + :g:`< C A B ) <g1:< C A B )>` = 2∟"),
        ],
    },
    "I.33": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`/ C D / <g1:/ C D />`", ":g:`/ A C / <g1:/ A C />`", ":g:`/ B D / <g1:/ B D />`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ C D />` :g:`/ C D / <g1:/ C D />`, :g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`, :g:`/ A C / <g1:/ A C />`, :g:`/ B D / <g1:/ B D />`",
        "contract": ":g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ B D />` :g:`/ B D / <g1:/ B D />`, :g:`/ A C / <g1:/ A C />` ∥ :g:`/ B D / <g1:/ B D />`",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ C D />` :g:`/ C D / <g1:/ C D />`, :g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`, :g:`/ A C / <g1:/ A C />`, :g:`/ B D / <g1:/ B D />`"),
            ("construct", [], "@fn(I.post.1)(:g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`/ B C / <g1:/ B C />`"),
            ("assert", ["I.29"], ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`, :g:`/ B C / <g1:/ B C />` ∩ :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` → :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< B C D )>` :g:`< B C D ) <g1:< B C D )>`"),
            ("assert", ["I.4"], ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D C />; g1:/ B C / = g1:/ C B />` :g:`/ D C / <g1:/ D C />`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ A B / = g1:/ D C />; g1:/ B C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`, :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< B C D )>` :g:`< B C D ) <g1:< B C D )>` → :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ B D />` :g:`/ B D / <g1:/ B D />`, :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D C B >>` :g:`< D C B > <g1:< D C B >>`, :g:`< A C B ) <g1:< A C B )>` :eq:`= <g1:< A C B ) = g1:< C B D )>` :g:`< C B D ) <g1:< C B D )>`"),
            ("conclude", ["I.27"], ":g:`< A C B ) <g1:< A C B )>` :eq:`= <g1:< A C B ) = g1:< C B D )>` :g:`< C B D ) <g1:< C B D )>` → :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ B D />` :g:`/ B D / <g1:/ B D />`, :g:`/ A C / <g1:/ A C />` ∥ :g:`/ B D / <g1:/ B D />`"),
        ],
    },
    "I.34": {
        "subtype": "theorem",
        "args": [":g:`< A C D B > <g1:< A C D B >>`", ":g:`/ B C / <g1:/ B C />`"],
        "returns": [],
        "given": ":g:`< A C D B > <g1:< A C D B >>` (:g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`, :g:`/ A C / <g1:/ A C />` ∥ :g:`/ B D / <g1:/ B D />`), :g:`/ B C / <g1:/ B C />`",
        "contract": ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ C D /; g1:/ A C / = g1:/ B D />` :g:`/ C D / <g1:/ C D />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A B / = g1:/ C D /; g1:/ A C / = g1:/ B D />` :g:`/ B D / <g1:/ B D />`, :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< C D B ); g1:< A B D ) = g1:< A C D )>` :g:`< C D B ) <g1:< C D B )>`, :g:`< A B D ) <g1:< A B D )>` :eq:`= <g1:< B A C ) = g1:< C D B ); g1:< A B D ) = g1:< A C D )>` :g:`< A C D ) <g1:< A C D )>`, :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D C B >>` :g:`< D C B > <g1:< D C B >>`",
        "steps": [
            ("given", [], ":g:`< A C D B > <g1:< A C D B >>` (:g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`, :g:`/ A C / <g1:/ A C />` ∥ :g:`/ B D / <g1:/ B D />`), :g:`/ B C / <g1:/ B C />`"),
            ("assert", ["I.29"], ":g:`/ A B / <g1:/ A B />` ∥ :g:`/ C D / <g1:/ C D />`, :g:`/ B C / <g1:/ B C />` ∩ :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` → :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< B C D )>` :g:`< B C D ) <g1:< B C D )>`"),
            ("assert", ["I.29"], ":g:`/ A C / <g1:/ A C />` ∥ :g:`/ B D / <g1:/ B D />`, :g:`/ B C / <g1:/ B C />` ∩ :g:`/ A C / <g1:/ A C />`, :g:`/ B D / <g1:/ B D />` → :g:`< A C B ) <g1:< A C B )>` :eq:`= <g1:< A C B ) = g1:< C B D )>` :g:`< C B D ) <g1:< C B D )>`"),
            ("assert", ["I.26"], ":g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< D C B ); g1:< B C A ) = g1:< C B D )>` :g:`< D C B ) <g1:< D C B )>`, :g:`< B C A ) <g1:< B C A )>` :eq:`= <g1:< A B C ) = g1:< D C B ); g1:< B C A ) = g1:< C B D )>` :g:`< C B D ) <g1:< C B D )>`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />` → :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ C D /; g1:/ A C / = g1:/ B D />` :g:`/ C D / <g1:/ C D />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A B / = g1:/ C D /; g1:/ A C / = g1:/ B D />` :g:`/ B D / <g1:/ B D />`, :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< C D B )>` :g:`< C D B ) <g1:< C D B )>`"),
            ("assert", ["I.cn.2"], ":g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< B C D )>` :g:`< B C D ) <g1:< B C D )>`, :g:`< C B D ) <g1:< C B D )>` :eq:`= <g1:< C B D ) = g1:< A C B )>` :g:`< A C B ) <g1:< A C B )>` → :g:`< A B D ) <g1:< A B D )>` :eq:`= <g1:< A B D ) = g1:< A C D )>` :g:`< A C D ) <g1:< A C D )>`"),
            ("conclude", ["I.4"], ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D C />; g1:/ B C / = g1:/ C B />` :g:`/ D C / <g1:/ D C />`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ A B / = g1:/ D C />; g1:/ B C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`, :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< B C D )>` :g:`< B C D ) <g1:< B C D )>` → :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D C B >>` :g:`< D C B > <g1:< D C B >>`"),
        ],
    },
    "I.35": {
        "subtype": "theorem",
        "args": [":g:`< A B C D > <g1:< A B C D >>`", ":g:`< E B C F > <g1:< E B C F >>`", ":g:`/ B C / <g1:/ B C />`", ":g:`/ A F / <g1:/ A F />`"],
        "returns": [],
        "given": ":g:`< A B C D > <g1:< A B C D >>`, :g:`< E B C F > <g1:< E B C F >>` on :g:`/ B C / <g1:/ B C />` (:g:`/ A F / <g1:/ A F />` ∥ :g:`/ B C / <g1:/ B C />`)",
        "contract": ":g:`< A B C D > <g1:< A B C D >>` :eq:`= <g1:< A B C D > = g1:< E B C F >>` :g:`< E B C F > <g1:< E B C F >>`",
        "steps": [
            ("given", [], ":g:`< A B C D > <g1:< A B C D >>`, :g:`< E B C F > <g1:< E B C F >>` on :g:`/ B C / <g1:/ B C />` (:g:`/ A F / <g1:/ A F />` ∥ :g:`/ B C / <g1:/ B C />`)"),
            ("assert", ["I.34", "I.cn.1"], ":g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ B C />` :g:`/ B C / <g1:/ B C />`, :g:`/ E F / <g1:/ E F />` :eq:`= <g1:/ E F / = g1:/ B C />` :g:`/ B C / <g1:/ B C />` → :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`"),
            ("assert", ["I.cn.2"], ":g:`/ A D / <g1:/ A D />` + :g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ A E / = g1:/ D F />` :g:`/ D E / <g1:/ D E />` + :g:`/ E F / <g1:/ E F />` → :g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`"),
            ("assert", ["I.29", "I.4"], ":g:`/ E A / <g1:/ E A />` :eq:`= <g1:/ E A / = g1:/ F D />; g1:/ A B / = g1:/ D C />` :g:`/ F D / <g1:/ F D />`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ E A / = g1:/ F D />; g1:/ A B / = g1:/ D C />` :g:`/ D C / <g1:/ D C />`, :g:`< E A B ) <g1:< E A B )>` :eq:`= <g1:< F D C ) = g1:< E A B )>` :g:`< F D C ) <g1:< F D C )>` → :g:`< E A B > <g1:< E A B >>` :eq:`= <g1:< E A B > = g1:< F D C >>` :g:`< F D C > <g1:< F D C >>`"),
            ("assert", ["I.cn.3"], ":g:`< E A B > <g1:< E A B >>` − :g:`< D G E > <g1:< D G E >>` :eq:`= <g1:< A B G D > = g1:< E G C F >>` :g:`< F D C > <g1:< F D C >>` − :g:`< D G E > <g1:< D G E >>` → :g:`< A B G D > <g1:< A B G D >>` :eq:`= <g1:< A B G D > = g1:< E G C F >>` :g:`< E G C F > <g1:< E G C F >>`"),
            ("conclude", ["I.cn.2"], ":g:`< A B G D > <g1:< A B G D >>` + :g:`< G B C > <g1:< G B C >>` :eq:`= <g1:< A B C D > = g1:< E B C F >>` :g:`< E G C F > <g1:< E G C F >>` + :g:`< G B C > <g1:< G B C >>` → :g:`< A B C D > <g1:< A B C D >>` :eq:`= <g1:< A B C D > = g1:< E B C F >>` :g:`< E B C F > <g1:< E B C F >>`"),
        ],
    },
    "I.36": {
        "subtype": "theorem",
        "args": [":g:`< A B C D > <g1:< A B C D >>`", ":g:`< E F G H > <g1:< E F G H >>`", ":g:`/ B C / <g1:/ B C />`", ":g:`/ F G / <g1:/ F G />`"],
        "returns": [],
        "given": ":g:`< A B C D > <g1:< A B C D >>`, :g:`< E F G H > <g1:< E F G H >>` (:g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ F G />` :g:`/ F G / <g1:/ F G />`, :g:`/ A H / <g1:/ A H />` ∥ :g:`/ B G / <g1:/ B G />`)",
        "contract": ":g:`< A B C D > <g1:< A B C D >>` :eq:`= <g1:< A B C D > = g1:< E F G H >>` :g:`< E F G H > <g1:< E F G H >>`",
        "steps": [
            ("given", [], ":g:`< A B C D > <g1:< A B C D >>`, :g:`< E F G H > <g1:< E F G H >>` (:g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ F G />` :g:`/ F G / <g1:/ F G />`, :g:`/ A H / <g1:/ A H />` ∥ :g:`/ B G / <g1:/ B G />`)"),
            ("construct", [], "@fn(I.post.1)(:g:`B <g1:B>`, :g:`E <g1:E>`) → :g:`/ B E / <g1:/ B E />`, @fn(I.post.1)(:g:`C <g1:C>`, :g:`H <g1:H>`) → :g:`/ C H / <g1:/ C H />`"),
            ("assert", ["I.34", "I.cn.1"], ":g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ F G />` :g:`/ F G / <g1:/ F G />`, :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ F G / = g1:/ E H />` :g:`/ E H / <g1:/ E H />` → :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E H />` :g:`/ E H / <g1:/ E H />`"),
            ("assert", ["I.33", "I.34"], ":g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E H />` :g:`/ E H / <g1:/ E H />`, :g:`/ B C / <g1:/ B C />` ∥ :g:`/ E H / <g1:/ E H />` → :g:`/ E B / <g1:/ E B />` :eq:`= <g1:/ E B / = g1:/ H C />` :g:`/ H C / <g1:/ H C />`, :g:`/ E B / <g1:/ E B />` ∥ :g:`/ H C / <g1:/ H C />` → :g:`< E B C H > <g1:< E B C H >>`"),
            ("assert", ["I.35"], ":g:`< A B C D > <g1:< A B C D >>` :eq:`= <g1:< E B C H > = g1:< A B C D >>` :g:`< E B C H > <g1:< E B C H >>`, :g:`< E F G H > <g1:< E F G H >>` :eq:`= <g1:< E F G H > = g1:< E B C H >>` :g:`< E B C H > <g1:< E B C H >>`"),
            ("conclude", ["I.cn.1"], ":g:`< A B C D > <g1:< A B C D >>` :eq:`= <g1:< E B C H > = g1:< A B C D >>` :g:`< E B C H > <g1:< E B C H >>`, :g:`< E F G H > <g1:< E F G H >>` :eq:`= <g1:< E F G H > = g1:< E B C H >>` :g:`< E B C H > <g1:< E B C H >>` → :g:`< A B C D > <g1:< A B C D >>` :eq:`= <g1:< A B C D > = g1:< E F G H >>` :g:`< E F G H > <g1:< E F G H >>`"),
        ],
    },
    "I.37": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< D B C > <g1:< D B C >>`", ":g:`/ B C / <g1:/ B C />`", ":g:`/ A D / <g1:/ A D />`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, :g:`< D B C > <g1:< D B C >>` (:g:`/ A D / <g1:/ A D />` ∥ :g:`/ B C / <g1:/ B C />`)",
        "contract": ":g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D B C >>` :g:`< D B C > <g1:< D B C >>`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, :g:`< D B C > <g1:< D B C >>` (:g:`/ A D / <g1:/ A D />` ∥ :g:`/ B C / <g1:/ B C />`)"),
            ("construct", [], "@fn(I.post.2)(:g:`/ A D / <g1:/ A D />`) → :g:`/ E A / <g1:/ E A />`, :g:`/ D F / <g1:/ D F />`"),
            ("construct", [], "@fn(I.31)(:g:`B <g1:B>`, :g:`/ C A / <g1:/ C A />`) → :g:`/ B E / <g1:/ B E />`, @fn(I.31)(:g:`C <g1:C>`, :g:`/ B D / <g1:/ B D />`) → :g:`/ C F / <g1:/ C F />`"),
            ("assert", ["I.35"], ":g:`/ B C / <g1:/ B C />` ∥ :g:`/ E F / <g1:/ E F />`, :g:`/ B E / <g1:/ B E />` ∥ :g:`/ C A / <g1:/ C A />`, :g:`/ B D / <g1:/ B D />` ∥ :g:`/ C F / <g1:/ C F />` → :g:`< E B C A > <g1:< E B C A >>` :eq:`= <g1:< E B C A > = g1:< D B C F >>` :g:`< D B C F > <g1:< D B C F >>`"),
            ("assert", ["I.34"], ":g:`/ A B / <g1:/ A B />` → :g:`< E A B > <g1:< E A B >>` :eq:`= <g1:< E A B > = g1:< A B C >>` :g:`< A B C > <g1:< A B C >>`, :g:`/ D C / <g1:/ D C />` → :g:`< D B C > <g1:< D B C >>` :eq:`= <g1:< D B C > = g1:< F D C >>` :g:`< F D C > <g1:< F D C >>`"),
            ("conclude", ["I.cn.1"], ":g:`< E B C A > <g1:< E B C A >>` :eq:`= <g1:< E B C A > = g1:< D B C F >>` :g:`< D B C F > <g1:< D B C F >>` → :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D B C >>` :g:`< D B C > <g1:< D B C >>`"),
        ],
    },
    "I.38": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< D E F > <g1:< D E F >>`", ":g:`/ B C / <g1:/ B C />`", ":g:`/ E F / <g1:/ E F />`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>` (:g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`, :g:`/ A D / <g1:/ A D />` ∥ :g:`/ B F / <g1:/ B F />`)",
        "contract": ":g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D E F >>` :g:`< D E F > <g1:< D E F >>`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, :g:`< D E F > <g1:< D E F >>` (:g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`, :g:`/ A D / <g1:/ A D />` ∥ :g:`/ B F / <g1:/ B F />`)"),
            ("construct", [], "@fn(I.post.2)(:g:`/ A D / <g1:/ A D />`) → :g:`/ G A / <g1:/ G A />`, :g:`/ D H / <g1:/ D H />`"),
            ("construct", [], "@fn(I.31)(:g:`B <g1:B>`, :g:`/ C A / <g1:/ C A />`) → :g:`/ B G / <g1:/ B G />`, @fn(I.31)(:g:`F <g1:F>`, :g:`/ D E / <g1:/ D E />`) → :g:`/ F H / <g1:/ F H />`"),
            ("assert", ["I.36"], ":g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`, :g:`/ B F / <g1:/ B F />` ∥ :g:`/ G H / <g1:/ G H />` → :g:`< G B C A > <g1:< G B C A >>` :eq:`= <g1:< G B C A > = g1:< D E F H >>` :g:`< D E F H > <g1:< D E F H >>`"),
            ("assert", ["I.34"], ":g:`/ A B / <g1:/ A B />` → :g:`< G A B > <g1:< G A B >>` :eq:`= <g1:< G A B > = g1:< A B C >>` :g:`< A B C > <g1:< A B C >>`, :g:`/ D F / <g1:/ D F />` → :g:`< D E F > <g1:< D E F >>` :eq:`= <g1:< D E F > = g1:< D H F >>` :g:`< D H F > <g1:< D H F >>`"),
            ("conclude", ["I.cn.1"], ":g:`< G B C A > <g1:< G B C A >>` :eq:`= <g1:< G B C A > = g1:< D E F H >>` :g:`< D E F H > <g1:< D E F H >>` → :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D E F >>` :g:`< D E F > <g1:< D E F >>`"),
        ],
    },
    "I.39": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< D B C > <g1:< D B C >>`", ":g:`/ B C / <g1:/ B C />`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D B C >>` :g:`< D B C > <g1:< D B C >>` on :g:`/ B C / <g1:/ B C />`",
        "contract": ":g:`/ A D / <g1:/ A D />` ∥ :g:`/ B C / <g1:/ B C />`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D B C >>` :g:`< D B C > <g1:< D B C >>` on :g:`/ B C / <g1:/ B C />`"),
            ("construct", [], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`D <g1:D>`) → :g:`/ A D / <g1:/ A D />`"),
            ("construct", [], "? ¬(:g:`/ A D / <g1:/ A D />` ∥ :g:`/ B C / <g1:/ B C />`) → @fn(I.31)(:g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />`) → :g:`/ A E / <g1:/ A E />` ∥ :g:`/ B C / <g1:/ B C />`, @fn(I.post.1)(:g:`E <g1:E>`, :g:`C <g1:C>`) → :g:`/ E C / <g1:/ E C />`"),
            ("assert", ["I.37"], ":g:`/ A E / <g1:/ A E />` ∥ :g:`/ B C / <g1:/ B C />` → :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< E B C >>` :g:`< E B C > <g1:< E B C >>`"),
            ("assert", ["I.cn.1", "I.cn.5"], ":g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D B C >>` :g:`< D B C > <g1:< D B C >>`, :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< E B C >>` :g:`< E B C > <g1:< E B C >>` → :g:`< D B C > <g1:< D B C >>` :eq:`= <g1:< D B C > = g1:< E B C >>` :g:`< E B C > <g1:< E B C >>` ⇒⇐"),
            ("conclude", ["I.def.23"], ":g:`/ A D / <g1:/ A D />` ∥ :g:`/ B C / <g1:/ B C />`"),
        ],
    },
    "I.40": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< C D E > <g1:< C D E >>`", ":g:`/ B C / <g1:/ B C />`", ":g:`/ C E / <g1:/ C E />`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< C D E >>` :g:`< C D E > <g1:< C D E >>`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ C E />` :g:`/ C E / <g1:/ C E />`",
        "contract": ":g:`/ A D / <g1:/ A D />` ∥ :g:`/ B E / <g1:/ B E />`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< C D E >>` :g:`< C D E > <g1:< C D E >>`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ C E />` :g:`/ C E / <g1:/ C E />`"),
            ("construct", [], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`D <g1:D>`) → :g:`/ A D / <g1:/ A D />`"),
            ("construct", [], "? ¬(:g:`/ A D / <g1:/ A D />` ∥ :g:`/ B E / <g1:/ B E />`) → @fn(I.31)(:g:`A <g1:A>`, :g:`/ B E / <g1:/ B E />`) → :g:`/ A F / <g1:/ A F />` ∥ :g:`/ B E / <g1:/ B E />`, @fn(I.post.1)(:g:`F <g1:F>`, :g:`E <g1:E>`) → :g:`/ F E / <g1:/ F E />`"),
            ("assert", ["I.38"], ":g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ C E />` :g:`/ C E / <g1:/ C E />`, :g:`/ A F / <g1:/ A F />` ∥ :g:`/ B E / <g1:/ B E />` → :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< F C E >>` :g:`< F C E > <g1:< F C E >>`"),
            ("assert", ["I.cn.1", "I.cn.5"], ":g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< D C E >>` :g:`< D C E > <g1:< D C E >>`, :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< F C E >>` :g:`< F C E > <g1:< F C E >>` → :g:`< D C E > <g1:< D C E >>` :eq:`= <g1:< D C E > = g1:< F C E >>` :g:`< F C E > <g1:< F C E >>` ⇒⇐"),
            ("conclude", ["I.def.23"], ":g:`/ A D / <g1:/ A D />` ∥ :g:`/ B E / <g1:/ B E />`"),
        ],
    },
    "I.41": {
        "subtype": "theorem",
        "args": [":g:`< A B C D > <g1:< A B C D >>`", ":g:`< E B C > <g1:< E B C >>`"],
        "returns": [],
        "given": ":g:`< A B C D > <g1:< A B C D >>`, :g:`< E B C > <g1:< E B C >>` (:g:`/ B C / <g1:/ B C />` ∥ :g:`/ A E / <g1:/ A E />`)",
        "contract": ":g:`< A B C D > <g1:< A B C D >>` :eq:`= <g1:< A B C D > = g1:< E B C >>` 2 :g:`< E B C > <g1:< E B C >>`",
        "steps": [
            ("given", [], ":g:`< A B C D > <g1:< A B C D >>`, :g:`< E B C > <g1:< E B C >>` (:g:`/ B C / <g1:/ B C />` ∥ :g:`/ A E / <g1:/ A E />`)"),
            ("construct", [], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`C <g1:C>`) → :g:`/ A C / <g1:/ A C />`"),
            ("assert", ["I.37"], ":g:`/ B C / <g1:/ B C />` ∥ :g:`/ A E / <g1:/ A E />` → :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< E B C >>` :g:`< E B C > <g1:< E B C >>`"),
            ("assert", ["I.34"], ":g:`/ A C / <g1:/ A C />` ∈ :g:`< A B C D > <g1:< A B C D >>` → :g:`< A B C D > <g1:< A B C D >>` :eq:`= <g1:< A B C > = g1:< A D C >>` 2 :g:`< A B C > <g1:< A B C >>`"),
            ("conclude", ["I.cn.1"], ":g:`< A B C D > <g1:< A B C D >>` :eq:`= <g1:< A B C > = g1:< A D C >>` 2 :g:`< A B C > <g1:< A B C >>`, :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< E B C >>` :g:`< E B C > <g1:< E B C >>` → :g:`< A B C D > <g1:< A B C D >>` :eq:`= <g1:< A B C D > = g1:< E B C >>` 2 :g:`< E B C > <g1:< E B C >>`"),
        ],
    },
    "I.42": {
        "subtype": "problem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< D ) <g1:< D )>`"],
        "returns": [":g:`< F E C G > <g1:< F E C G >>`"],
        "given": ":g:`< A B C > <g1:< A B C >>`, :g:`< D ) <g1:< D )>`",
        "contract": ":g:`< F E C G > <g1:< F E C G >>` (:g:`< F E C G > <g1:< F E C G >>` :eq:`= <g1:< F E C G > = g1:< A B C >>` :g:`< A B C > <g1:< A B C >>`, :g:`< C E F ) <g1:< C E F )>` :eq:`= <g1:< C E F ) = g1:< D )>` :g:`< D ) <g1:< D )>`)",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>`, :g:`< D ) <g1:< D )>`"),
            ("construct", [], "@fn(I.10)(:g:`/ B C / <g1:/ B C />`) → :g:`E <g1:E>` (:g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ E C />` :g:`/ E C / <g1:/ E C />`), @fn(I.post.1)(:g:`A <g1:A>`, :g:`E <g1:E>`) → :g:`/ A E / <g1:/ A E />`"),
            ("construct", [], "@fn(I.23)(:g:`/ E C / <g1:/ E C />`, :g:`E <g1:E>`, :g:`< D ) <g1:< D )>`) → :g:`< C E F ) <g1:< C E F )>` (:g:`< C E F ) <g1:< C E F )>` :eq:`= <g1:< C E F ) = g1:< D )>` :g:`< D ) <g1:< D )>`)"),
            ("construct", [], "@fn(I.31)(:g:`A <g1:A>`, :g:`/ E C / <g1:/ E C />`) → :g:`/ A G / <g1:/ A G />`, @fn(I.31)(:g:`C <g1:C>`, :g:`/ E F / <g1:/ E F />`) → :g:`/ C G / <g1:/ C G />` → :g:`< F E C G > <g1:< F E C G >>`"),
            ("assert", ["I.38"], ":g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ E C />` :g:`/ E C / <g1:/ E C />`, :g:`/ B C / <g1:/ B C />` ∥ :g:`/ A G / <g1:/ A G />` → :g:`< A B E > <g1:< A B E >>` :eq:`= <g1:< A B E > = g1:< A E C >>` :g:`< A E C > <g1:< A E C >>` → :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B E > = g1:< A E C >>` 2 :g:`< A E C > <g1:< A E C >>`"),
            ("assert", ["I.41"], ":g:`/ E C / <g1:/ E C />` ∥ :g:`/ A G / <g1:/ A G />` → :g:`< F E C G > <g1:< F E C G >>` :eq:`= <g1:< F E C G > = g1:< A E C >>` 2 :g:`< A E C > <g1:< A E C >>`"),
            ("conclude", ["I.cn.1"], ":g:`< F E C G > <g1:< F E C G >>` :eq:`= <g1:< F E C G > = g1:< A B C >>` :g:`< A B C > <g1:< A B C >>`, :g:`< C E F ) <g1:< C E F )>` :eq:`= <g1:< C E F ) = g1:< D )>` :g:`< D ) <g1:< D )>`"),
        ],
    },
    "I.43": {
        "subtype": "theorem",
        "args": [":g:`< A B C D > <g1:< A B C D >>`", ":g:`/ A C / <g1:/ A C />`"],
        "returns": [],
        "given": ":g:`< A B C D > <g1:< A B C D >>`, :g:`/ A C / <g1:/ A C />`, :g:`< A E K H > <g1:< A E K H >>`, :g:`< K F C G > <g1:< K F C G >>`, :g:`< E B F K > <g1:< E B F K >>`, :g:`< H K G D > <g1:< H K G D >>`",
        "contract": ":g:`< E B F K > <g1:< E B F K >>` :eq:`= <g1:< E B F K > = g1:< H K G D >>` :g:`< H K G D > <g1:< H K G D >>`",
        "steps": [
            ("given", [], ":g:`< A B C D > <g1:< A B C D >>`, :g:`/ A C / <g1:/ A C />`, :g:`< A E K H > <g1:< A E K H >>`, :g:`< K F C G > <g1:< K F C G >>`, :g:`< E B F K > <g1:< E B F K >>`, :g:`< H K G D > <g1:< H K G D >>`"),
            ("assert", ["I.34"], ":g:`< A B C D > <g1:< A B C D >>`, :g:`/ A C / <g1:/ A C />` → :g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< A C D >>` :g:`< A C D > <g1:< A C D >>`"),
            ("assert", ["I.34"], ":g:`< A E K H > <g1:< A E K H >>`, :g:`< K F C G > <g1:< K F C G >>` → :g:`< A E K > <g1:< A E K >>` :eq:`= <g1:< A E K > = g1:< A H K >; g1:< K F C > = g1:< K G C >>` :g:`< A H K > <g1:< A H K >>`, :g:`< K F C > <g1:< K F C >>` :eq:`= <g1:< A E K > = g1:< A H K >; g1:< K F C > = g1:< K G C >>` :g:`< K G C > <g1:< K G C >>`"),
            ("assert", ["I.cn.2"], ":g:`< A E K > <g1:< A E K >>` :eq:`= <g1:< A E K > = g1:< A H K >; g1:< K F C > = g1:< K G C >>` :g:`< A H K > <g1:< A H K >>`, :g:`< K F C > <g1:< K F C >>` :eq:`= <g1:< A E K > = g1:< A H K >; g1:< K F C > = g1:< K G C >>` :g:`< K G C > <g1:< K G C >>` → :g:`< A E K > <g1:< A E K >>` + :g:`< K F C > <g1:< K F C >>` = :g:`< A H K > <g1:< A H K >>` + :g:`< K G C > <g1:< K G C >>`"),
            ("conclude", ["I.cn.3"], ":g:`< A B C > <g1:< A B C >>` :eq:`= <g1:< A B C > = g1:< A C D >>` :g:`< A C D > <g1:< A C D >>` → :g:`< E B F K > <g1:< E B F K >>` :eq:`= <g1:< E B F K > = g1:< H K G D >>` :g:`< H K G D > <g1:< H K G D >>`"),
        ],
    },
    "I.44": {
        "subtype": "problem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`< C > <g1:< C >>`", ":g:`< D ) <g1:< D )>`"],
        "returns": [":g:`< A B M L > <g1:< A B M L >>`"],
        "given": ":g:`/ A B / <g1:/ A B />`, :g:`< C > <g1:< C >>`, :g:`< D ) <g1:< D )>`",
        "contract": ":g:`< A B M L > <g1:< A B M L >>` :eq:`= <g1:< A B M L > = g1:< C >>` :g:`< C > <g1:< C >>`, :g:`< A B M ) <g1:< A B M )>` :eq:`= <g1:< A B M ) = g1:< D )>` :g:`< D ) <g1:< D )>`",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />`, :g:`< C > <g1:< C >>`, :g:`< D ) <g1:< D )>`"),
            ("construct", [], "@fn(I.42)(:g:`< C > <g1:< C >>`, :g:`< D ) <g1:< D )>`) → :g:`< B E F G > <g1:< B E F G >>` (:eq:`= <g1:< B E F G > = g1:< C >>` :g:`< C > <g1:< C >>`, :g:`< E B G ) <g1:< E B G )>` :eq:`= <g1:< E B G ) = g1:< D )>` :g:`< D ) <g1:< D )>`), @fn(I.post.2)(:g:`/ F G / <g1:/ F G />`) → :g:`H <g1:H>`, @fn(I.31)(:g:`A <g1:A>`, :g:`/ B G / <g1:/ B G />`) → :g:`/ A H / <g1:/ A H />`, @fn(I.post.1)(:g:`H <g1:H>`, :g:`B <g1:B>`) → :g:`/ H B / <g1:/ H B />`"),
            ("assert", ["I.29", "I.post.5"], ":g:`/ A H / <g1:/ A H />` ∥ :g:`/ E F / <g1:/ E F />` → :g:`< A H F ) <g1:< A H F )>` + :g:`< H F E ) <g1:< H F E )>` = 2∟ → :g:`< B H G ) <g1:< B H G )>` + :g:`< G F E ) <g1:< G F E )>` < 2∟ → :g:`[ H B ] <g1:/ H K />` ∩ :g:`[ F E ] <g1:/ F K />` ≠ ∅"),
            ("construct", [], "@fn(I.post.2)(:g:`/ H B / <g1:/ H B />`, :g:`/ F E / <g1:/ F E />`) → :g:`K <g1:K>`, @fn(I.31)(:g:`K <g1:K>`, :g:`/ E A / <g1:/ E A />`) → :g:`/ K L / <g1:/ K L />`, @fn(I.post.2)(:g:`/ H A / <g1:/ H A />`, :g:`/ G B / <g1:/ G B />`) → :g:`L <g1:L>`, :g:`M <g1:M>`"),
            ("assert", ["I.43", "I.cn.1"], ":g:`< H L K F > <g1:< H L K F >>`, :g:`/ H K / <g1:/ H K />` → :g:`< A B M L > <g1:< A B M L >>` :eq:`= <g1:< A B M L > = g1:< B E F G >>` :g:`< B E F G > <g1:< B E F G >>` :eq:`= <g1:< B E F G > = g1:< C >>` :g:`< C > <g1:< C >>` → :g:`< A B M L > <g1:< A B M L >>` :eq:`= <g1:< A B M L > = g1:< C >>` :g:`< C > <g1:< C >>`"),
            ("assert", ["I.15", "I.cn.1"], ":g:`< A B M ) <g1:< A B M )>` :eq:`= <g1:< G B E ) = g1:< A B M )>` :g:`< E B G ) <g1:< E B G )>` :eq:`= <g1:< G B E ) = g1:< D )>` :g:`< D ) <g1:< D )>` → :g:`< A B M ) <g1:< A B M )>` :eq:`= <g1:< A B M ) = g1:< D )>` :g:`< D ) <g1:< D )>`"),
            ("conclude", ["I.43"], ":g:`< A B M L > <g1:< A B M L >>` :eq:`= <g1:< A B M L > = g1:< C >>` :g:`< C > <g1:< C >>`, :g:`< A B M ) <g1:< A B M )>` :eq:`= <g1:< A B M ) = g1:< D )>` :g:`< D ) <g1:< D )>`"),
        ],
    },
    "I.45": {
        "subtype": "problem",
        "args": [":g:`< A B C D > <g1:< A B C D >>`", ":g:`< E ) <g1:< E )>`"],
        "returns": [":g:`< K F L M > <g1:< K F L M >>`"],
        "given": ":g:`< A B C D > <g1:< A B C D >>`, :g:`< E ) <g1:< E )>`",
        "contract": ":g:`< K F L M > <g1:< K F L M >>` :eq:`= <g1:< K F L M > = g1:< A B C D >>` :g:`< A B C D > <g1:< A B C D >>` (:g:`< F K M ) <g1:< F K M )>` :eq:`= <g1:< F K M ) = g1:< E )>` :g:`< E ) <g1:< E )>`)",
        "steps": [
            ("given", [], ":g:`< A B C D > <g1:< A B C D >>`, :g:`< E ) <g1:< E )>`"),
            ("construct", [], "@fn(I.post.1)(:g:`D <g1:D>`, :g:`B <g1:B>`) → :g:`/ D B / <g1:/ D B />`, @fn(I.42)(:g:`< A B D > <g1:< A B D >>`, :g:`< E ) <g1:< E )>`) → :g:`< F K H G > <g1:< F K H G >>` (:eq:`= <g1:< F K H G > = g1:< A B D >>` :g:`< A B D > <g1:< A B D >>`, :g:`< H K F ) <g1:< H K F )>` :eq:`= <g1:< H K F ) = g1:< E )>` :g:`< E ) <g1:< E )>`)"),
            ("construct", [], "@fn(I.44)(:g:`/ G H / <g1:/ G H />`, :g:`< D B C > <g1:< D B C >>`, :g:`< E ) <g1:< E )>`) → :g:`< G H M L > <g1:< G H M L >>` (:eq:`= <g1:< G H M L > = g1:< D B C >>` :g:`< D B C > <g1:< D B C >>`, :g:`< G H M ) <g1:< G H M )>` :eq:`= <g1:< G H M ) = g1:< E )>` :g:`< E ) <g1:< E )>`)"),
            ("assert", ["I.cn.1", "I.cn.2", "I.29", "I.14"], ":g:`< H K F ) <g1:< H K F )>` :eq:`= <g1:< H K F ) = g1:< G H M )>` :g:`< G H M ) <g1:< G H M )>` → :g:`< K H G ) <g1:< K H G )>` + :g:`< G H M ) <g1:< G H M )>` = :g:`< F K H ) <g1:< F K H )>` + :g:`< K H G ) <g1:< K H G )>` = 2∟ → :g:`/ K H / <g1:/ K H />`, :g:`/ H M / <g1:/ H M />` ∈ :g:`[ K M ] <g1:/ K M />`"),
            ("assert", ["I.29", "I.cn.2", "I.14"], ":g:`< M H G ) <g1:< M H G )>` :eq:`= <g1:< M H G ) = g1:< H G F )>` :g:`< H G F ) <g1:< H G F )>` → :g:`< H G F ) <g1:< H G F )>` + :g:`< H G L ) <g1:< H G L )>` = :g:`< M H G ) <g1:< M H G )>` + :g:`< H G L ) <g1:< H G L )>` = 2∟ → :g:`/ F G / <g1:/ F G />`, :g:`/ G L / <g1:/ G L />` ∈ :g:`[ F L ] <g1:/ F L />`"),
            ("assert", ["I.34", "I.cn.1", "I.30", "I.33"], ":g:`/ F K / <g1:/ F K />` :eq:`= <g1:/ F K / = g1:/ H G / = g1:/ M L />` :g:`/ H G / <g1:/ H G />` :eq:`= <g1:/ F K / = g1:/ H G / = g1:/ M L />` :g:`/ M L / <g1:/ M L />`, :g:`/ F K / <g1:/ F K />` ∥ :g:`/ H G / <g1:/ H G />` ∥ :g:`/ M L / <g1:/ M L />` → :g:`/ K M / <g1:/ K M />` :eq:`= <g1:/ K M / = g1:/ F L />` :g:`/ F L / <g1:/ F L />`, :g:`/ K M / <g1:/ K M />` ∥ :g:`/ F L / <g1:/ F L />` → :g:`< K F L M > <g1:< K F L M >>`"),
            ("conclude", ["I.cn.2"], ":g:`< A B D > <g1:< A B D >>` :eq:`= <g1:< A B D > = g1:< F K H G >; g1:< D B C > = g1:< G H M L >>` :g:`< F K H G > <g1:< F K H G >>`, :g:`< D B C > <g1:< D B C >>` :eq:`= <g1:< A B D > = g1:< F K H G >; g1:< D B C > = g1:< G H M L >>` :g:`< G H M L > <g1:< G H M L >>` → :g:`< K F L M > <g1:< K F L M >>` :eq:`= <g1:< K F L M > = g1:< A B C D >>` :g:`< A B C D > <g1:< A B C D >>` (:g:`< F K M ) <g1:< F K M )>` :eq:`= <g1:< F K M ) = g1:< E )>` :g:`< E ) <g1:< E )>`)"),
        ],
    },
    "I.46": {
        "subtype": "problem",
        "args": [":g:`/ A B / <g1:/ A B />`"],
        "returns": [":g:`< A D E B > <g1:< A D E B >>`"],
        "given": ":g:`/ A B / <g1:/ A B />`",
        "contract": ":g:`< A D E B > <g1:< A D E B >>` (:g:`/ B A / <g1:/ B A />` :eq:`= <g1:/ B A / = g1:/ A D / = g1:/ D E / = g1:/ E B />` :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ B A / = g1:/ A D / = g1:/ D E / = g1:/ E B />` :g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ B A / = g1:/ A D / = g1:/ D E / = g1:/ E B />` :g:`/ E B / <g1:/ E B />`, :g:`< B A D ) <g1:< B A D )>` :eq:`= <g1:< B A D ) = g1:< A D E ) = g1:< A B E ) = g1:< B E D )>` :g:`< A D E ) <g1:< A D E )>` :eq:`= <g1:< B A D ) = g1:< A D E ) = g1:< A B E ) = g1:< B E D )>` :g:`< A B E ) <g1:< A B E )>` :eq:`= <g1:< B A D ) = g1:< A D E ) = g1:< A B E ) = g1:< B E D )>` :g:`< B E D ) <g1:< B E D )>` = ∟)",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />`"),
            ("construct", [], "@fn(I.11)(:g:`/ A B / <g1:/ A B />`, :g:`A <g1:A>`) → :g:`/ A C / <g1:/ A C />` ⊥ :g:`/ A B / <g1:/ A B />`, @fn(I.3)(:g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`) → :g:`/ A D / <g1:/ A D />` (:eq:`= <g1:/ A D / = g1:/ A B />` :g:`/ A B / <g1:/ A B />`)"),
            ("construct", [], "@fn(I.31)(:g:`D <g1:D>`, :g:`/ A B / <g1:/ A B />`) → :g:`/ D E / <g1:/ D E />` ∥ :g:`/ A B / <g1:/ A B />`, @fn(I.31)(:g:`B <g1:B>`, :g:`/ A D / <g1:/ A D />`) → :g:`/ B E / <g1:/ B E />` ∥ :g:`/ A D / <g1:/ A D />` → :g:`< A D E B > <g1:< A D E B >>`"),
            ("assert", ["I.34", "I.cn.1"], ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A D / = g1:/ B E />` :g:`/ D E / <g1:/ D E />`, :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A B / = g1:/ D E /; g1:/ A D / = g1:/ B E />` :g:`/ B E / <g1:/ B E />`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ A D />` :g:`/ A D / <g1:/ A D />` → :g:`/ B A / <g1:/ B A />` :eq:`= <g1:/ B A / = g1:/ A D / = g1:/ D E / = g1:/ E B />` :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ B A / = g1:/ A D / = g1:/ D E / = g1:/ E B />` :g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ B A / = g1:/ A D / = g1:/ D E / = g1:/ E B />` :g:`/ E B / <g1:/ E B />`"),
            ("assert", ["I.29", "I.34"], ":g:`< B A D ) <g1:< B A D )>` + :g:`< A D E ) <g1:< A D E )>` = 2∟, :g:`< B A D ) <g1:< B A D )>` = ∟ → :g:`< B A D ) <g1:< B A D )>` :eq:`= <g1:< B A D ) = g1:< A D E ) = g1:< A B E ) = g1:< B E D )>` :g:`< A D E ) <g1:< A D E )>` :eq:`= <g1:< B A D ) = g1:< A D E ) = g1:< A B E ) = g1:< B E D )>` :g:`< A B E ) <g1:< A B E )>` :eq:`= <g1:< B A D ) = g1:< A D E ) = g1:< A B E ) = g1:< B E D )>` :g:`< B E D ) <g1:< B E D )>` = ∟"),
            ("conclude", ["I.def.22"], ":g:`/ B A / <g1:/ B A />` :eq:`= <g1:/ B A / = g1:/ A D / = g1:/ D E / = g1:/ E B />` :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ B A / = g1:/ A D / = g1:/ D E / = g1:/ E B />` :g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ B A / = g1:/ A D / = g1:/ D E / = g1:/ E B />` :g:`/ E B / <g1:/ E B />`, :g:`< B A D ) <g1:< B A D )>` :eq:`= <g1:< B A D ) = g1:< A D E ) = g1:< A B E ) = g1:< B E D )>` :g:`< A D E ) <g1:< A D E )>` :eq:`= <g1:< B A D ) = g1:< A D E ) = g1:< A B E ) = g1:< B E D )>` :g:`< A B E ) <g1:< A B E )>` :eq:`= <g1:< B A D ) = g1:< A D E ) = g1:< A B E ) = g1:< B E D )>` :g:`< B E D ) <g1:< B E D )>` = ∟ → :g:`< A D E B > <g1:< A D E B >>`"),
        ],
    },
    "I.47": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`< B A C ) <g1:< B A C )>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>` (:g:`< B A C ) <g1:< B A C )>` = ∟)",
        "contract": ":g:`< B D E C > <g1:< B D E C >>` = :g:`< G B > <g1:< G B >>` + :g:`< H C > <g1:< H C >>`",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>` (:g:`< B A C ) <g1:< B A C )>` = ∟)"),
            ("construct", [], "@fn(I.46)(:g:`/ B C / <g1:/ B C />`, :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />`) → :g:`< B D E C > <g1:< B D E C >>`, :g:`< G B > <g1:< G B >>`, :g:`< H C > <g1:< H C >>`"),
            ("construct", [], "@fn(I.31)(:g:`A <g1:A>`, :g:`/ B D / <g1:/ B D />`) → :g:`/ A L / <g1:/ A L />` ∥ :g:`/ B D / <g1:/ B D />`, @fn(I.post.1)(:g:`A <g1:A>`, :g:`D <g1:D>`) → :g:`/ A D / <g1:/ A D />`, @fn(I.post.1)(:g:`F <g1:F>`, :g:`C <g1:C>`) → :g:`/ F C / <g1:/ F C />`, @fn(I.post.1)(:g:`A <g1:A>`, :g:`E <g1:E>`) → :g:`/ A E / <g1:/ A E />`, @fn(I.post.1)(:g:`B <g1:B>`, :g:`K <g1:K>`) → :g:`/ B K / <g1:/ B K />`"),
            ("assert", ["I.14"], ":g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< B A G )>` :g:`< B A G ) <g1:< B A G )>` = ∟ → :g:`/ C A / <g1:/ C A />`, :g:`/ A G / <g1:/ A G />` ∈ :g:`[ C G ] <g1:[ C A ]>`, :g:`/ B A / <g1:/ B A />`, :g:`/ A H / <g1:/ A H />` ∈ :g:`[ B H ] <g1:[ B A ]>`"),
            ("assert", ["I.cn.2", "I.4"], ":g:`< D B C ) <g1:< D B C )>` :eq:`= <g1:< D B C ) = g1:< F B A )>` :g:`< F B A ) <g1:< F B A )>` → :g:`< D B A ) <g1:< D B A )>` :eq:`= <g1:< D B A ) = g1:< F B C )>` :g:`< F B C ) <g1:< F B C )>`, :g:`/ D B / <g1:/ D B />` :eq:`= <g1:/ D B / = g1:/ B C /; g1:/ F B / = g1:/ B A />` :g:`/ B C / <g1:/ B C />`, :g:`/ F B / <g1:/ F B />` :eq:`= <g1:/ D B / = g1:/ B C /; g1:/ F B / = g1:/ B A />` :g:`/ B A / <g1:/ B A />` → :g:`< A B D > <g1:< A B D >>` :eq:`= <g1:< A B D > = g1:< F B C >>` :g:`< F B C > <g1:< F B C >>`"),
            ("assert", ["I.41"], ":g:`< B L > <g1:< B L >>` = 2 :g:`< A B D > <g1:< A B D >>`, :g:`< G B > <g1:< G B >>` = 2 :g:`< F B C > <g1:< F B C >>` → :g:`< B L > <g1:< B L >>` :eq:`= <g1:< B L > = g1:< G B >>` :g:`< G B > <g1:< G B >>`, :g:`< C L > <g1:< C L >>` :eq:`= <g1:< C L > = g1:< H C >>` :g:`< H C > <g1:< H C >>`"),
            ("conclude", ["I.cn.2"], ":g:`< B D E C > <g1:< B D E C >>` = :g:`< G B > <g1:< G B >>` + :g:`< H C > <g1:< H C >>`"),
        ],
    },
    "I.48": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>` (:fn:`square_on_segment <G.75>`\\ (:g:`/ B C / <g1:/ B C />`) = :fn:`square_on_segment <G.75>`\\ (:g:`/ B A / <g1:/ B A />`) + :fn:`square_on_segment <G.75>`\\ (:g:`/ A C / <g1:/ A C />`))",
        "contract": ":g:`< B A C ) <g1:< B A C )>` = ∟",
        "steps": [
            ("given", [], ":g:`< A B C > <g1:< A B C >>` (@fn(I.46)(:g:`/ B C / <g1:/ B C />`) = @fn(I.46)(:g:`/ B A / <g1:/ B A />`) + @fn(I.46)(:g:`/ A C / <g1:/ A C />`))"),
            ("construct", [], "@fn(I.11)(:g:`/ A C / <g1:/ A C />`, :g:`A <g1:A>`) → :g:`/ A D / <g1:/ A D />` ⊥ :g:`/ A C / <g1:/ A C />`, @fn(I.3)(:g:`/ B A / <g1:/ B A />`) → :g:`/ A D / <g1:/ A D />` (:eq:`= <g1:/ A D / = g1:/ B A />` :g:`/ B A / <g1:/ B A />`), @fn(I.post.1)(:g:`D <g1:D>`, :g:`C <g1:C>`) → :g:`/ D C / <g1:/ D C />`"),
            ("assert", ["I.cn.2"], ":g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ A B />` :g:`/ A B / <g1:/ A B />` → @fn(I.46)(:g:`/ D A / <g1:/ D A />`) + @fn(I.46)(:g:`/ A C / <g1:/ A C />`) = @fn(I.46)(:g:`/ B A / <g1:/ B A />`) + @fn(I.46)(:g:`/ A C / <g1:/ A C />`)"),
            ("assert", ["I.47", "I.cn.1"], ":g:`< D A C ) <g1:< D A C )>` = ∟ → @fn(I.46)(:g:`/ D C / <g1:/ D C />`) = @fn(I.46)(:g:`/ D A / <g1:/ D A />`) + @fn(I.46)(:g:`/ A C / <g1:/ A C />`) = @fn(I.46)(:g:`/ B C / <g1:/ B C />`) → :g:`/ D C / <g1:/ D C />` :eq:`= <g1:/ D C / = g1:/ B C />` :g:`/ B C / <g1:/ B C />`"),
            ("assert", ["I.8"], ":g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ B A />` :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ A C />` :g:`/ A C / <g1:/ A C />`, :g:`/ D C / <g1:/ D C />` :eq:`= <g1:/ D C / = g1:/ B C />` :g:`/ B C / <g1:/ B C />` → :g:`< D A C ) <g1:< D A C )>` :eq:`= <g1:< D A C ) = g1:< B A C )>` :g:`< B A C ) <g1:< B A C )>`"),
            ("conclude", ["I.cn.1"], ":g:`< D A C ) <g1:< D A C )>` = ∟, :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< D A C )>` :g:`< D A C ) <g1:< D A C )>` → :g:`< B A C ) <g1:< B A C )>` = ∟"),
        ],
    },
    "II.1": {
        "subtype": "theorem",
        "args": [":g:`A <g1:A>`", ":g:`/ B C / <g1:/ B C />`", ":g:`D <g1:D>`", ":g:`E <g1:E>`"],
        "returns": [],
        "given": ":g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />` (:g:`D <g1:D>`, :g:`E <g1:E>` ∈ :g:`/ B C / <g1:/ B C />`)",
        "contract": ":fn:`contained_rectangle <G.81>`\\ (:g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />`) = :fn:`contained_rectangle <G.81>`\\ (:g:`A <g1:A>`, :g:`/ B D / <g1:/ B D />`) + :fn:`contained_rectangle <G.81>`\\ (:g:`A <g1:A>`, :g:`/ D E / <g1:/ D E />`) + :fn:`contained_rectangle <G.81>`\\ (:g:`A <g1:A>`, :g:`/ E C / <g1:/ E C />`)",
        "steps": [
            ("given", [], ":g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />` (:g:`/ B C / <g1:/ B C />` = :g:`/ B D / <g1:/ B D />` + :g:`/ D E / <g1:/ D E />` + :g:`/ E C / <g1:/ E C />`)"),
            ("construct", [], "@fn(I.11)(:g:`/ B C / <g1:/ B C />`, :g:`B <g1:B>`) → :g:`/ B F / <g1:/ B F />` ⊥ :g:`/ B C / <g1:/ B C />`, @fn(I.3)(:g:`/ B F / <g1:/ B F />`, :g:`A <g1:A>`) → :g:`/ B G / <g1:/ B G />` (:eq:`= <g1:/ B G / = g1:A>` :g:`A <g1:A>`)"),
            ("construct", ["I.31"], "@fn(I.31)(:g:`G <g1:G>`, :g:`/ B C / <g1:/ B C />`) → :g:`/ G H / <g1:/ G H />` ∥ :g:`/ B C / <g1:/ B C />`, @fn(I.31)(:g:`D <g1:D>`, :g:`E <g1:E>`, :g:`C <g1:C>`, :g:`/ B G / <g1:/ B G />`) → :g:`/ D K / <g1:/ D K />` ∥ :g:`/ E L / <g1:/ E L />` ∥ :g:`/ C H / <g1:/ C H />` ∥ :g:`/ B G / <g1:/ B G />`"),
            ("assert", ["II.def.1"], ":g:`< B H > <g1:< B H >>` = :g:`< B K > <g1:< B K >>` + :g:`< D L > <g1:< D L >>` + :g:`< E H > <g1:< E H >>`, :g:`/ B G / <g1:/ B G />` :eq:`= <g1:/ B G / = g1:A>` :g:`A <g1:A>` → :g:`< B H > <g1:< B H >>` = @fn(II.def.1)(:g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />`), :g:`< B K > <g1:< B K >>` = @fn(II.def.1)(:g:`A <g1:A>`, :g:`/ B D / <g1:/ B D />`)"),
            ("assert", ["I.34", "II.def.1"], ":g:`/ D K / <g1:/ D K />` :eq:`= <g1:/ D K / = g1:/ B G / = g1:A>` :g:`/ E L / <g1:/ E L />` :eq:`= <g1:/ E L / = g1:/ B G / = g1:A>` :g:`/ B G / <g1:/ B G />` :eq:`= <g1:/ B G / = g1:A>` :g:`A <g1:A>` → :g:`< D L > <g1:< D L >>` = @fn(II.def.1)(:g:`A <g1:A>`, :g:`/ D E / <g1:/ D E />`), :g:`< E H > <g1:< E H >>` = @fn(II.def.1)(:g:`A <g1:A>`, :g:`/ E C / <g1:/ E C />`)"),
            ("conclude", ["I.cn.1"], "@fn(II.def.1)(:g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />`) = @fn(II.def.1)(:g:`A <g1:A>`, :g:`/ B D / <g1:/ B D />`) + @fn(II.def.1)(:g:`A <g1:A>`, :g:`/ D E / <g1:/ D E />`) + @fn(II.def.1)(:g:`A <g1:A>`, :g:`/ E C / <g1:/ E C />`)"),
        ],
    },
    "II.2": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`C <g1:C>`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` (:g:`C <g1:C>` ∈ :g:`/ A B / <g1:/ A B />`)",
        "contract": ":fn:`contained_rectangle <G.81>`\\ (:g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`) + :fn:`contained_rectangle <G.81>`\\ (:g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />`) = :fn:`square <G.63>`\\ (:g:`/ A B / <g1:/ A B />`)",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` (:g:`/ A B / <g1:/ A B />` = :g:`/ A C / <g1:/ A C />` + :g:`/ B C / <g1:/ B C />`)"),
            ("construct", ["I.46"], "@fn(I.46)(:g:`/ A B / <g1:/ A B />`) → :g:`< A D E B > <g1:< A D E B >>` (:g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ A B />` :g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ A B />` :g:`/ A B / <g1:/ A B />`)"),
            ("construct", ["I.31"], "@fn(I.31)(:g:`C <g1:C>`, :g:`/ A D / <g1:/ A D />`) → :g:`/ C F / <g1:/ C F />` ∥ :g:`/ A D / <g1:/ A D />`, :g:`/ B E / <g1:/ B E />`"),
            ("assert", ["I.def.22"], ":g:`< A E > <g1:< A E >>` = :g:`< A F > <g1:< A F >>` + :g:`< C E > <g1:< C E >>`, :g:`< A E > <g1:< A E >>` = @fn(I.def.22)(:g:`/ A B / <g1:/ A B />`)"),
            ("assert", ["I.def.22", "II.def.1"], ":g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ A B />` :g:`/ A B / <g1:/ A B />` → :g:`< A F > <g1:< A F >>` = @fn(II.def.1)(:g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />`), :g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ A B />` :g:`/ A B / <g1:/ A B />` → :g:`< C E > <g1:< C E >>` = @fn(II.def.1)(:g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`)"),
            ("conclude", ["I.cn.1"], "@fn(II.def.1)(:g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />`) + @fn(II.def.1)(:g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`) = @fn(I.def.22)(:g:`/ A B / <g1:/ A B />`)"),
        ],
    },
    "II.3": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`C <g1:C>`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` (:g:`C <g1:C>` ∈ :g:`/ A B / <g1:/ A B />`)",
        "contract": ":fn:`contained_rectangle <G.81>`\\ (:g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`) = :fn:`contained_rectangle <G.81>`\\ (:g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`) + :fn:`square <G.63>`\\ (:g:`/ B C / <g1:/ B C />`)",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` (:g:`/ A B / <g1:/ A B />` = :g:`/ A C / <g1:/ A C />` + :g:`/ B C / <g1:/ B C />`)"),
            ("construct", ["I.46"], "@fn(I.46)(:g:`/ B C / <g1:/ B C />`) → :g:`< C D E B > <g1:< C D E B >>` (:g:`/ C D / <g1:/ C D />` :eq:`= <g1:/ C D / = g1:/ B C />` :g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ B C />` :g:`/ B C / <g1:/ B C />`)"),
            ("construct", ["I.post.2", "I.31"], "@fn(I.post.2)(:g:`/ D E / <g1:/ D E />`) → :g:`F <g1:F>`, @fn(I.31)(:g:`A <g1:A>`, :g:`/ C D / <g1:/ C D />`) → :g:`/ A F / <g1:/ A F />` ∥ :g:`/ C D / <g1:/ C D />`, :g:`/ B E / <g1:/ B E />`"),
            ("assert", ["I.def.22", "II.def.1"], ":g:`< A E > <g1:< A E >>` = :g:`< A D > <g1:< A D >>` + :g:`< C E > <g1:< C E >>`, :g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ B C />` :g:`/ B C / <g1:/ B C />` → :g:`< A E > <g1:< A E >>` = @fn(II.def.1)(:g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`)"),
            ("assert", ["I.def.22", "II.def.1"], ":g:`/ C D / <g1:/ C D />` :eq:`= <g1:/ C D / = g1:/ B C />` :g:`/ B C / <g1:/ B C />` → :g:`< A D > <g1:< A D >>` = @fn(II.def.1)(:g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`), :g:`< D B > <g1:< D B >>` = @fn(I.def.22)(:g:`/ B C / <g1:/ B C />`)"),
            ("conclude", ["I.cn.1"], "@fn(II.def.1)(:g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`) = @fn(II.def.1)(:g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`) + @fn(I.def.22)(:g:`/ B C / <g1:/ B C />`)"),
        ],
    },
    "II.4": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`C <g1:C>`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` (:g:`C <g1:C>` ∈ :g:`/ A B / <g1:/ A B />`)",
        "contract": ":fn:`square_on_segment <G.75>`\\ (:g:`/ A B / <g1:/ A B />`) = :fn:`square_on_segment <G.75>`\\ (:g:`/ A C / <g1:/ A C />`) + :fn:`square_on_segment <G.75>`\\ (:g:`/ B C / <g1:/ B C />`) + 2 · :fn:`contained_rectangle <G.81>`\\ (:g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`)",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` (:g:`/ A B / <g1:/ A B />` = :g:`/ A C / <g1:/ A C />` + :g:`/ B C / <g1:/ B C />`)"),
            ("construct", ["I.46", "I.post.1"], "@fn(I.46)(:g:`/ A B / <g1:/ A B />`) → :g:`< A D E B > <g1:< A D E B >>`, @fn(I.post.1)(:g:`B <g1:B>`, :g:`D <g1:D>`) → :g:`/ B D / <g1:/ B D />`"),
            ("construct", ["I.31"], "@fn(I.31)(:g:`C <g1:C>`, :g:`/ A D / <g1:/ A D />`) → :g:`/ C F / <g1:/ C F />` ∥ :g:`/ A D / <g1:/ A D />`, :g:`/ C F / <g1:/ C F />` ∩ :g:`/ B D / <g1:/ B D />` → :g:`G <g1:G>`, @fn(I.31)(:g:`G <g1:G>`, :g:`/ A B / <g1:/ A B />`) → :g:`/ H K / <g1:/ H K />` ∥ :g:`/ A B / <g1:/ A B />`"),
            ("assert", ["I.29", "I.5", "I.6", "I.34"], ":g:`< C G B ) <g1:< C G B )>` :eq:`= <g1:< C G B ) = g1:< A D B )>` :g:`< A D B ) <g1:< A D B )>` :eq:`= <g1:< A D B ) = g1:< A B D )>` :g:`< A B D ) <g1:< A B D )>` → :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ C G / = g1:/ G K / = g1:/ B K />` :g:`/ C G / <g1:/ C G />` :eq:`= <g1:/ B C / = g1:/ C G / = g1:/ G K / = g1:/ B K />` :g:`/ G K / <g1:/ G K />` :eq:`= <g1:/ B C / = g1:/ C G / = g1:/ G K / = g1:/ B K />` :g:`/ B K / <g1:/ B K />`"),
            ("assert", ["I.29", "I.34", "I.def.22"], ":g:`< K B C ) <g1:< K B C )>` :eq:`= <g1:< C G K ) = g1:< G K B ) = g1:< K B C ) = g1:< G C B )>` :g:`< G C B ) <g1:< G C B )>` :eq:`= <g1:< C G K ) = g1:< G K B ) = g1:< K B C ) = g1:< G C B )>` :g:`< C G K ) <g1:< C G K )>` :eq:`= <g1:< C G K ) = g1:< G K B ) = g1:< K B C ) = g1:< G C B )>` :g:`< G K B ) <g1:< G K B )>` → :g:`< C G K B > <g1:< C G K B >>` = @fn(I.46)(:g:`/ B C / <g1:/ B C />`), :g:`< H F > <g1:< H F >>` = @fn(I.46)(:g:`/ A C / <g1:/ A C />`)"),
            ("assert", ["I.43", "II.def.1"], ":g:`< A G > <g1:< A G >>` :eq:`= <g1:< A G > = g1:< G E >>` :g:`< G E > <g1:< G E >>` = @fn(II.def.1)(:g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`) → :g:`< A G > <g1:< A G >>` + :g:`< G E > <g1:< G E >>` = 2 · @fn(II.def.1)(:g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`)"),
            ("conclude", ["I.cn.2"], "@fn(I.46)(:g:`/ A B / <g1:/ A B />`) = @fn(I.46)(:g:`/ A C / <g1:/ A C />`) + @fn(I.46)(:g:`/ B C / <g1:/ B C />`) + 2 · @fn(II.def.1)(:g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />`)"),
        ],
    },
    "II.5": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`C <g1:C>`", ":g:`D <g1:D>`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` (:g:`C <g1:C>`, :g:`D <g1:D>` ∈ :g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`)",
        "contract": ":fn:`contained_rectangle <G.81>`\\ (:g:`/ A D / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />`) + :fn:`square_on_segment <G.75>`\\ (:g:`/ C D / <g1:/ C D />`) = :fn:`square_on_segment <G.75>`\\ (:g:`/ C B / <g1:/ C B />`)",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` (:g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`, :g:`/ A B / <g1:/ A B />` = :g:`/ A D / <g1:/ A D />` + :g:`/ D B / <g1:/ D B />`)"),
            ("construct", ["I.46", "I.post.1"], "@fn(I.46)(:g:`/ C B / <g1:/ C B />`) → :g:`< C E F B > <g1:< C E F B >>`, @fn(I.post.1)(:g:`B <g1:B>`, :g:`E <g1:E>`) → :g:`/ B E / <g1:/ B E />`"),
            ("construct", ["I.31"], "@fn(I.31)(:g:`D <g1:D>`, :g:`/ C E / <g1:/ C E />`) → :g:`/ D G / <g1:/ D G />` ∥ :g:`/ C E / <g1:/ C E />`, @fn(I.31)(:g:`H <g1:H>`, :g:`/ A B / <g1:/ A B />`) → :g:`/ K M / <g1:/ K M />` ∥ :g:`/ A B / <g1:/ A B />`, @fn(I.31)(:g:`A <g1:A>`, :g:`/ C L / <g1:/ C L />`) → :g:`/ A K / <g1:/ A K />` ∥ :g:`/ C L / <g1:/ C L />`"),
            ("assert", ["I.43", "I.cn.2", "I.36", "I.cn.1"], ":g:`< C H > <g1:< C H >>` :eq:`= <g1:< C H > = g1:< H F >>` :g:`< H F > <g1:< H F >>` → :g:`< C M > <g1:< C M >>` :eq:`= <g1:< C M > = g1:< D F >>` :g:`< D F > <g1:< D F >>`, :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />` → :g:`< A L > <g1:< A L >>` :eq:`= <g1:< C M > = g1:< A L >>` :g:`< C M > <g1:< C M >>` :eq:`= <g1:< A L > = g1:< D F >>` :g:`< D F > <g1:< D F >>`"),
            ("assert", ["I.cn.2", "II.def.1", "II.def.2"], ":g:`< A L > <g1:< A L >>` + :g:`< C H > <g1:< C H >>` = :g:`< D F > <g1:< D F >>` + :g:`< C H > <g1:< C H >>` → :g:`< A H > <g1:< A H >>` :eq:`= <g1:< A H > = g1:< N O P >>` :g:`< N O P > <g1:< N O P >>` = @fn(II.def.1)(:g:`/ A D / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />`)"),
            ("conclude", ["I.cn.2"], ":g:`< N O P > <g1:< N O P >>` + :g:`< L G > <g1:< L G >>` = :g:`< C E F B > <g1:< C E F B >>` → @fn(II.def.1)(:g:`/ A D / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />`) + @fn(I.46)(:g:`/ C D / <g1:/ C D />`) = @fn(I.46)(:g:`/ C B / <g1:/ C B />`)"),
        ],
    },
    "II.6": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`C <g1:C>`", ":g:`/ B D / <g1:/ B D />`"],
        "returns": [],
        "given": ":g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`, :g:`/ A D / <g1:/ A D />` = :g:`/ A B / <g1:/ A B />` + :g:`/ B D / <g1:/ B D />`",
        "contract": ":fn:`contained_rectangle <G.81>`\\ (:g:`/ A D / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />`) + :fn:`square <G.63>`\\ (:g:`/ C B / <g1:/ C B />`) = :fn:`square <G.63>`\\ (:g:`/ C D / <g1:/ C D />`)",
        "steps": [
            ("given", [], ":g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`, :g:`/ A D / <g1:/ A D />` = :g:`/ A B / <g1:/ A B />` + :g:`/ B D / <g1:/ B D />`"),
            ("construct", ["I.46", "I.post.1"], "@fn(I.46)(:g:`/ C D / <g1:/ C D />`) → :g:`< C E F D > <g1:< C E F D >>`, @fn(I.post.1)(:g:`D <g1:D>`, :g:`E <g1:E>`) → :g:`/ D E / <g1:/ D E />`"),
            ("construct", ["I.31"], "@fn(I.31)(:g:`B <g1:B>`, :g:`/ E C / <g1:/ E C />`) → :g:`/ B G / <g1:/ B G />` ∥ :g:`/ E C / <g1:/ E C />`, @fn(I.31)(:g:`H <g1:H>`, :g:`/ A B / <g1:/ A B />`) → :g:`/ K M / <g1:/ K M />` ∥ :g:`/ A B / <g1:/ A B />`, @fn(I.31)(:g:`A <g1:A>`, :g:`/ C L / <g1:/ C L />`) → :g:`/ A K / <g1:/ A K />` ∥ :g:`/ C L / <g1:/ C L />`"),
            ("assert", ["I.36", "I.43", "I.cn.2"], ":g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />` → :g:`< A L > <g1:< A L >>` :eq:`= <g1:< A L > = g1:< C H >>` :g:`< C H > <g1:< C H >>` :eq:`= <g1:< C H > = g1:< H F >>` :g:`< H F > <g1:< H F >>`; + :g:`< C M > <g1:< C M >>` → :g:`< A M > <g1:< A M >>` :eq:`= <g1:< A M > = g1:< N O P >>` :g:`< N O P > <g1:< N O P >>`"),
            ("assert", ["II.def.1", "II.def.2"], ":g:`/ D M / <g1:/ D M />` :eq:`= <g1:/ D M / = g1:/ D B />` :g:`/ D B / <g1:/ D B />` → :g:`< A M > <g1:< A M >>` = @fn(II.def.1)(:g:`/ A D / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />`) = :g:`< N O P > <g1:< N O P >>`"),
            ("conclude", ["I.cn.2", "I.def.22"], "+ :g:`< L G > <g1:< L G >>` (= @fn(I.def.22)(:g:`/ C B / <g1:/ C B />`)) → @fn(II.def.1)(:g:`/ A D / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />`) + @fn(I.def.22)(:g:`/ C B / <g1:/ C B />`) = :g:`< N O P > <g1:< N O P >>` + :g:`< L G > <g1:< L G >>` = @fn(I.def.22)(:g:`/ C D / <g1:/ C D />`)"),
        ],
    },
    "II.7": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`C <g1:C>`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` (:g:`C <g1:C>` ∈ :g:`/ A B / <g1:/ A B />`)",
        "contract": ":fn:`square <G.63>`\\ (:g:`/ A B / <g1:/ A B />`) + :fn:`square <G.63>`\\ (:g:`/ B C / <g1:/ B C />`) = 2 · :fn:`contained_rectangle <G.81>`\\ (:g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`) + :fn:`square <G.63>`\\ (:g:`/ C A / <g1:/ C A />`)",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` = :g:`/ A C / <g1:/ A C />` + :g:`/ C B / <g1:/ C B />`"),
            ("construct", ["I.46", "I.def.14"], "@fn(I.46)(:g:`/ A B / <g1:/ A B />`) → :g:`< A D E B > <g1:< A D E B >>`, draw :g:`/ B D / <g1:/ B D />`, :g:`/ C N / <g1:/ C N />` ∥ :g:`/ A D / <g1:/ A D />`, :g:`/ H F / <g1:/ H F />` ∥ :g:`/ A B / <g1:/ A B />`"),
            ("assert", ["I.43", "I.cn.2"], ":g:`< A G > <g1:< A G >>` :eq:`= <g1:< A G > = g1:< G E >>` :g:`< G E > <g1:< G E >>`; + :g:`< C F > <g1:< C F >>` → :g:`< A F > <g1:< A F >>` :eq:`= <g1:< A F > = g1:< C E >>` :g:`< C E > <g1:< C E >>` → :g:`< A F > <g1:< A F >>` + :g:`< C E > <g1:< C E >>` = 2 · :g:`< A F > <g1:< A F >>`"),
            ("assert", ["II.def.1", "II.def.2"], ":g:`< A F > <g1:< A F >>` + :g:`< C E > <g1:< C E >>` = :g:`< K L M > <g1:< K L M >>` + :g:`< C F > <g1:< C F >>`, :g:`/ B F / <g1:/ B F />` :eq:`= <g1:/ B F / = g1:/ B C />` :g:`/ B C / <g1:/ B C />` → :g:`< K L M > <g1:< K L M >>` + :g:`< C F > <g1:< C F >>` = 2 · @fn(II.def.1)(:g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`)"),
            ("conclude", ["I.cn.2", "I.def.22"], "+ :g:`< D G > <g1:< D G >>` (= @fn(I.def.22)(:g:`/ A C / <g1:/ A C />`)) → @fn(I.def.22)(:g:`/ A B / <g1:/ A B />`) + @fn(I.def.22)(:g:`/ B C / <g1:/ B C />`) = 2 · @fn(II.def.1)(:g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`) + @fn(I.def.22)(:g:`/ A C / <g1:/ A C />`)"),
        ],
    },
    "II.8": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`C <g1:C>`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` (:g:`C <g1:C>` ∈ :g:`/ A B / <g1:/ A B />`)",
        "contract": "4 · :fn:`contained_rectangle <G.81>`\\ (:g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`) + :fn:`square <G.63>`\\ (:g:`/ A C / <g1:/ A C />`) = :fn:`square <G.63>`\\ (:g:`/ A B / <g1:/ A B />` + :g:`/ B C / <g1:/ B C />`)",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` = :g:`/ A C / <g1:/ A C />` + :g:`/ C B / <g1:/ C B />`"),
            ("construct", ["I.post.2", "I.3", "I.46", "I.31"], "@fn(I.3)(:g:`/ C B / <g1:/ C B />`) → :g:`/ B D / <g1:/ B D />` (:eq:`= <g1:/ B D / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`), @fn(I.46)(:g:`/ A D / <g1:/ A D />`) → :g:`< A E F D > <g1:< A E F D >>`, draw :g:`/ D E / <g1:/ D E />` and parallels :g:`/ C H / <g1:/ C H />`, :g:`/ B L / <g1:/ B L />`, :g:`/ M N / <g1:/ M N />`, :g:`/ O P / <g1:/ O P />`"),
            ("assert", ["I.34", "I.36", "I.43"], ":g:`/ C B / <g1:/ C B />` :eq:`= <g1:/ C B / = g1:/ B D / = g1:/ G K / = g1:/ K N />` :g:`/ B D / <g1:/ B D />` → :g:`< D K > <g1:< B D N K >>` :eq:`= <g1:< B D N K > = g1:< C B K G > = g1:< G K R Q > = g1:< K N P R >>` :g:`< C K > <g1:< C B K G >>` :eq:`= <g1:< C B K G > = g1:< G K R Q >>` :g:`< G R > <g1:< G K R Q >>` :eq:`= <g1:< G K R Q > = g1:< K N P R >>` :g:`< R N > <g1:< K N P R >>` → sum = 4 · :g:`< C K > <g1:< C B K G >>`"),
            ("assert", ["I.36", "I.43", "II.def.1", "II.def.2"], ":g:`< A G > <g1:< A C G M >>` :eq:`= <g1:< A C G M > = g1:< M G Q O > = g1:< Q R L H > = g1:< R P F L >>` :g:`< M Q > <g1:< M G Q O >>` :eq:`= <g1:< M G Q O > = g1:< Q R L H >>` :g:`< Q L > <g1:< Q R L H >>` :eq:`= <g1:< Q R L H > = g1:< R P F L >>` :g:`< R F > <g1:< R P F L >>` → gnomon :g:`< S T U > <g1:< S T U >>` = 4 · :g:`< A K > <g1:< A B K M >>` = 4 · @fn(II.def.1)(:g:`/ A B / <g1:/ A B />`, :g:`/ B D / <g1:/ B D />`)"),
            ("assert", ["I.34", "I.cn.2"], ":g:`< O H > <g1:< O Q H E >>` = :fn:`square <G.63>`\\ (:g:`/ A C / <g1:/ A C />`) → 4 · @fn(II.def.1)(:g:`/ A B / <g1:/ A B />`, :g:`/ B D / <g1:/ B D />`) + :fn:`square <G.63>`\\ (:g:`/ A C / <g1:/ A C />`) = :g:`< S T U > <g1:< S T U >>` + :g:`< O H > <g1:< O Q H E >>` = :g:`< A E F D > <g1:< A E F D >>`"),
            ("conclude", ["I.cn.1"], ":g:`/ B D / <g1:/ B D />` :eq:`= <g1:/ B D / = g1:/ B C />` :g:`/ B C / <g1:/ B C />` → 4 · @fn(II.def.1)(:g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`) + :fn:`square <G.63>`\\ (:g:`/ A C / <g1:/ A C />`) = :fn:`square <G.63>`\\ (:g:`/ A D / <g1:/ A D />`) = :fn:`square <G.63>`\\ (:g:`/ A B / <g1:/ A B />` + :g:`/ B C / <g1:/ B C />`)"),
        ],
    },
    "II.9": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`C <g1:C>`", ":g:`D <g1:D>`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` (:g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`, :g:`D <g1:D>` ∈ :g:`/ C B / <g1:/ C B />`)",
        "contract": ":fn:`square <G.63>`\\ (:g:`/ A D / <g1:/ A D />`) + :fn:`square <G.63>`\\ (:g:`/ D B / <g1:/ D B />`) = 2 · (:fn:`square <G.63>`\\ (:g:`/ A C / <g1:/ A C />`) + :fn:`square <G.63>`\\ (:g:`/ C D / <g1:/ C D />`))",
        "steps": [
            ("given", [], ":g:`/ A B / <g1:/ A B />` cut equally at :g:`C <g1:C>` (:g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`) and unequally at :g:`D <g1:D>`"),
            ("construct", ["I.11", "I.3", "I.post.1", "I.31"], "@fn(I.11)(:g:`/ A B / <g1:/ A B />`, :g:`C <g1:C>`) → :g:`/ C E / <g1:/ C E />` (:eq:`= <g1:/ C E / = g1:/ A C / = g1:/ C B />` :g:`/ A C / <g1:/ A C />`), join :g:`/ E A / <g1:/ E A />`, :g:`/ E B / <g1:/ E B />`, draw :g:`/ D F / <g1:/ D F />` ∥ :g:`/ C E / <g1:/ C E />`, :g:`/ F G / <g1:/ G F />` ∥ :g:`/ A B / <g1:/ A B />`, join :g:`/ A F / <g1:/ A F />`"),
            ("assert", ["I.5", "I.32", "I.29", "I.6"], ":g:`< C A E ) <g1:< E A C )>` :eq:`= <g1:< E A C ) = g1:< A E C ) = g1:< C E B ) = g1:< E B C )>` :g:`< C E A ) <g1:< A E C )>` :eq:`= <g1:< A E C ) = g1:< C E B )>` :g:`< C E B ) <g1:< C E B )>` :eq:`= <g1:< C E B ) = g1:< E B C )>` :g:`< E B C ) <g1:< E B C )>` = ½ right → :g:`< A E B ) <g1:< A E B )>` is right, :g:`/ E G / <g1:/ G E />` :eq:`= <g1:/ G E / = g1:/ G F />` :g:`/ G F / <g1:/ G F />`, :g:`/ F D / <g1:/ D F />` :eq:`= <g1:/ D F / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`"),
            ("assert", ["I.47", "I.34"], ":g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C E />` :g:`/ C E / <g1:/ C E />` → :fn:`square <G.63>`\\ (:g:`/ E A / <g1:/ E A />`) = 2 · :fn:`square <G.63>`\\ (:g:`/ A C / <g1:/ A C />`); :g:`/ E G / <g1:/ G E />` :eq:`= <g1:/ G E / = g1:/ G F / = g1:/ C D />` :g:`/ G F / <g1:/ G F />` :eq:`= <g1:/ G F / = g1:/ C D />` :g:`/ C D / <g1:/ C D />` → :fn:`square <G.63>`\\ (:g:`/ E F / <g1:/ E F />`) = 2 · :fn:`square <G.63>`\\ (:g:`/ C D / <g1:/ C D />`)"),
            ("assert", ["I.47", "I.cn.2"], ":fn:`square <G.63>`\\ (:g:`/ A F / <g1:/ A F />`) = :fn:`square <G.63>`\\ (:g:`/ A E / <g1:/ E A />`) + :fn:`square <G.63>`\\ (:g:`/ E F / <g1:/ E F />`) = :fn:`square <G.63>`\\ (:g:`/ A D / <g1:/ A D />`) + :fn:`square <G.63>`\\ (:g:`/ D F / <g1:/ D F />`) = 2 · (:fn:`square <G.63>`\\ (:g:`/ A C / <g1:/ A C />`) + :fn:`square <G.63>`\\ (:g:`/ C D / <g1:/ C D />`))"),
            ("conclude", ["I.cn.1"], ":g:`/ D F / <g1:/ D F />` :eq:`= <g1:/ D F / = g1:/ D B />` :g:`/ D B / <g1:/ D B />` → :fn:`square <G.63>`\\ (:g:`/ A D / <g1:/ A D />`) + :fn:`square <G.63>`\\ (:g:`/ D B / <g1:/ D B />`) = 2 · (:fn:`square <G.63>`\\ (:g:`/ A C / <g1:/ A C />`) + :fn:`square <G.63>`\\ (:g:`/ C D / <g1:/ C D />`))"),
        ],
    },
    "II.10": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`C <g1:C>`", ":g:`/ B D / <g1:/ B D />`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />` (:g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`), :g:`/ B D / <g1:/ B D />`",
        "contract": ":fn:`square_on_segment <G.75>`\\ (:g:`/ A D / <g1:/ A D />`) + :fn:`square_on_segment <G.75>`\\ (:g:`/ D B / <g1:/ D B />`) = 2 · (:fn:`square_on_segment <G.75>`\\ (:g:`/ A C / <g1:/ A C />`) + :fn:`square_on_segment <G.75>`\\ (:g:`/ C D / <g1:/ C D />`))",
        "steps": [
            ("given", ["I.def.4"], ":g:`/ A B / <g1:/ A B />` (:g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`), :g:`/ B D / <g1:/ B D />` (:g:`/ A D / <g1:/ A D />` = :g:`/ A B / <g1:/ A B />` + :g:`/ B D / <g1:/ B D />`)"),
            ("construct", ["I.11", "I.3", "I.post.1"], "@fn(I.11)(:g:`/ A B / <g1:/ A B />`, :g:`C <g1:C>`) → :g:`/ C E / <g1:/ C E />` ⊥ :g:`/ A B / <g1:/ A B />`, @fn(I.3)(:g:`/ C E / <g1:/ C E />`, :g:`/ A C / <g1:/ A C />`) → :g:`/ C E / <g1:/ C E />` :eq:`= <g1:/ C E / = g1:/ A C / = g1:/ C B />` :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ C E / = g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`, @fn(I.post.1)(:g:`E <g1:E>`, :g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ E A / <g1:/ E A />`, :g:`/ E B / <g1:/ E B />`"),
            ("construct", ["I.31", "I.29", "I.post.5"], "@fn(I.31)(:g:`E <g1:E>`, :g:`/ A D / <g1:/ A D />`) → :g:`/ E F / <g1:/ E F />` ∥ :g:`/ A D / <g1:/ A D />`, @fn(I.31)(:g:`D <g1:D>`, :g:`/ C E / <g1:/ C E />`) → :g:`/ F D / <g1:/ F D />` ∥ :g:`/ C E / <g1:/ C E />`, :g:`[ E B ] <g1:[ E B ]>` ∩ :g:`[ F D ] <g1:[ F D ]>` → :g:`G <g1:G>`, :g:`/ A G / <g1:/ A G />`"),
            ("assert", ["I.5", "I.32", "I.15", "I.29", "I.34", "I.6"], ":g:`< A E B ) <g1:< A E B )>` is right, :g:`< D G B ) <g1:< D G B )>` :eq:`= <g1:< D G B ) = g1:< D B G )>` :g:`< D B G ) <g1:< D B G )>` → :g:`/ G D / <g1:/ G D />` :eq:`= <g1:/ B D / = g1:/ G D />` :g:`/ B D / <g1:/ B D />`, :g:`< E G F ) <g1:< E G F )>` :eq:`= <g1:< E G F ) = g1:< F E G )>` :g:`< F E G ) <g1:< F E G )>` → :g:`/ G F / <g1:/ G F />` :eq:`= <g1:/ G F / = g1:/ E F />` :g:`/ E F / <g1:/ E F />` :eq:`= <g1:/ E F / = g1:/ C D />` :g:`/ C D / <g1:/ C D />`"),
            ("assert", ["I.47", "I.34", "I.cn.1"], ":fn:`square_on_segment <G.75>`\\ (:g:`/ E A / <g1:/ E A />`) = 2 · :fn:`square_on_segment <G.75>`\\ (:g:`/ A C / <g1:/ A C />`), :fn:`square_on_segment <G.75>`\\ (:g:`/ E G / <g1:/ E G />`) = 2 · :fn:`square_on_segment <G.75>`\\ (:g:`/ E F / <g1:/ E F />`) = 2 · :fn:`square_on_segment <G.75>`\\ (:g:`/ C D / <g1:/ C D />`)"),
            ("conclude", ["I.47", "I.cn.1"], ":fn:`square_on_segment <G.75>`\\ (:g:`/ A D / <g1:/ A D />`) + :fn:`square_on_segment <G.75>`\\ (:g:`/ D B / <g1:/ D B />`) = :fn:`square_on_segment <G.75>`\\ (:g:`/ A G / <g1:/ A G />`) = 2 · (:fn:`square_on_segment <G.75>`\\ (:g:`/ A C / <g1:/ A C />`) + :fn:`square_on_segment <G.75>`\\ (:g:`/ C D / <g1:/ C D />`))"),
        ],
    },
    "II.11": {
        "subtype": "problem",
        "args": [":g:`/ A B / <g1:/ A B />`"],
        "returns": [":g:`H <g1:H>`"],
        "given": ":g:`/ A B / <g1:/ A B />`",
        "contract": ":fn:`contained_rectangle <G.81>`\\ (:g:`/ A B / <g1:/ A B />`, :g:`/ B H / <g1:/ B H />`) :eq:`= <g1:< H B D K > = g1:< A F G H >>` :fn:`square_on_segment <G.75>`\\ (:g:`/ A H / <g1:/ A H />`)",
        "steps": [
            ("given", ["I.def.4"], ":g:`/ A B / <g1:/ A B />`"),
            ("construct", ["I.46", "I.10", "I.post.1"], "@fn(I.46)(:g:`/ A B / <g1:/ A B />`) → :g:`< A B D C > <g1:< A B D C >>`, @fn(I.10)(:g:`/ A C / <g1:/ A C />`) → :g:`E <g1:E>` (:g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E C />` :g:`/ E C / <g1:/ E C />`), @fn(I.post.1)(:g:`B <g1:B>`, :g:`E <g1:E>`) → :g:`/ B E / <g1:/ B E />`"),
            ("construct", ["I.post.2", "I.3", "I.46"], "@fn(I.post.2)(:g:`/ C A / <g1:/ C A />`) → :g:`F <g1:F>`, @fn(I.3)(:g:`/ E F / <g1:/ E F />`, :g:`/ B E / <g1:/ B E />`) → :g:`/ E F / <g1:/ E F />` :eq:`= <g1:/ E F / = g1:/ B E />` :g:`/ B E / <g1:/ B E />`, @fn(I.46)(:g:`/ A F / <g1:/ A F />`) → :g:`< F H > <g1:< F H >>`, @fn(I.post.2)(:g:`/ G H / <g1:/ G H />`) → :g:`K <g1:K>`"),
            ("assert", ["II.6", "I.47", "I.cn.3"], "@fn(II.def.1)(:g:`/ C F / <g1:/ C F />`, :g:`/ F A / <g1:/ F A />`) + :fn:`square_on_segment <G.75>`\\ (:g:`/ A E / <g1:/ A E />`) = :fn:`square_on_segment <G.75>`\\ (:g:`/ E F / <g1:/ E F />`) = :fn:`square_on_segment <G.75>`\\ (:g:`/ E B / <g1:/ E B />`) = :fn:`square_on_segment <G.75>`\\ (:g:`/ A B / <g1:/ A B />`) + :fn:`square_on_segment <G.75>`\\ (:g:`/ A E / <g1:/ A E />`) → :g:`< F K > <g1:< C F G K >>` :eq:`= <g1:< C F G K > = g1:< A B D C >>` :g:`< A B D C > <g1:< A B D C >>`"),
            ("assert", ["I.cn.3"], ":g:`< F K > <g1:< C F G K >>` − :g:`< A K > <g1:< A H K C >>` = :g:`< A B D C > <g1:< A B D C >>` − :g:`< A K > <g1:< A H K C >>` → :g:`< F H > <g1:< A F G H >>` :eq:`= <g1:< A F G H > = g1:< H B D K >>` :g:`< H D > <g1:< H B D K >>`"),
            ("conclude", ["I.def.22", "II.def.1"], ":fn:`contained_rectangle <G.81>`\\ (:g:`/ A B / <g1:/ A B />`, :g:`/ B H / <g1:/ B H />`) :eq:`= <g1:< H B D K > = g1:< A F G H >>` :fn:`square_on_segment <G.75>`\\ (:g:`/ A H / <g1:/ A H />`)"),
        ],
    },
    "II.12": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`/ B D / <g1:/ B D />`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>` (:g:`< B A C ) <g1:< B A C )>` > ∟), :g:`/ B D / <g1:/ B D />` ⊥ :g:`[ C A ] <g1:[ C A ]>`",
        "contract": ":fn:`square_on_segment <G.75>`\\ (:g:`/ B C / <g1:/ B C />`) = :fn:`square_on_segment <G.75>`\\ (:g:`/ B A / <g1:/ B A />`) + :fn:`square_on_segment <G.75>`\\ (:g:`/ A C / <g1:/ A C />`) + 2 :fn:`contained_rectangle <G.81>`\\ (:g:`/ C A / <g1:/ C A />`, :g:`/ A D / <g1:/ A D />`)",
        "steps": [
            ("given", ["I.def.11", "I.def.21"], ":g:`< A B C > <g1:< A B C >>` (:g:`< B A C ) <g1:< B A C )>` > ∟)"),
            ("construct", ["I.post.2", "I.12"], "@fn(I.post.2)(:g:`/ C A / <g1:/ C A />`) → :g:`[ C A ] <g1:[ C A ]>`, @fn(I.12)(:g:`[ C A ] <g1:[ C A ]>`, :g:`B <g1:B>`) → :g:`/ B D / <g1:/ B D />` ⊥ :g:`[ C A ] <g1:[ C A ]>` (:g:`< C D B ) <g1:< C D B )>` = ∟)"),
            ("assert", ["II.4"], ":g:`/ C D / <g1:/ C D />` = :g:`/ C A / <g1:/ C A />` + :g:`/ A D / <g1:/ A D />` → @fn(I.46)(:g:`/ C D / <g1:/ C D />`) = @fn(I.46)(:g:`/ C A / <g1:/ C A />`) + @fn(I.46)(:g:`/ A D / <g1:/ A D />`) + 2 @fn(II.def.1)(:g:`/ C A / <g1:/ C A />`, :g:`/ A D / <g1:/ A D />`)"),
            ("assert", ["I.cn.2"], "@fn(I.46)(:g:`/ C D / <g1:/ C D />`) + @fn(I.46)(:g:`/ D B / <g1:/ D B />`) = @fn(I.46)(:g:`/ C A / <g1:/ C A />`) + @fn(I.46)(:g:`/ A D / <g1:/ A D />`) + @fn(I.46)(:g:`/ D B / <g1:/ D B />`) + 2 @fn(II.def.1)(:g:`/ C A / <g1:/ C A />`, :g:`/ A D / <g1:/ A D />`)"),
            ("assert", ["I.47"], ":g:`< C D B ) <g1:< C D B )>` = ∟ → @fn(I.46)(:g:`/ C B / <g1:/ C B />`) = @fn(I.46)(:g:`/ C D / <g1:/ C D />`) + @fn(I.46)(:g:`/ D B / <g1:/ D B />`), @fn(I.46)(:g:`/ A B / <g1:/ A B />`) = @fn(I.46)(:g:`/ A D / <g1:/ A D />`) + @fn(I.46)(:g:`/ D B / <g1:/ D B />`)"),
            ("conclude", ["I.cn.1"], "@fn(I.46)(:g:`/ B C / <g1:/ B C />`) = @fn(I.46)(:g:`/ B A / <g1:/ B A />`) + @fn(I.46)(:g:`/ A C / <g1:/ A C />`) + 2 @fn(II.def.1)(:g:`/ C A / <g1:/ C A />`, :g:`/ A D / <g1:/ A D />`)"),
        ],
    },
    "II.13": {
        "subtype": "theorem",
        "args": [":g:`< A B C > <g1:< A B C >>`", ":g:`/ A D / <g1:/ A D />`"],
        "returns": [],
        "given": ":g:`< A B C > <g1:< A B C >>` (:g:`< A B C ) <g1:< A B C )>` < ∟), :g:`/ A D / <g1:/ A D />` ⊥ :g:`/ B C / <g1:/ B C />`",
        "contract": ":fn:`square_on_segment <G.75>`\\ (:g:`/ A C / <g1:/ A C />`) + 2 :fn:`contained_rectangle <G.81>`\\ (:g:`/ C B / <g1:/ C B />`, :g:`/ B D / <g1:/ B D />`) = :fn:`square_on_segment <G.75>`\\ (:g:`/ C B / <g1:/ C B />`) + :fn:`square_on_segment <G.75>`\\ (:g:`/ B A / <g1:/ B A />`)",
        "steps": [
            ("given", ["I.def.12", "I.def.21"], ":g:`< A B C > <g1:< A B C >>` (:g:`< A B C ) <g1:< A B C )>` < ∟)"),
            ("construct", ["I.12"], "@fn(I.12)(:g:`/ B C / <g1:/ B C />`, :g:`A <g1:A>`) → :g:`/ A D / <g1:/ A D />` ⊥ :g:`/ B C / <g1:/ B C />` (:g:`< A D B ) <g1:< A D B )>` = ∟)"),
            ("assert", ["II.7"], ":g:`/ C B / <g1:/ C B />` = :g:`/ B D / <g1:/ B D />` + :g:`/ D C / <g1:/ D C />` → @fn(I.46)(:g:`/ C B / <g1:/ C B />`) + @fn(I.46)(:g:`/ B D / <g1:/ B D />`) = 2 @fn(II.def.1)(:g:`/ C B / <g1:/ C B />`, :g:`/ B D / <g1:/ B D />`) + @fn(I.46)(:g:`/ D C / <g1:/ D C />`)"),
            ("assert", ["I.cn.2"], "@fn(I.46)(:g:`/ C B / <g1:/ C B />`) + @fn(I.46)(:g:`/ B D / <g1:/ B D />`) + @fn(I.46)(:g:`/ D A / <g1:/ D A />`) = 2 @fn(II.def.1)(:g:`/ C B / <g1:/ C B />`, :g:`/ B D / <g1:/ B D />`) + @fn(I.46)(:g:`/ A D / <g1:/ A D />`) + @fn(I.46)(:g:`/ D C / <g1:/ D C />`)"),
            ("assert", ["I.47"], ":g:`< A D B ) <g1:< A D B )>` = ∟ → @fn(I.46)(:g:`/ A B / <g1:/ A B />`) = @fn(I.46)(:g:`/ B D / <g1:/ B D />`) + @fn(I.46)(:g:`/ D A / <g1:/ D A />`), @fn(I.46)(:g:`/ A C / <g1:/ A C />`) = @fn(I.46)(:g:`/ A D / <g1:/ A D />`) + @fn(I.46)(:g:`/ D C / <g1:/ D C />`)"),
            ("conclude", ["I.cn.1"], "@fn(I.46)(:g:`/ C B / <g1:/ C B />`) + @fn(I.46)(:g:`/ B A / <g1:/ B A />`) = @fn(I.46)(:g:`/ A C / <g1:/ A C />`) + 2 @fn(II.def.1)(:g:`/ C B / <g1:/ C B />`, :g:`/ B D / <g1:/ B D />`)"),
        ],
    },
    "II.14": {
        "subtype": "problem",
        "args": [":g:`A <g1:A>`"],
        "returns": [":g:`/ E H / <g1:/ E H />`"],
        "given": ":g:`A <g1:A>`",
        "contract": ":fn:`square_on_segment <G.75>`\\ (:g:`/ E H / <g1:/ E H />`) :eq:`= <g1:/ E H / = g1:A>` :g:`A <g1:A>`",
        "steps": [
            ("given", [], ":g:`A <g1:A>`"),
            ("construct", ["I.45", "I.post.2", "I.3"], "@fn(I.45)(:g:`A <g1:A>`) → :g:`< B D E C > <g1:< B D E C >>` (:eq:`= <g1:< B D E C > = g1:A>` :g:`A <g1:A>`), ? ¬(:g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ E D />` :g:`/ E D / <g1:/ E D />`) → @fn(I.post.2)(:g:`/ B E / <g1:/ B E />`) → :g:`[ B F ] <g1:[ B E ]>`, @fn(I.3)(:g:`[ B F ] <g1:[ B E ]>`, :g:`/ E D / <g1:/ E D />`) → :g:`/ E F / <g1:/ E F />` (:eq:`= <g1:/ E F / = g1:/ E D />` :g:`/ E D / <g1:/ E D />`)"),
            ("construct", ["I.10", "I.def.18", "I.post.2", "I.post.1"], "@fn(I.10)(:g:`/ B F / <g1:/ B F />`) → :g:`G <g1:G>` (:g:`/ G B / <g1:/ G B />` :eq:`= <g1:/ G B / = g1:/ G F />` :g:`/ G F / <g1:/ G F />`), @fn(I.def.18)(:g:`G <g1:G>`, :g:`/ G B / <g1:/ G B />`) → :g:`( B H F ) <g1:( B H F )>`, @fn(I.post.2)(:g:`/ D E / <g1:/ E D />`) ∩ :g:`( B H F ) <g1:( B H F )>` → :g:`H <g1:H>`, @fn(I.post.1)(:g:`G <g1:G>`, :g:`H <g1:H>`) → :g:`/ G H / <g1:/ G H />`"),
            ("assert", ["II.5", "I.def.15"], ":g:`/ G B / <g1:/ G B />` :eq:`= <g1:/ G B / = g1:/ G F />` :g:`/ G F / <g1:/ G F />` → @fn(II.def.1)(:g:`/ B E / <g1:/ B E />`, :g:`/ E F / <g1:/ E F />`) + @fn(I.46)(:g:`/ E G / <g1:/ E G />`) = @fn(I.46)(:g:`/ G F / <g1:/ G F />`), :g:`/ G F / <g1:/ G F />` :eq:`= <g1:/ G F / = g1:/ G H />` :g:`/ G H / <g1:/ G H />` → @fn(II.def.1)(:g:`/ B E / <g1:/ B E />`, :g:`/ E F / <g1:/ E F />`) + @fn(I.46)(:g:`/ E G / <g1:/ E G />`) = @fn(I.46)(:g:`/ G H / <g1:/ G H />`)"),
            ("assert", ["I.47", "I.cn.1", "I.cn.3"], "@fn(I.46)(:g:`/ E H / <g1:/ E H />`) + @fn(I.46)(:g:`/ E G / <g1:/ E G />`) = @fn(I.46)(:g:`/ G H / <g1:/ G H />`) → @fn(II.def.1)(:g:`/ B E / <g1:/ B E />`, :g:`/ E F / <g1:/ E F />`) + @fn(I.46)(:g:`/ E G / <g1:/ E G />`) = @fn(I.46)(:g:`/ E H / <g1:/ E H />`) + @fn(I.46)(:g:`/ E G / <g1:/ E G />`) → @fn(II.def.1)(:g:`/ B E / <g1:/ B E />`, :g:`/ E F / <g1:/ E F />`) = @fn(I.46)(:g:`/ E H / <g1:/ E H />`)"),
            ("conclude", ["II.def.1", "I.cn.1"], ":g:`/ E F / <g1:/ E F />` :eq:`= <g1:/ E F / = g1:/ E D />` :g:`/ E D / <g1:/ E D />` → :g:`< B D E C > <g1:< B D E C >>` = @fn(II.def.1)(:g:`/ B E / <g1:/ B E />`, :g:`/ E F / <g1:/ E F />`) = @fn(I.46)(:g:`/ E H / <g1:/ E H />`), :g:`< B D E C > <g1:< B D E C >>` :eq:`= <g1:< B D E C > = g1:A>` :g:`A <g1:A>` → @fn(I.46)(:g:`/ E H / <g1:/ E H />`) :eq:`= <g1:/ E H / = g1:A>` :g:`A <g1:A>`"),
        ],
    },
    "III.1": {
        "subtype": "problem",
        "args": [":g:`( A B C ) <g1:( A B C )>`"],
        "returns": [":g:`F <g1:F>`"],
        "given": ":g:`( A B C ) <g1:( A B C )>`",
        "contract": ":g:`F <g1:F>` is the :term:`center <G.11>` of :g:`( A B C ) <g1:( A B C )>`",
        "steps": [
            ("given", ["I.def.15"], ":g:`( A B C ) <g1:( A B C )>`"),
            ("construct", ["I.10", "I.11"], ":g:`/ A B / <g1:/ A B />` in :g:`( A B C ) <g1:( A B C )>`, @fn(I.10)(:g:`/ A B / <g1:/ A B />`) → :g:`D <g1:D>` (:g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`), @fn(I.11)(:g:`/ A B / <g1:/ A B />`, :g:`D <g1:D>`) → :g:`/ C E / <g1:/ C E />` ⊥ :g:`/ A B / <g1:/ A B />`, @fn(I.10)(:g:`/ C E / <g1:/ C E />`) → :g:`F <g1:F>` (:g:`/ C F / <g1:/ C F />` :eq:`= <g1:/ C F / = g1:/ F E />` :g:`/ F E / <g1:/ F E />`)"),
            ("construct", ["I.post.1"], "Suppose :g:`G <g1:G>` ≠ :g:`F <g1:F>` is the center; @fn(I.post.1)(:g:`G <g1:G>`, :g:`A <g1:A>`, :g:`D <g1:D>`, :g:`B <g1:B>`) → :g:`/ G A / <g1:/ G A />`, :g:`/ G D / <g1:/ G D />`, :g:`/ G B / <g1:/ G B />`"),
            ("assert", ["I.def.15", "I.8", "I.def.10"], ":g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`, :g:`/ D G / <g1:/ D G />` common, :g:`/ G A / <g1:/ G A />` :eq:`= <g1:/ G A / = g1:/ G B />` :g:`/ G B / <g1:/ G B />` → :g:`< A D G ) <g1:< A D G )>` :eq:`= <g1:< A D G ) = g1:< G D B )>` :g:`< G D B ) <g1:< G D B )>` is right"),
            ("assert", ["I.def.10", "I.cn.5"], ":g:`< F D B ) <g1:< F D B )>` is right → :g:`< F D B ) <g1:< F D B )>` :eq:`= <g1:< F D B ) = g1:< G D B )>` :g:`< G D B ) <g1:< G D B )>`, the greater to the less ⇒⇐"),
            ("conclude", ["I.def.15", "I.def.16"], ":g:`G <g1:G>` is not the center → :g:`F <g1:F>` is the center of :g:`( A B C ) <g1:( A B C )>`"),
        ],
    },
    "III.2": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`A <g1:A>`", ":g:`B <g1:B>`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>`, :g:`A <g1:A>`, :g:`B <g1:B>` ∈ :g:`( A B C ) <g1:( A B C )>`",
        "contract": ":g:`/ A B / <g1:/ A E B />` falls within :g:`( A B C ) <g1:( A B C )>`",
        "steps": [
            ("given", ["I.def.15"], ":g:`( A B C ) <g1:( A B C )>`, :g:`A <g1:A>`, :g:`B <g1:B>` ∈ :g:`( A B C ) <g1:( A B C )>`"),
            ("construct", ["III.1", "I.post.1"], "Suppose :g:`/ A E B / <g1:/ A E B />` falls outside :g:`( A B C ) <g1:( A B C )>`; @fn(III.1)(:g:`( A B C ) <g1:( A B C )>`) → :g:`D <g1:D>`, @fn(I.post.1)(:g:`D <g1:D>`, :g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ D A / <g1:/ D A />`, :g:`/ D B / <g1:/ D B />`, draw :g:`/ D F E / <g1:/ D F E />`"),
            ("assert", ["I.def.15", "I.5", "I.16"], ":g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ D B />` :g:`/ D B / <g1:/ D B />` → :g:`< D A E ) <g1:< D A E )>` :eq:`= <g1:< D A E ) = g1:< D B E )>` :g:`< D B E ) <g1:< D B E )>`, and exterior :g:`< D E B ) <g1:< D E B )>` > :g:`< D A E ) <g1:< D A E )>` → :g:`< D E B ) <g1:< D E B )>` > :g:`< D B E ) <g1:< D B E )>`"),
            ("assert", ["I.19"], ":g:`< D E B ) <g1:< D E B )>` > :g:`< D B E ) <g1:< D B E )>` in :g:`< D B E > <g1:< D B E >>` → :g:`/ D B / <g1:/ D B />` > :g:`/ D E / <g1:/ D E />`"),
            ("assert", ["I.def.15", "I.cn.5"], ":g:`/ D B / <g1:/ D B />` :eq:`= <g1:/ D B / = g1:/ D F />` :g:`/ D F / <g1:/ D F />` → :g:`/ D F / <g1:/ D F />` > :g:`/ D E / <g1:/ D E />`, the less than the greater ⇒⇐"),
            ("conclude", [], ":g:`/ A B / <g1:/ A E B />` does not fall outside or on :g:`( A B C ) <g1:( A B C )>` → :g:`/ A B / <g1:/ A E B />` falls within :g:`( A B C ) <g1:( A B C )>`"),
        ],
    },
    "III.3": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`/ C D / <g1:/ C D />`", ":g:`/ A B / <g1:/ A B />`", ":g:`F <g1:F>`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>`, diameter :g:`/ C D / <g1:/ C D />`, chord :g:`/ A B / <g1:/ A B />` (:g:`F <g1:F>` = :g:`/ C D / <g1:/ C D />` ∩ :g:`/ A B / <g1:/ A B />`)",
        "contract": ":g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ F B />` :g:`/ F B / <g1:/ F B />` ⇔ :g:`/ C D / <g1:/ C D />` ⊥ :g:`/ A B / <g1:/ A B />`",
        "steps": [
            ("given", ["I.def.15"], ":g:`( A B C ) <g1:( A B C )>`, diameter :g:`/ C D / <g1:/ C D />` through center, chord :g:`/ A B / <g1:/ A B />` not through center, :g:`F <g1:F>` = :g:`/ C D / <g1:/ C D />` ∩ :g:`/ A B / <g1:/ A B />`"),
            ("construct", ["I.def.16", "I.post.1"], "Take center :g:`E <g1:E>` of :g:`( A B C ) <g1:( A B C )>`; @fn(I.post.1)(:g:`E <g1:E>`, :g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ E A / <g1:/ E A />`, :g:`/ E B / <g1:/ E B />`"),
            ("assert", ["I.def.15", "I.8", "I.def.10"], "If :g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`, with :g:`/ F E / <g1:/ F E />` common and :g:`/ E A / <g1:/ E A />` :eq:`= <g1:/ E A / = g1:/ E B />` :g:`/ E B / <g1:/ E B />` → :g:`< A F E ) <g1:< A F E )>` :eq:`= <g1:< A F E ) = g1:< B F E )>` :g:`< B F E ) <g1:< B F E )>` is right (:g:`/ C D / <g1:/ C D />` ⊥ :g:`/ A B / <g1:/ A B />`)"),
            ("assert", ["I.def.15", "I.5"], "Conversely, if :g:`< A F E ) <g1:< A F E )>` :eq:`= <g1:< A F E ) = g1:< B F E )>` :g:`< B F E ) <g1:< B F E )>` are right, since :g:`/ E A / <g1:/ E A />` :eq:`= <g1:/ E A / = g1:/ E B />` :g:`/ E B / <g1:/ E B />` → :g:`< E A F ) <g1:< E A F )>` :eq:`= <g1:< E A F ) = g1:< E B F )>` :g:`< E B F ) <g1:< E B F )>`"),
            ("assert", ["I.26"], "In :g:`< E A F > <g1:< E A F >>`, :g:`< E B F > <g1:< E B F >>`, two angles equal two angles and :g:`/ E F / <g1:/ E F />` common → :g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`"),
            ("conclude", [], ":g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ F B />` :g:`/ F B / <g1:/ F B />` ⇔ :g:`/ C D / <g1:/ C D />` ⊥ :g:`/ A B / <g1:/ A B />`"),
        ],
    },
    "III.4": {
        "subtype": "theorem",
        "args": [":g:`( A B C D ) <g1:( A B C D )>`", ":g:`/ A C / <g1:/ A C />`", ":g:`/ B D / <g1:/ B D />`", ":g:`E <g1:E>`"],
        "returns": [],
        "given": ":g:`( A B C D ) <g1:( A B C D )>`, non-central chords :g:`/ A C / <g1:/ A C />`, :g:`/ B D / <g1:/ B D />` (:g:`E <g1:E>` = :g:`/ A C / <g1:/ A C />` ∩ :g:`/ B D / <g1:/ B D />`)",
        "contract": "¬(:g:`/ A E / <g1:/ A E />` = :g:`/ E C / <g1:/ E C />` ∧ :g:`/ B E / <g1:/ B E />` = :g:`/ E D / <g1:/ E D />`)",
        "steps": [
            ("given", ["I.def.15"], ":g:`( A B C D ) <g1:( A B C D )>`, chords :g:`/ A C / <g1:/ A C />`, :g:`/ B D / <g1:/ B D />` not through center, :g:`E <g1:E>` = :g:`/ A C / <g1:/ A C />` ∩ :g:`/ B D / <g1:/ B D />`"),
            ("construct", ["III.1", "I.post.1"], "Suppose :g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E C />` :g:`/ E C / <g1:/ E C />` and :g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ E D />` :g:`/ E D / <g1:/ E D />`; @fn(III.1)(:g:`( A B C D ) <g1:( A B C D )>`) → :g:`F <g1:F>`, @fn(I.post.1)(:g:`F <g1:F>`, :g:`E <g1:E>`) → :g:`/ F E / <g1:/ F E />`"),
            ("assert", ["III.3"], ":g:`/ F E / <g1:/ F E />` through center bisects :g:`/ A C / <g1:/ A C />` (:g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E C />` :g:`/ E C / <g1:/ E C />`) → :g:`< F E A ) <g1:< F E A )>` is right"),
            ("assert", ["III.3"], ":g:`/ F E / <g1:/ F E />` through center bisects :g:`/ B D / <g1:/ B D />` (:g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ E D />` :g:`/ E D / <g1:/ E D />`) → :g:`< F E B ) <g1:< F E B )>` is right"),
            ("assert", ["I.post.4", "I.cn.5"], ":g:`< F E A ) <g1:< F E A )>` :eq:`= <g1:< F E A ) = g1:< F E B )>` :g:`< F E B ) <g1:< F E B )>`, the less to the greater ⇒⇐"),
            ("conclude", [], ":g:`/ A C / <g1:/ A C />` and :g:`/ B D / <g1:/ B D />` do not bisect one another"),
        ],
    },
    "III.5": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`( C D G ) <g1:( C D G )>`", ":g:`B <g1:B>`", ":g:`C <g1:C>`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>` ∩ :g:`( C D G ) <g1:( C D G )>` = {:g:`B <g1:B>`, :g:`C <g1:C>`}",
        "contract": "center(:g:`( A B C ) <g1:( A B C )>`) ≠ center(:g:`( C D G ) <g1:( C D G )>`)",
        "steps": [
            ("given", ["I.def.15"], ":g:`( A B C ) <g1:( A B C )>` and :g:`( C D G ) <g1:( C D G )>` cut one another at :g:`B <g1:B>`, :g:`C <g1:C>`"),
            ("construct", ["I.def.16", "I.post.1"], "Suppose :g:`E <g1:E>` is their common center; @fn(I.post.1)(:g:`E <g1:E>`, :g:`C <g1:C>`) → :g:`/ E C / <g1:/ E C />`, draw :g:`/ E F G / <g1:/ E F G />` through at random"),
            ("assert", ["I.def.15"], ":g:`E <g1:E>` is center of :g:`( A B C ) <g1:( A B C )>` → :g:`/ E C / <g1:/ E C />` :eq:`= <g1:/ E C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`"),
            ("assert", ["I.def.15"], ":g:`E <g1:E>` is center of :g:`( C D G ) <g1:( C D G )>` → :g:`/ E C / <g1:/ E C />` :eq:`= <g1:/ E C / = g1:/ E G />` :g:`/ E G / <g1:/ E G />`"),
            ("assert", ["I.cn.1", "I.cn.5"], ":g:`/ E F / <g1:/ E F />` :eq:`= <g1:/ E F / = g1:/ E G />` :g:`/ E G / <g1:/ E G />`, the less to the greater ⇒⇐"),
            ("conclude", ["I.def.16"], ":g:`E <g1:E>` is not the common center of :g:`( A B C ) <g1:( A B C )>` and :g:`( C D G ) <g1:( C D G )>`"),
        ],
    },
    "III.6": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`( C D E ) <g1:( C D E )>`", ":g:`C <g1:C>`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>`, :g:`( C D E ) <g1:( C D E )>` touching at :g:`C <g1:C>`",
        "contract": "center(:g:`( A B C ) <g1:( A B C )>`) ≠ center(:g:`( C D E ) <g1:( C D E )>`)",
        "steps": [
            ("given", ["III.def.3"], ":g:`( A B C ) <g1:( A B C )>`, :g:`( C D E ) <g1:( C D E )>` touching at :g:`C <g1:C>`"),
            ("construct", ["I.post.1"], "assume common center :g:`F <g1:F>`; @fn(I.post.1)(:g:`F <g1:F>`, :g:`C <g1:C>`) → :g:`/ F C / <g1:/ F C />`, draw :g:`/ F E B / <g1:/ F E B />`"),
            ("assert", ["I.def.15", "I.def.16"], ":g:`F <g1:F>` = center(:g:`( A B C ) <g1:( A B C )>`) → :g:`/ F C / <g1:/ F C />` :eq:`= <g1:/ F C / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`"),
            ("assert", ["I.def.15", "I.cn.1", "I.cn.5"], ":g:`F <g1:F>` = center(:g:`( C D E ) <g1:( C D E )>`) → :g:`/ F C / <g1:/ F C />` :eq:`= <g1:/ F C / = g1:/ F E />` :g:`/ F E / <g1:/ F E />` → :g:`/ F E / <g1:/ F E />` :eq:`= <g1:/ F E / = g1:/ F B />` :g:`/ F B / <g1:/ F B />` (< > ⇒⇐)"),
            ("conclude", [], "center(:g:`( A B C ) <g1:( A B C )>`) ≠ center(:g:`( C D E ) <g1:( C D E )>`)"),
        ],
    },
    "III.7": {
        "subtype": "theorem",
        "args": [":g:`( A B C D ) <g1:( A B C D )>`", ":g:`/ A D / <g1:/ A D />`", ":g:`E <g1:E>`", ":g:`F <g1:F>`"],
        "returns": [],
        "given": ":g:`( A B C D ) <g1:( A B C D )>` with center :g:`E <g1:E>`, diameter :g:`/ A D / <g1:/ A D />`, and point :g:`F <g1:F>` ∈ :g:`/ E D / <g1:/ E D />` (:g:`F <g1:F>` ≠ :g:`E <g1:E>`)",
        "contract": ":g:`/ F A / <g1:/ F A />` > :g:`/ F B / <g1:/ F B />` > :g:`/ F C / <g1:/ F C />` > :g:`/ F G / <g1:/ F G />` > :g:`/ F D / <g1:/ F D />`, and :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ F G / = g1:/ F H />` :g:`/ F H / <g1:/ F H />` (unique pair)",
        "steps": [
            ("given", ["I.def.15", "I.def.17"], ":g:`( A B C D ) <g1:( A B C D )>`, diameter :g:`/ A D / <g1:/ A D />`, center :g:`E <g1:E>`, eccentric point :g:`F <g1:F>`, segments :g:`/ F B / <g1:/ F B />`, :g:`/ F C / <g1:/ F C />`, :g:`/ F G / <g1:/ F G />`"),
            ("construct", ["I.post.1", "I.23"], "@fn(I.post.1)(:g:`E <g1:E>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`G <g1:G>`) → :g:`/ E B / <g1:/ E B />`, :g:`/ E C / <g1:/ E C />`, :g:`/ E G / <g1:/ E G />`; @fn(I.23)(:g:`/ E F / <g1:/ E F />`, :g:`E <g1:E>`, :g:`< G E F ) <g1:< G E F )>`) → :g:`< F E H ) <g1:< F E H )>` :eq:`= <g1:< F E H ) = g1:< G E F )>` :g:`< G E F ) <g1:< G E F )>`, join :g:`/ F H / <g1:/ F H />`"),
            ("assert", ["I.20", "I.24"], ":g:`/ E B / <g1:/ E B />` + :g:`/ E F / <g1:/ E F />` > :g:`/ F B / <g1:/ F B />`, :g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E B />` :g:`/ E B / <g1:/ E B />` → :g:`/ F A / <g1:/ F A />` > :g:`/ F B / <g1:/ F B />`; :g:`< B E F ) <g1:< B E F )>` > :g:`< C E F ) <g1:< C E F )>` → :g:`/ F B / <g1:/ F B />` > :g:`/ F C / <g1:/ F C />` > :g:`/ F G / <g1:/ F G />`"),
            ("assert", ["I.20"], ":g:`/ F G / <g1:/ F G />` + :g:`/ E F / <g1:/ E F />` > :g:`/ E G / <g1:/ E G />` :eq:`= <g1:/ E G / = g1:/ E D />` :g:`/ E D / <g1:/ E D />` → :g:`/ F G / <g1:/ F G />` > :g:`/ F D / <g1:/ F D />`"),
            ("assert", ["I.4", "I.cn.1"], ":g:`< G E F > <g1:< G E F >>` ≃ :g:`< H E F > <g1:< H E F >>` → :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ F G / = g1:/ F H />` :g:`/ F H / <g1:/ F H />`; if :g:`/ F K / <g1:/ F K />` :eq:`= <g1:/ F K / = g1:/ F G />` :g:`/ F G / <g1:/ F G />` then :g:`/ F K / <g1:/ F K />` :eq:`= <g1:/ F K / = g1:/ F H />` :g:`/ F H / <g1:/ F H />` ⇒⇐"),
            ("conclude", [], ":g:`/ F A / <g1:/ F A />` > :g:`/ F B / <g1:/ F B />` > :g:`/ F C / <g1:/ F C />` > :g:`/ F G / <g1:/ F G />` > :g:`/ F D / <g1:/ F D />`, and only two equal segments :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ F G / = g1:/ F H />` :g:`/ F H / <g1:/ F H />` fall from :g:`F <g1:F>`"),
        ],
    },
    "III.8": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`D <g1:D>`", ":g:`/ D A / <g1:/ D A />`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>`, exterior point :g:`D <g1:D>`, secants :g:`/ D A / <g1:/ D A />` (through center), :g:`/ D E / <g1:/ D E />`, :g:`/ D F / <g1:/ D F />`, :g:`/ D C / <g1:/ D C />`",
        "contract": ":g:`/ D A / <g1:/ D A />` > :g:`/ D E / <g1:/ D E />` > :g:`/ D F / <g1:/ D F />` > :g:`/ D C / <g1:/ D C />`, :g:`/ D G / <g1:/ D G />` < :g:`/ D K / <g1:/ D K />` < :g:`/ D L / <g1:/ D L />` < :g:`/ D H / <g1:/ D H />`, and :g:`/ D K / <g1:/ D K />` :eq:`= <g1:/ D K / = g1:/ D B />` :g:`/ D B / <g1:/ D B />` (unique pair)",
        "steps": [
            ("given", ["I.def.15", "I.def.17"], ":g:`( A B C ) <g1:( A B C )>`, exterior point :g:`D <g1:D>`, secants :g:`/ D A / <g1:/ D A />` (cutting at :g:`G <g1:G>`), :g:`/ D E / <g1:/ D E />` (:g:`K <g1:K>`), :g:`/ D F / <g1:/ D F />` (:g:`L <g1:L>`), :g:`/ D C / <g1:/ D C />` (:g:`H <g1:H>`)"),
            ("construct", ["III.1", "I.post.1", "I.23"], "@fn(III.1)(:g:`( A B C ) <g1:( A B C )>`) → :g:`M <g1:M>`; join radii :g:`/ M E / <g1:/ M E />`, :g:`/ M F / <g1:/ M F />`, :g:`/ M C / <g1:/ M C />`, :g:`/ M K / <g1:/ M K />`, :g:`/ M L / <g1:/ M L />`, :g:`/ M H / <g1:/ M H />`; @fn(I.23)(:g:`/ M D / <g1:/ M D />`, :g:`M <g1:M>`, :g:`< K M D ) <g1:< K M D )>`) → :g:`< D M B ) <g1:< D M B )>` :eq:`= <g1:< D M B ) = g1:< K M D )>` :g:`< K M D ) <g1:< K M D )>`, join :g:`/ D B / <g1:/ D B />`"),
            ("assert", ["I.20", "I.24"], ":g:`/ D A / <g1:/ D A />` = :g:`/ M E / <g1:/ M E />` + :g:`/ M D / <g1:/ M D />` > :g:`/ D E / <g1:/ D E />`; :g:`< E M D ) <g1:< E M D )>` > :g:`< F M D ) <g1:< F M D )>` → :g:`/ D E / <g1:/ D E />` > :g:`/ D F / <g1:/ D F />` > :g:`/ D C / <g1:/ D C />`"),
            ("assert", ["I.20", "I.21"], ":g:`/ M K / <g1:/ M K />` + :g:`/ D K / <g1:/ D K />` > :g:`/ M D / <g1:/ M D />` and :g:`/ M G / <g1:/ M G />` :eq:`= <g1:/ M G / = g1:/ M K />` :g:`/ M K / <g1:/ M K />` → :g:`/ D G / <g1:/ D G />` < :g:`/ D K / <g1:/ D K />`; :g:`/ M K / <g1:/ M K />` + :g:`/ D K / <g1:/ D K />` < :g:`/ M L / <g1:/ M L />` + :g:`/ D L / <g1:/ D L />` → :g:`/ D K / <g1:/ D K />` < :g:`/ D L / <g1:/ D L />` < :g:`/ D H / <g1:/ D H />`"),
            ("assert", ["I.4", "I.cn.1"], ":g:`< M K D > <g1:< M K D >>` ≃ :g:`< M B D > <g1:< M B D >>` → :g:`/ D K / <g1:/ D K />` :eq:`= <g1:/ D K / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`; if :g:`/ D N / <g1:/ D N />` :eq:`= <g1:/ D N / = g1:/ D K />` :g:`/ D K / <g1:/ D K />` then :g:`/ D B / <g1:/ D B />` :eq:`= <g1:/ D B / = g1:/ D N />` :g:`/ D N / <g1:/ D N />` ⇒⇐"),
            ("conclude", [], ":g:`/ D A / <g1:/ D A />` > :g:`/ D E / <g1:/ D E />` > :g:`/ D F / <g1:/ D F />` > :g:`/ D C / <g1:/ D C />`, :g:`/ D G / <g1:/ D G />` < :g:`/ D K / <g1:/ D K />` < :g:`/ D L / <g1:/ D L />` < :g:`/ D H / <g1:/ D H />`, and only two equal segments :g:`/ D K / <g1:/ D K />` :eq:`= <g1:/ D K / = g1:/ D B />` :g:`/ D B / <g1:/ D B />` fall from :g:`D <g1:D>`"),
        ],
    },
    "III.9": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`D <g1:D>`", ":g:`/ D A / <g1:/ D A />`", ":g:`/ D B / <g1:/ D B />`", ":g:`/ D C / <g1:/ D C />`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>`, interior point :g:`D <g1:D>`, :g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ D B / = g1:/ D C />` :g:`/ D B / <g1:/ D B />` :eq:`= <g1:/ D A / = g1:/ D B / = g1:/ D C />` :g:`/ D C / <g1:/ D C />`",
        "contract": ":g:`D <g1:D>` = center(:g:`( A B C ) <g1:( A B C )>`)",
        "steps": [
            ("given", ["I.def.15"], ":g:`( A B C ) <g1:( A B C )>`, interior point :g:`D <g1:D>`, :g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ D B / = g1:/ D C />` :g:`/ D B / <g1:/ D B />` :eq:`= <g1:/ D A / = g1:/ D B / = g1:/ D C />` :g:`/ D C / <g1:/ D C />`"),
            ("construct", ["I.post.1", "I.10", "I.post.2"], "join :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, bisect at :g:`E <g1:E>`, :g:`F <g1:F>` (:g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E B />` :g:`/ E B / <g1:/ E B />`, :g:`/ B F / <g1:/ B F />` :eq:`= <g1:/ B F / = g1:/ F C />` :g:`/ F C / <g1:/ F C />`), draw :g:`/ G K / <g1:/ G K />` through :g:`E <g1:E>`, :g:`D <g1:D>` and :g:`/ H L / <g1:/ H L />` through :g:`F <g1:F>`, :g:`D <g1:D>`"),
            ("assert", ["I.8", "I.def.10"], ":g:`< A E D > <g1:< A E D >>` ≃ :g:`< B E D > <g1:< B E D >>` → :g:`< A E D ) <g1:< A E D )>` :eq:`= <g1:< A E D ) = g1:< B E D )>` :g:`< B E D ) <g1:< B E D )>` (right) → :g:`/ G K / <g1:/ G K />` ⊥ :g:`/ A B / <g1:/ A B />`"),
            ("assert", ["III.1"], ":g:`/ G K / <g1:/ G K />` bisects :g:`/ A B / <g1:/ A B />` ⊥ → center(:g:`( A B C ) <g1:( A B C )>`) ∈ :g:`/ G K / <g1:/ G K />`; similarly center(:g:`( A B C ) <g1:( A B C )>`) ∈ :g:`/ H L / <g1:/ H L />`"),
            ("conclude", ["I.def.16"], ":g:`/ G K / <g1:/ G K />` ∩ :g:`/ H L / <g1:/ H L />` = :g:`D <g1:D>` → :g:`D <g1:D>` = center(:g:`( A B C ) <g1:( A B C )>`)"),
        ],
    },
    "III.10": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`( D E F ) <g1:( D E F )>`"],
        "returns": [],
        "given": "circles :g:`( A B C ) <g1:( A B C )>`, :g:`( D E F ) <g1:( D E F )>`",
        "contract": "| :g:`( A B C ) <g1:( A B C )>` ∩ :g:`( D E F ) <g1:( D E F )>` | ≤ 2",
        "steps": [
            ("given", ["I.def.15"], "assume :g:`( A B C ) <g1:( A B C )>` cuts :g:`( D E F ) <g1:( D E F )>` at :g:`B <g1:B>`, :g:`G <g1:G>`, :g:`F <g1:F>`, :g:`H <g1:H>`"),
            ("construct", ["I.post.1", "I.10", "I.11", "I.post.2"], "join :g:`/ B H / <g1:/ B H />`, :g:`/ B G / <g1:/ B G />`, bisect at :g:`K <g1:K>`, :g:`L <g1:L>` (:g:`/ B K / <g1:/ B K />` :eq:`= <g1:/ B K / = g1:/ K H />` :g:`/ K H / <g1:/ K H />`, :g:`/ B L / <g1:/ B L />` :eq:`= <g1:/ B L / = g1:/ L G />` :g:`/ L G / <g1:/ L G />`); draw :g:`/ A C / <g1:/ A C />` ⊥ :g:`/ B H / <g1:/ B H />` at :g:`K <g1:K>` and :g:`/ M E / <g1:/ M E />` ⊥ :g:`/ B G / <g1:/ B G />` at :g:`L <g1:L>`"),
            ("assert", ["III.1"], ":g:`/ A C / <g1:/ A C />` bisects :g:`/ B H / <g1:/ B H />` ⊥ → center(:g:`( A B C ) <g1:( A B C )>`) ∈ :g:`/ A C / <g1:/ A C />`; :g:`/ N O / <g1:/ N O />` bisects :g:`/ B G / <g1:/ B G />` ⊥ → center(:g:`( A B C ) <g1:( A B C )>`) ∈ :g:`/ N O / <g1:/ N O />`"),
            ("assert", ["III.1", "I.def.16"], ":g:`/ A C / <g1:/ A C />` ∩ :g:`/ N O / <g1:/ N O />` = :g:`P <g1:P>` → :g:`P <g1:P>` = center(:g:`( A B C ) <g1:( A B C )>`) and :g:`P <g1:P>` = center(:g:`( D E F ) <g1:( D E F )>`)"),
            ("conclude", ["III.5"], "center(:g:`( A B C ) <g1:( A B C )>`) = center(:g:`( D E F ) <g1:( D E F )>`) = :g:`P <g1:P>` ⇒⇐ (@fn(III.5)) → | :g:`( A B C ) <g1:( A B C )>` ∩ :g:`( D E F ) <g1:( D E F )>` | ≤ 2"),
        ],
    },
    "III.11": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`( A D E ) <g1:( A D E )>`", ":g:`A <g1:A>`", ":g:`F <g1:F>`", ":g:`G <g1:G>`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>`, :g:`( A D E ) <g1:( A D E )>` touch internally at :g:`A <g1:A>`, center(:g:`( A B C ) <g1:( A B C )>`) = :g:`F <g1:F>`, center(:g:`( A D E ) <g1:( A D E )>`) = :g:`G <g1:G>`",
        "contract": ":g:`A <g1:A>` ∈ :g:`[ F G ] <g1:[ F H ]>`",
        "steps": [
            ("given", ["III.def.3", "I.def.16"], ":g:`( A B C ) <g1:( A B C )>`, :g:`( A D E ) <g1:( A D E )>` touch internally at :g:`A <g1:A>`, center(:g:`( A B C ) <g1:( A B C )>`) = :g:`F <g1:F>`, center(:g:`( A D E ) <g1:( A D E )>`) = :g:`G <g1:G>`"),
            ("construct", ["I.post.1", "I.post.2"], "assume :g:`A <g1:A>` ∉ :g:`[ F G ] <g1:[ F H ]>` → :g:`/ F G H / <g1:/ F H />`, :g:`/ A F / <g1:/ A F />`, :g:`/ A G / <g1:/ A G />`"),
            ("assert", ["I.20", "I.def.15"], "in :g:`< A F G > <g1:< A F G >>`, :g:`/ A G / <g1:/ A G />` + :g:`/ G F / <g1:/ G F />` > :g:`/ F A / <g1:/ F A />` :eq:`= <g1:/ A F / = g1:/ F H />` :g:`/ F H / <g1:/ F H />` → :g:`/ A G / <g1:/ A G />` > :g:`/ G H / <g1:/ G H />`"),
            ("assert", ["I.def.15", "I.cn.5"], ":g:`/ A G / <g1:/ A G />` :eq:`= <g1:/ A G / = g1:/ G D />` :g:`/ G D / <g1:/ G D />` → :g:`/ G D / <g1:/ G D />` > :g:`/ G H / <g1:/ G H />` (the less than the greater) ⇒⇐"),
            ("conclude", [], ":g:`A <g1:A>` ∈ :g:`[ F G ] <g1:[ F H ]>`"),
        ],
    },
    "III.12": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( F A )>`", ":g:`( A D E ) <g1:( G A )>`", ":g:`A <g1:A>`", ":g:`F <g1:F>`", ":g:`G <g1:G>`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( F A )>`, :g:`( A D E ) <g1:( G A )>` touch externally at :g:`A <g1:A>`, center(:g:`( A B C ) <g1:( F A )>`) = :g:`F <g1:F>`, center(:g:`( A D E ) <g1:( G A )>`) = :g:`G <g1:G>`",
        "contract": ":g:`A <g1:A>` ∈ :g:`/ F G / <g1:/ F G />`",
        "steps": [
            ("given", ["III.def.3", "I.def.16"], ":g:`( A B C ) <g1:( F A )>`, :g:`( A D E ) <g1:( G A )>` touch externally at :g:`A <g1:A>`, center(:g:`( A B C ) <g1:( F A )>`) = :g:`F <g1:F>`, center(:g:`( A D E ) <g1:( G A )>`) = :g:`G <g1:G>`"),
            ("construct", ["I.post.1"], "assume :g:`A <g1:A>` ∉ :g:`/ F G / <g1:/ F G />` → :g:`/ F C D G / <g1:/ F G />`, :g:`/ F A / <g1:/ F A />`, :g:`/ A G / <g1:/ G A />`"),
            ("assert", ["I.def.15", "I.cn.2"], ":g:`/ F A / <g1:/ F A />` :eq:`= <g1:/ F A / = g1:/ F C />` :g:`/ F C / <g1:/ F C />`, :g:`/ G A / <g1:/ G A />` :eq:`= <g1:/ G A / = g1:/ G D />` :g:`/ G D / <g1:/ G D />` → :g:`/ F A / <g1:/ F A />` + :g:`/ A G / <g1:/ G A />` = :g:`/ F C / <g1:/ F C />` + :g:`/ G D / <g1:/ G D />`"),
            ("assert", ["I.cn.5", "I.20"], ":g:`/ F G / <g1:/ F G />` > :g:`/ F C / <g1:/ F C />` + :g:`/ G D / <g1:/ G D />` = :g:`/ F A / <g1:/ F A />` + :g:`/ A G / <g1:/ G A />`, but in :g:`< F A G > <g1:< F A G >>`, :g:`/ F G / <g1:/ F G />` < :g:`/ F A / <g1:/ F A />` + :g:`/ A G / <g1:/ G A />` ⇒⇐"),
            ("conclude", [], ":g:`A <g1:A>` ∈ :g:`/ F G / <g1:/ F G />`"),
        ],
    },
    "III.13": {
        "subtype": "theorem",
        "args": [":g:`( A B D C ) <g1:( G B )>`", ":g:`( E B F D ) <g1:( H B )>`", ":g:`( A C K ) <g1:( A C K )>`"],
        "returns": [],
        "given": "circles :g:`( A B D C ) <g1:( G B )>`, :g:`( E B F D ) <g1:( H B )>` (internal) or :g:`( A B D C ) <g1:( G B )>`, :g:`( A C K ) <g1:( A C K )>` (external) touching",
        "contract": "|( C₁ ) ∩ ( C₂ )| ≤ 1",
        "steps": [
            ("given", ["III.def.3"], "assume :g:`( A B D C ) <g1:( G B )>` and :g:`( E B F D ) <g1:( H B )>` touch internally at two points :g:`B <g1:B>`, :g:`D <g1:D>`"),
            ("construct", ["I.def.16", "III.11"], "center(:g:`( A B D C ) <g1:( G B )>`) = :g:`G <g1:G>`, center(:g:`( E B F D ) <g1:( H B )>`) = :g:`H <g1:H>` → @fn(III.11)(:g:`G <g1:G>`, :g:`H <g1:H>`) → :g:`/ B G H D / <g1:/ B D />`"),
            ("assert", ["I.def.15", "I.cn.5"], ":g:`/ B G / <g1:/ B G />` :eq:`= <g1:/ B G / = g1:/ G D />` :g:`/ G D / <g1:/ G D />` > :g:`/ H D / <g1:/ H D />` → :g:`/ B H / <g1:/ B H />` ≫ :g:`/ H D / <g1:/ H D />`, but :g:`/ B H / <g1:/ B H />` :eq:`= <g1:/ B H / = g1:/ H D />` :g:`/ H D / <g1:/ H D />` ⇒⇐"),
            ("construct", ["I.post.1"], "assume :g:`( A C K ) <g1:( A C K )>` and :g:`( A B D C ) <g1:( G B )>` touch externally at two points :g:`A <g1:A>`, :g:`C <g1:C>` → :g:`/ A C / <g1:/ A C />`"),
            ("assert", ["III.2", "III.def.3"], "@fn(III.2)(:g:`A <g1:A>`, :g:`C <g1:C>`) → :g:`/ A C / <g1:/ A C />` inside both :g:`( A B D C ) <g1:( G B )>` and :g:`( A C K ) <g1:( A C K )>`, contradicting external contact ⇒⇐"),
            ("conclude", [], "a circle does not touch a circle at more points than one, whether internally or externally"),
        ],
    },
    "III.14": {
        "subtype": "theorem",
        "args": [":g:`( A B D C ) <g1:( E A )>`", ":g:`/ A B / <g1:/ A B />`", ":g:`/ C D / <g1:/ C D />`"],
        "returns": [],
        "given": ":g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` chords in :g:`( A B D C ) <g1:( E A )>`",
        "contract": ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ C D />` :g:`/ C D / <g1:/ C D />` ⇔ :g:`/ E F / <g1:/ E F />` :eq:`= <g1:/ E F / = g1:/ E G />` :g:`/ E G / <g1:/ E G />`",
        "steps": [
            ("given", ["III.def.4"], ":g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` chords in :g:`( A B D C ) <g1:( E A )>`, first with :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ C D />` :g:`/ C D / <g1:/ C D />`"),
            ("construct", ["III.1", "I.12", "I.post.1"], "@fn(III.1)(:g:`( A B D C ) <g1:( E A )>`) → :g:`E <g1:E>`, :g:`/ E F / <g1:/ E F />` ⊥ :g:`/ A B / <g1:/ A B />`, :g:`/ E G / <g1:/ E G />` ⊥ :g:`/ C D / <g1:/ C D />`, join :g:`/ A E / <g1:/ A E />`, :g:`/ E C / <g1:/ E C />`"),
            ("assert", ["III.3"], "@fn(III.3)(:g:`/ E F / <g1:/ E F />`, :g:`/ A B / <g1:/ A B />`) → :g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`, :g:`/ C G / <g1:/ C G />` :eq:`= <g1:/ C G / = g1:/ G D />` :g:`/ G D / <g1:/ G D />` → (:g:`/ A B / <g1:/ A B />` = :g:`/ C D / <g1:/ C D />` ⇔ :g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ C G />` :g:`/ C G / <g1:/ C G />`)"),
            ("assert", ["I.def.15", "I.47"], ":g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E C />` :g:`/ E C / <g1:/ E C />` → sq(:g:`/ A F / <g1:/ A F />`) + sq(:g:`/ E F / <g1:/ E F />`) = sq(:g:`/ A E / <g1:/ A E />`) = sq(:g:`/ E C / <g1:/ E C />`) = sq(:g:`/ C G / <g1:/ C G />`) + sq(:g:`/ E G / <g1:/ E G />`)"),
            ("assert", ["I.cn.3", "III.def.4"], ":g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ C G />` :g:`/ C G / <g1:/ C G />` ⇒ sq(:g:`/ E F / <g1:/ E F />`) = sq(:g:`/ E G / <g1:/ E G />`) ⇒ :g:`/ E F / <g1:/ E F />` :eq:`= <g1:/ E F / = g1:/ E G />` :g:`/ E G / <g1:/ E G />` (and conversely :g:`/ E F / <g1:/ E F />` = :g:`/ E G / <g1:/ E G />` ⇒ :g:`/ A F / <g1:/ A F />` = :g:`/ C G / <g1:/ C G />` ⇒ :g:`/ A B / <g1:/ A B />` = :g:`/ C D / <g1:/ C D />`)"),
            ("conclude", [], ":g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ C D />` :g:`/ C D / <g1:/ C D />` ⇔ :g:`/ E F / <g1:/ E F />` :eq:`= <g1:/ E F / = g1:/ E G />` :g:`/ E G / <g1:/ E G />`"),
        ],
    },
    "III.15": {
        "subtype": "theorem",
        "args": [":g:`( A B C D ) <g1:( E A )>`", ":g:`/ A D / <g1:/ A D />`", ":g:`/ B C / <g1:/ B C />`", ":g:`/ F G / <g1:/ F G />`", ":g:`E <g1:E>`"],
        "returns": [],
        "given": ":g:`( A B C D ) <g1:( E A )>` with center :g:`E <g1:E>`, diameter :g:`/ A D / <g1:/ A D />`, and chords :g:`/ B C / <g1:/ B C />` (nearer :g:`E <g1:E>`) and :g:`/ F G / <g1:/ F G />` (more remote)",
        "contract": ":g:`/ A D / <g1:/ A D />` > :g:`/ B C / <g1:/ B C />` > :g:`/ F G / <g1:/ F G />`",
        "steps": [
            ("given", ["I.def.17", "III.def.5"], ":g:`( A B C D ) <g1:( E A )>` with center :g:`E <g1:E>`, diameter :g:`/ A D / <g1:/ A D />`, and chords :g:`/ B C / <g1:/ B C />` nearer :g:`E <g1:E>` than :g:`/ F G / <g1:/ F G />`"),
            ("construct", ["I.12", "III.def.5"], ":g:`/ E H / <g1:/ E H />` ⊥ :g:`/ B C / <g1:/ B C />`, :g:`/ E K / <g1:/ E K />` ⊥ :g:`/ F G / <g1:/ F G />` → :g:`/ E K / <g1:/ E K />` > :g:`/ E H / <g1:/ E H />`"),
            ("construct", ["I.3", "I.11", "I.post.1"], "@fn(I.3)(:g:`/ E K / <g1:/ E K />`, :g:`/ E H / <g1:/ E H />`) → :g:`/ E L / <g1:/ E L />` :eq:`= <g1:/ E L / = g1:/ E H />` :g:`/ E H / <g1:/ E H />`, draw :g:`/ M N / <g1:/ M N />` ⊥ :g:`/ E K / <g1:/ E K />` at :g:`L <g1:L>`, join :g:`/ M E / <g1:/ M E />`, :g:`/ E N / <g1:/ E N />`, :g:`/ F E / <g1:/ F E />`, :g:`/ E G / <g1:/ E G />`"),
            ("assert", ["III.14", "I.def.15", "I.20"], "@fn(III.14)(:g:`/ E H / <g1:/ E H />` = :g:`/ E L / <g1:/ E L />`) → :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ M N />` :g:`/ M N / <g1:/ M N />`; :g:`/ A D / <g1:/ A D />` = :g:`/ A E / <g1:/ A E />` + :g:`/ E D / <g1:/ E D />` = :g:`/ M E / <g1:/ M E />` + :g:`/ E N / <g1:/ E N />` > :g:`/ M N / <g1:/ M N />` = :g:`/ B C / <g1:/ B C />`"),
            ("assert", ["I.24"], "in :g:`< M E N > <g1:< M E N >>` and :g:`< F E G > <g1:< F E G >>`, :g:`/ M E / <g1:/ M E />` = :g:`/ F E / <g1:/ F E />`, :g:`/ E N / <g1:/ E N />` = :g:`/ E G / <g1:/ E G />`, :g:`< M E N ) <g1:< M E N )>` > :g:`< F E G ) <g1:< F E G )>` → :g:`/ M N / <g1:/ M N />` > :g:`/ F G / <g1:/ F G />` → :g:`/ B C / <g1:/ B C />` > :g:`/ F G / <g1:/ F G />`"),
            ("conclude", [], ":g:`/ A D / <g1:/ A D />` > :g:`/ B C / <g1:/ B C />` > :g:`/ F G / <g1:/ F G />`"),
        ],
    },
    "III.16": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`D <g1:D>`", ":g:`/ A B / <g1:/ A B />`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>` about center :g:`D <g1:D>` with diameter :g:`/ A B / <g1:/ A B />`",
        "contract": ":g:`/ A E / <g1:/ A E />` ⊥ :g:`/ A B / <g1:/ A B />` falls outside :g:`( A B C ) <g1:( A B C )>`, no segment interposed between :g:`/ A E / <g1:/ A E />` and :g:`( C H A ) <g1:( C H A )>`, :g:`/ A E / <g1:/ A E />` touches :g:`( A B C ) <g1:( A B C )>`",
        "steps": [
            ("given", ["I.def.15", "I.def.17"], ":g:`( A B C ) <g1:( A B C )>` about center :g:`D <g1:D>` with diameter :g:`/ A B / <g1:/ A B />`"),
            ("construct", ["I.def.10", "I.post.1"], "assume perpendicular at :g:`A <g1:A>` falls within as :g:`/ C A / <g1:/ C A />`, join :g:`/ D C / <g1:/ D C />`"),
            ("assert", ["I.5", "I.17"], ":g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ D C />` :g:`/ D C / <g1:/ D C />` → :g:`< D A C ) <g1:< D A C )>` :eq:`= <g1:< D A C ) = g1:< A C D )>` :g:`< A C D ) <g1:< A C D )>` = right angle ⇒⇐, so perpendicular falls outside as :g:`/ A E / <g1:/ A E />`"),
            ("assert", ["I.19", "I.def.15"], "assume :g:`/ F A / <g1:/ F A />` interposed and :g:`/ D G / <g1:/ D G />` ⊥ :g:`/ F A / <g1:/ F A />` → :g:`/ D A / <g1:/ D A />` > :g:`/ D G / <g1:/ D G />`, and :g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ D H />` :g:`/ D H / <g1:/ D H />` → :g:`/ D H / <g1:/ D H />` > :g:`/ D G / <g1:/ D G />` ⇒⇐"),
            ("conclude", ["III.def.7", "III.def.2"], "no segment interposed between :g:`/ A E / <g1:/ A E />` and :g:`( C H A ) <g1:( C H A )>`; semicircle angle > any acute angle > horn-like angle; :g:`/ A E / <g1:/ A E />` touches :g:`( A B C ) <g1:( A B C )>`"),
        ],
    },
    "III.17": {
        "subtype": "problem",
        "args": [":g:`A <g1:A>`", ":g:`( B C D ) <g1:( B C D )>`"],
        "returns": [":g:`/ A B / <g1:/ A B />`"],
        "given": ":g:`A <g1:A>`, :g:`( B C D ) <g1:( B C D )>`",
        "contract": ":g:`/ A B / <g1:/ A B />` touches :g:`( B C D ) <g1:( B C D )>` at :g:`B <g1:B>`",
        "steps": [
            ("given", ["I.def.1", "I.def.15"], ":g:`A <g1:A>`, :g:`( B C D ) <g1:( B C D )>`"),
            ("construct", ["III.1", "I.post.1", "I.post.3"], "@fn(III.1)(:g:`( B C D ) <g1:( B C D )>`) → :g:`E <g1:E>`, @fn(I.post.1)(:g:`A <g1:A>`, :g:`E <g1:E>`) → :g:`/ A E / <g1:/ A E />` (:g:`D <g1:D>` = :g:`/ A E / <g1:/ A E />` ∩ :g:`( B C D ) <g1:( B C D )>`), @fn(I.post.3)(:g:`E <g1:E>`, :g:`A <g1:A>`) → :g:`( A F G ) <g1:( A F G )>`"),
            ("construct", ["I.11", "I.post.1"], ":g:`/ D F / <g1:/ D F />` ⊥ :g:`/ E A / <g1:/ E A />` (:g:`F <g1:F>` ∈ :g:`( A F G ) <g1:( A F G )>`), @fn(I.post.1)(:g:`E <g1:E>`, :g:`F <g1:F>`) → :g:`/ E F / <g1:/ E F />` (:g:`B <g1:B>` = :g:`/ E F / <g1:/ E F />` ∩ :g:`( B C D ) <g1:( B C D )>`), @fn(I.post.1)(:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ A B / <g1:/ A B />`"),
            ("assert", ["I.def.15", "I.4"], ":g:`/ E A / <g1:/ E A />` :eq:`= <g1:/ E A / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`, :g:`/ E D / <g1:/ E D />` :eq:`= <g1:/ E D / = g1:/ E B />` :g:`/ E B / <g1:/ E B />`, common :g:`< D E F ) <g1:< D E F )>` → :g:`< D E F > <g1:< D E F >>` ≃ :g:`< B E A > <g1:< B E A >>`, :g:`< E B A ) <g1:< E B A )>` :eq:`= <g1:< E D F ) = g1:< E B A )>` :g:`< E D F ) <g1:< E D F )>` = right angle"),
            ("conclude", ["III.16", "III.def.2"], ":g:`/ E B / <g1:/ E B />` is a radius and :g:`< E B A ) <g1:< E B A )>` is right → :g:`/ A B / <g1:/ A B />` touches :g:`( B C D ) <g1:( B C D )>` at :g:`B <g1:B>`"),
        ],
    },
    "III.18": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`/ D E / <g1:/ D E />`", ":g:`C <g1:C>`", ":g:`F <g1:F>`"],
        "returns": [],
        "given": ":g:`/ D E / <g1:/ D E />` touches :g:`( A B C ) <g1:( A B C )>` at :g:`C <g1:C>`, center(:g:`( A B C ) <g1:( A B C )>`) = :g:`F <g1:F>`, radius :g:`/ F C / <g1:/ F C />`",
        "contract": ":g:`/ F C / <g1:/ F C />` ⊥ :g:`/ D E / <g1:/ D E />`",
        "steps": [
            ("given", ["III.def.2", "I.def.16"], ":g:`/ D E / <g1:/ D E />` touches :g:`( A B C ) <g1:( A B C )>` at :g:`C <g1:C>`, center(:g:`( A B C ) <g1:( A B C )>`) = :g:`F <g1:F>`, join :g:`/ F C / <g1:/ F C />`"),
            ("construct", ["I.def.10"], "assume :g:`/ F C / <g1:/ F C />` is not ⊥ :g:`/ D E / <g1:/ D E />`, and draw :g:`/ F G / <g1:/ F G />` ⊥ :g:`/ D E / <g1:/ D E />` cutting :g:`( A B C ) <g1:( A B C )>` at :g:`B <g1:B>`"),
            ("assert", ["I.17", "I.19"], ":g:`< F G C ) <g1:< F G C )>` is right → :g:`< F C G ) <g1:< F C G )>` is acute → :g:`/ F C / <g1:/ F C />` > :g:`/ F G / <g1:/ F G />`"),
            ("assert", ["I.def.15", "I.cn.5"], ":g:`/ F C / <g1:/ F C />` :eq:`= <g1:/ F C / = g1:/ F B />` :g:`/ F B / <g1:/ F B />` → :g:`/ F B / <g1:/ F B />` > :g:`/ F G / <g1:/ F G />` (the less than the greater) ⇒⇐"),
            ("conclude", ["I.def.10"], ":g:`/ F C / <g1:/ F C />` ⊥ :g:`/ D E / <g1:/ D E />`"),
        ],
    },
    "III.19": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`/ D E / <g1:/ D E />`", ":g:`C <g1:C>`", ":g:`/ C A / <g1:/ C A />`"],
        "returns": [],
        "given": ":g:`/ D E / <g1:/ D E />` touches :g:`( A B C ) <g1:( A B C )>` at :g:`C <g1:C>`, :g:`/ C A / <g1:/ C A />` ⊥ :g:`/ D E / <g1:/ D E />`",
        "contract": "center(:g:`( A B C ) <g1:( A B C )>`) ∈ :g:`/ A C / <g1:/ A C />`",
        "steps": [
            ("given", ["III.def.2", "I.def.10"], ":g:`/ D E / <g1:/ D E />` touches :g:`( A B C ) <g1:( A B C )>` at :g:`C <g1:C>`, :g:`/ C A / <g1:/ C A />` ⊥ :g:`/ D E / <g1:/ D E />`"),
            ("construct", ["I.def.16", "I.post.1"], "assume center(:g:`( A B C ) <g1:( A B C )>`) = :g:`F <g1:F>` ∉ :g:`/ A C / <g1:/ A C />`, join :g:`/ C F / <g1:/ C F />`"),
            ("assert", ["III.18"], ":g:`/ D E / <g1:/ D E />` touches :g:`( A B C ) <g1:( A B C )>` at :g:`C <g1:C>` and :g:`F <g1:F>` is center → :g:`/ F C / <g1:/ F C />` ⊥ :g:`/ D E / <g1:/ D E />` → :g:`< F C E ) <g1:< F C E )>` is right"),
            ("assert", ["I.post.4", "I.cn.5"], ":g:`< A C E ) <g1:< A C E )>` is right → :g:`< F C E ) <g1:< F C E )>` :eq:`= <g1:< F C E ) = g1:< A C E )>` :g:`< A C E ) <g1:< A C E )>` (the less to the greater) ⇒⇐"),
            ("conclude", ["I.def.16"], "center(:g:`( A B C ) <g1:( A B C )>`) ∈ :g:`/ A C / <g1:/ A C />`"),
        ],
    },
    "III.20": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`< B E C ) <g1:< B E C )>`", ":g:`< B A C ) <g1:< B A C )>`", ":g:`( B C ) <g1:( B C )>`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>` with center :g:`E <g1:E>`, central angle :g:`< B E C ) <g1:< B E C )>` and inscribed angle :g:`< B A C ) <g1:< B A C )>` on base arc :g:`( B C ) <g1:( B C )>`",
        "contract": ":g:`< B E C ) <g1:< B E C )>` = 2 · :g:`< B A C ) <g1:< B A C )>`",
        "steps": [
            ("given", ["I.def.15", "III.def.10"], ":g:`( A B C ) <g1:( A B C )>` with center :g:`E <g1:E>`, central angle :g:`< B E C ) <g1:< B E C )>` and inscribed angle :g:`< B A C ) <g1:< B A C )>` on base arc :g:`( B C ) <g1:( B C )>`"),
            ("construct", ["I.post.1", "I.post.2"], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`E <g1:E>`) → :g:`/ A E / <g1:/ A E />`, @fn(I.post.2)(:g:`/ A E / <g1:/ A E />`) → :g:`/ A F / <g1:/ A F />`"),
            ("assert", ["I.5", "I.32"], ":g:`/ E A / <g1:/ E A />` :eq:`= <g1:/ E A / = g1:/ E B />` :g:`/ E B / <g1:/ E B />` → :g:`< E A B ) <g1:< E A B )>` :eq:`= <g1:< E A B ) = g1:< E B A )>` :g:`< E B A ) <g1:< E B A )>` → :g:`< B E F ) <g1:< B E F )>` = :g:`< E A B ) <g1:< E A B )>` + :g:`< E B A ) <g1:< E B A )>` = 2 · :g:`< E A B ) <g1:< E A B )>`"),
            ("assert", ["I.5", "I.32", "I.cn.2"], "similarly :g:`< F E C ) <g1:< F E C )>` = 2 · :g:`< E A C ) <g1:< E A C )>` → whole :g:`< B E C ) <g1:< B E C )>` = 2 · :g:`< B A C ) <g1:< B A C )>`"),
            ("conclude", ["I.32", "I.cn.3"], "for inflected :g:`< B D C ) <g1:< B D C )>` with :g:`/ D E G / <g1:/ D G />`, :g:`< G E C ) <g1:< G E C )>` = 2 · :g:`< E D C ) <g1:< E D C )>` and :g:`< G E B ) <g1:< G E B )>` = 2 · :g:`< E D B ) <g1:< E D B )>` → remainder :g:`< B E C ) <g1:< B E C )>` = 2 · :g:`< B D C ) <g1:< B D C )>`"),
        ],
    },
    "III.21": {
        "subtype": "theorem",
        "args": [":g:`( A B C D ) <g1:( A B C D )>`", ":g:`< B A E D ) <g1:< B A E D )>`", ":g:`< B A D ) <g1:< B A D )>`", ":g:`< B E D ) <g1:< B E D )>`"],
        "returns": [],
        "given": ":g:`( A B C D ) <g1:( A B C D )>`, :g:`< B A D ) <g1:< B A D )>`, :g:`< B E D ) <g1:< B E D )>` ∈ :g:`< B A E D ) <g1:< B A E D )>`",
        "contract": ":g:`< B A D ) <g1:< B A D )>` :eq:`= <g1:< B A D ) = g1:< B E D )>` :g:`< B E D ) <g1:< B E D )>`",
        "steps": [
            ("given", ["I.def.15", "III.def.8"], ":g:`( A B C D ) <g1:( A B C D )>`, :g:`< B A D ) <g1:< B A D )>`, :g:`< B E D ) <g1:< B E D )>` ∈ :g:`< B A E D ) <g1:< B A E D )>`"),
            ("construct", ["III.1", "I.post.1"], "@fn(III.1)(:g:`( A B C D ) <g1:( A B C D )>`) → :g:`F <g1:F>`, @fn(I.post.1)(:g:`B <g1:B>`, :g:`F <g1:F>`) → :g:`/ B F / <g1:/ B F />`, @fn(I.post.1)(:g:`F <g1:F>`, :g:`D <g1:D>`) → :g:`/ F D / <g1:/ F D />`"),
            ("assert", ["III.20"], ":g:`< B F D ) <g1:< B F D )>` at center :g:`F <g1:F>`, :g:`< B A D ) <g1:< B A D )>` on arc with base :g:`( B C D ) <g1:( B C D )>` → :g:`< B F D ) <g1:< B F D )>` = 2 · :g:`< B A D ) <g1:< B A D )>`"),
            ("assert", ["III.20"], ":g:`< B F D ) <g1:< B F D )>` at center :g:`F <g1:F>`, :g:`< B E D ) <g1:< B E D )>` on arc with base :g:`( B C D ) <g1:( B C D )>` → :g:`< B F D ) <g1:< B F D )>` = 2 · :g:`< B E D ) <g1:< B E D )>`"),
            ("conclude", ["I.cn.1"], ":g:`< B A D ) <g1:< B A D )>` :eq:`= <g1:< B A D ) = g1:< B E D )>` :g:`< B E D ) <g1:< B E D )>`"),
        ],
    },
    "III.22": {
        "subtype": "theorem",
        "args": [":g:`( A B C D ) <g1:( A B C D )>`", ":g:`< A B C D > <g1:< A B C D >>`"],
        "returns": [],
        "given": ":g:`< A B C D > <g1:< A B C D >>` inscribed in :g:`( A B C D ) <g1:( A B C D )>`",
        "contract": ":g:`< A B C ) <g1:< A B C )>` + :g:`< A D C ) <g1:< A D C )>` = 2∟, :g:`< B A D ) <g1:< B A D )>` + :g:`< D C B ) <g1:< D C B )>` = 2∟",
        "steps": [
            ("given", ["I.def.15", "I.def.19"], ":g:`( A B C D ) <g1:( A B C D )>`, quadrilateral :g:`< A B C D > <g1:< A B C D >>` inscribed in :g:`( A B C D ) <g1:( A B C D )>`"),
            ("construct", ["I.post.1"], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`C <g1:C>`) → :g:`/ A C / <g1:/ A C />`, @fn(I.post.1)(:g:`B <g1:B>`, :g:`D <g1:D>`) → :g:`/ B D / <g1:/ B D />`"),
            ("assert", ["I.32"], "in :g:`< A B C > <g1:< A B C >>`, :g:`< C A B ) <g1:< C A B )>` + :g:`< A B C ) <g1:< A B C )>` + :g:`< B C A ) <g1:< B C A )>` = 2∟"),
            ("assert", ["III.21", "I.cn.2"], ":g:`< C A B ) <g1:< C A B )>` :eq:`= <g1:< C A B ) = g1:< B D C )>` :g:`< B D C ) <g1:< B D C )>` in :g:`( B A D C ) <g1:( B A D C )>`, :g:`< A C B ) <g1:< A C B )>` :eq:`= <g1:< A C B ) = g1:< A D B )>` :g:`< A D B ) <g1:< A D B )>` in :g:`( A D C B ) <g1:( A D C B )>` → :g:`< A D C ) <g1:< A D C )>` = :g:`< B A C ) <g1:< B A C )>` + :g:`< A C B ) <g1:< A C B )>`"),
            ("conclude", ["I.cn.2", "I.cn.1"], ":g:`< A B C ) <g1:< A B C )>` + :g:`< A D C ) <g1:< A D C )>` = :g:`< A B C ) <g1:< A B C )>` + :g:`< B A C ) <g1:< B A C )>` + :g:`< A C B ) <g1:< A C B )>` = 2∟, and :g:`< B A D ) <g1:< B A D )>` + :g:`< D C B ) <g1:< D C B )>` = 2∟"),
        ],
    },
    "III.23": {
        "subtype": "theorem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`( A C B ) <g1:( A C B )>`", ":g:`( A D B ) <g1:( A D B )>`"],
        "returns": [],
        "given": "similar circle segments :g:`( A C B ) <g1:( A C B )>`, :g:`( A D B ) <g1:( A D B )>` on the same side of :g:`/ A B / <g1:/ A B />`",
        "contract": "¬(:g:`( A C B ) <g1:( A C B )>` ≠ :g:`( A D B ) <g1:( A D B )>`)",
        "steps": [
            ("given", ["III.def.6", "III.def.11"], "assume similar and unequal circle segments :g:`( A C B ) <g1:( A C B )>`, :g:`( A D B ) <g1:( A D B )>` on the same side of :g:`/ A B / <g1:/ A B />`"),
            ("construct", ["I.post.1"], "draw :g:`/ A C D / <g1:/ A C D />` through both arcs, @fn(I.post.1)(:g:`C <g1:C>`, :g:`B <g1:B>`) → :g:`/ C B / <g1:/ C B />`, @fn(I.post.1)(:g:`D <g1:D>`, :g:`B <g1:B>`) → :g:`/ D B / <g1:/ D B />`"),
            ("assert", ["III.def.11"], ":g:`( A C B ) <g1:( A C B )>` ~ :g:`( A D B ) <g1:( A D B )>` → :g:`< A C B ) <g1:< A C B )>` :eq:`= <g1:< A C B ) = g1:< A D B )>` :g:`< A D B ) <g1:< A D B )>`"),
            ("assert", ["I.16"], "in :g:`< C D B > <g1:< C D B >>`, exterior :g:`< A C B ) <g1:< A C B )>` > interior :g:`< A D B ) <g1:< A D B )>` ⇒⇐"),
            ("conclude", [], "on :g:`/ A B / <g1:/ A B />`, two similar and unequal circle segments cannot be constructed on the same side"),
        ],
    },
    "III.24": {
        "subtype": "theorem",
        "args": [":g:`( A E B ) <g1:( A E B )>`", ":g:`( C F D ) <g1:( C F D )>`", ":g:`/ A B / <g1:/ A B />`", ":g:`/ C D / <g1:/ C D />`"],
        "returns": [],
        "given": ":g:`( A E B ) <g1:( A E B )>` ~ :g:`( C F D ) <g1:( C F D )>`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ C D />` :g:`/ C D / <g1:/ C D />`",
        "contract": ":g:`( A E B ) <g1:( A E B )>` :eq:`= <g1:( A E B ) = g1:( C F D )>` :g:`( C F D ) <g1:( C F D )>`",
        "steps": [
            ("given", ["III.def.11", "I.def.4"], ":g:`( A E B ) <g1:( A E B )>` ~ :g:`( C F D ) <g1:( C F D )>` on equal chords :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ C D />` :g:`/ C D / <g1:/ C D />`"),
            ("construct", ["I.cn.4"], "apply :g:`( A E B ) <g1:( A E B )>` to :g:`( C F D ) <g1:( C F D )>` with :g:`A <g1:A>` :coincide:`≃ <g1:A ≡ g1:C>` :g:`C <g1:C>` and :g:`/ A B / <g1:/ A B />` along :g:`/ C D / <g1:/ C D />` → :g:`B <g1:B>` :coincide:`≃ <g1:B ≡ g1:D>` :g:`D <g1:D>`"),
            ("assert", ["III.23"], ":g:`/ A B / <g1:/ A B />` :coincide:`≃ <g1:/ A B / ≡ g1:/ C D />` :g:`/ C D / <g1:/ C D />` → :g:`( A E B ) <g1:( A E B )>` cannot fall wholly inside or outside :g:`( C F D ) <g1:( C F D )>`"),
            ("assert", ["III.10"], "if :g:`( A E B ) <g1:( A E B )>` falls awry as :g:`( C G D ) <g1:( C G D )>`, two circles cut at more than two points ⇒⇐"),
            ("conclude", ["I.cn.4"], ":g:`( A E B ) <g1:( A E B )>` :coincide:`≃ <g1:( A E B ) ≡ g1:( C F D )>` :g:`( C F D ) <g1:( C F D )>` → :g:`( A E B ) <g1:( A E B )>` :eq:`= <g1:( A E B ) = g1:( C F D )>` :g:`( C F D ) <g1:( C F D )>`"),
        ],
    },
    "III.25": {
        "subtype": "problem",
        "args": [":g:`( A B C ) <g1:( A B C )>`"],
        "returns": [":g:`E <g1:E>`", ":g:`( E A ) <g1:( A B C )>`"],
        "given": "circle segment :g:`( A B C ) <g1:( A B C )>` with base chord :g:`/ A C / <g1:/ A C />`",
        "contract": "@fn(I.post.3)(:g:`E <g1:E>`, :g:`A <g1:A>`) → :g:`( E A ) <g1:( A B C )>` completing :g:`( A B C ) <g1:( A B C )>`",
        "steps": [
            ("given", ["III.def.6"], "circle segment :g:`( A B C ) <g1:( A B C )>` on chord :g:`/ A C / <g1:/ A C />`"),
            ("construct", ["I.10", "I.11", "I.post.1"], "@fn(I.10)(:g:`/ A C / <g1:/ A C />`) → :g:`D <g1:D>` (:g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ D C />` :g:`/ D C / <g1:/ D C />`), @fn(I.11)(:g:`/ A C / <g1:/ A C />`, :g:`D <g1:D>`) → :g:`/ D B / <g1:/ D B />` ⊥ :g:`/ A C / <g1:/ A C />`, @fn(I.post.1)(:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ A B / <g1:/ A B />`"),
            ("construct", ["I.23", "I.post.2", "I.post.1"], "@fn(I.23)(:g:`/ B A / <g1:/ B A />`, :g:`A <g1:A>`, :g:`< A B D ) <g1:< A B D )>`) → :g:`< B A E ) <g1:< B A E )>` :eq:`= <g1:< B A E ) = g1:< A B D )>` :g:`< A B D ) <g1:< A B D )>`, @fn(I.post.2)(:g:`/ D B / <g1:/ D B />`) ∩ :g:`/ A E / <g1:/ A E />` → :g:`E <g1:E>`, @fn(I.post.1)(:g:`E <g1:E>`, :g:`C <g1:C>`) → :g:`/ E C / <g1:/ E C />`"),
            ("assert", ["I.6", "I.4"], ":g:`< A B E ) <g1:< A B E )>` :eq:`= <g1:< A B E ) = g1:< B A E )>` :g:`< B A E ) <g1:< B A E )>` → :g:`/ E B / <g1:/ E B />` :eq:`= <g1:/ E B / = g1:/ E A />` :g:`/ E A / <g1:/ E A />`; in :g:`< A D E > <g1:< A D E >>`, :g:`< C D E > <g1:< C D E >>`, :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ D C />` :g:`/ D C / <g1:/ D C />`, :g:`/ D E / <g1:/ D E />` common, :g:`< A D E ) <g1:< A D E )>` :eq:`= <g1:< A D E ) = g1:< C D E )>` :g:`< C D E ) <g1:< C D E )>` → :g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ C E />` :g:`/ C E / <g1:/ C E />`"),
            ("conclude", ["I.cn.1", "III.9", "I.post.3"], ":g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E B / = g1:/ E C />` :g:`/ E B / <g1:/ E B />` :eq:`= <g1:/ A E / = g1:/ E B / = g1:/ E C />` :g:`/ E C / <g1:/ E C />` → :g:`E <g1:E>` is the center of :g:`( A B C ) <g1:( A B C )>`, @fn(I.post.3)(:g:`E <g1:E>`, :g:`A <g1:A>`) → :g:`( E A ) <g1:( A B C )>`"),
        ],
    },
    "III.26": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`( D E F ) <g1:( D E F )>`", ":g:`< B G C ) <g1:< B G C )>`", ":g:`< E H F ) <g1:< E H F )>`", ":g:`< B A C ) <g1:< B A C )>`", ":g:`< E D F ) <g1:< E D F )>`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` :g:`( D E F ) <g1:( D E F )>`, :g:`< B G C ) <g1:< B G C )>` :eq:`= <g1:< B G C ) = g1:< E H F )>` :g:`< E H F ) <g1:< E H F )>`, :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`",
        "contract": ":g:`( B K C ) <g1:( B K C )>` :eq:`= <g1:( B K C ) = g1:( E L F )>` :g:`( E L F ) <g1:( E L F )>`",
        "steps": [
            ("given", ["III.def.1", "III.def.9"], ":g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` :g:`( D E F ) <g1:( D E F )>`, :g:`< B G C ) <g1:< B G C )>` :eq:`= <g1:< B G C ) = g1:< E H F )>` :g:`< E H F ) <g1:< E H F )>`, :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`"),
            ("construct", ["I.post.1"], "@fn(I.post.1)(:g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`/ B C / <g1:/ B C />`, @fn(I.post.1)(:g:`E <g1:E>`, :g:`F <g1:F>`) → :g:`/ E F / <g1:/ E F />`"),
            ("assert", ["III.def.1", "I.4"], ":g:`/ B G / <g1:/ B G />` :eq:`= <g1:/ B G / = g1:/ G C / = g1:/ E H / = g1:/ H F />` :g:`/ G C / <g1:/ G C />` :eq:`= <g1:/ B G / = g1:/ G C / = g1:/ E H / = g1:/ H F />` :g:`/ E H / <g1:/ E H />` :eq:`= <g1:/ B G / = g1:/ G C / = g1:/ E H / = g1:/ H F />` :g:`/ H F / <g1:/ H F />`, :g:`< B G C ) <g1:< B G C )>` :eq:`= <g1:< B G C ) = g1:< E H F )>` :g:`< E H F ) <g1:< E H F )>` → :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`"),
            ("assert", ["III.def.11", "III.24"], ":g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`, :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />` → :g:`( B A C ) <g1:( B A C )>` :eq:`= <g1:( B A C ) = g1:( E D F )>` :g:`( E D F ) <g1:( E D F )>`"),
            ("conclude", ["I.cn.3"], ":g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` :g:`( D E F ) <g1:( D E F )>`, :g:`( B A C ) <g1:( B A C )>` :eq:`= <g1:( B A C ) = g1:( E D F )>` :g:`( E D F ) <g1:( E D F )>` → :g:`( B K C ) <g1:( B K C )>` :eq:`= <g1:( B K C ) = g1:( E L F )>` :g:`( E L F ) <g1:( E L F )>`"),
        ],
    },
    "III.27": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`( D E F ) <g1:( D E F )>`", ":g:`( B C ) <g1:( B C )>`", ":g:`( E F ) <g1:( E F )>`", ":g:`< B G C ) <g1:< B G C )>`", ":g:`< E H F ) <g1:< E H F )>`", ":g:`< B A C ) <g1:< B A C )>`", ":g:`< E D F ) <g1:< E D F )>`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` :g:`( D E F ) <g1:( D E F )>`, :g:`( B C ) <g1:( B C )>` :eq:`= <g1:( B C ) = g1:( E F )>` :g:`( E F ) <g1:( E F )>`",
        "contract": ":g:`< B G C ) <g1:< B G C )>` :eq:`= <g1:< B G C ) = g1:< E H F )>` :g:`< E H F ) <g1:< E H F )>`, :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`",
        "steps": [
            ("given", ["III.def.1", "III.def.9"], ":g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` :g:`( D E F ) <g1:( D E F )>`, :g:`( B C ) <g1:( B C )>` :eq:`= <g1:( B C ) = g1:( E F )>` :g:`( E F ) <g1:( E F )>`, :g:`< B G C ) <g1:< B G C )>`, :g:`< E H F ) <g1:< E H F )>` at centers :g:`G <g1:G>`, :g:`H <g1:H>`, :g:`< B A C ) <g1:< B A C )>`, :g:`< E D F ) <g1:< E D F )>` at arcs"),
            ("construct", ["I.23"], "assume :g:`< B G C ) <g1:< B G C )>` > :g:`< E H F ) <g1:< E H F )>` → @fn(I.23)(:g:`/ B G / <g1:/ B G />`, :g:`G <g1:G>`, :g:`< E H F ) <g1:< E H F )>`) → :g:`< B G K ) <g1:< B G K )>` (:eq:`= <g1:< B G K ) = g1:< E H F )>` :g:`< E H F ) <g1:< E H F )>`)"),
            ("assert", ["III.26"], ":g:`< B G K ) <g1:< B G K )>` :eq:`= <g1:< B G K ) = g1:< E H F )>` :g:`< E H F ) <g1:< E H F )>` → :g:`( B K ) <g1:( B K )>` :eq:`= <g1:( B K ) = g1:( E F )>` :g:`( E F ) <g1:( E F )>`"),
            ("assert", ["I.cn.1", "I.cn.5"], ":g:`( B K ) <g1:( B K )>` :eq:`= <g1:( B K ) = g1:( E F )>` :g:`( E F ) <g1:( E F )>` :eq:`= <g1:( E F ) = g1:( B C )>` :g:`( B C ) <g1:( B C )>` ⇒⇐ → :g:`< B G C ) <g1:< B G C )>` :eq:`= <g1:< B G C ) = g1:< E H F )>` :g:`< E H F ) <g1:< E H F )>`"),
            ("conclude", ["III.20"], ":g:`< B A C ) <g1:< B A C )>` = ½ :g:`< B G C ) <g1:< B G C )>`, :g:`< E D F ) <g1:< E D F )>` = ½ :g:`< E H F ) <g1:< E H F )>` → :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>`"),
        ],
    },
    "III.28": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`( D E F ) <g1:( D E F )>`", ":g:`/ A B / <g1:/ A B />`", ":g:`/ D E / <g1:/ D E />`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` :g:`( D E F ) <g1:( D E F )>`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />`",
        "contract": ":g:`( A C B ) <g1:( A C B )>` :eq:`= <g1:( A C B ) = g1:( D F E )>` :g:`( D F E ) <g1:( D F E )>`, :g:`( A G B ) <g1:( A G B )>` :eq:`= <g1:( A G B ) = g1:( D H E )>` :g:`( D H E ) <g1:( D H E )>`",
        "steps": [
            ("given", ["III.def.1", "I.def.4"], ":g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` :g:`( D E F ) <g1:( D E F )>`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />` cutting off greater arcs :g:`( A C B ) <g1:( A C B )>`, :g:`( D F E ) <g1:( D F E )>` and lesser arcs :g:`( A G B ) <g1:( A G B )>`, :g:`( D H E ) <g1:( D H E )>`"),
            ("construct", ["III.1", "I.post.1"], "@fn(III.1)(:g:`( A B C ) <g1:( A B C )>`) → :g:`K <g1:K>`, @fn(III.1)(:g:`( D E F ) <g1:( D E F )>`) → :g:`L <g1:L>`, @fn(I.post.1)(:g:`A <g1:A>`, :g:`K <g1:K>`, :g:`B <g1:B>`) → :g:`/ A K / <g1:/ A K />`, :g:`/ K B / <g1:/ K B />`, @fn(I.post.1)(:g:`D <g1:D>`, :g:`L <g1:L>`, :g:`E <g1:E>`) → :g:`/ D L / <g1:/ D L />`, :g:`/ L E / <g1:/ L E />`"),
            ("assert", ["III.def.1", "I.8"], ":g:`/ A K / <g1:/ A K />` :eq:`= <g1:/ A K / = g1:/ K B / = g1:/ D L / = g1:/ L E />` :g:`/ K B / <g1:/ K B />` :eq:`= <g1:/ A K / = g1:/ K B / = g1:/ D L / = g1:/ L E />` :g:`/ D L / <g1:/ D L />` :eq:`= <g1:/ A K / = g1:/ K B / = g1:/ D L / = g1:/ L E />` :g:`/ L E / <g1:/ L E />`, :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />` → :g:`< A K B ) <g1:< A K B )>` :eq:`= <g1:< A K B ) = g1:< D L E )>` :g:`< D L E ) <g1:< D L E )>`"),
            ("assert", ["III.26"], ":g:`< A K B ) <g1:< A K B )>` :eq:`= <g1:< A K B ) = g1:< D L E )>` :g:`< D L E ) <g1:< D L E )>` → :g:`( A G B ) <g1:( A G B )>` :eq:`= <g1:( A G B ) = g1:( D H E )>` :g:`( D H E ) <g1:( D H E )>`"),
            ("conclude", ["I.cn.3"], ":g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` :g:`( D E F ) <g1:( D E F )>`, :g:`( A G B ) <g1:( A G B )>` :eq:`= <g1:( A G B ) = g1:( D H E )>` :g:`( D H E ) <g1:( D H E )>` → :g:`( A C B ) <g1:( A C B )>` :eq:`= <g1:( A C B ) = g1:( D F E )>` :g:`( D F E ) <g1:( D F E )>`"),
        ],
    },
    "III.29": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`( D E F ) <g1:( D E F )>`", ":g:`( B G C ) <g1:( B G C )>`", ":g:`( E H F ) <g1:( E H F )>`", ":g:`/ B C / <g1:/ B C />`", ":g:`/ E F / <g1:/ E F />`"],
        "returns": [],
        "given": ":g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` :g:`( D E F ) <g1:( D E F )>`, :g:`( B G C ) <g1:( B G C )>` :eq:`= <g1:( B G C ) = g1:( E H F )>` :g:`( E H F ) <g1:( E H F )>`",
        "contract": ":g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`",
        "steps": [
            ("given", ["III.def.1", "I.def.4"], ":g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` :g:`( D E F ) <g1:( D E F )>`, :g:`( B G C ) <g1:( B G C )>` :eq:`= <g1:( B G C ) = g1:( E H F )>` :g:`( E H F ) <g1:( E H F )>`, subtended by :g:`/ B C / <g1:/ B C />`, :g:`/ E F / <g1:/ E F />`"),
            ("construct", ["III.1", "I.post.1"], "@fn(III.1)(:g:`( A B C ) <g1:( A B C )>`) → :g:`K <g1:K>`, @fn(III.1)(:g:`( D E F ) <g1:( D E F )>`) → :g:`L <g1:L>`, @fn(I.post.1)(:g:`B <g1:B>`, :g:`K <g1:K>`, :g:`C <g1:C>`) → :g:`/ B K / <g1:/ B K />`, :g:`/ K C / <g1:/ K C />`, @fn(I.post.1)(:g:`E <g1:E>`, :g:`L <g1:L>`, :g:`F <g1:F>`) → :g:`/ E L / <g1:/ E L />`, :g:`/ L F / <g1:/ L F />`"),
            ("assert", ["III.27"], ":g:`( B G C ) <g1:( B G C )>` :eq:`= <g1:( B G C ) = g1:( E H F )>` :g:`( E H F ) <g1:( E H F )>` → :g:`< B K C ) <g1:< B K C )>` :eq:`= <g1:< B K C ) = g1:< E L F )>` :g:`< E L F ) <g1:< E L F )>`"),
            ("assert", ["III.def.1"], ":g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:( A B C ) = g1:( D E F )>` :g:`( D E F ) <g1:( D E F )>` → :g:`/ B K / <g1:/ B K />` :eq:`= <g1:/ B K / = g1:/ K C / = g1:/ E L / = g1:/ L F />` :g:`/ K C / <g1:/ K C />` :eq:`= <g1:/ B K / = g1:/ K C / = g1:/ E L / = g1:/ L F />` :g:`/ E L / <g1:/ E L />` :eq:`= <g1:/ B K / = g1:/ K C / = g1:/ E L / = g1:/ L F />` :g:`/ L F / <g1:/ L F />`"),
            ("conclude", ["I.4"], ":g:`/ B K / <g1:/ B K />`, :g:`/ K C / <g1:/ K C />` :eq:`= <g1:/ B K / = g1:/ E L /; g1:/ K C / = g1:/ L F />` :g:`/ E L / <g1:/ E L />`, :g:`/ L F / <g1:/ L F />`, :g:`< B K C ) <g1:< B K C )>` :eq:`= <g1:< B K C ) = g1:< E L F )>` :g:`< E L F ) <g1:< E L F )>` → :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ E F />` :g:`/ E F / <g1:/ E F />`"),
        ],
    },
    "III.30": {
        "subtype": "problem",
        "args": [":g:`( A D B ) <g1:( A D B )>`"],
        "returns": [":g:`D <g1:D>`"],
        "given": ":g:`( A D B ) <g1:( A D B )>`",
        "contract": ":g:`D <g1:D>` ∈ :g:`( A D B ) <g1:( A D B )>`, :g:`( A D ) <g1:( A D )>` :eq:`= <g1:( A D ) = g1:( D B )>` :g:`( D B ) <g1:( D B )>`",
        "steps": [
            ("given", [], ":g:`( A D B ) <g1:( A D B )>`"),
            ("construct", ["I.post.1", "I.10"], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`/ A B / <g1:/ A B />`, @fn(I.10)(:g:`/ A B / <g1:/ A B />`) → :g:`C <g1:C>` (:g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`)"),
            ("construct", ["I.11", "I.post.1"], "@fn(I.11)(:g:`/ A B / <g1:/ A B />`, :g:`C <g1:C>`) → :g:`/ C D / <g1:/ C D />` ⊥ :g:`/ A B / <g1:/ A B />`, @fn(I.post.1)(:g:`A <g1:A>`, :g:`D <g1:D>`, :g:`B <g1:B>`) → :g:`/ A D / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />`"),
            ("assert", ["I.def.10", "I.4"], ":g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ C B />` :g:`/ C B / <g1:/ C B />`, :g:`/ C D / <g1:/ C D />` common, :g:`< A C D ) <g1:< A C D )>` :eq:`= <g1:< A C D ) = g1:< B C D )>` :g:`< B C D ) <g1:< B C D )>` → :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`"),
            ("conclude", ["I.def.18", "III.28"], ":g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`, :g:`( A D ) <g1:( A D )>`, :g:`( D B ) <g1:( D B )>` < semicircle → :g:`( A D ) <g1:( A D )>` :eq:`= <g1:( A D ) = g1:( D B )>` :g:`( D B ) <g1:( D B )>`"),
        ],
    },
    "III.31": {
        "subtype": "theorem",
        "args": [":g:`( A B C D ) <g1:( A B C D )>`", ":g:`/ B C / <g1:/ B C />`", ":g:`E <g1:E>`"],
        "returns": [],
        "given": ":g:`( A B C D ) <g1:( A B C D )>`, diameter :g:`/ B C / <g1:/ B C />`, center :g:`E <g1:E>`, chords :g:`/ B A / <g1:/ B A />`, :g:`/ A C / <g1:/ A C />`, :g:`/ A D / <g1:/ A D />`, :g:`/ D C / <g1:/ D C />`",
        "contract": ":g:`< B A C ) <g1:< B A C )>` = ∟, :g:`< A B C ) <g1:< A B C )>` < ∟, :g:`< A D C ) <g1:< A D C )>` > ∟",
        "steps": [
            ("given", ["I.def.15", "I.def.17", "I.def.18", "III.def.8"], ":g:`( A B C D ) <g1:( A B C D )>`, diameter :g:`/ B C / <g1:/ B C />`, center :g:`E <g1:E>`, semicircle :g:`( B A C ) <g1:( B A C )>`, greater segment :g:`( A B C ) <g1:( A B C )>`, lesser segment :g:`( A D C ) <g1:( A D C )>`"),
            ("construct", ["I.post.1", "I.post.2"], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`E <g1:E>`) → :g:`/ A E / <g1:/ A E />`, @fn(I.post.2)(:g:`/ B A / <g1:/ B A />`, :g:`F <g1:F>`) → :g:`/ B F / <g1:/ B F />`"),
            ("assert", ["I.def.15", "I.5", "I.cn.2"], ":g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ E A />` :g:`/ E A / <g1:/ E A />` :eq:`= <g1:/ C E / = g1:/ E A />` :g:`/ C E / <g1:/ C E />` → :g:`< A B E ) <g1:< A B E )>` :eq:`= <g1:< A B E ) = g1:< B A E )>` :g:`< B A E ) <g1:< B A E )>`, :g:`< A C E ) <g1:< A C E )>` :eq:`= <g1:< A C E ) = g1:< C A E )>` :g:`< C A E ) <g1:< C A E )>` → :g:`< B A C ) <g1:< B A C )>` = :g:`< A B C ) <g1:< A B C )>` + :g:`< A C B ) <g1:< A C B )>`"),
            ("assert", ["I.32", "I.cn.1", "I.def.10"], ":g:`< F A C ) <g1:< F A C )>` = :g:`< A B C ) <g1:< A B C )>` + :g:`< A C B ) <g1:< A C B )>` → :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< F A C )>` :g:`< F A C ) <g1:< F A C )>` = ∟"),
            ("assert", ["I.17", "III.22"], ":g:`< B A C ) <g1:< B A C )>` + :g:`< A B C ) <g1:< A B C )>` < 2∟ → :g:`< A B C ) <g1:< A B C )>` < ∟; :g:`< A B C ) <g1:< A B C )>` + :g:`< A D C ) <g1:< A D C )>` = 2∟ → :g:`< A D C ) <g1:< A D C )>` > ∟"),
            ("conclude", ["I.cn.5"], ":g:`< B A C ) <g1:< B A C )>` = ∟, :g:`< A B C ) <g1:< A B C )>` < ∟, :g:`< A D C ) <g1:< A D C )>` > ∟; angle(:g:`( A B C ) <g1:( A B C )>`, :g:`/ A C / <g1:/ A C />`) > ∟, angle(:g:`( A D C ) <g1:( A D C )>`, :g:`/ C A / <g1:/ C A />`) < ∟"),
        ],
    },
    "III.32": {
        "subtype": "theorem",
        "args": [":g:`( A B C D ) <g1:( A B C D )>`", ":g:`/ E F / <g1:/ E F />`", ":g:`/ B D / <g1:/ B D />`"],
        "returns": [],
        "given": "tangent :g:`/ E F / <g1:/ E F />` touching :g:`( A B C D ) <g1:( A B C D )>` at :g:`B <g1:B>`, chord :g:`/ B D / <g1:/ B D />`",
        "contract": ":g:`< F B D ) <g1:< F B D )>` :eq:`= <g1:< F B D ) = g1:< B A D )>` :g:`< B A D ) <g1:< B A D )>`, :g:`< E B D ) <g1:< E B D )>` :eq:`= <g1:< E B D ) = g1:< B C D )>` :g:`< D C B ) <g1:< B C D )>`",
        "steps": [
            ("given", ["III.def.2", "III.def.6"], "tangent :g:`/ E F / <g1:/ E F />` touching :g:`( A B C D ) <g1:( A B C D )>` at :g:`B <g1:B>`, chord :g:`/ B D / <g1:/ B D />` cutting :g:`( A B C D ) <g1:( A B C D )>` into segments :g:`( B A D ) <g1:( B A D )>`, :g:`( D C B ) <g1:( D C B )>`"),
            ("construct", ["I.11", "I.post.1"], "@fn(I.11)(:g:`/ E F / <g1:/ E F />`, :g:`B <g1:B>`) → :g:`/ B A / <g1:/ B A />` ⊥ :g:`/ E F / <g1:/ E F />`, point :g:`C <g1:C>` ∈ :g:`( D C B ) <g1:( D C B )>`, @fn(I.post.1)(:g:`A <g1:A>`, :g:`D <g1:D>`, :g:`C <g1:C>`, :g:`B <g1:B>`) → :g:`/ A D / <g1:/ A D />`, :g:`/ D C / <g1:/ D C />`, :g:`/ C B / <g1:/ C B />`"),
            ("assert", ["III.19", "III.31"], ":g:`/ B A / <g1:/ B A />` ⊥ :g:`/ E F / <g1:/ E F />` at :g:`B <g1:B>` → :g:`/ B A / <g1:/ B A />` is a diameter of :g:`( A B C D ) <g1:( A B C D )>` → :g:`< A D B ) <g1:< A D B )>` = ∟"),
            ("assert", ["I.32", "I.cn.3"], ":g:`< B A D ) <g1:< B A D )>` + :g:`< A B D ) <g1:< A B D )>` = ∟ = :g:`< A B F ) <g1:< A B F )>` = :g:`< D B F ) <g1:< F B D )>` + :g:`< A B D ) <g1:< A B D )>` → :g:`< D B F ) <g1:< F B D )>` :eq:`= <g1:< F B D ) = g1:< B A D )>` :g:`< B A D ) <g1:< B A D )>`"),
            ("assert", ["III.22", "I.13"], ":g:`< B A D ) <g1:< B A D )>` + :g:`< B C D ) <g1:< B C D )>` = 2∟ = :g:`< D B F ) <g1:< F B D )>` + :g:`< D B E ) <g1:< E B D )>`"),
            ("conclude", ["I.cn.3"], ":g:`< F B D ) <g1:< F B D )>` :eq:`= <g1:< F B D ) = g1:< B A D )>` :g:`< B A D ) <g1:< B A D )>`, :g:`< E B D ) <g1:< E B D )>` :eq:`= <g1:< E B D ) = g1:< B C D )>` :g:`< D C B ) <g1:< B C D )>`"),
        ],
    },
    "III.33": {
        "subtype": "problem",
        "args": [":g:`/ A B / <g1:/ A B />`", ":g:`< C ) <g1:< C )>`"],
        "returns": [":g:`( A E B ) <g1:( A E B )>`"],
        "given": ":g:`/ A B / <g1:/ A B />`, :g:`< C ) <g1:< C )>`",
        "contract": ":g:`< A E B ) <g1:< A E B )>` in segment :g:`( A E B ) <g1:( A E B )>` on :g:`/ A B / <g1:/ A B />` :eq:`= <g1:< A E B ) = g1:< C )>` :g:`< C ) <g1:< C )>`",
        "steps": [
            ("given", ["I.def.4", "I.def.9", "III.def.6"], ":g:`/ A B / <g1:/ A B />`, rectilineal angle :g:`< C ) <g1:< C )>`"),
            ("construct", ["I.23", "I.11", "I.10", "I.post.1"], "@fn(I.23)(:g:`/ A B / <g1:/ A B />`, :g:`A <g1:A>`, :g:`< C ) <g1:< C )>`) → :g:`< B A D ) <g1:< B A D )>` :eq:`= <g1:< B A D ) = g1:< C )>` :g:`< C ) <g1:< C )>`, @fn(I.11)(:g:`/ D A / <g1:/ D A />`, :g:`A <g1:A>`) → :g:`/ A E / <g1:/ A E />` ⊥ :g:`/ D A / <g1:/ D A />`, @fn(I.10)(:g:`/ A B / <g1:/ A B />`) → :g:`F <g1:F>`, @fn(I.11)(:g:`/ A B / <g1:/ A B />`, :g:`F <g1:F>`) → :g:`/ F G / <g1:/ F G />` ⊥ :g:`/ A B / <g1:/ A B />`, @fn(I.post.1)(:g:`G <g1:G>`, :g:`B <g1:B>`) → :g:`/ G B / <g1:/ G B />`"),
            ("construct", ["I.4", "I.post.3", "I.post.1"], ":g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`, :g:`< A F G ) <g1:< A F G )>` :eq:`= <g1:< A F G ) = g1:< B F G )>` :g:`< B F G ) <g1:< B F G )>` → :g:`/ A G / <g1:/ A G />` :eq:`= <g1:/ A G / = g1:/ G B />` :g:`/ G B / <g1:/ G B />`; @fn(I.post.3)(:g:`G <g1:G>`, :g:`A <g1:A>`) → :g:`( A B E ) <g1:( A B E )>`, @fn(I.post.1)(:g:`E <g1:E>`, :g:`B <g1:B>`) → :g:`/ E B / <g1:/ E B />`"),
            ("assert", ["III.16"], ":g:`/ A D / <g1:/ A D />` ⊥ diameter :g:`/ A E / <g1:/ A E />` at :g:`A <g1:A>` → :g:`/ A D / <g1:/ A D />` touches :g:`( A B E ) <g1:( A B E )>` at :g:`A <g1:A>`"),
            ("assert", ["III.32"], "tangent :g:`/ A D / <g1:/ A D />` and chord :g:`/ A B / <g1:/ A B />` at :g:`A <g1:A>` → :g:`< D A B ) <g1:< B A D )>` :eq:`= <g1:< B A D ) = g1:< A E B )>` :g:`< A E B ) <g1:< A E B )>` in alternate segment :g:`( A E B ) <g1:( A E B )>`"),
            ("conclude", ["I.cn.1", "III.31"], ":g:`< B A D ) <g1:< B A D )>` :eq:`= <g1:< B A D ) = g1:< C )>` :g:`< C ) <g1:< C )>` → :g:`< A E B ) <g1:< A E B )>` :eq:`= <g1:< A E B ) = g1:< C )>` :g:`< C ) <g1:< C )>` in segment :g:`( A E B ) <g1:( A E B )>` on :g:`/ A B / <g1:/ A B />`"),
        ],
    },
    "III.34": {
        "subtype": "problem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`< D ) <g1:< D )>`"],
        "returns": [":g:`( B A C ) <g1:( B A C )>`"],
        "given": ":g:`( A B C ) <g1:( A B C )>`, :g:`< D ) <g1:< D )>`",
        "contract": ":g:`< B A C ) <g1:< B A C )>` in segment :g:`( B A C ) <g1:( B A C )>` cut off from :g:`( A B C ) <g1:( A B C )>` :eq:`= <g1:< B A C ) = g1:< D )>` :g:`< D ) <g1:< D )>`",
        "steps": [
            ("given", ["I.def.15", "I.def.9"], "circle :g:`( A B C ) <g1:( A B C )>`, rectilineal angle :g:`< D ) <g1:< D )>`"),
            ("construct", ["III.16"], "tangent :g:`/ E F / <g1:/ E F />` touching :g:`( A B C ) <g1:( A B C )>` at :g:`B <g1:B>`"),
            ("construct", ["I.23"], "@fn(I.23)(:g:`/ F B / <g1:/ F B />`, :g:`B <g1:B>`, :g:`< D ) <g1:< D )>`) → :g:`< F B C ) <g1:< F B C )>` :eq:`= <g1:< F B C ) = g1:< D )>` :g:`< D ) <g1:< D )>` with chord :g:`/ B C / <g1:/ B C />`"),
            ("assert", ["III.32"], "tangent :g:`/ E F / <g1:/ E F />` and chord :g:`/ B C / <g1:/ B C />` at :g:`B <g1:B>` → :g:`< F B C ) <g1:< F B C )>` :eq:`= <g1:< F B C ) = g1:< B A C )>` :g:`< B A C ) <g1:< B A C )>` in alternate segment :g:`( B A C ) <g1:( B A C )>`"),
            ("conclude", ["I.cn.1", "III.def.8"], ":g:`< F B C ) <g1:< F B C )>` :eq:`= <g1:< F B C ) = g1:< D )>` :g:`< D ) <g1:< D )>` → :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< D )>` :g:`< D ) <g1:< D )>` in segment :g:`( B A C ) <g1:( B A C )>`"),
        ],
    },
    "III.35": {
        "subtype": "theorem",
        "args": [":g:`( A B C D ) <g1:( A B C D )>`", ":g:`/ A C / <g1:/ A C />`", ":g:`/ B D / <g1:/ B D />`"],
        "returns": [],
        "given": ":g:`/ A C / <g1:/ A C />`, :g:`/ B D / <g1:/ B D />` in :g:`( A B C D ) <g1:( A B C D )>` intersecting at :g:`E <g1:E>`",
        "contract": "rect(:g:`/ A E / <g1:/ A E />`, :g:`/ E C / <g1:/ E C />`) :eq:`= <g1:/ A E / = g1:/ D E />, g1:/ E C / = g1:/ E B />` rect(:g:`/ D E / <g1:/ D E />`, :g:`/ E B / <g1:/ E B />`)",
        "steps": [
            ("given", ["I.def.15"], ":g:`/ A C / <g1:/ A C />` ∩ :g:`/ B D / <g1:/ B D />` → :g:`E <g1:E>` inside :g:`( A B C D ) <g1:( A B C D )>`"),
            ("construct", ["III.1", "I.12", "I.post.1"], "@fn(III.1)(:g:`( A B C D ) <g2:( A B C D )>`) → :g:`F <g2:F>`, @fn(I.12)(:g:`/ A C / <g2:/ A C />`, :g:`F <g2:F>`) → :g:`/ F G / <g2:/ F G />` ⊥ :g:`/ A C / <g2:/ A C />`, @fn(I.12)(:g:`/ B D / <g2:/ B D />`, :g:`F <g2:F>`) → :g:`/ F H / <g2:/ F H />` ⊥ :g:`/ B D / <g2:/ B D />`, @fn(I.post.1)(:g:`F <g2:F>`, :g:`B <g2:B>`, :g:`C <g2:C>`, :g:`E <g2:E>`) → :g:`/ F B / <g2:/ F B />`, :g:`/ F C / <g2:/ F C />`, :g:`/ F E / <g2:/ F E />`"),
            ("assert", ["III.3", "II.5"], ":g:`/ A G / <g2:/ A G />` :eq:`= <g2:/ A G / = g2:/ G C />` :g:`/ G C / <g2:/ G C />` → rect(:g:`/ A E / <g2:/ A E />`, :g:`/ E C / <g2:/ E C />`) + :g:`/ E G / <g2:/ E G />`² = :g:`/ G C / <g2:/ G C />`²"),
            ("assert", ["I.cn.2", "I.47"], "rect(:g:`/ A E / <g2:/ A E />`, :g:`/ E C / <g2:/ E C />`) + :g:`/ F E / <g2:/ F E />`² = :g:`/ F C / <g2:/ F C />`² and rect(:g:`/ D E / <g2:/ D E />`, :g:`/ E B / <g2:/ E B />`) + :g:`/ F E / <g2:/ F E />`² = :g:`/ F B / <g2:/ F B />`²"),
            ("conclude", ["I.def.15", "I.cn.1", "I.cn.3"], ":g:`/ F C / <g2:/ F C />` :eq:`= <g2:/ F C / = g2:/ F B />` :g:`/ F B / <g2:/ F B />` → rect(:g:`/ A E / <g1:/ A E />`, :g:`/ E C / <g1:/ E C />`) = rect(:g:`/ D E / <g1:/ D E />`, :g:`/ E B / <g1:/ E B />`)"),
        ],
    },
    "III.36": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`D <g1:D>`", ":g:`/ D C A / <g1:/ A D />`", ":g:`/ D B / <g1:/ D B />`"],
        "returns": [],
        "given": ":g:`D <g1:D>` outside :g:`( A B C ) <g1:( A B C )>`, secant :g:`/ D C A / <g1:/ A D />`, tangent :g:`/ D B / <g1:/ D B />`",
        "contract": "rect(:g:`/ A D / <g1:/ A D />`, :g:`/ C D / <g1:/ C D />`) = :g:`/ D B / <g1:/ D B />`²",
        "steps": [
            ("given", ["III.def.2"], ":g:`D <g1:D>` outside :g:`( A B C ) <g1:( A B C )>`, secant :g:`/ D C A / <g1:/ A D />`, tangent :g:`/ D B / <g1:/ D B />` at :g:`B <g1:B>`"),
            ("construct", ["III.1", "I.post.1", "III.18"], "@fn(III.1)(:g:`( A B C ) <g1:( A B C )>`) → :g:`F <g1:F>`, @fn(I.post.1)(:g:`F <g1:F>`, :g:`B <g1:B>`) → :g:`/ F B / <g1:/ F B />` ⊥ :g:`/ D B / <g1:/ D B />` (:g:`< F B D ) <g1:< F B D )>` is right)"),
            ("assert", ["I.def.15", "II.6"], ":g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ F C />` :g:`/ F C / <g1:/ F C />` → rect(:g:`/ A D / <g1:/ A D />`, :g:`/ C D / <g1:/ C D />`) + :g:`/ F C / <g1:/ F C />`² = :g:`/ F D / <g1:/ F D />`²"),
            ("assert", ["I.def.15", "I.47"], ":g:`/ F C / <g1:/ F C />` :eq:`= <g1:/ F C / = g1:/ F B />` :g:`/ F B / <g1:/ F B />` and :g:`/ F D / <g1:/ F D />`² = :g:`/ F B / <g1:/ F B />`² + :g:`/ D B / <g1:/ D B />`²"),
            ("conclude", ["I.cn.1", "I.cn.3"], "Subtracting :g:`/ F B / <g1:/ F B />`² → rect(:g:`/ A D / <g1:/ A D />`, :g:`/ C D / <g1:/ C D />`) = :g:`/ D B / <g1:/ D B />`²"),
        ],
    },
    "III.37": {
        "subtype": "theorem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`D <g1:D>`", ":g:`/ D C A / <g1:/ A D />`", ":g:`/ D B / <g1:/ D B />`"],
        "returns": [],
        "given": ":g:`D <g1:D>` outside :g:`( A B C ) <g1:( A B C )>`, secant :g:`/ D C A / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />` with rect(:g:`/ A D / <g1:/ A D />`, :g:`/ C D / <g1:/ C D />`) = :g:`/ D B / <g1:/ D B />`²",
        "contract": ":g:`/ D B / <g1:/ D B />` touches :g:`( A B C ) <g1:( A B C )>` at :g:`B <g1:B>`",
        "steps": [
            ("given", ["I.def.15"], "rect(:g:`/ A D / <g1:/ A D />`, :g:`/ C D / <g1:/ C D />`) = :g:`/ D B / <g1:/ D B />`²"),
            ("construct", ["III.17", "III.1", "I.post.1"], "@fn(III.17)(:g:`D <g1:D>`, :g:`( A B C ) <g1:( A B C )>`) → tangent :g:`/ D E / <g1:/ D E />`, @fn(III.1)(:g:`( A B C ) <g1:( A B C )>`) → :g:`F <g1:F>`, @fn(I.post.1)(:g:`F <g1:F>`, :g:`E <g1:E>`, :g:`B <g1:B>`, :g:`D <g1:D>`) → :g:`/ F E / <g1:/ F E />`, :g:`/ F B / <g1:/ F B />`, :g:`/ F D / <g1:/ F D />`"),
            ("assert", ["III.18", "III.36", "I.cn.1"], ":g:`< F E D ) <g1:< F E D )>` is right and rect(:g:`/ A D / <g1:/ A D />`, :g:`/ C D / <g1:/ C D />`) = :g:`/ D E / <g1:/ D E />`² → :g:`/ D B / <g1:/ D B />` :eq:`= <g1:/ D B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />`"),
            ("assert", ["I.def.15", "I.8"], ":g:`/ F B / <g1:/ F B />` :eq:`= <g1:/ F B / = g1:/ F E />` :g:`/ F E / <g1:/ F E />`, :g:`/ F D / <g1:/ F D />` common, :g:`/ D B / <g1:/ D B />` :eq:`= <g1:/ D B / = g1:/ D E />` :g:`/ D E / <g1:/ D E />` → :g:`< D B F ) <g1:< D B F )>` :eq:`= <g1:< D B F ) = g1:< F E D )>` :g:`< F E D ) <g1:< F E D )>` is right"),
            ("conclude", ["III.16"], ":g:`/ D B / <g1:/ D B />` ⊥ :g:`/ F B / <g1:/ F B />` at extremity :g:`B <g1:B>` → :g:`/ D B / <g1:/ D B />` touches :g:`( A B C ) <g1:( A B C )>`"),
        ],
    },
    "IV.1": {
        "subtype": "problem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`D <g1:D>`"],
        "returns": [":g:`/ C A / <g1:/ C A />`"],
        "given": ":g:`( A B C ) <g1:( A B C )>`, :g:`D <g1:D>` not greater than the :term:`diameter <G.61>` of :g:`( A B C ) <g1:( A B C )>`",
        "contract": ":g:`/ C A / <g1:/ C A />` is :term:`fitted into <G.146>` :g:`( A B C ) <g1:( A B C )>` with :g:`/ C A / <g1:/ C A />` :eq:`= <g1:/ C A / = g1:D>` :g:`D <g1:D>`",
        "steps": [
            ("given", ["I.def.4", "I.def.15", "I.def.17", "IV.def.7"], ":g:`( A B C ) <g1:( A B C )>`, :g:`D <g1:D>` not greater than the diameter of :g:`( A B C ) <g1:( A B C )>`"),
            ("construct", ["I.def.17", "I.3"], "Draw diameter :g:`/ B C / <g1:/ B C />` of :g:`( A B C ) <g1:( A B C )>`; if :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:D>` :g:`D <g1:D>`, it is done; if :g:`/ B C / <g1:/ B C />` > :g:`D <g1:D>`, @fn(I.3)(:g:`/ B C / <g1:/ B C />`, :g:`D <g1:D>`) → :g:`/ C E / <g1:/ C E />` :eq:`= <g1:/ C E / = g1:D>` :g:`D <g1:D>`"),
            ("construct", ["I.post.3", "I.post.1"], "@fn(I.post.3)(:g:`C <g1:C>`, :g:`E <g1:E>`) → :g:`( E A F ) <g1:( E A F )>`, @fn(I.post.1)(:g:`C <g1:C>`, :g:`A <g1:A>`) → :g:`/ C A / <g1:/ C A />`"),
            ("assert", ["I.def.15"], ":g:`C <g1:C>` is the center of :g:`( E A F ) <g1:( E A F )>` → :g:`/ C A / <g1:/ C A />` :eq:`= <g1:/ C A / = g1:/ C E />` :g:`/ C E / <g1:/ C E />`"),
            ("conclude", ["I.cn.1", "IV.def.7"], ":g:`/ C E / <g1:/ C E />` :eq:`= <g1:/ C E / = g1:D>` :g:`D <g1:D>` → :g:`/ C A / <g1:/ C A />` :eq:`= <g1:/ C A / = g1:D>` :g:`D <g1:D>` fitted into :g:`( A B C ) <g1:( A B C )>`"),
        ],
    },
    "IV.2": {
        "subtype": "problem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`< D E F > <g1:< D E F >>`"],
        "returns": [":g:`< A B C > <g1:< A B C >>`"],
        "given": ":g:`( A B C ) <g1:( A B C )>`, :g:`< D E F > <g1:< D E F >>`",
        "contract": ":g:`< A B C > <g1:< A B C >>` is :term:`inscribed in <G.148>` :g:`( A B C ) <g1:( A B C )>` and equiangular with :g:`< D E F > <g1:< D E F >>`",
        "steps": [
            ("given", ["I.def.15", "I.def.19", "IV.def.3"], ":g:`( A B C ) <g1:( A B C )>`, :g:`< D E F > <g1:< D E F >>`"),
            ("construct", ["III.16"], "@fn(III.16)(:g:`( A B C ) <g1:( A B C )>`, :g:`A <g1:A>`) → tangent :g:`/ G H / <g1:/ G H />` touching :g:`( A B C ) <g1:( A B C )>` at :g:`A <g1:A>`"),
            ("construct", ["I.23", "I.post.1"], "@fn(I.23)(:g:`/ A H / <g1:/ A H />`, :g:`A <g1:A>`, :g:`< D E F ) <g1:< D E F )>`) → :g:`< H A C ) <g1:< H A C )>` :eq:`= <g1:< H A C ) = g1:< D E F )>` :g:`< D E F ) <g1:< D E F )>`, @fn(I.23)(:g:`/ A G / <g1:/ A G />`, :g:`A <g1:A>`, :g:`< D F E ) <g1:< D F E )>`) → :g:`< G A B ) <g1:< G A B )>` :eq:`= <g1:< G A B ) = g1:< D F E )>` :g:`< D F E ) <g1:< D F E )>`, @fn(I.post.1)(:g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`/ B C / <g1:/ B C />`"),
            ("assert", ["III.32", "I.cn.1"], "Tangent :g:`/ A H / <g1:/ A H />` and chord :g:`/ A C / <g1:/ A C />` → :g:`< H A C ) <g1:< H A C )>` :eq:`= <g1:< H A C ) = g1:< A B C )>` :g:`< A B C ) <g1:< A B C )>`, and :g:`< H A C ) <g1:< H A C )>` :eq:`= <g1:< H A C ) = g1:< D E F )>` :g:`< D E F ) <g1:< D E F )>` → :g:`< A B C ) <g1:< A B C )>` :eq:`= <g1:< A B C ) = g1:< D E F )>` :g:`< D E F ) <g1:< D E F )>`"),
            ("assert", ["III.32", "I.cn.1"], "Similarly, tangent :g:`/ A G / <g1:/ A G />` and chord :g:`/ A B / <g1:/ A B />` → :g:`< G A B ) <g1:< G A B )>` :eq:`= <g1:< G A B ) = g1:< A C B )>` :g:`< A C B ) <g1:< A C B )>` :eq:`= <g1:< A C B ) = g1:< D F E )>` :g:`< D F E ) <g1:< D F E )>`"),
            ("conclude", ["I.32", "IV.def.3"], "Remaining :g:`< B A C ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>` → :g:`< A B C > <g1:< A B C >>` is inscribed in :g:`( A B C ) <g1:( A B C )>` equiangular with :g:`< D E F > <g1:< D E F >>`"),
        ],
    },
    "IV.3": {
        "subtype": "problem",
        "args": [":g:`( A B C ) <g1:( A B C )>`", ":g:`< D E F > <g1:< D E F >>`"],
        "returns": [":g:`< L M N > <g1:< L M N >>`"],
        "given": ":g:`( A B C ) <g1:( A B C )>`, :g:`< D E F > <g1:< D E F >>`",
        "contract": ":g:`< L M N > <g1:< L M N >>` is :term:`circumscribed about <G.150>` :g:`( A B C ) <g1:( A B C )>` and equiangular with :g:`< D E F > <g1:< D E F >>`",
        "steps": [
            ("given", ["I.def.15", "I.def.19", "IV.def.4"], ":g:`( A B C ) <g1:( A B C )>`, :g:`< D E F > <g1:< D E F >>`"),
            ("construct", ["I.post.2", "III.1", "I.23"], "@fn(I.post.2)(:g:`/ E F / <g1:/ E F />`) → :g:`/ H G / <g1:/ H G />`, @fn(III.1)(:g:`( A B C ) <g1:( A B C )>`) → center :g:`K <g1:K>`, draw :g:`/ K B / <g1:/ K B />`, @fn(I.23)(:g:`/ K B / <g1:/ K B />`, :g:`K <g1:K>`) → :g:`< B K A ) <g1:< B K A )>` :eq:`= <g1:< B K A ) = g1:< D E G )>` :g:`< D E G ) <g1:< D E G )>`, :g:`< B K C ) <g1:< B K C )>` :eq:`= <g1:< B K C ) = g1:< D F H )>` :g:`< D F H ) <g1:< D F H )>`"),
            ("construct", ["III.16"], "@fn(III.16)(:g:`( A B C ) <g1:( A B C )>`, :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`) → tangents :g:`/ L A M / <g1:/ L A M />`, :g:`/ M B N / <g1:/ M B N />`, :g:`/ N C L / <g1:/ N C L />` forming :g:`< L M N > <g1:< L M N >>`"),
            ("assert", ["III.18", "I.32"], "Radii :g:`/ K A / <g1:/ K A />`, :g:`/ K B / <g1:/ K B />`, :g:`/ K C / <g1:/ K C />` ⊥ tangents → :g:`< K A M ) <g1:< K A M )>`, :g:`< K B M ) <g1:< K B M )>` are right; in :g:`< A M B K > <g1:< A M B K >>`, :g:`< A K B ) <g1:< A K B )>` + :g:`< A M B ) <g1:< A M B )>` = 2 right angles"),
            ("assert", ["I.13", "I.cn.3"], ":g:`< D E G ) <g1:< D E G )>` + :g:`< D E F ) <g1:< D E F )>` = 2 right angles and :g:`< A K B ) <g1:< A K B )>` :eq:`= <g1:< A K B ) = g1:< D E G )>` :g:`< D E G ) <g1:< D E G )>` → :g:`< A M B ) <g1:< A M B )>` :eq:`= <g1:< A M B ) = g1:< D E F )>` :g:`< D E F ) <g1:< D E F )>`; similarly :g:`< L N B ) <g1:< L N B )>` :eq:`= <g1:< L N B ) = g1:< D F E )>` :g:`< D F E ) <g1:< D F E )>`"),
            ("conclude", ["I.32", "IV.def.4"], "Remaining :g:`< M L N ) <g1:< M L N )>` :eq:`= <g1:< M L N ) = g1:< E D F )>` :g:`< E D F ) <g1:< E D F )>` → :g:`< L M N > <g1:< L M N >>` is circumscribed about :g:`( A B C ) <g1:( A B C )>` equiangular with :g:`< D E F > <g1:< D E F >>`"),
        ],
    },
    "IV.4": {
        "subtype": "problem",
        "args": [":g:`< A B C > <g1:< A B C >>`"],
        "returns": [":g:`( E F G ) <g1:( E F G )>`"],
        "given": ":g:`< A B C > <g1:< A B C >>`",
        "contract": ":g:`( E F G ) <g1:( E F G )>` is :term:`inscribed in <G.153>` :g:`< A B C > <g1:< A B C >>`",
        "steps": [
            ("given", ["I.def.15", "I.def.19", "IV.def.5"], ":g:`< A B C > <g1:< A B C >>`"),
            ("construct", ["I.9"], "@fn(I.9)(:g:`< A B C ) <g1:< A B C )>`, :g:`< A C B ) <g1:< A C B )>`) → bisectors :g:`/ B D / <g1:/ B D />`, :g:`/ C D / <g1:/ C D />` meeting at :g:`D <g1:D>`"),
            ("construct", ["I.12", "I.def.10"], "@fn(I.12)(:g:`D <g1:D>`, :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C A / <g1:/ C A />`) → :g:`/ D E / <g1:/ D E />` ⊥ :g:`/ A B / <g1:/ A B />`, :g:`/ D F / <g1:/ D F />` ⊥ :g:`/ B C / <g1:/ B C />`, :g:`/ D G / <g1:/ D G />` ⊥ :g:`/ C A / <g1:/ C A />`"),
            ("assert", ["I.26", "I.cn.1"], "In :g:`< E B D > <g1:< E B D >>`, :g:`< F B D > <g1:< F B D >>`: :g:`< A B D ) <g1:< A B D )>` :eq:`= <g1:< A B D ) = g1:< C B D )>` :g:`< C B D ) <g1:< C B D )>`, right :g:`< B E D ) <g1:< B E D )>` :eq:`= <g1:< B E D ) = g1:< B F D )>` :g:`< B F D ) <g1:< B F D )>`, :g:`/ B D / <g1:/ B D />` common → :g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ D E / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`; similarly :g:`/ D G / <g1:/ D G />` :eq:`= <g1:/ D G / = g1:/ D F />` :g:`/ D F / <g1:/ D F />`, so :g:`/ D E / <g1:/ D E />` :eq:`= <g1:/ D E / = g1:/ D F / = g1:/ D G />` :g:`/ D F / <g1:/ D F />` :eq:`= <g1:/ D E / = g1:/ D F / = g1:/ D G />` :g:`/ D G / <g1:/ D G />`"),
            ("assert", ["III.16"], "Angles at :g:`E <g1:E>`, :g:`F <g1:F>`, :g:`G <g1:G>` are right → circle with center :g:`D <g1:D>` and radius :g:`/ D E / <g1:/ D E />` passes through :g:`E <g1:E>`, :g:`F <g1:F>`, :g:`G <g1:G>` and touches :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C A / <g1:/ C A />` without cutting them"),
            ("conclude", ["I.post.3", "IV.def.5"], "@fn(I.post.3)(:g:`D <g1:D>`, :g:`E <g1:E>`) → :g:`( E F G ) <g1:( E F G )>` is inscribed in :g:`< A B C > <g1:< A B C >>`"),
        ],
    },
    "IV.5": {
        "subtype": "problem",
        "args": [":g:`< A B C > <g1:< A B C >>`"],
        "returns": [":g:`( A B C ) <g1:( A B C )>`"],
        "given": ":g:`< A B C > <g1:< A B C >>`",
        "contract": ":g:`( A B C ) <g1:( A B C )>` is :term:`circumscribed about <G.156>` :g:`< A B C > <g1:< A B C >>`",
        "steps": [
            ("given", ["I.def.19", "IV.def.6"], ":g:`< A B C > <g1:< A B C >>`"),
            ("construct", ["I.10", "I.11"], "@fn(I.10)(:g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />`) → :g:`D <g1:D>` (:g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`), :g:`E <g1:E>` (:g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E C />` :g:`/ E C / <g1:/ E C />`); @fn(I.11)(:g:`D <g1:D>`, :g:`E <g1:E>`) → :g:`/ D F / <g1:/ D F />` ⊥ :g:`/ A B / <g1:/ A B />`, :g:`/ E F / <g1:/ E F />` ⊥ :g:`/ A C / <g1:/ A C />` meeting at :g:`F <g1:F>`"),
            ("construct", ["I.post.1"], "Whether :g:`F <g1:F>` falls within :g:`< A B C > <g1:< A B C >>`, on :g:`/ B C / <g1:/ B C />`, or outside :g:`/ B C / <g1:/ B C />`, @fn(I.post.1)(:g:`F <g1:F>`, :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`) → :g:`/ F A / <g1:/ F A />`, :g:`/ F B / <g1:/ F B />`, :g:`/ F C / <g1:/ F C />`"),
            ("assert", ["I.def.10", "I.4", "I.cn.1"], ":g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ D B />` :g:`/ D B / <g1:/ D B />`, :g:`/ D F / <g1:/ D F />` common ⊥ :g:`/ A B / <g1:/ A B />` → :g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`; similarly :g:`/ C F / <g1:/ C F />` :eq:`= <g1:/ C F / = g1:/ A F />` :g:`/ A F / <g1:/ A F />` → :g:`/ F A / <g1:/ F A />` :eq:`= <g1:/ F A / = g1:/ F B / = g1:/ F C />` :g:`/ F B / <g1:/ F B />` :eq:`= <g1:/ F A / = g1:/ F B / = g1:/ F C />` :g:`/ F C / <g1:/ F C />`"),
            ("construct", ["I.post.3", "I.def.15", "IV.def.6"], "@fn(I.post.3)(:g:`F <g1:F>`, :g:`A <g1:A>`) → :g:`( A B C ) <g1:( A B C )>` passing through :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`"),
            ("conclude", ["III.31", "IV.def.6"], ":g:`( A B C ) <g1:( A B C )>` is circumscribed about :g:`< A B C > <g1:< A B C >>` (:g:`F <g1:F>` inside ⇒ :g:`< B A C ) <g1:< B A C )>` acute; :g:`F <g1:F>` on :g:`/ B C / <g1:/ B C />` ⇒ right; :g:`F <g1:F>` outside ⇒ obtuse)"),
        ],
    },
    "IV.6": {
        "subtype": "problem",
        "args": [":g:`( A B C D ) <g1:( A B C D )>`"],
        "returns": [":g:`< A B C D > <g1:< A B C D >>`"],
        "given": ":g:`( A B C D ) <g1:( A B C D )>`",
        "contract": ":g:`< A B C D > <g1:< A B C D >>` is a :term:`square <G.63>` :term:`inscribed in <G.148>` :g:`( A B C D ) <g1:( A B C D )>`",
        "steps": [
            ("given", ["I.def.15", "IV.def.3"], ":g:`( A B C D ) <g1:( A B C D )>`"),
            ("construct", ["III.1", "I.11"], "Draw two diameters :g:`/ A C / <g1:/ A C />` and :g:`/ B D / <g1:/ B D />` of :g:`( A B C D ) <g1:( A B C D )>` at right angles to one another through center :g:`E <g1:E>` (:g:`/ A C / <g1:/ A C />` ⊥ :g:`/ B D / <g1:/ B D />`)"),
            ("construct", ["I.post.1"], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`) → :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D A / <g1:/ D A />`"),
            ("assert", ["I.def.15", "I.def.10", "I.4"], ":g:`/ B E / <g1:/ B E />` :eq:`= <g1:/ B E / = g1:/ E D />` :g:`/ E D / <g1:/ E D />` (center :g:`E <g1:E>`), :g:`/ E A / <g1:/ E A />` common ⊥ :g:`/ B D / <g1:/ B D />` → :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ D A />` :g:`/ D A / <g1:/ D A />`; similarly :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D A />` :g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D A />` :g:`/ C D / <g1:/ C D />` :eq:`= <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D A />` :g:`/ D A / <g1:/ D A />` (equilateral)"),
            ("assert", ["I.def.17", "I.def.18", "III.31"], ":g:`/ B D / <g1:/ B D />` is a diameter → :g:`( B A D ) <g1:( B A D )>` is a semicircle → :g:`< B A D ) <g1:< B A D )>` is right; similarly :g:`< A B C ) <g1:< A B C )>`, :g:`< B C D ) <g1:< B C D )>`, :g:`< C D A ) <g1:< C D A )>` are :eq:`right <g1:< B A D ) = g1:< A B C ) = g1:< B C D ) = g1:< C D A )>` (right-angled)"),
            ("conclude", ["I.def.22", "IV.def.3"], ":g:`< A B C D > <g1:< A B C D >>` is both equilateral and right-angled → square :g:`< A B C D > <g1:< A B C D >>` is inscribed in :g:`( A B C D ) <g1:( A B C D )>`"),
        ],
    },
    "IV.7": {
        "subtype": "problem",
        "args": [":g:`( A B C D ) <g1:( A B C D )>`"],
        "returns": [":g:`< F G H K > <g1:< F G H K >>`"],
        "given": ":g:`( A B C D ) <g1:( A B C D )>`",
        "contract": ":g:`< F G H K > <g1:< F G H K >>` is a :term:`square <G.63>` :term:`circumscribed about <G.150>` :g:`( A B C D ) <g1:( A B C D )>`",
        "steps": [
            ("given", ["I.def.15", "IV.def.4"], ":g:`( A B C D ) <g1:( A B C D )>`"),
            ("construct", ["I.11", "III.16"], "Draw diameters :g:`/ A C / <g1:/ A C />` ⊥ :g:`/ B D / <g1:/ B D />` through center :g:`E <g1:E>`; through :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` draw tangents :g:`/ F G / <g1:/ F G />`, :g:`/ G H / <g1:/ G H />`, :g:`/ H K / <g1:/ H K />`, :g:`/ K F / <g1:/ K F />` touching :g:`( A B C D ) <g1:( A B C D )>`"),
            ("assert", ["III.18", "I.28", "I.30"], "Angles at :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` are right (:g:`< A E B ) <g1:< A E B )>` :eq:`= <g1:< A E B ) = g1:< E B G )>` :g:`< E B G ) <g1:< E B G )>`) → :g:`/ G H / <g1:/ G H />` ∥ :g:`/ A C / <g1:/ A C />` ∥ :g:`/ K F / <g1:/ K F />` and :g:`/ F G / <g1:/ F G />` ∥ :g:`/ B D / <g1:/ B D />` ∥ :g:`/ H K / <g1:/ H K />`"),
            ("assert", ["I.34", "I.def.15"], ":g:`< G H C A > <g1:< G H C A >>`, :g:`< A C K F > <g1:< A C K F >>`, :g:`< F G B D > <g1:< F G B D >>`, :g:`< B H K D > <g1:< B H K D >>` are parallelograms and :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ B D />` :g:`/ B D / <g1:/ B D />` → :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ F G / = g1:/ G H / = g1:/ H K / = g1:/ K F />` :g:`/ G H / <g1:/ G H />` :eq:`= <g1:/ F G / = g1:/ G H / = g1:/ H K / = g1:/ K F />` :g:`/ H K / <g1:/ H K />` :eq:`= <g1:/ F G / = g1:/ G H / = g1:/ H K / = g1:/ K F />` :g:`/ K F / <g1:/ K F />` (equilateral)"),
            ("assert", ["I.34"], "In parallelogram :g:`< G B E A > <g1:< G B E A >>`, :g:`< A E B ) <g1:< A E B )>` is right → opposite angle :g:`< A G B ) <g1:< A G B )>` is :eq:`right <g1:< A E B ) = g1:< A G B ) = g1:< G H K ) = g1:< H K F ) = g1:< K F G )>`, and similarly :g:`< G H K ) <g1:< G H K )>`, :g:`< H K F ) <g1:< H K F )>`, :g:`< K F G ) <g1:< K F G )>` are right (right-angled)"),
            ("conclude", ["I.def.22", "IV.def.4"], ":g:`< F G H K > <g1:< F G H K >>` is both equilateral and right-angled → square :g:`< F G H K > <g1:< F G H K >>` is circumscribed about :g:`( A B C D ) <g1:( A B C D )>`"),
        ],
    },
    "IV.8": {
        "subtype": "problem",
        "args": [":g:`< A B C D > <g1:< A B C D >>`"],
        "returns": [":g:`( E F H K ) <g1:( E F H K )>`"],
        "given": ":g:`< A B C D > <g1:< A B C D >>`",
        "contract": ":g:`( E F H K ) <g1:( E F H K )>` is :term:`inscribed in <G.153>` the square :g:`< A B C D > <g1:< A B C D >>`",
        "steps": [
            ("given", ["I.def.22", "IV.def.5"], ":g:`< A B C D > <g1:< A B C D >>`"),
            ("construct", ["I.10", "I.31"], "@fn(I.10)(:g:`/ A D / <g1:/ A D />`, :g:`/ A B / <g1:/ A B />`) → :g:`E <g1:E>` (:g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ E D />` :g:`/ E D / <g1:/ E D />`), :g:`F <g1:F>` (:g:`/ A F / <g1:/ A F />` :eq:`= <g1:/ A F / = g1:/ F B />` :g:`/ F B / <g1:/ F B />`); @fn(I.31)(:g:`E <g1:E>`, :g:`F <g1:F>`) → :g:`/ E H / <g1:/ E H />` ∥ :g:`/ A B / <g1:/ A B />`, :g:`/ F K / <g1:/ F K />` ∥ :g:`/ A D / <g1:/ A D />` meeting at :g:`G <g1:G>`"),
            ("assert", ["I.34", "I.def.22"], ":g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ A B />` :g:`/ A B / <g1:/ A B />` → halves :g:`/ A E / <g1:/ A E />` :eq:`= <g1:/ A E / = g1:/ A F />` :g:`/ A F / <g1:/ A F />`; in parallelogram :g:`< A F G E > <g1:< A F G E >>` and its neighbors, opposite sides are equal → :g:`/ G E / <g1:/ G E />` :eq:`= <g1:/ G E / = g1:/ G F / = g1:/ G H / = g1:/ G K />` :g:`/ G F / <g1:/ G F />` :eq:`= <g1:/ G E / = g1:/ G F / = g1:/ G H / = g1:/ G K />` :g:`/ G H / <g1:/ G H />` :eq:`= <g1:/ G E / = g1:/ G F / = g1:/ G H / = g1:/ G K />` :g:`/ G K / <g1:/ G K />`"),
            ("construct", ["I.post.3", "I.def.15"], "@fn(I.post.3)(:g:`G <g1:G>`, :g:`E <g1:E>`) → :g:`( E F H K ) <g1:( E F H K )>` passing through :g:`E <g1:E>`, :g:`F <g1:F>`, :g:`H <g1:H>`, :g:`K <g1:K>`"),
            ("assert", ["III.16"], "Angles at :g:`E <g1:E>`, :g:`F <g1:F>`, :g:`H <g1:H>`, :g:`K <g1:K>` are right → if :g:`( E F H K ) <g1:( E F H K )>` cut any side of :g:`< A B C D > <g1:< A B C D >>`, the perpendicular to the diameter at its extremity would fall inside the circle ⇒⇐"),
            ("conclude", ["III.16", "IV.def.5"], ":g:`( E F H K ) <g1:( E F H K )>` touches :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D A / <g1:/ D A />` → circle :g:`( E F H K ) <g1:( E F H K )>` is inscribed in square :g:`< A B C D > <g1:< A B C D >>`"),
        ],
    },
    "IV.9": {
        "subtype": "problem",
        "args": [":g:`< A B C D > <g1:< A B C D >>`"],
        "returns": [":g:`( A B C D ) <g1:( A B C D )>`"],
        "given": ":g:`< A B C D > <g1:< A B C D >>` is a :term:`square <G.63>`",
        "contract": ":g:`( A B C D ) <g1:( A B C D )>` is :term:`circumscribed about <G.156>` :g:`< A B C D > <g1:< A B C D >>`",
        "steps": [
            ("given", ["I.def.22", "IV.def.6"], ":g:`< A B C D > <g1:< A B C D >>` is the given :term:`square <G.63>`"),
            ("construct", ["I.post.1"], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`C <g1:C>`) → :g:`/ A C / <g1:/ A C />`, @fn(I.post.1)(:g:`B <g1:B>`, :g:`D <g1:D>`) → :g:`/ B D / <g1:/ B D />`, :g:`/ A C / <g1:/ A C />` ∩ :g:`/ B D / <g1:/ B D />` → :g:`E <g1:E>`"),
            ("assert", ["I.def.22", "I.8"], ":g:`/ D A / <g1:/ D A />` :eq:`= <g1:/ D A / = g1:/ A B />` :g:`/ A B / <g1:/ A B />`, :g:`/ A C / <g1:/ A C />` common, :g:`/ D C / <g1:/ D C />` :eq:`= <g1:/ D C / = g1:/ B C />` :g:`/ B C / <g1:/ B C />` → :g:`< D A C ) <g1:< D A C )>` :eq:`= <g1:< D A C ) = g1:< B A C )>` :g:`< B A C ) <g1:< B A C )>`; similarly :g:`/ A C / <g1:/ A C />`, :g:`/ B D / <g1:/ B D />` bisect :g:`< A B C ) <g1:< A B C )>`, :g:`< B C D ) <g1:< B C D )>`, :g:`< C D A ) <g1:< C D A )>`"),
            ("assert", ["I.def.22", "I.6"], ":g:`< D A B ) <g1:< D A B )>` :eq:`= <g1:< D A B ) = g1:< A B C )>` :g:`< A B C ) <g1:< A B C )>` → halves :g:`< E A B ) <g1:< B A C )>` :eq:`= <g1:< B A C ) = g1:< E B A )>` :g:`< E B A ) <g1:< E B A )>` → :g:`/ E A / <g1:/ E A />` :eq:`= <g1:/ E A / = g1:/ E B />` :g:`/ E B / <g1:/ E B />`; similarly :g:`/ E A / <g1:/ E A />` :eq:`= <g1:/ E A / = g1:/ E B / = g1:/ E C / = g1:/ E D />` :g:`/ E B / <g1:/ E B />` = :g:`/ E C / <g1:/ E C />` = :g:`/ E D / <g1:/ E D />`"),
            ("conclude", ["I.post.3", "I.def.15", "IV.def.6"], "@fn(I.post.3)(:g:`E <g1:E>`, :g:`A <g1:A>`) → :g:`( A B C D ) <g1:( A B C D )>` passes through :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>` and is circumscribed about square :g:`< A B C D > <g1:< A B C D >>`"),
        ],
    },
    "IV.10": {
        "subtype": "problem",
        "args": [":g:`/ A B / <g1:/ A B />`"],
        "returns": [":g:`< A B D > <g1:< A B D >>`"],
        "given": ":g:`/ A B / <g1:/ A B />` is any :term:`segment <G.4>`",
        "contract": ":g:`< A B D > <g1:< A B D >>` is an :term:`isosceles triangle <G.13>` (:g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ A D />` :g:`/ A D / <g1:/ A D />`) with :g:`< B D A ) <g1:< B D A )>` :eq:`= <g1:< B D A ) = g1:< C B D )>` :g:`< D B A ) <g1:< C B D )>` = 2 :g:`< D A B ) <g1:< D A C )>`",
        "steps": [
            ("given", ["I.def.20"], "Let any segment :g:`/ A B / <g1:/ A B />` be set out"),
            ("construct", ["II.11", "I.post.3", "IV.1"], "@fn(II.11)(:g:`/ A B / <g1:/ A B />`) → :g:`C <g1:C>` (:g:`< A B , B C >` = :g:`< C A >`), @fn(I.post.3)(:g:`A <g1:A>`, :g:`B <g1:B>`) → :g:`( B D E ) <g1:( B D E )>`, @fn(IV.1)(:g:`( B D E ) <g1:( B D E )>`, :g:`/ A C / <g1:/ A C />`) → :g:`/ B D / <g1:/ B D />` :eq:`= <g1:/ B D / = g1:/ A C />` :g:`/ A C / <g1:/ A C />`"),
            ("construct", ["I.post.1", "IV.5"], "@fn(I.post.1)(:g:`A <g1:A>`, :g:`D <g1:D>`) → :g:`/ A D / <g1:/ A D />`, @fn(I.post.1)(:g:`D <g1:D>`, :g:`C <g1:C>`) → :g:`/ D C / <g1:/ D C />`, @fn(IV.5)(:g:`< A C D > <g1:< A C D >>`) → :g:`( A C D ) <g1:( A C D )>`"),
            ("assert", ["III.37", "III.32"], ":g:`< A B , B C >` = :g:`< A C >` and :g:`/ A C / <g1:/ A C />` :eq:`= <g1:/ A C / = g1:/ B D />` :g:`/ B D / <g1:/ B D />` → :g:`< A B , B C >` = :g:`< B D >` → :g:`/ B D / <g1:/ B D />` touches :g:`( A C D ) <g1:( A C D )>` → :g:`< B D C ) <g1:< B D C )>` :eq:`= <g1:< B D C ) = g1:< D A C )>` :g:`< D A C ) <g1:< D A C )>`"),
            ("assert", ["I.cn.2", "I.32", "I.5"], "Add :g:`< C D A ) <g1:< C D A )>` → :g:`< B D A ) <g1:< B D A )>` = :g:`< C D A ) <g1:< C D A )>` + :g:`< D A C ) <g1:< D A C )>` = :g:`< B C D ) <g1:< B C D )>`; since :g:`/ A D / <g1:/ A D />` :eq:`= <g1:/ A D / = g1:/ A B />` :g:`/ A B / <g1:/ A B />`, :g:`< B D A ) <g1:< B D A )>` :eq:`= <g1:< B D A ) = g1:< C B D ) = g1:< B C D )>` :g:`< D B A ) <g1:< C B D )>` = :g:`< B C D ) <g1:< B C D )>`"),
            ("assert", ["I.6", "I.5", "I.32"], ":g:`< D B C ) <g1:< C B D )>` :eq:`= <g1:< C B D ) = g1:< B C D )>` :g:`< B C D ) <g1:< B C D )>` → :g:`/ B D / <g1:/ B D />` :eq:`= <g1:/ B D / = g1:/ C D / = g1:/ A C />` :g:`/ D C / <g1:/ C D />` = :g:`/ C A / <g1:/ A C />` → :g:`< C D A ) <g1:< C D A )>` :eq:`= <g1:< C D A ) = g1:< D A C )>` :g:`< D A C ) <g1:< D A C )>` → :g:`< B C D ) <g1:< B C D )>` = 2 :g:`< D A C ) <g1:< D A C )>`"),
            ("conclude", ["I.def.20"], "In isosceles triangle :g:`< A B D > <g1:< A B D >>` (:g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ A D />` :g:`/ A D / <g1:/ A D />`), each base angle :g:`< B D A ) <g1:< B D A )>` :eq:`= <g1:< B D A ) = g1:< C B D )>` :g:`< D B A ) <g1:< C B D )>` is double vertex angle :g:`< D A B ) <g1:< D A C )>`"),
        ],
    },
    "IV.11": {
        "subtype": "problem",
        "args": [":g:`( A B C D E ) <g1:( A B C D E )>`"],
        "returns": [":g:`< A B C D E > <g1:< A B C D E >>`"],
        "given": ":g:`( A B C D E ) <g1:( A B C D E )>` is a given :term:`circle <G.10>`",
        "contract": ":g:`< A B C D E > <g1:< A B C D E >>` is an :term:`equilateral <G.13>` and equiangular pentagon :term:`inscribed in <G.148>` :g:`( A B C D E ) <g1:( A B C D E )>`",
        "steps": [
            ("given", ["I.def.15", "IV.def.3"], ":g:`( A B C D E ) <g1:( A B C D E )>` is the given circle"),
            ("construct", ["IV.10", "IV.2"], "@fn(IV.10)() → :g:`< F G H > <g1:< F G H >>` (:g:`< F G H ) <g1:< F G H )>` :eq:`= <g1:< F G H ) = g1:< F H G )>` :g:`< F H G ) <g1:< F H G )>` = 2 :g:`< G F H ) <g1:< G F H )>`), @fn(IV.2)(:g:`( A B C D E ) <g1:( A B C D E )>`, :g:`< F G H > <g1:< F G H >>`) → :g:`< A C D > <g1:< A C D >>` (:g:`< A C D ) <g1:< A C D )>` :eq:`= <g1:< A C D ) = g1:< C D A )>` :g:`< C D A ) <g1:< C D A )>` = 2 :g:`< C A D ) <g1:< C A D )>`)"),
            ("construct", ["I.9", "I.post.1"], "@fn(I.9)(:g:`< A C D ) <g1:< A C D )>`) → :g:`/ C E / <g1:/ C E />`, @fn(I.9)(:g:`< C D A ) <g1:< C D A )>`) → :g:`/ D B / <g1:/ D B />`, @fn(I.post.1)(:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>`) → :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E A / <g1:/ E A />`"),
            ("assert", ["III.26", "III.29"], ":g:`< C A D ) <g1:< C A D )>` :eq:`= <g1:< C A D ) = g1:< A C E ) = g1:< E C D ) = g1:< C D B ) = g1:< B D A )>` :g:`< A C E ) <g1:< A C E )>` = :g:`< E C D ) <g1:< E C D )>` = :g:`< C D B ) <g1:< C D B )>` = :g:`< B D A ) <g1:< B D A )>` → arcs :g:`( A B ) <g1:( A B )>` :eq:`= <g1:( A B ) = g1:( B C ) = g1:( C D ) = g1:( D E ) = g1:( E A )>` :g:`( B C ) <g1:( B C )>` = :g:`( C D ) <g1:( C D )>` = :g:`( D E ) <g1:( D E )>` = :g:`( E A ) <g1:( E A )>` → sides :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D E / = g1:/ E A />` :g:`/ B C / <g1:/ B C />` = :g:`/ C D / <g1:/ C D />` = :g:`/ D E / <g1:/ D E />` = :g:`/ E A / <g1:/ E A />`"),
            ("assert", ["I.cn.2", "III.27"], ":g:`( A B ) <g1:( A B )>` :eq:`= <g1:( A B ) = g1:( D E )>` :g:`( D E ) <g1:( D E )>` + :g:`( B C D ) <g1:( B C D )>` → :g:`( A B C D ) <g1:( A B C D )>` :eq:`= <g1:( A B C D ) = g1:( E D C B )>` :g:`( E D C B ) <g1:( E D C B )>` → :g:`< A E D ) <g1:< A E D )>` :eq:`= <g1:< B A E ) = g1:< A B C ) = g1:< B C D ) = g1:< C D E ) = g1:< A E D )>` :g:`< B A E ) <g1:< B A E )>` = :g:`< A B C ) <g1:< A B C )>` = :g:`< B C D ) <g1:< B C D )>` = :g:`< C D E ) <g1:< C D E )>`"),
            ("conclude", ["IV.def.3"], ":g:`< A B C D E > <g1:< A B C D E >>` is an equilateral and equiangular pentagon inscribed in :g:`( A B C D E ) <g1:( A B C D E )>`"),
        ],
    },
    "IV.12": {
        "subtype": "problem",
        "args": [":g:`( A B C D E ) <g1:( A B C D E )>`"],
        "returns": [":g:`< G H K L M > <g1:< G H K L M >>`"],
        "given": ":g:`( A B C D E ) <g1:( A B C D E )>` is a given :term:`circle <G.10>`",
        "contract": ":g:`< G H K L M > <g1:< G H K L M >>` is an :term:`equilateral <G.13>` and equiangular pentagon :term:`circumscribed about <G.150>` :g:`( A B C D E ) <g1:( A B C D E )>`",
        "steps": [
            ("given", ["I.def.15", "IV.def.4"], ":g:`( A B C D E ) <g1:( A B C D E )>` is the given circle"),
            ("construct", ["IV.11", "III.16"], "@fn(IV.11)(:g:`( A B C D E ) <g1:( A B C D E )>`) → vertices :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>` with equal arcs :g:`( A B ) <g1:( A B )>` :eq:`= <g1:( A B ) = g1:( B C ) = g1:( C D ) = g1:( D E ) = g1:( E A )>` :g:`( B C ) <g1:( B C )>` = :g:`( C D ) <g1:( C D )>` = :g:`( D E ) <g1:( D E )>` = :g:`( E A ) <g1:( E A )>`, @fn(III.16)(:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>`) → tangents :g:`/ G H / <g1:/ G H />`, :g:`/ H K / <g1:/ H K />`, :g:`/ K L / <g1:/ K L />`, :g:`/ L M / <g1:/ L M />`, :g:`/ M G / <g1:/ M G />`"),
            ("construct", ["III.1", "I.post.1"], "@fn(III.1)(:g:`( A B C D E ) <g1:( A B C D E )>`) → center :g:`F <g1:F>`, @fn(I.post.1)(:g:`F <g1:F>`, :g:`B <g1:B>`, :g:`K <g1:K>`, :g:`C <g1:C>`, :g:`L <g1:L>`, :g:`D <g1:D>`) → :g:`/ F B / <g1:/ F B />`, :g:`/ F K / <g1:/ F K />`, :g:`/ F C / <g1:/ F C />`, :g:`/ F L / <g1:/ F L />`, :g:`/ F D / <g1:/ F D />`"),
            ("assert", ["III.18", "I.47", "I.8"], ":g:`/ F B / <g1:/ F B />` ⊥ :g:`/ H K / <g1:/ H K />`, :g:`/ F C / <g1:/ F C />` ⊥ :g:`/ K L / <g1:/ K L />`, :g:`/ F D / <g1:/ F D />` ⊥ :g:`/ L M / <g1:/ L M />` → :g:`< F C >` + :g:`< C K >` = :g:`< F K >` = :g:`< F B >` + :g:`< B K >` → :g:`/ B K / <g1:/ B K />` :eq:`= <g1:/ B K / = g1:/ K C />` :g:`/ C K / <g1:/ K C />` → :g:`< B F K ) <g1:< B F K )>` :eq:`= <g1:< B F K ) = g1:< K F C )>` :g:`< K F C ) <g1:< K F C )>` and :g:`< B K F ) <g1:< B K F )>` :eq:`= <g1:< B K F ) = g1:< F K C )>` :g:`< F K C ) <g1:< F K C )>`"),
            ("assert", ["III.27", "I.26"], ":g:`( B C ) <g1:( B C )>` :eq:`= <g1:( B C ) = g1:( C D )>` :g:`( C D ) <g1:( C D )>` → :g:`< B F C ) <g1:< B F C )>` :eq:`= <g1:< B F C ) = g1:< C F D )>` :g:`< C F D ) <g1:< C F D )>` → halves :g:`< K F C ) <g1:< K F C )>` :eq:`= <g1:< K F C ) = g1:< C F L )>` :g:`< L F C ) <g1:< C F L )>`, with :g:`< F C K ) <g1:< F C K )>` :eq:`= <g1:< F C K ) = g1:< F C L )>` :g:`< F C L ) <g1:< F C L )>` and :g:`/ F C / <g1:/ F C />` common → :g:`/ K C / <g1:/ K C />` :eq:`= <g1:/ K C / = g1:/ C L />` :g:`/ C L / <g1:/ C L />` and :g:`< F K C ) <g1:< F K C )>` :eq:`= <g1:< F K C ) = g1:< F L C )>` :g:`< F L C ) <g1:< F L C )>`"),
            ("assert", ["I.cn.1"], ":g:`/ K L / <g1:/ K L />` = 2 :g:`/ K C / <g1:/ K C />` = 2 :g:`/ B K / <g1:/ B K />` = :g:`/ H K / <g1:/ H K />` → :g:`/ G H / <g1:/ G H />` :eq:`= <g1:/ G H / = g1:/ H K / = g1:/ K L / = g1:/ L M / = g1:/ M G />` :g:`/ H K / <g1:/ H K />` = :g:`/ K L / <g1:/ K L />` = :g:`/ L M / <g1:/ L M />` = :g:`/ M G / <g1:/ M G />`, and doubles :g:`< G H K ) <g1:< K H G )>` :eq:`= <g1:< K H G ) = g1:< B K C ) = g1:< D L C ) = g1:< G M L ) = g1:< H G M )>` :g:`< H K L ) <g1:< B K C )>` = :g:`< K L M ) <g1:< D L C )>` = :g:`< L M G ) <g1:< G M L )>` = :g:`< M G H ) <g1:< H G M )>`"),
            ("conclude", ["IV.def.4"], ":g:`< G H K L M > <g1:< G H K L M >>` is an equilateral and equiangular pentagon circumscribed about :g:`( A B C D E ) <g1:( A B C D E )>`"),
        ],
    },
    "IV.13": {
        "subtype": "problem",
        "args": [":g:`< A B C D E > <g1:< A B C D E >>`"],
        "returns": [":g:`( G H K L M ) <g1:( G H K L M )>`"],
        "given": "Equilateral and equiangular pentagon :g:`< A B C D E > <g1:< A B C D E >>`",
        "contract": "Circle :g:`( G H K L M ) <g1:( G H K L M )>` is :term:`inscribed in <G.153>` regular pentagon :g:`< A B C D E > <g1:< A B C D E >>`",
        "steps": [
            ("given", ["I.def.20", "IV.def.5"], "Equilateral and equiangular pentagon :g:`< A B C D E > <g1:< A B C D E >>`"),
            ("construct", ["I.9", "I.post.1"], "@fn(I.9)(:g:`< B C D ) <g1:< B C D )>`, :g:`< C D E ) <g1:< C D E )>`) → :g:`/ F C / <g1:/ F C />`, :g:`/ F D / <g1:/ F D />` meeting at :g:`F <g1:F>`; @fn(I.post.1)(:g:`F <g1:F>`, :g:`B <g1:B>`, :g:`A <g1:A>`, :g:`E <g1:E>`) → :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />`"),
            ("construct", ["I.12"], "@fn(I.12)(:g:`F <g1:F>`, :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E A / <g1:/ E A />`) → perpendiculars :g:`/ F G / <g1:/ F G />`, :g:`/ F H / <g1:/ F H />`, :g:`/ F K / <g1:/ F K />`, :g:`/ F L / <g1:/ F L />`, :g:`/ F M / <g1:/ F M />`"),
            ("assert", ["I.4"], ":g:`/ B C / <g1:/ B C />` :eq:`= <g1:/ B C / = g1:/ C D />` :g:`/ C D / <g1:/ C D />`, :g:`/ F C / <g1:/ F C />` common, :g:`< B C F ) <g1:< B C F )>` :eq:`= <g1:< B C F ) = g1:< D C F )>` :g:`< D C F ) <g1:< D C F )>` → :g:`< C B F ) <g1:< C B F )>` :eq:`= <g1:< C B F ) = g1:< C D F )>` :g:`< C D F ) <g1:< C D F )>` → :g:`< A B F ) <g1:< A B F )>` :eq:`= <g1:< A B F ) = g1:< C B F )>` :g:`< C B F ) <g1:< C B F )>`, and :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />` bisect :g:`< A B C ) <g1:< A B C )>`, :g:`< B A E ) <g1:< B A E )>`, :g:`< A E D ) <g1:< A E D )>`"),
            ("assert", ["I.def.10", "I.26"], "In :g:`< F H C > <g1:< F H C >>`, :g:`< F K C > <g1:< F K C >>`: :g:`< B C F ) <g1:< B C F )>` :eq:`= <g1:< B C F ) = g1:< D C F )>` :g:`< D C F ) <g1:< D C F )>`, right angles :g:`< F H C ) <g1:< F H C )>` :eq:`= <g1:< F H C ) = g1:< F K C )>` :g:`< F K C ) <g1:< F K C )>`, :g:`/ F C / <g1:/ F C />` common → :g:`/ F G / <g1:/ F G />` :eq:`= <g1:/ F G / = g1:/ F H / = g1:/ F K / = g1:/ F L / = g1:/ F M />` :g:`/ F H / <g1:/ F H />` = :g:`/ F K / <g1:/ F K />` = :g:`/ F L / <g1:/ F L />` = :g:`/ F M / <g1:/ F M />`"),
            ("conclude", ["I.post.3", "I.def.15", "III.16", "IV.def.5"], "@fn(I.post.3)(:g:`F <g1:F>`, :g:`G <g1:G>`) → :g:`( G H K L M ) <g1:( G H K L M )>` passes through :g:`G <g1:G>`, :g:`H <g1:H>`, :g:`K <g1:K>`, :g:`L <g1:L>`, :g:`M <g1:M>` and touches all five sides → :g:`( G H K L M ) <g1:( G H K L M )>` is inscribed in :g:`< A B C D E > <g1:< A B C D E >>`"),
        ],
    },
    "IV.14": {
        "subtype": "problem",
        "args": [":g:`< A B C D E > <g1:< A B C D E >>`"],
        "returns": [":g:`( A B C D E ) <g1:( A B C D E )>`"],
        "given": "Equilateral and equiangular pentagon :g:`< A B C D E > <g1:< A B C D E >>`",
        "contract": "Circle :g:`( A B C D E ) <g1:( A B C D E )>` is :term:`circumscribed about <G.156>` regular pentagon :g:`< A B C D E > <g1:< A B C D E >>`",
        "steps": [
            ("given", ["I.def.20", "IV.def.6"], "Equilateral and equiangular pentagon :g:`< A B C D E > <g1:< A B C D E >>`"),
            ("construct", ["I.9", "I.post.1"], "@fn(I.9)(:g:`< B C D ) <g1:< B C D )>`, :g:`< C D E ) <g1:< C D E )>`) → :g:`/ F C / <g1:/ F C />`, :g:`/ F D / <g1:/ F D />` meeting at :g:`F <g1:F>`; @fn(I.post.1)(:g:`F <g1:F>`, :g:`B <g1:B>`, :g:`A <g1:A>`, :g:`E <g1:E>`) → :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />`"),
            ("assert", ["IV.13"], "As in IV.13, :g:`/ F B / <g1:/ F B />`, :g:`/ F A / <g1:/ F A />`, :g:`/ F E / <g1:/ F E />` bisect :g:`< C B A ) <g1:< C B A )>`, :g:`< B A E ) <g1:< B A E )>`, :g:`< A E D ) <g1:< A E D )>`; and since :g:`< B C D ) <g1:< B C D )>` :eq:`= <g1:< B C D ) = g1:< C D E )>` :g:`< C D E ) <g1:< C D E )>`, their halves :g:`< F C D ) <g1:< F C D )>` :eq:`= <g1:< F C D ) = g1:< C D F )>` :g:`< C D F ) <g1:< C D F )>`"),
            ("assert", ["I.6"], "In :g:`< F C D > <g1:< F C D >>`, :g:`< F C D ) <g1:< F C D )>` :eq:`= <g1:< F C D ) = g1:< C D F )>` :g:`< C D F ) <g1:< C D F )>` → :g:`/ F C / <g1:/ F C />` :eq:`= <g1:/ F C / = g1:/ F D />` :g:`/ F D / <g1:/ F D />`; similarly :g:`/ F A / <g1:/ F A />` :eq:`= <g1:/ F A / = g1:/ F B / = g1:/ F C / = g1:/ F D / = g1:/ F E />` :g:`/ F B / <g1:/ F B />` = :g:`/ F C / <g1:/ F C />` = :g:`/ F D / <g1:/ F D />` = :g:`/ F E / <g1:/ F E />`"),
            ("conclude", ["I.post.3", "I.def.15", "I.def.16", "IV.def.6"], "@fn(I.post.3)(:g:`F <g1:F>`, :g:`A <g1:A>`) → :g:`( A B C D E ) <g1:( A B C D E )>` passes through :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`D <g1:D>`, :g:`E <g1:E>` → :g:`( A B C D E ) <g1:( A B C D E )>` is circumscribed about :g:`< A B C D E > <g1:< A B C D E >>`"),
        ],
    },
    "IV.15": {
        "subtype": "problem",
        "args": [":g:`( A B C D E F ) <g1:( A B C D E F )>`"],
        "returns": [":g:`< A B C D E F > <g1:< A B C D E F >>`"],
        "given": "Circle :g:`( A B C D E F ) <g1:( A B C D E F )>`",
        "contract": "Hexagon :g:`< A B C D E F > <g1:< A B C D E F >>` is :term:`equilateral <G.13>`, equiangular, and :term:`inscribed in <G.148>` :g:`( A B C D E F ) <g1:( A B C D E F )>`",
        "steps": [
            ("given", ["I.def.15", "IV.def.3"], "Circle :g:`( A B C D E F ) <g1:( A B C D E F )>`"),
            ("construct", ["I.def.17", "III.1", "I.post.3"], "Draw diameter :g:`/ A D / <g1:/ A D />`, @fn(III.1)(:g:`( A B C D E F ) <g1:( A B C D E F )>`) → center :g:`G <g1:G>`, @fn(I.post.3)(:g:`D <g1:D>`, :g:`G <g1:G>`) → :g:`( E G C H ) <g1:( E G C H )>`"),
            ("construct", ["I.post.1", "I.post.2"], "Join :g:`/ G E / <g1:/ G E />`, :g:`/ G C / <g1:/ G C />` and produce to :g:`B <g1:B>`, :g:`F <g1:F>` (:g:`/ B E / <g1:/ B E />`, :g:`/ C F / <g1:/ C F />`); join :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`, :g:`/ C D / <g1:/ C D />`, :g:`/ D E / <g1:/ D E />`, :g:`/ E F / <g1:/ E F />`, :g:`/ F A / <g1:/ F A />`"),
            ("assert", ["I.def.15", "I.def.20", "I.5", "I.32", "I.13", "I.15"], "Radii :g:`/ G E / <g1:/ G E />` :eq:`= <g1:/ G E / = g1:/ G D / = g1:/ D E />` :g:`/ G D / <g1:/ G D />` = :g:`/ D E / <g1:/ D E />` → :g:`< E G D > <g1:< E G D >>`, :g:`< D G C > <g1:< D G C >>` equilateral → all six central angles :g:`< E G D ) <g1:< E G D )>` :eq:`= <g1:< E G D ) = g1:< D G C ) = g1:< C G B ) = g1:< B G A ) = g1:< A G F ) = g1:< F G E )>` :g:`< D G C ) <g1:< D G C )>` = :g:`< C G B ) <g1:< C G B )>` = :g:`< B G A ) <g1:< B G A )>` = :g:`< A G F ) <g1:< A G F )>` = :g:`< F G E ) <g1:< F G E )>`"),
            ("assert", ["III.26", "III.29"], "Equal central angles subtend equal arcs :g:`( A B ) <g1:( A B )>` :eq:`= <g1:( A B ) = g1:( B C ) = g1:( C D ) = g1:( D E ) = g1:( E F ) = g1:( F A )>` :g:`( B C ) <g1:( B C )>` = :g:`( C D ) <g1:( C D )>` = :g:`( D E ) <g1:( D E )>` = :g:`( E F ) <g1:( E F )>` = :g:`( F A ) <g1:( F A )>` → :g:`/ A B / <g1:/ A B />` :eq:`= <g1:/ A B / = g1:/ B C / = g1:/ C D / = g1:/ D E / = g1:/ E F / = g1:/ F A />` :g:`/ B C / <g1:/ B C />` = :g:`/ C D / <g1:/ C D />` = :g:`/ D E / <g1:/ D E />` = :g:`/ E F / <g1:/ E F />` = :g:`/ F A / <g1:/ F A />` (:g:`< A B C D E F > <g1:< A B C D E F >>` is equilateral)"),
            ("conclude", ["I.cn.2", "III.27", "IV.def.3"], ":g:`( F A B C D ) <g1:( F A B C D )>` :eq:`= <g1:( F A B C D ) = g1:( E D C B A )>` :g:`( E D C B A ) <g1:( E D C B A )>` → :g:`< F E D ) <g1:< F E D )>` :eq:`= <g1:< F E D ) = g1:< A F E )>` :g:`< A F E ) <g1:< A F E )>` and all 6 interior angles equal → :g:`< A B C D E F > <g1:< A B C D E F >>` is an equilateral and equiangular hexagon inscribed in :g:`( A B C D E F ) <g1:( A B C D E F )>` (Porism: side = radius :g:`/ G D / <g1:/ G D />`)"),
        ],
    },
    "IV.16": {
        "subtype": "problem",
        "args": [":g:`( A B C D ) <g1:( A B C D )>`"],
        "returns": [":g:`< A B E C D > <g1:< A B E C D >>`"],
        "given": "Circle :g:`( A B C D ) <g1:( A B C D )>`",
        "contract": "Fifteen-angled figure :g:`< A B E C D > <g1:< A B E C D >>` is :term:`equilateral <G.13>`, equiangular, and :term:`inscribed in <G.148>` :g:`( A B C D ) <g1:( A B C D )>`",
        "steps": [
            ("given", ["I.def.14", "I.def.15", "IV.def.3"], "Circle :g:`( A B C D ) <g1:( A B C D )>`"),
            ("construct", ["IV.2", "IV.11"], "In :g:`( A B C D ) <g1:( A B C D )>` inscribe side :g:`/ A C / <g1:/ A C />` of equilateral triangle :g:`< A C D > <g1:< A C D >>` (@fn(IV.2)) and side :g:`/ A B / <g1:/ A B />` of regular pentagon (@fn(IV.11))"),
            ("construct", ["III.30", "I.post.1"], "@fn(III.30)(:g:`( B C ) <g1:( B C )>`) → :g:`E <g1:E>` (:g:`( B E ) <g1:( B E )>` :eq:`= <g1:( B E ) = g1:( E C )>` :g:`( E C ) <g1:( E C )>`); @fn(I.post.1)(:g:`B <g1:B>`, :g:`E <g1:E>`, :g:`C <g1:C>`) → :g:`/ B E / <g1:/ B E />`, :g:`/ E C / <g1:/ E C />`"),
            ("assert", ["I.cn.3"], "Of 15 equal parts of :g:`( A B C D ) <g1:( A B C D )>`, arc :g:`( A B C ) <g1:( A B C )>` (⅓ of circle) contains 5 and arc :g:`( A B ) <g1:( A B )>` (⅕ of circle) contains 3 → remainder arc :g:`( B C ) <g1:( B C )>` contains 5 − 3 = 2 parts"),
            ("conclude", ["III.29", "IV.1", "IV.def.3", "IV.def.7"], "Bisecting :g:`( B C ) <g1:( B C )>` at :g:`E <g1:E>` makes each of :g:`( B E ) <g1:( B E )>`, :g:`( E C ) <g1:( E C )>` equal to 1/15 of :g:`( A B C D ) <g1:( A B C D )>`; fitting chords equal to :g:`/ B E / <g1:/ B E />`, :g:`/ E C / <g1:/ E C />` continuously around :g:`( A B C D ) <g1:( A B C D )>` inscribes the regular fifteen-angled figure :g:`< A B E C D > <g1:< A B E C D >>`"),
        ],
    },
}


def _render_curated_proposition(
    canonical_ref: str,
    g_name: str,
    sem_name: str,
    id_map: Dict[str, str],
    g_to_sem_name: Dict[str, str],
    enun_block: Optional[str],
    picture_blocks: List[str],
    footer_blocks: List[str],
) -> str:
    """Render a curated symbolic proposition (`signature` + `step` blocks) resolving Euclid IDs via `id_map`."""
    spec = CURATED_PROPOSITIONS[canonical_ref]
    sig_kind = str(spec.get("subtype", "prop"))
    args = list(spec.get("args", []))  # type: ignore[arg-type]
    returns = list(spec.get("returns", []))  # type: ignore[arg-type]
    given_str = str(spec.get("given", ""))
    contract_str = str(spec.get("contract", ""))
    steps_spec = list(spec.get("steps", []))  # type: ignore[arg-type]

    fn_self = f":fn:`{sem_name} <{g_name}>`" if g_name else f"**{sem_name}**"
    args_str = ", ".join(args)
    if sig_kind == "problem" and returns:
        header_line = f"{fn_self}\\ ({args_str}) → {', '.join(returns)}"
    else:
        header_line = f"{fn_self}\\ ({args_str})"

    contract_kw = "construct" if sig_kind == "problem" else "prove"
    sig_lines = [
        f".. signature:: {sig_kind}",
        "",
        f"   | {header_line}",
        f"   | **given** {given_str}",
        f"   | **{contract_kw}** {contract_str}",
    ]
    sig_block = "\n".join(sig_lines)

    def _expand_fn_tokens(s: str) -> str:
        def _repl(m: re.Match[str]) -> str:
            euclid_id = m.group(1).strip()
            g_target = id_map.get(euclid_id, euclid_id)
            fn_name = g_to_sem_name.get(g_target) or SEMANTIC_NAMES.get(euclid_id, euclid_id)
            return _fn_tag(fn_name, g_target)

        return re.sub(r"@fn\(([^)]+)\)", _repl, s)

    header_blocks: List[str] = []
    if enun_block:
        header_blocks.append(enun_block)
    header_blocks.append(sig_block)
    header_blocks.extend(picture_blocks)

    rendered_steps: List[str] = []
    for kind, rule_euclid_ids, body_tmpl in steps_spec:
        g_targets = [id_map.get(eid, eid) for eid in rule_euclid_ids]
        just_str = _format_rule_justification(g_targets, g_to_sem_name) if g_targets else None
        arg_str = f"{kind} {just_str}" if just_str else kind
        body_expanded = _expand_fn_tokens(body_tmpl)
        rendered_steps.append(f".. step:: {arg_str}\n\n   {body_expanded}")

    return "\n\n".join(header_blocks + rendered_steps + footer_blocks)



def generate_pseudocode_rst(
    heath_content_rst: str,
    canonical_ref: str,
    node_type: str,
    g_name: str = "",
    subtype: Optional[str] = None,
    id_map: Optional[Dict[str, str]] = None,
    g_to_sem_name: Optional[Dict[str, str]] = None,
    local_svg_names: Optional[List[str]] = None,
) -> str:
    """Transform a Heath RST body (with G-Index roles/justifications) into Track 1 Pseudocode RST."""
    id_map = id_map or {}
    g_to_sem_name = g_to_sem_name or {}
    local_svg_names = local_svg_names or []

    if node_type in ("def", "post", "cn"):
        m_enun = re.match(
            r"^\.\.\s+enunciation::\n+((?:[ \t]+[^\n]*\n?|\n)*)(.*)",
            heath_content_rst.strip(),
            re.DOTALL,
        )
        if m_enun:
            raw_enun = m_enun.group(1)
            rest = m_enun.group(2).strip()
            tight_enun = tighten_enunciation_text(raw_enun, canonical_ref)
            sem_name = g_to_sem_name.get(g_name) or get_semantic_name(
                canonical_ref, node_type, subtype, tight_enun
            )
            sig_block = _build_signature_block(
                canonical_ref, node_type, subtype, g_name, sem_name, [], [], None, []
            )
            indented = "\n".join(f"   {line}" for line in tight_enun.splitlines())
            out = f".. enunciation::\n\n{indented}\n\n{sig_block}"
            for svg_name in local_svg_names:
                if svg_name not in rest:
                    out += f"\n\n.. picture:: {svg_name}"
            if rest:
                out += f"\n\n{rest}"
            return out
        return heath_content_rst

    # Unwrap :term: roles before pseudocode clause matching; inject_pseudocode_terms re-injects first-use :term: roles afterwards
    clean_prop_rst = re.sub(
        r":term:`([^`<]+?)(?:\s*<[^>]+>)?`",
        lambda m: m.group(1).strip(),
        heath_content_rst,
    )
    lines = clean_prop_rst.strip().splitlines()
    blocks: List[str] = []
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if not line.strip():
            idx += 1
            continue
        if line.startswith(".. "):
            block_lines = [line]
            idx += 1
            while idx < len(lines) and (not lines[idx].strip() or lines[idx].startswith((" ", "\t"))):
                block_lines.append(lines[idx])
                idx += 1
            blocks.append("\n".join(block_lines).rstrip())
        else:
            block_lines = [line]
            idx += 1
            while idx < len(lines) and lines[idx].strip() and not lines[idx].startswith(".. "):
                block_lines.append(lines[idx])
                idx += 1
            blocks.append("\n".join(block_lines).rstrip())

    enun_block: Optional[str] = None
    raw_enun_parts: List[str] = []
    picture_blocks: List[str] = []
    step_items: List[Tuple[str, List[str], str]] = []  # (kind, just_targets, body)
    footer_blocks: List[str] = []
    given_clauses: List[str] = []
    goal_clauses: List[str] = []
    pending_premise: Optional[str] = None
    pending_just_targets: List[str] = []
    last_constructed_seg: Optional[str] = None
    constructed_circles: List[str] = []
    circle_aliases: Dict[frozenset[str], str] = {}
    tight_enun_text = ""

    def _update_last_seg(body_text: str) -> None:
        nonlocal last_constructed_seg
        for m_seg in re.finditer(r":g:`/\s*[A-Za-z0-9_]+\s+[A-Za-z0-9_]+\s*/\s*<[^>]+>`", body_text):
            last_constructed_seg = m_seg.group(0)

    for b in blocks:
        b_strip = b.strip()
        if b_strip.startswith(".. enunciation::"):
            if not step_items and not picture_blocks and not given_clauses and not goal_clauses:
                b_lines = b_strip.splitlines()
                raw_enun = "\n".join(l.strip() for l in b_lines[1:] if l.strip())
                raw_enun_parts.append(raw_enun)
                merged_raw_enun = re.sub(r"(\w)-\s+(\w)", r"\1\2", " ".join(raw_enun_parts))
                tight_enun_text = tighten_enunciation_text(merged_raw_enun, canonical_ref)
                enun_block = f".. enunciation::\n\n   {tight_enun_text}"
            else:
                footer_blocks.append(b_strip)
            continue

        if b_strip.startswith(".. picture::"):
            picture_blocks.append(b_strip)
            continue

        if b_strip.startswith((".. porism::", ".. lemma::", ".. scholium::")):
            footer_blocks.append(b_strip)
            continue

        if b_strip.startswith(".. qed::"):
            continue

        m_dir = re.match(
            r"^\.\.\s+(assertion|subclause|sub-clause)::(?:[ \t]+([^\n]+))?\n+([\s\S]+)$",
            b_strip,
        )
        if m_dir:
            dir_just_raw = (m_dir.group(2) or "").strip() or None
            dir_body = " ".join(l.strip() for l in m_dir.group(3).splitlines() if l.strip())
            dir_body, inline_just_raw = _extract_inline_justifications(dir_body)
            j_targets = (
                _parse_just_targets(dir_just_raw)
                or _parse_just_targets(inline_just_raw)
                or list(pending_just_targets)
            )
            pending_just_targets = []

            # Check if this .. assertion:: block in Heath is actually a construction step (like in G.17 / G.20)
            if not pending_premise:
                rewritten_dir = _rewrite_clause_to_pseudocode(
                    dir_body,
                    is_first_step=(len(step_items) == 0),
                    id_map=id_map,
                    last_constructed_seg=last_constructed_seg,
                    constructed_circles=constructed_circles,
                    circle_aliases=circle_aliases,
                )
                if rewritten_dir and rewritten_dir[0] in ("construct", "intersect", "intersect_and_join", "construct_and_intersect"):
                    r_kind, r_text, used_fn = rewritten_dir
                    r_text = _apply_circle_aliases(r_text, circle_aliases)
                    _update_last_seg(r_text)
                    if r_kind == "intersect_and_join":
                        int_text, join_text = r_text.split("|||", 1)
                        step_items.append(("intersect", [], int_text))
                        step_items.append(("construct", [], join_text))
                    elif r_kind == "construct_and_intersect":
                        c_text, int_text = r_text.split("|||", 1)
                        step_items.append(("construct", [], c_text))
                        step_items.append(("intersect", [], int_text))
                    else:
                        if not used_fn and j_targets and r_kind == "construct":
                            fn_t = j_targets[0]
                            fn_n = g_to_sem_name.get(fn_t, fn_t)
                            r_text = f"{_fn_tag(fn_n, fn_t).rstrip('\\ ')}: {r_text}"
                        step_items.append((r_kind, [], r_text))
                    continue

            if pending_premise:
                prem = pending_premise.rstrip(",; ")
                combined = f"{prem} → {dir_body}"
                pending_premise = None
            else:
                combined = dir_body
            cleaned = _strip_redundant_type_nouns(combined)
            cleaned = _apply_circle_aliases(cleaned, circle_aliases)
            cleaned = re.sub(r"^(?:Now,\s*|Again,\s*|Then,\s*|And\s+|But\s+|For,\s*)", "", cleaned)
            if cleaned and cleaned[0].islower():
                cleaned = cleaned[0].upper() + cleaned[1:]
            if not j_targets and re.search(r"\bis\s+the\s+(?:centre|center)\s+of\b", cleaned, re.IGNORECASE):
                j_targets = [id_map.get("I.def.15", "G.2")]
            step_items.append(("assert", j_targets, cleaned))
            continue

        clauses = _split_clauses_preserving_roles(b_strip)
        for c in clauses:
            c_clean, c_just_raw = _extract_inline_justifications(c)
            c_targets = _parse_just_targets(c_just_raw)
            if c_clean.endswith(",") and re.match(
                r"^(?:Now,\s*|Again,\s*|Then,\s*|For,\s*|Since\b|And\s+since\b)",
                c_clean,
                re.IGNORECASE,
            ):
                pending_premise = _apply_circle_aliases(
                    _strip_redundant_type_nouns(c_clean), circle_aliases
                )
                if c_targets:
                    pending_just_targets = c_targets
                continue

            if re.match(r"^And\s+things\s+which\s+are\s+equal\b", c_clean, re.IGNORECASE) and c_targets:
                pending_just_targets = c_targets
                continue

            rewritten = _rewrite_clause_to_pseudocode(
                c_clean,
                is_first_step=(len(step_items) == 0),
                id_map=id_map,
                last_constructed_seg=last_constructed_seg,
                constructed_circles=constructed_circles,
                circle_aliases=circle_aliases,
            )
            if not rewritten:
                continue

            kind, text, used_fn = rewritten
            text = _apply_circle_aliases(text, circle_aliases)
            if kind == "goal":
                goal_clauses.append(text)
                continue

            j_targets = c_targets or list(pending_just_targets)
            pending_just_targets = []
            if pending_premise:
                text = f"{pending_premise.rstrip(',; ')} → {text}"
                pending_premise = None

            _update_last_seg(text)

            if kind == "given":
                given_clauses.append(text)
                step_items.append(("given", [], text))
            elif kind == "given_and_construct":
                g_text, c_text = text.split("|||", 1)
                given_clauses.append(g_text)
                step_items.append(("given", [], g_text))
                step_items.append(("construct", [], c_text))
                if canonical_ref == "I.7" and not goal_clauses:
                    goal_clauses.append(f"distinct :g:`/ A D / <g1:/ A D />`, :g:`/ D B / <g1:/ D B />` on the same side with :g:`/ C A / <g1:/ C A />` :eq:`equal <g1:/ C A / = g1:/ D A /; g1:/ C B / = g1:/ D B />` to :g:`/ D A / <g1:/ D A />` and :g:`/ C B / <g1:/ C B />` to :g:`/ D B / <g1:/ D B />` cannot exist")
            elif kind == "intersect_and_join":
                int_text, join_text = text.split("|||", 1)
                step_items.append(("intersect", [], int_text))
                step_items.append(("construct", [], join_text))
            elif kind == "construct_and_intersect":
                c_text, int_text = text.split("|||", 1)
                step_items.append(("construct", [], c_text))
                step_items.append(("intersect", [], int_text))
            elif kind == "construct":
                # If a general construct step has a justification target not yet embedded as :fn:, embed it!
                if not used_fn and j_targets and ":fn:`" not in text:
                    fn_t = j_targets[0]
                    fn_n = g_to_sem_name.get(fn_t, fn_t)
                    text = f"{_fn_tag(fn_n, fn_t).rstrip('\\ ')}: {text}"
                step_items.append(("construct", [], text))
            else:
                if not j_targets and used_fn:
                    j_targets = [used_fn]
                elif not j_targets and re.search(r"\bis\s+the\s+(?:centre|center)\s+of\b", text, re.IGNORECASE):
                    j_targets = [id_map.get("I.def.15", "G.2")]
                step_items.append((kind, j_targets, text))

    # Promote final step to `conclude`, or append a `conclude` step from goal_clauses if missing
    conclude_body: Optional[str] = None
    if step_items:
        last_kind, last_targets, last_body = step_items[-1]
        if last_kind == "assert":
            step_items[-1] = ("conclude", last_targets, last_body)
            conclude_body = last_body
        elif last_kind == "conclude":
            conclude_body = last_body
    if not conclude_body and goal_clauses:
        conclude_body = "; ".join(goal_clauses)
        step_items.append(("conclude", [], conclude_body))

    sem_name = g_to_sem_name.get(g_name) or get_semantic_name(
        canonical_ref, node_type, subtype, tight_enun_text
    )
    if canonical_ref in CURATED_PROPOSITIONS:
        return _render_curated_proposition(
            canonical_ref,
            g_name,
            sem_name,
            id_map,
            g_to_sem_name,
            enun_block,
            picture_blocks,
            footer_blocks,
        )

    construct_bodies = [b for k, _, b in step_items if k == "construct"]
    sig_block = _build_signature_block(
        canonical_ref,
        node_type,
        subtype,
        g_name,
        sem_name,
        given_clauses,
        goal_clauses,
        conclude_body,
        construct_bodies,
    )

    header_blocks: List[str] = []
    if enun_block:
        header_blocks.append(enun_block)
    header_blocks.append(sig_block)
    header_blocks.extend(picture_blocks)

    rendered_steps: List[str] = []
    for kind, j_targets, body in step_items:
        just_str = _format_rule_justification(j_targets, g_to_sem_name) if j_targets else None
        arg_str = f"{kind} {just_str}" if just_str else kind
        clean_body = " ".join(l.strip() for l in body.splitlines() if l.strip())
        if kind in ("given", "assert", "conclude"):
            clean_body = _symbolize_step_text(clean_body)
        rendered_steps.append(f".. step:: {arg_str}\n\n   {clean_body}")

    all_parts = header_blocks + rendered_steps + footer_blocks
    return "\n\n".join(all_parts)

