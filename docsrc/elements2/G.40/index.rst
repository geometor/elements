:order: 40
:number: 40
:canonical_id: G.40
:original_id: I.28
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, segment, angle, right-angle, parallel, equality
:dependencies: G.22, G.25, G.39
:excerpt: If a straight line falling on two straight lines make the exterior angle equal to the interior and opposite angle on the same side, or the interior angles on the same side equal to two right angles, the straight lines will be parallel to one another.

.. _G.40:
.. _I.28:

G.40
====

.. rubric:: `I.28 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/28/>`_

.. enunciation::

   If a straight line falling on two straight lines make the exterior angle equal to the interior and opposite angle on the same side, or the interior angles on the same side equal to two right angles, the straight lines will be parallel to one another.

For let the straight line :g:`/ E F / <0324.g1:/ E F />` falling on the two straight lines :g:`/ A B / <0324.g1:/ A B />`, :g:`/ C D / <0324.g1:/ C D />` make the exterior angle :g:`< E G B ) <0324.g1:< E G B )>` :eq:`equal <0324.g1:< E G B ) = 0324.g1:< G H D )>` to the interior and opposite angle :g:`< G H D ) <0324.g1:< G H D )>`, or the interior angles on the same side, namely :g:`< B G H ) <0324.g1:< B G H )>`, :g:`< G H D ) <0324.g1:< G H D )>`, equal to two right angles;

I say that :g:`/ A B / <0324.g1:/ A B />` is parallel to :g:`/ C D / <0324.g1:/ C D />`.

.. picture:: 0324.g1.svg
   :alt: Folio 0324 Figure 1 - Proposition 28

For, since the angle :g:`< E G B ) <0324.g1:< E G B )>` is :eq:`equal <0324.g1:< E G B ) = 0324.g1:< G H D )>` to the angle :g:`< G H D ) <0324.g1:< G H D )>`, while the angle :g:`< E G B ) <0324.g1:< E G B )>` is :eq:`equal <0324.g1:< E G B ) = 0324.g1:< A G H )>` to the angle :g:`< A G H ) <0324.g1:< A G H )>`, :just:`[G.25] <G.25>`

.. assertion::

   the angle :g:`< A G H ) <0324.g1:< A G H )>` is also :eq:`equal <0324.g1:< A G H ) = 0324.g1:< G H D )>` to the angle :g:`< G H D ) <0324.g1:< G H D )>`;

.. subclause::

   and they are alternate;

.. assertion:: [G.39] <G.39>

   therefore :g:`/ A B / <0324.g1:/ A B />` is parallel to :g:`/ C D / <0324.g1:/ C D />`.

Again, since the angles :g:`< B G H ) <0324.g1:< B G H )>`, :g:`< G H D ) <0324.g1:< G H D )>` are equal to two right angles, and the angles :g:`< A G H ) <0324.g1:< A G H )>`, :g:`< B G H ) <0324.g1:< B G H )>` are also equal to two right angles, :just:`[G.22] <G.22>`

.. assertion::

   the angles :g:`< A G H ) <0324.g1:< A G H )>`, :g:`< B G H ) <0324.g1:< B G H )>` are equal to the angles :g:`< B G H ) <0324.g1:< B G H )>`, :g:`< G H D ) <0324.g1:< G H D )>`.

Let the angle :g:`< B G H ) <0324.g1:< B G H )>` be subtracted from each;

.. assertion::

   therefore the remaining angle :g:`< A G H ) <0324.g1:< A G H )>` is :eq:`equal <0324.g1:< A G H ) = 0324.g1:< G H D )>` to the remaining angle :g:`< G H D ) <0324.g1:< G H D )>`;

.. subclause::

   and they are alternate;

.. assertion:: [G.39] <G.39>

   therefore :g:`/ A B / <0324.g1:/ A B />` is parallel to :g:`/ C D / <0324.g1:/ C D />`.

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
     "G.38" [label="G.38", tooltip="G.38 (I.def.23)", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27)", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.40" [label="G.40", tooltip="G.40 (I.28)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
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
     "G.25" -> "G.22";
     "G.40" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.40" -> "G.25";
     "G.27" -> "G.26";
     "G.39" -> "G.27";
     "G.39" -> "G.38";
     "G.40" -> "G.39";
   }
