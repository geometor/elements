:order: 48
:number: 48
:canonical_id: G.48
:original_id: I.35
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, segment, angle, triangle, quadrilateral, parallel, parallelogram, equality
:dependencies: G.1, G.6, G.11, G.21, G.42, G.47
:excerpt: Parallelograms which are on the same base and in the same parallels are equal to one another.

.. _G.48:
.. _I.35:

G.48
====

.. rubric:: `I.35 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/35/>`_

.. enunciation::

   Parallelograms which are on the same base and in the same parallels are equal to one another.

Let :g:`< A B C D > <0341.g1:< A B C D >>`, :g:`< E B C F > <0341.g1:< E B C F >>` be parallelograms on the same base :g:`/ B C / <0341.g1:/ B C />` and in the same parallels :g:`/ A F / <0341.g1:/ A F />`, :g:`/ B C / <0341.g1:/ B C />`;

I say that :g:`< A B C D > <0341.g1:< A B C D >>` is :eq:`equal <0341.g1:< A B C D > = 0341.g1:< E B C F >>` to the parallelogram :g:`< E B C F > <0341.g1:< E B C F >>`.

For, since :g:`< A B C D > <0341.g1:< A B C D >>` is a parallelogram, :g:`/ A D / <0341.g1:/ A D />` is :eq:`equal <0341.g1:/ A D / = 0341.g1:/ B C />` to :g:`/ B C / <0341.g1:/ B C />`. :just:`[G.47] <G.47>`
For the same reason also :g:`/ E F / <0341.g1:/ E F />` is :eq:`equal <0341.g1:/ E F / = 0341.g1:/ B C />` to :g:`/ B C / <0341.g1:/ B C />`,

.. assertion:: [G.1] <G.1>

   so that :g:`/ A D / <0341.g1:/ A D />` is also :eq:`equal <0341.g1:/ A D / = 0341.g1:/ E F />` to :g:`/ E F / <0341.g1:/ E F />`;

and :g:`/ D E / <0341.g1:/ D E />` is common;

.. assertion:: [G.21] <G.21>

   therefore the whole :g:`/ A E / <0341.g1:/ A E />` is :eq:`equal <0341.g1:/ A E / = 0341.g1:/ D F />` to the whole :g:`/ D F / <0341.g1:/ D F />`.

But :g:`/ A B / <0341.g1:/ A B />` is also :eq:`equal <0341.g1:/ A B / = 0341.g1:/ D C />` to :g:`/ D C / <0341.g1:/ D C />`; :just:`[G.47] <G.47>`

therefore the two sides :g:`/ E A / <0341.g1:/ E A />`, :g:`/ A B / <0341.g1:/ A B />` are :eq:`equal <0341.g1:/ E A / = 0341.g1:/ F D /; 0341.g1:/ A B / = 0341.g1:/ D C />` to the two sides :g:`/ F D / <0341.g1:/ F D />`, :g:`/ D C / <0341.g1:/ D C />` respectively,

.. picture:: 0341.g1.svg
   :alt: Folio 0341 Figure 1 - Proposition 35

and the angle :g:`< F D C ) <0341.g1:< F D C )>` is :eq:`equal <0341.g1:< F D C ) = 0341.g1:< E A B )>` to the angle :g:`< E A B ) <0341.g1:< E A B )>`, the exterior to the interior; :just:`[G.42] <G.42>`

.. subclause::

   therefore the base :g:`/ E B / <0341.g1:/ E B />` is :eq:`equal <0341.g1:/ E B / = 0341.g1:/ F C />` to the base :g:`/ F C / <0341.g1:/ F C />`,

.. assertion:: [G.11] <G.11>

   and the triangle :g:`< E A B > <0341.g1:< E A B >>` will be :eq:`equal <0341.g1:< E A B > = 0341.g1:< F D C >>` to the triangle :g:`< F D C > <0341.g1:< F D C >>`.\ [#f1]_

Let :g:`< D G E > <0341.g1:< D G E >>` be subtracted\ [#f2]_ from each;

.. assertion:: [G.6] <G.6>

   therefore the trapezium :g:`< A B G D > <0341.g1:< A B G D >>` which remains is :eq:`equal <0341.g1:< A B G D > = 0341.g1:< E G C F >>` to the trapezium :g:`< E G C F > <0341.g1:< E G C F >>` which remains.

Let the triangle :g:`< G B C > <0341.g1:< G B C >>` be added to each;

.. assertion:: [G.21] <G.21>

   therefore the whole parallelogram :g:`< A B C D > <0341.g1:< A B C D >>` is :eq:`equal <0341.g1:< A B C D > = 0341.g1:< E B C F >>` to the whole parallelogram :g:`< E B C F > <0341.g1:< E B C F >>`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **FDC.** The text has “:g:`< D F C ) <0341.g1:< D F C )>`.”

.. [#f2] **Let DGE be subtracted.** :person:`Euclid <euclid>` speaks of the triangle :g:`< D G E > <0341.g1:< D G E >>` without any explanation that, in the case which he takes (where :g:`/ A D / <0341.g1:/ A D />`, :g:`/ E F / <0341.g1:/ E F />` have no point in common), :g:`/ B E / <0341.g1:/ B E />`, :g:`/ C D / <0341.g1:/ C D />` must meet at a point :g:`G <0341.g1:G>` between the two parallels. He allows this to appear from the figure simply.

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
     "G.37" [label="G.37", tooltip="G.37 (I.26)", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5)", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29)", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34)", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
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
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.37" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
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
     "G.37" -> "G.27";
     "G.47" -> "G.37";
     "G.42" -> "G.41";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.48" -> "G.47";
   }

Required for
------------

:ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
