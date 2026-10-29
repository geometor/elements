:order: 27
:number: 27
:canonical_id: G.27
:original_id: I.16
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, angle, triangle, equality
:dependencies: G.3, G.7, G.9, G.11, G.17, G.25, G.26
:excerpt: In any triangle, if one of the sides be produced, the exterior angle is greater than either of the interior and opposite angles.

.. _G.27:
.. _I.16:

G.27
====

.. rubric:: `I.16 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/16/>`_

.. enunciation::

   In any triangle, if one of the sides be produced, the exterior angle\ [#f1]_ is greater than either of the interior and opposite angles.\ [#f2]_

.. picture:: 0293.g1.svg
   :alt: Proposition 16 figure

Let :g:`< A B C > <0293.g1:< A B C >>` be a triangle, and let one side of it :g:`/ B C / <0293.g1:/ B C />` be produced to :g:`D <0293.g1:D>`;

I say that the exterior angle :g:`< A C D ) <0293.g1:< A C D )>` is greater than either of the interior and opposite angles :g:`< C B A ) <0293.g1:< C B A )>`, :g:`< B A C ) <0293.g1:< B A C )>`.

Let :g:`/ A C / <0293.g1:/ A C />` be :eq:`bisected <0293.g1:/ A E / = 0293.g1:/ E C />` at :g:`E <0293.g1:E>`, :just:`[G.17] <G.17>`

and let :g:`/ B E / <0293.g1:/ B E />` be joined and produced in a straight line to :g:`F <0293.g1:F>`; let :g:`/ E F / <0293.g1:/ E F />` be made :eq:`equal <0293.g1:/ E F / = 0293.g1:/ B E />` to :g:`/ B E / <0293.g1:/ B E />`, :just:`[G.9] <G.9>`

let :g:`/ F C / <0293.g1:/ F C />` be joined, :just:`[G.3] <G.3>`

and let :g:`/ A C / <0293.g1:/ A C />` be drawn through to :g:`G <0293.g1:G>`.\ [#f3]_ :just:`[G.7] <G.7>`

Then, since :g:`/ A E / <0293.g1:/ A E />` is :eq:`equal <0293.g1:/ A E / = 0293.g1:/ E C /; 0293.g1:/ B E / = 0293.g1:/ E F />` to :g:`/ E C / <0293.g1:/ E C />`, and :g:`/ B E / <0293.g1:/ B E />` to :g:`/ E F / <0293.g1:/ E F />`,

.. assertion::

   the two sides :g:`/ A E / <0293.g1:/ A E />`, :g:`/ E B / <0293.g1:/ E B />` are :eq:`equal <0293.g1:/ A E / = 0293.g1:/ C E /; 0293.g1:/ E B / = 0293.g1:/ E F />` to the two sides :g:`/ C E / <0293.g1:/ C E />`, :g:`/ E F / <0293.g1:/ E F />` respectively;

and the angle :g:`< A E B ) <0293.g1:< A E B )>` is :eq:`equal <0293.g1:< A E B ) = 0293.g1:< F E C )>` to the angle :g:`< F E C ) <0293.g1:< F E C )>`,

.. subclause:: [G.25] <G.25>

   for they are vertical angles.

.. assertion::

   Therefore the base :g:`/ A B / <0293.g1:/ A B />` is :eq:`equal <0293.g1:/ A B / = 0293.g1:/ F C />` to the base :g:`/ F C / <0293.g1:/ F C />`,

.. assertion::

   and the triangle :g:`< A B E > <0293.g1:< A B E >>` is :eq:`equal <0293.g1:< A B E > = 0293.g1:< C F E >>` to the triangle :g:`< C F E > <0293.g1:< C F E >>`,\ [#f4]_

and the remaining angles are equal to the remaining angles respectively, namely those which the equal sides subtend; :just:`[G.11] <G.11>`

.. assertion::

   therefore the angle :g:`< B A E ) <0293.g1:< B A E )>` is :eq:`equal <0293.g1:< B A E ) = 0293.g1:< E C F )>` to the angle :g:`< E C F ) <0293.g1:< E C F )>`.

But the angle :g:`< E C D ) <0293.g1:< E C D )>` is greater than the angle :g:`< E C F ) <0293.g1:< E C F )>`; :just:`[G.26] <G.26>`

.. assertion::

   therefore the angle :g:`< A C D ) <0293.g1:< A C D )>` is greater than the angle :g:`< B A E ) <0293.g1:< B A E )>`.

Similarly also, if :g:`/ B C / <0293.g1:/ B C />` be bisected, the angle :g:`< B C G ) <0293.g1:< B C G )>`, that is, the angle :g:`< A C D ) <0293.g1:< A C D )>` [I. 15], can be proved greater than the angle :g:`< A B C ) <0293.g1:< A B C )>` as well.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **the exterior angle,** literally “the outside angle,” ἡ ἐκτὸς :term:`γωνία <angle>`.

.. [#f2] **the interior and opposite angles,** τῶν ἐντὸς καὶ ἀπεναντίον γωνιῶν.

.. [#f3] **let** :g:`/ A C / <0293.g1:/ A C />` **be drawn through to** :g:`G <0293.g1:G>`. The word is διήχθω, a variation on the more usual ἐκβεβλήσθω, “let it be produced.”

.. [#f4] :g:`< C F E > <0293.g1:< C F E >>`, in the text “:g:`< F E C > <0293.g1:< F E C >>`.”

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
     "G.27" [label="G.27", tooltip="G.27 (I.16)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
   }

Required for
------------

:ref:`G.29 <G.29>`, :ref:`G.30 <G.30>`, :ref:`G.31 <G.31>`, :ref:`G.32 <G.32>`, :ref:`G.33 <G.33>`, :ref:`G.34 <G.34>`, :ref:`G.35 <G.35>`, :ref:`G.36 <G.36>`, :ref:`G.37 <G.37>`, :ref:`G.39 <G.39>`, :ref:`G.40 <G.40>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.47 <G.47>`, :ref:`G.48 <G.48>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.56 <G.56>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
