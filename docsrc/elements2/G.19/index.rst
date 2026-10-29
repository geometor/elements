:order: 19
:number: 19
:canonical_id: G.19
:original_id: I.11
:volume: I
:book: I
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry
:category: problem, construction, plane-geometry
:tags: book-i, point, segment, angle, triangle, right-angle, equality
:dependencies: G.5, G.9, G.15, G.18
:excerpt: To draw a straight line at right angles to a given straight line from a given point on it.

.. _G.19:
.. _I.11:

G.19
====

.. rubric:: `I.11 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/11/>`_

.. enunciation::

   To draw a straight line at right angles to a given straight line from a given point on it.

.. picture:: 0283.g1.svg
   :alt: Proposition 11 figure

Let :g:`/ A B / <0283.g1:/ A B />` be the given straight line, and :g:`C <0283.g1:C>` the given point on it.

Thus it is required to draw from the point :g:`C <0283.g1:C>` a straight line at right angles to the straight line :g:`/ A B / <0283.g1:/ A B />`.

Let a point :g:`D <0283.g1:D>` be taken at random on :g:`/ A C / <0283.g1:/ A C />`; let :g:`/ C E / <0283.g1:/ C E />` be made :eq:`equal <0283.g1:/ C E / = 0283.g1:/ C D />` to :g:`/ C D / <0283.g1:/ C D />`;\ [#f1]_ :just:`[G.9] <G.9>`

on :g:`/ D E / <0283.g1:/ D E />` let the :eq:`equilateral <0283.g1:/ D E / = 0283.g1:/ D F / = 0283.g1:/ F E />` triangle :g:`< F D E > <0283.g1:< F D E >>` be constructed, :just:`[G.5] <G.5>`

and let :g:`/ F C / <0283.g1:/ F C />` be joined;

I say that the straight line :g:`/ F C / <0283.g1:/ F C />` has been drawn at :eq:`right angles <0283.g1:< D C F ) = 0283.g1:< E C F )>` to the given straight line :g:`/ A B / <0283.g1:/ A B />` from :g:`C <0283.g1:C>` the given point on it.

For, since :g:`/ D C / <0283.g1:/ D C />` is :eq:`equal <0283.g1:/ D C / = 0283.g1:/ C E />` to :g:`/ C E / <0283.g1:/ C E />`, and :g:`/ C F / <0283.g1:/ C F />` is common,

.. assertion::

   the two sides :g:`/ D C / <0283.g1:/ D C />`, :g:`/ C F / <0283.g1:/ C F />` are :eq:`equal <0283.g1:/ D C / = 0283.g1:/ E C />` to the two sides :g:`/ E C / <0283.g1:/ E C />`, :g:`/ C F / <0283.g1:/ C F />` respectively;

and the base :g:`/ D F / <0283.g1:/ D F />` is :eq:`equal <0283.g1:/ D F / = 0283.g1:/ F E />` to the base :g:`/ F E / <0283.g1:/ F E />`;

.. assertion:: [G.15] <G.15>

   therefore the angle :g:`< D C F ) <0283.g1:< D C F )>` is :eq:`equal <0283.g1:< D C F ) = 0283.g1:< E C F )>` to the angle :g:`< E C F ) <0283.g1:< E C F )>`;

and they are adjacent angles.

But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right; :just:`[G.18] <G.18>`

.. assertion::

   therefore each of the angles :g:`< D C F ) <0283.g1:< D C F )>`, :g:`< F C E ) <0283.g1:< F C E )>` is :eq:`right <0283.g1:< D C F ) = 0283.g1:< F C E )>`.

Therefore the straight line :g:`/ C F / <0283.g1:/ C F />` has been drawn at :eq:`right angles <0283.g1:< D C F ) = 0283.g1:< F C E )>` to the given straight line :g:`/ A B / <0283.g1:/ A B />` from the given point :g:`C <0283.g1:C>` on it.

.. qed::

   Q. E. F.

.. [#f1] **let** :g:`/ C E / <0283.g1:/ C E />` **be made equal to** :g:`/ C D / <0283.g1:/ C D />`. The verb is κείσθω which, as well as the other parts of κεῖμαι, is constantly used for the passive of τίθημι “to place”; and the latter word is constantly used in the sense of *making*, e.g., one straight line equal to another straight line.

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
     "G.19" [label="G.19", tooltip="G.19 (I.11)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.19" -> "G.5";
     "G.8" -> "G.6";
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
   }

Required for
------------

:ref:`G.22 <G.22>`, :ref:`G.24 <G.24>`, :ref:`G.25 <G.25>`, :ref:`G.27 <G.27>`, :ref:`G.28 <G.28>`, :ref:`G.29 <G.29>`, :ref:`G.30 <G.30>`, :ref:`G.31 <G.31>`, :ref:`G.32 <G.32>`, :ref:`G.33 <G.33>`, :ref:`G.34 <G.34>`, :ref:`G.35 <G.35>`, :ref:`G.36 <G.36>`, :ref:`G.37 <G.37>`, :ref:`G.39 <G.39>`, :ref:`G.40 <G.40>`, :ref:`G.42 <G.42>`, :ref:`G.43 <G.43>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.47 <G.47>`, :ref:`G.48 <G.48>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.56 <G.56>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
