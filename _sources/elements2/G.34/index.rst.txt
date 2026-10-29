:order: 34
:number: 34
:canonical_id: G.34
:original_id: I.23
:volume: I
:book: I
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry
:category: problem, construction, plane-geometry
:tags: book-i, point, segment, line, angle, triangle, equality
:dependencies: G.15, G.33
:excerpt: On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.

.. _G.34:
.. _I.23:

G.34
====

.. rubric:: `I.23 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/23/>`_

.. enunciation::

   On a given straight line and at a point on it to construct a rectilineal angle equal to a given rectilineal angle.

Let :g:`/ A B / <0308.g1:/ A B />` be the given straight line, :g:`A <0308.g1:A>` the point on it, and the angle :g:`< D C E ) <0308.g1:< D C E )>` the given rectilineal angle;

thus it is required to construct on the given straight line :g:`/ A B / <0308.g1:/ A B />`, and at the point :g:`A <0308.g1:A>` on it, a rectilineal angle equal to the given rectilineal angle :g:`< D C E ) <0308.g1:< D C E )>`.

.. picture:: 0308.g1.svg
   :alt: Folio 0308 Figure 1 - Proposition 23

On the straight lines :g:`[ C D ] <0308.g1:[ C D ]>`, :g:`[ C E ] <0308.g1:[ C E ]>` respectively let the points :g:`D <0308.g1:D>`, :g:`E <0308.g1:E>` be taken at random; let :g:`/ D E / <0308.g1:/ D E />` be joined, and out of three straight lines which are equal to the three
straight lines :g:`/ C D / <0308.g1:/ C D />`, :g:`/ D E / <0308.g1:/ D E />`, :g:`/ C E / <0308.g1:/ C E />` let the triangle :g:`< A F G > <0308.g1:< A F G >>` be constructed in such a way that :g:`/ C D / <0308.g1:/ C D />` is :eq:`equal <0308.g1:/ C D / = 0308.g1:/ A F /; 0308.g1:/ C E / = 0308.g1:/ A G /; 0308.g1:/ D E / = 0308.g1:/ F G />` to :g:`/ A F / <0308.g1:/ A F />`, :g:`/ C E / <0308.g1:/ C E />` to :g:`/ A G / <0308.g1:/ A G />`, and further :g:`/ D E / <0308.g1:/ D E />` to :g:`/ F G / <0308.g1:/ F G />`. :just:`[G.33] <G.33>`

Then, since the two sides :g:`/ D C / <0308.g1:/ D C />`, :g:`/ C E / <0308.g1:/ C E />` are :eq:`equal <0308.g1:/ D C / = 0308.g1:/ F A /; 0308.g1:/ C E / = 0308.g1:/ A G />` to the two sides :g:`/ F A / <0308.g1:/ F A />`, :g:`/ A G / <0308.g1:/ A G />` respectively, and the base :g:`/ D E / <0308.g1:/ D E />` is :eq:`equal <0308.g1:/ D E / = 0308.g1:/ F G />` to the base :g:`/ F G / <0308.g1:/ F G />`,

.. assertion:: [G.15] <G.15>

   the angle :g:`< D C E ) <0308.g1:< D C E )>` is :eq:`equal <0308.g1:< D C E ) = 0308.g1:< F A G )>` to the angle :g:`< F A G ) <0308.g1:< F A G )>`.

Therefore on the given straight line :g:`/ A B / <0308.g1:/ A B />`, and at the point :g:`A <0308.g1:A>` on it, the rectilineal angle :g:`< F A G ) <0308.g1:< F A G )>` has been constructed :eq:`equal <0308.g1:< F A G ) = 0308.g1:< D C E )>` to the given rectilineal angle :g:`< D C E ) <0308.g1:< D C E )>`.

.. qed::

   Q. E. F.

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
     "G.34" [label="G.34", tooltip="G.34 (I.23)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
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
     "G.25" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
   }

Required for
------------

:ref:`G.35 <G.35>`, :ref:`G.36 <G.36>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
