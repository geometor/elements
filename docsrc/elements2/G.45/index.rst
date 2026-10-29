:order: 45
:number: 45
:canonical_id: G.45
:original_id: I.32
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, line, angle, triangle, right-angle, equality
:dependencies: G.22, G.42, G.44
:excerpt: In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to two right angles.

.. _G.45:
.. _I.32:

G.45
====

.. rubric:: `I.32 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/32/>`_

.. enunciation::

   In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to two right angles.

Let :g:`< A B C > <0331.g1:< A B C >>` be a triangle, and let one side of it :g:`[ B D ] <0331.g1:[ B D ]>` be produced to :g:`D <0331.g1:D>`;

I say that the exterior angle :g:`< A C D ) <0331.g1:< A C D )>` is equal to the two interior and opposite angles :g:`< C A B ) <0331.g1:< C A B )>`, :g:`< A B C ) <0331.g1:< A B C )>`, and the three interior angles of the triangle :g:`< A B C ) <0331.g1:< A B C )>`, :g:`< B C A ) <0331.g1:< B C A )>`, :g:`< C A B ) <0331.g1:< C A B )>` are equal to two right angles.

For let :g:`/ C E / <0331.g1:/ C E />` be drawn through the point :g:`C <0331.g1:C>` parallel to the straight line :g:`/ A B / <0331.g1:/ A B />`. :just:`[G.44] <G.44>`

.. picture:: 0331.g1.svg
   :alt: Folio 0331 Figure 1 - Proposition 32

Then, since :g:`/ A B / <0331.g1:/ A B />` is parallel to :g:`/ C E / <0331.g1:/ C E />`, and :g:`/ A C / <0331.g1:/ A C />` has fallen upon them,

.. assertion:: [G.42] <G.42>

   the alternate angles :g:`< B A C ) <0331.g1:< B A C )>`, :g:`< A C E ) <0331.g1:< A C E )>` are :eq:`equal <0331.g1:< B A C ) = 0331.g1:< A C E )>` to one another.

Again, since :g:`/ A B / <0331.g1:/ A B />` is parallel to :g:`/ C E / <0331.g1:/ C E />`, and the straight line :g:`/ B D / <0331.g1:/ B D />` has fallen upon them,

.. assertion:: [G.42] <G.42>

   the exterior angle :g:`< E C D ) <0331.g1:< E C D )>` is :eq:`equal <0331.g1:< E C D ) = 0331.g1:< A B C )>` to the interior and opposite angle :g:`< A B C ) <0331.g1:< A B C )>`.

But the angle :g:`< A C E ) <0331.g1:< A C E )>` was also proved :eq:`equal <0331.g1:< A C E ) = 0331.g1:< B A C )>` to the angle :g:`< B A C ) <0331.g1:< B A C )>`;

.. assertion::

   therefore the whole angle :g:`< A C D ) <0331.g1:< A C D )>` is equal to the two interior and opposite angles :g:`< B A C ) <0331.g1:< B A C )>`, :g:`< A B C ) <0331.g1:< A B C )>`.

Let the angle :g:`< A C B ) <0331.g1:< A C B )>` be added to each;

.. assertion::

   therefore the angles :g:`< A C D ) <0331.g1:< A C D )>`, :g:`< A C B ) <0331.g1:< A C B )>` are equal to the three angles :g:`< A B C ) <0331.g1:< A B C )>`, :g:`< B C A ) <0331.g1:< B C A )>`, :g:`< C A B ) <0331.g1:< C A B )>`.

But the angles :g:`< A C D ) <0331.g1:< A C D )>`, :g:`< A C B ) <0331.g1:< A C B )>` are equal to two right angles; :just:`[G.22] <G.22>`

.. assertion::

   therefore the angles :g:`< A B C ) <0331.g1:< A B C )>`, :g:`< B C A ) <0331.g1:< B C A )>`, :g:`< C A B ) <0331.g1:< C A B )>` are also equal to two right angles.

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
     "G.1" [label="G.1", tooltip="G.1 (I.cn.1)", fillcolor="#442222", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.15)", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.post.1)", fillcolor="#444422", URL="../G.3/index.html", target="_top"];
     "G.4" [label="G.4", tooltip="G.4 (I.post.3)", fillcolor="#444422", URL="../G.4/index.html", target="_top"];
     "G.5" [label="G.5", tooltip="G.5 (I.1)", fillcolor="#222244", URL="../G.5/index.html", target="_top"];
     "G.6" [label="G.6", tooltip="G.6 (I.cn.3)", fillcolor="#442222", URL="../G.6/index.html", target="_top"];
     "G.7" [label="G.7", tooltip="G.7 (I.post.2)", fillcolor="#444422", URL="../G.7/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.2)", fillcolor="#222244", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.3)", fillcolor="#222244", URL="../G.9/index.html", target="_top"];
     "G.10" [label="G.10", tooltip="G.10 (I.cn.4)", fillcolor="#442222", URL="../G.10/index.html", target="_top"];
     "G.11" [label="G.11", tooltip="G.11 (I.4)", fillcolor="#222244", URL="../G.11/index.html", target="_top"];
     "G.12" [label="G.12", tooltip="G.12 (I.5)", fillcolor="#222244", URL="../G.12/index.html", target="_top"];
     "G.14" [label="G.14", tooltip="G.14 (I.7)", fillcolor="#222244", URL="../G.14/index.html", target="_top"];
     "G.15" [label="G.15", tooltip="G.15 (I.8)", fillcolor="#222244", URL="../G.15/index.html", target="_top"];
     "G.16" [label="G.16", tooltip="G.16 (I.9)", fillcolor="#222244", URL="../G.16/index.html", target="_top"];
     "G.17" [label="G.17", tooltip="G.17 (I.10)", fillcolor="#222244", URL="../G.17/index.html", target="_top"];
     "G.18" [label="G.18", tooltip="G.18 (I.def.10)", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.11)", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2)", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13)", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4)", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15)", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.26" [label="G.26", tooltip="G.26 (I.cn.5)", fillcolor="#442222", URL="../G.26/index.html", target="_top"];
     "G.27" [label="G.27", tooltip="G.27 (I.16)", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18)", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19)", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20)", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22)", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23)", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23)", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27)", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5)", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29)", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31)", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.45" [label="G.45", tooltip="G.45 (I.32)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.42" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.45" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.39" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.45" -> "G.42";
     "G.45" -> "G.44";
   }
