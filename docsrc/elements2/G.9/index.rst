:order: 9
:number: 9
:canonical_id: G.9
:original_id: I.3
:volume: I
:book: I
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry
:category: problem, construction, plane-geometry
:tags: book-i, point, segment, circle, equality
:dependencies: G.1, G.2, G.4, G.8
:excerpt: Given two unequal straight lines, to cut off from the greater a straight line equal to the less.

.. _G.9:
.. _I.3:

G.9
===

.. rubric:: `I.3 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/03/>`_

.. enunciation::

   Given two unequal straight lines, to cut off from the greater a straight line equal to the less.

.. picture:: 0260.g1.svg
   :alt: Proposition 3 figure

Let :g:`/ A B / <0260.g1:/ A B />`, :g:`C <0260.g1:C>` be the two given unequal straight lines, and let :g:`/ A B / <0260.g1:/ A B />` be the greater of them.

Thus it is required to cut off from :g:`/ A B / <0260.g1:/ A B />` the greater a straight line equal to :g:`C <0260.g1:C>` the less.

At the point :g:`A <0260.g1:A>` let :g:`/ A D / <0260.g1:/ A D />` be placed :eq:`equal <0260.g1:/ A D / = 0260.g1:C>` to the straight line :g:`C <0260.g1:C>`; :just:`[G.8] <G.8>`

and with centre :g:`A <0260.g1:A>` and distance :g:`/ A D / <0260.g1:/ A D />` let the circle :g:`( D E F ) <0260.g1:( D E F )>` be described. :just:`[G.4] <G.4>`
Now, since the point :g:`A <0260.g1:A>` is the centre of the circle :g:`( D E F ) <0260.g1:( D E F )>`,

.. assertion:: [G.2] <G.2>

   :g:`/ A E / <0260.g1:/ A E />` is :eq:`equal <0260.g1:/ A E / = 0260.g1:/ A D />` to :g:`/ A D / <0260.g1:/ A D />`.

But :g:`C <0260.g1:C>` is also :eq:`equal <0260.g1:C = 0260.g1:/ A D />` to :g:`/ A D / <0260.g1:/ A D />`.

Therefore each of the straight lines :g:`/ A E / <0260.g1:/ A E />`, :g:`C <0260.g1:C>` is :eq:`equal <0260.g1:/ A E / = 0260.g1:C = 0260.g1:/ A D />` to :g:`/ A D / <0260.g1:/ A D />`; so that :g:`/ A E / <0260.g1:/ A E />` is also :eq:`equal <0260.g1:/ A E / = 0260.g1:C>` to :g:`C <0260.g1:C>`. :just:`[G.1] <G.1>`

Therefore, given the two straight lines :g:`/ A B / <0260.g1:/ A B />`, :g:`C <0260.g1:C>`, from :g:`/ A B / <0260.g1:/ A B />` the greater :g:`/ A E / <0260.g1:/ A E />` has been cut off :eq:`equal <0260.g1:/ A E / = 0260.g1:C>` to :g:`C <0260.g1:C>` the less.

.. qed::

   (Being) what it was required to do.

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
     "G.9" [label="G.9", tooltip="G.9 (I.3)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.8" -> "G.5";
     "G.8" -> "G.6";
     "G.8" -> "G.7";
     "G.9" -> "G.8";
   }

Required for
------------

:ref:`G.12 <G.12>`, :ref:`G.14 <G.14>`, :ref:`G.15 <G.15>`, :ref:`G.16 <G.16>`, :ref:`G.17 <G.17>`, :ref:`G.19 <G.19>`, :ref:`G.20 <G.20>`, :ref:`G.22 <G.22>`, :ref:`G.24 <G.24>`, :ref:`G.25 <G.25>`, :ref:`G.27 <G.27>`, :ref:`G.28 <G.28>`, :ref:`G.29 <G.29>`, :ref:`G.30 <G.30>`, :ref:`G.31 <G.31>`, :ref:`G.32 <G.32>`, :ref:`G.33 <G.33>`, :ref:`G.34 <G.34>`, :ref:`G.35 <G.35>`, :ref:`G.36 <G.36>`, :ref:`G.37 <G.37>`, :ref:`G.39 <G.39>`, :ref:`G.40 <G.40>`, :ref:`G.42 <G.42>`, :ref:`G.43 <G.43>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.47 <G.47>`, :ref:`G.48 <G.48>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.56 <G.56>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
