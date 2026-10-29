:order: 43
:number: 43
:canonical_id: G.43
:original_id: I.30
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, segment, angle, parallel, equality
:dependencies: G.1, G.42
:excerpt: Straight lines parallel to the same straight line are also parallel to one another.

.. _G.43:
.. _I.30:

G.43
====

.. rubric:: `I.30 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/30/>`_

.. enunciation::

   Straight lines parallel to the same straight line are also parallel to one another.

.. picture:: 0328.g1.svg
   :alt: Folio 0328 Figure 1 - Proposition 30

Let each of the straight lines :g:`/ A B / <0328.g1:/ A B />`, :g:`/ C D / <0328.g1:/ C D />` be parallel to :g:`/ E F / <0328.g1:/ E F />`;

I say that :g:`/ A B / <0328.g1:/ A B />` is also parallel to :g:`/ C D / <0328.g1:/ C D />`.

For let the straight line :g:`/ G K / <0328.g1:/ G K />` fall upon them;

Then, since the straight line :g:`/ G K / <0328.g1:/ G K />` has fallen on the parallel straight lines :g:`/ A B / <0328.g1:/ A B />`, :g:`/ E F / <0328.g1:/ E F />`,

.. assertion:: [G.42] <G.42>

   the angle :g:`< A G K ) <0328.g1:< A G K )>` is :eq:`equal <0328.g1:< A G K ) = 0328.g1:< G H F )>` to the angle :g:`< G H F ) <0328.g1:< G H F )>`.

Again, since the straight line :g:`/ G K / <0328.g1:/ G K />` has fallen on the parallel straight lines :g:`/ E F / <0328.g1:/ E F />`, :g:`/ C D / <0328.g1:/ C D />`,

.. assertion:: [G.42] <G.42>

   the angle :g:`< G H F ) <0328.g1:< G H F )>` is :eq:`equal <0328.g1:< G H F ) = 0328.g1:< G K D )>` to the angle :g:`< G K D ) <0328.g1:< G K D )>`.

But the angle :g:`< A G K ) <0328.g1:< A G K )>` was also proved :eq:`equal <0328.g1:< A G K ) = 0328.g1:< G H F )>` to the angle :g:`< G H F ) <0328.g1:< G H F )>`;

.. assertion:: [G.1] <G.1>

   therefore the angle :g:`< A G K ) <0328.g1:< A G K )>` is also :eq:`equal <0328.g1:< A G K ) = 0328.g1:< G K D )>` to the angle :g:`< G K D ) <0328.g1:< G K D )>`;

.. subclause::

   and they are alternate.

.. assertion::

   Therefore :g:`/ A B / <0328.g1:/ A B />` is parallel to :g:`/ C D / <0328.g1:/ C D />`.\ [#f1]_

.. qed::

   Q. E. D.

.. [#f1] The usual conclusion in general terms ("Therefore etc.") repeating the enunciation is, curiously enough, wanting at the end of this proposition.

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
     "G.18" [label="G.18", tooltip="G.18 (I.def.10)", fillcolor="#224422", URL="../G.18/index.html", target="_top"];
     "G.19" [label="G.19", tooltip="G.19 (I.11)", fillcolor="#222244", URL="../G.19/index.html", target="_top"];
     "G.21" [label="G.21", tooltip="G.21 (I.cn.2)", fillcolor="#442222", URL="../G.21/index.html", target="_top"];
     "G.22" [label="G.22", tooltip="G.22 (I.13)", fillcolor="#222244", URL="../G.22/index.html", target="_top"];
     "G.23" [label="G.23", tooltip="G.23 (I.post.4)", fillcolor="#444422", URL="../G.23/index.html", target="_top"];
     "G.25" [label="G.25", tooltip="G.25 (I.15)", fillcolor="#222244", URL="../G.25/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5)", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29)", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.43" [label="G.43", tooltip="G.43 (I.30)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.43" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.8" -> "G.5";
     "G.19" -> "G.5";
     "G.8" -> "G.6";
     "G.25" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.19" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.19" -> "G.15";
     "G.19" -> "G.18";
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
     "G.42" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.42" -> "G.25";
     "G.42" -> "G.41";
     "G.43" -> "G.42";
   }

Required for
------------

:ref:`G.58 <G.58>`
