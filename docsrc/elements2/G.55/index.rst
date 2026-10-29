:order: 55
:number: 55
:canonical_id: G.55
:original_id: I.42
:volume: I
:book: I
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry
:category: problem, construction, plane-geometry
:tags: book-i, point, segment, angle, triangle, quadrilateral, parallelogram, equality
:dependencies: G.34, G.44, G.51, G.54
:excerpt: To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.

.. _G.55:
.. _I.42:

G.55
====

.. rubric:: `I.42 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/42/>`_

.. enunciation::

   To construct, in a given rectilineal angle, a parallelogram equal to a given triangle.

Let :g:`< A B C > <0353.g2:< A B C >>` be the given triangle, and :g:`< D ) <0353.g2:< D )>` the given rectilineal angle;

thus it is required to construct in the rectilineal angle :g:`< D ) <0353.g2:< D )>` a parallelogram :eq:`equal <0353.g2:< F E C G > = 0353.g2:< A B C >>` to the triangle :g:`< A B C > <0353.g2:< A B C >>`.

Let :g:`/ B C / <0353.g2:/ B C />` be :eq:`bisected <0353.g2:/ B E / = 0353.g2:/ E C />` at :g:`E <0353.g2:E>`, and let :g:`/ A E / <0353.g2:/ A E />` be joined; on the straight line :g:`/ E C / <0353.g2:/ E C />`, and at the point :g:`E <0353.g2:E>` on it, let the angle :g:`< C E F ) <0353.g2:< C E F )>` be constructed :eq:`equal <0353.g2:< C E F ) = 0353.g2:< D )>` to the angle :g:`< D ) <0353.g2:< D )>`; :just:`[G.34] <G.34>`

through :g:`A <0353.g2:A>` let :g:`/ A G / <0353.g2:/ A G />` be drawn parallel to :g:`/ E C / <0353.g2:/ E C />`, and :just:`[G.44] <G.44>`

through :g:`C <0353.g2:C>` let :g:`/ C G / <0353.g2:/ C G />` be drawn parallel to :g:`/ E F / <0353.g2:/ E F />`.

.. picture:: 0353.g2.svg
   :alt: Folio 0353 Figure 2 - Proposition 42

Then :g:`< F E C G > <0353.g2:< F E C G >>` is a parallelogram.

And, since :g:`/ B E / <0353.g2:/ B E />` is :eq:`equal <0353.g2:/ B E / = 0353.g2:/ E C />` to :g:`/ E C / <0353.g2:/ E C />`, the triangle :g:`< A B E > <0353.g2:< A B E >>` is also :eq:`equal <0353.g2:< A B E > = 0353.g2:< A E C >>` to the triangle :g:`< A E C > <0353.g2:< A E C >>`, for they are on :eq:`equal <0353.g2:/ B E / = 0353.g2:/ E C />` bases :g:`/ B E / <0353.g2:/ B E />`, :g:`/ E C / <0353.g2:/ E C />` and in the same parallels :g:`/ B C / <0353.g2:/ B C />`, :g:`/ A G / <0353.g2:/ A G />`; :just:`[G.51] <G.51>`

.. assertion::

   therefore the triangle :g:`< A B C > <0353.g2:< A B C >>` is double of the triangle :g:`< A E C > <0353.g2:< A E C >>`.

.. subclause:: [G.54] <G.54>

   But the parallelogram :g:`< F E C G > <0353.g2:< F E C G >>` is also double of the triangle :g:`< A E C > <0353.g2:< A E C >>`, for it has the same base with it and is in the same parallels with it;

.. assertion::

   therefore the parallelogram :g:`< F E C G > <0353.g2:< F E C G >>` is :eq:`equal <0353.g2:< F E C G > = 0353.g2:< A B C >>` to the triangle :g:`< A B C > <0353.g2:< A B C >>`.

And it has the angle :g:`< C E F ) <0353.g2:< C E F )>` :eq:`equal <0353.g2:< C E F ) = 0353.g2:< D )>` to the given angle :g:`< D ) <0353.g2:< D )>`.

.. qed::

   Therefore the parallelogram :g:`< F E C G > <0353.g2:< F E C G >>` has been constructed :eq:`equal <0353.g2:< F E C G > = 0353.g2:< A B C >>` to the given triangle :g:`< A B C > <0353.g2:< A B C >>`, in the angle :g:`< C E F ) <0353.g2:< C E F )>` which is :eq:`equal <0353.g2:< C E F ) = 0353.g2:< D )>` to :g:`< D ) <0353.g2:< D )>`. :just:`Q. E. F.`

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
     "G.37" [label="G.37", tooltip="G.37 (I.26)", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23)", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27)", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5)", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29)", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31)", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.46" [label="G.46", tooltip="G.46 (I.33)", fillcolor="#222244", URL="../G.46/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34)", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35)", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.49" [label="G.49", tooltip="G.49 (I.36)", fillcolor="#222244", URL="../G.49/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37)", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.51" [label="G.51", tooltip="G.51 (I.38)", fillcolor="#222244", URL="../G.51/index.html", target="_top"];
     "G.54" [label="G.54", tooltip="G.54 (I.41)", fillcolor="#222244", URL="../G.54/index.html", target="_top"];
     "G.55" [label="G.55", tooltip="G.55 (I.42)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
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
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
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
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
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
     "G.55" -> "G.34";
     "G.47" -> "G.37";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.46" -> "G.39";
     "G.42" -> "G.41";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.50" -> "G.44";
     "G.51" -> "G.44";
     "G.55" -> "G.44";
     "G.49" -> "G.46";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.50" -> "G.47";
     "G.51" -> "G.47";
     "G.54" -> "G.47";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.51" -> "G.49";
     "G.54" -> "G.50";
     "G.55" -> "G.51";
     "G.55" -> "G.54";
   }

Required for
------------

:ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`
