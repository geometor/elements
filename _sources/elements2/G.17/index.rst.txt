:order: 17
:number: 17
:canonical_id: G.17
:original_id: I.10
:volume: I
:book: I
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry
:category: problem, construction, plane-geometry
:tags: book-i, point, segment, angle, triangle, bisect, equality
:dependencies: G.5, G.11, G.16
:excerpt: To bisect a given finite straight line.

.. _G.17:
.. _I.10:

G.17
====

.. rubric:: `I.10 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/10/>`_

.. enunciation::

   To bisect a given finite straight line.

.. picture:: 0281.g1.svg
   :alt: Proposition 10 figure

Let :g:`/ A B / <0281.g1:/ A B />` be the given finite straight line. Thus it is required to bisect the finite straight line :g:`/ A B / <0281.g1:/ A B />`.

Let the :eq:`equilateral <0281.g1:/ A B / = 0281.g1:/ A C / = 0281.g1:/ B C />` triangle :g:`< A B C > <0281.g1:< A B C >>` be constructed on it, :just:`[G.5] <G.5>`

and let the angle :g:`< A C B ) <0281.g1:< A C B )>` be :eq:`bisected <0281.g1:< A C D ) = 0281.g1:< B C D )>` by the straight line :g:`/ C D / <0281.g1:/ C D />`; :just:`[G.16] <G.16>`

I say that the straight line :g:`/ A B / <0281.g1:/ A B />` has been :eq:`bisected <0281.g1:/ A D / = 0281.g1:/ B D />` at the point :g:`D <0281.g1:D>`.

For, since :g:`/ A C / <0281.g1:/ A C />` is :eq:`equal <0281.g1:/ A C / = 0281.g1:/ C B />` to :g:`/ C B / <0281.g1:/ C B />`, and :g:`/ C D / <0281.g1:/ C D />` is common,

.. assertion::

   the two sides :g:`/ A C / <0281.g1:/ A C />`, :g:`/ C D / <0281.g1:/ C D />` are :eq:`equal <0281.g1:/ A C / = 0281.g1:/ B C />` to the two sides :g:`/ B C / <0281.g1:/ B C />`, :g:`/ C D / <0281.g1:/ C D />` respectively;

and the angle :g:`< A C D ) <0281.g1:< A C D )>` is :eq:`equal <0281.g1:< A C D ) = 0281.g1:< B C D )>` to the angle :g:`< B C D ) <0281.g1:< B C D )>`;

.. assertion:: [G.11] <G.11>

   therefore the base :g:`/ A D / <0281.g1:/ A D />` is :eq:`equal <0281.g1:/ A D / = 0281.g1:/ B D />` to the base :g:`/ B D / <0281.g1:/ B D />`.

Therefore the given finite straight line :g:`/ A B / <0281.g1:/ A B />` has been :eq:`bisected <0281.g1:/ A D / = 0281.g1:/ B D />` at :g:`D <0281.g1:D>`.

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
     "G.17" [label="G.17", tooltip="G.17 (I.10)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
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
     "G.17" -> "G.5";
     "G.8" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.17" -> "G.16";
   }

Required for
------------

:ref:`G.20 <G.20>`, :ref:`G.27 <G.27>`, :ref:`G.29 <G.29>`, :ref:`G.30 <G.30>`, :ref:`G.31 <G.31>`, :ref:`G.32 <G.32>`, :ref:`G.33 <G.33>`, :ref:`G.34 <G.34>`, :ref:`G.35 <G.35>`, :ref:`G.36 <G.36>`, :ref:`G.37 <G.37>`, :ref:`G.39 <G.39>`, :ref:`G.40 <G.40>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.47 <G.47>`, :ref:`G.48 <G.48>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.56 <G.56>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
