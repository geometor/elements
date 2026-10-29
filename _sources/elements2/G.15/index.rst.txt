:order: 15
:number: 15
:canonical_id: G.15
:original_id: I.8
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, angle, triangle, equality
:dependencies: G.14
:excerpt: If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal straight lines.

.. _G.15:
.. _I.8:

G.15
====

.. rubric:: `I.8 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/08/>`_

.. enunciation::

   If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal straight lines.

.. picture:: 0275.g1.svg
   :alt: Proposition 8 figure

Let :g:`< A B C > <0275.g1:< A B C >>`, :g:`< D E F > <0275.g1:< D E F >>` be two triangles having the two sides :g:`/ A B / <0275.g1:/ A B />`, :g:`/ A C / <0275.g1:/ A C />` :eq:`equal <0275.g1:/ A B / = 0275.g1:/ D E /; 0275.g1:/ A C / = 0275.g1:/ D F />` to the two sides :g:`/ D E / <0275.g1:/ D E />`, :g:`/ D F / <0275.g1:/ D F />` respectively, namely :g:`/ A B / <0275.g1:/ A B />` to :g:`/ D E / <0275.g1:/ D E />`, and :g:`/ A C / <0275.g1:/ A C />` to :g:`/ D F / <0275.g1:/ D F />`; and let them have the base :g:`/ B C / <0275.g1:/ B C />` :eq:`equal <0275.g1:/ B C / = 0275.g1:/ E F />` to the base :g:`/ E F / <0275.g1:/ E F />`;

I say that the angle :g:`< B A C ) <0275.g1:< B A C )>` is also :eq:`equal <0275.g1:< B A C ) = 0275.g1:< E D F )>` to the angle :g:`< E D F ) <0275.g1:< E D F )>`.

For, if the triangle :g:`< A B C > <0275.g1:< A B C >>` be applied to the triangle :g:`< D E F > <0275.g1:< D E F >>`, and if the point :g:`B <0275.g1:B>` be placed on the point :g:`E <0275.g1:E>` and the straight line :g:`/ B C / <0275.g1:/ B C />` on :g:`/ E F / <0275.g1:/ E F />`,

.. subclause::

   the point :g:`C <0275.g1:C>` will also coincide with :g:`F <0275.g1:F>`,

.. assertion::

   because :g:`/ B C / <0275.g1:/ B C />` is :eq:`equal <0275.g1:/ B C / = 0275.g1:/ E F />` to :g:`/ E F / <0275.g1:/ E F />`.

Then, :g:`/ B C / <0275.g1:/ B C />` coinciding with :g:`/ E F / <0275.g1:/ E F />`,

.. subclause::

   :g:`/ B A / <0275.g1:/ B A />`, :g:`/ A C / <0275.g1:/ A C />`\ [#f1]_ will also coincide with :g:`/ E D / <0275.g1:/ E D />`, :g:`/ D F / <0275.g1:/ D F />`;

for, if the base :g:`/ B C / <0275.g1:/ B C />` coincides with the base :g:`/ E F / <0275.g1:/ E F />`, and the sides :g:`/ B A / <0275.g1:/ B A />`, :g:`/ A C / <0275.g1:/ A C />` do not coincide with :g:`/ E D / <0275.g1:/ E D />`, :g:`/ D F / <0275.g1:/ D F />` but fall beside them\ [#f2]_ as :g:`/ E G / <0275.g1:/ E G />`, :g:`/ G F / <0275.g1:/ G F />`,

.. subclause::

   then, given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there will have been constructed on the same straight line (from its extremities), and on the same side of it, two other straight lines meeting in another point and :eq:`equal <0275.g1:/ E D / = 0275.g1:/ E G /; 0275.g1:/ D F / = 0275.g1:/ G F />` to the former two respectively, namely each to that which has the same extremity with it.

But they cannot be so constructed. :just:`[G.14] <G.14>`

Therefore it is not possible that, if the base :g:`/ B C / <0275.g1:/ B C />` be applied to the base :g:`/ E F / <0275.g1:/ E F />`, the sides :g:`/ B A / <0275.g1:/ B A />`, :g:`/ A C / <0275.g1:/ A C />` should not coincide with :g:`/ E D / <0275.g1:/ E D />`, :g:`/ D F / <0275.g1:/ D F />`;

.. assertion::

   they will therefore coincide,

so that the angle :g:`< B A C ) <0275.g1:< B A C )>` will also coincide with the angle :g:`< E D F ) <0275.g1:< E D F )>`, and will be :eq:`equal <0275.g1:< B A C ) = 0275.g1:< E D F )>` to it.

.. qed::

   If therefore etc. :just:`Q. E. D.`

.. [#f1] **BA, AC.** The text has here “:g:`/ B A / <0275.g1:/ B A />`, :g:`/ C A / <0275.g1:/ C A />`.”

.. [#f2] **fall beside them.** The Greek has the future, παραλλάξουσι. παραλλάττω means “to pass by without touching,” “to miss” or “to deviate.”

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
     "G.15" [label="G.15", tooltip="G.15 (I.8)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.8" -> "G.6";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
   }

Required for
------------

:ref:`G.16 <G.16>`, :ref:`G.17 <G.17>`, :ref:`G.19 <G.19>`, :ref:`G.20 <G.20>`, :ref:`G.22 <G.22>`, :ref:`G.24 <G.24>`, :ref:`G.25 <G.25>`, :ref:`G.27 <G.27>`, :ref:`G.28 <G.28>`, :ref:`G.29 <G.29>`, :ref:`G.30 <G.30>`, :ref:`G.31 <G.31>`, :ref:`G.32 <G.32>`, :ref:`G.33 <G.33>`, :ref:`G.34 <G.34>`, :ref:`G.35 <G.35>`, :ref:`G.36 <G.36>`, :ref:`G.37 <G.37>`, :ref:`G.39 <G.39>`, :ref:`G.40 <G.40>`, :ref:`G.42 <G.42>`, :ref:`G.43 <G.43>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.47 <G.47>`, :ref:`G.48 <G.48>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.56 <G.56>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
