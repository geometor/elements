:order: 14
:number: 14
:canonical_id: G.14
:original_id: I.7
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, angle, equality, reductio-ad-absurdum
:dependencies: G.3, G.12
:excerpt: Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its extremities), and on the same side of it, two other straight lines meeting in another point and equal to the former two respectively, namely each to that which has the same extremity with it.

.. _G.14:
.. _I.7:

G.14
====

.. rubric:: `I.7 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/07/>`_

.. enunciation::

   Given two straight lines constructed on a straight line (from its extremities) and meeting in a point, there cannot be constructed on the same straight line (from its extremities), and on the same side of it, two other straight lines meeting in another point and equal to the former two respectively, namely each to that which has the same extremity with it.\ [#f1]_

.. picture:: 0272.g2.svg
   :alt: Proposition 7 figure

For, if possible, given two straight lines :g:`/ A C / <0272.g2:/ A C />`, :g:`/ C B / <0272.g2:/ C B />` constructed on the straight line :g:`/ A B / <0272.g2:/ A B />` and meeting at the point :g:`C <0272.g2:C>`, let two other straight lines :g:`/ A D / <0272.g2:/ A D />`, :g:`/ D B / <0272.g2:/ D B />` be constructed on the same straight line :g:`/ A B / <0272.g2:/ A B />`, on the same side of it, meeting in another point :g:`D <0272.g2:D>` and :eq:`equal <0272.g2:/ C A / = 0272.g2:/ D A /; 0272.g2:/ C B / = 0272.g2:/ D B />` to the former two respectively, namely each to that which has the same extremity with it, so that :g:`/ C A / <0272.g2:/ C A />` is :eq:`equal <0272.g2:/ C A / = 0272.g2:/ D A />` to :g:`/ D A / <0272.g2:/ D A />` which has the same extremity :g:`A <0272.g2:A>` with it, and
:g:`/ C B / <0272.g2:/ C B />` to :g:`/ D B / <0272.g2:/ D B />` which has the same extremity :g:`B <0272.g2:B>` with it; and let :g:`/ C D / <0272.g2:/ C D />` be joined. :just:`[G.3] <G.3>`

Then, since :g:`/ A C / <0272.g2:/ A C />` is :eq:`equal <0272.g2:/ A C / = 0272.g2:/ A D />` to :g:`/ A D / <0272.g2:/ A D />`,

.. subclause:: [G.12] <G.12>

   the angle :g:`< A C D ) <0272.g2:< A C D )>` is also :eq:`equal <0272.g2:< A C D ) = 0272.g2:< A D C )>` to the angle :g:`< A D C ) <0272.g2:< A D C )>`;

therefore the angle :g:`< A D C ) <0272.g2:< A D C )>` is greater than the angle :g:`< D C B ) <0272.g2:< D C B )>`;\ [#f2]_ therefore the angle :g:`< C D B ) <0272.g2:< C D B )>` is much greater\ [#f3]_ than the angle :g:`< D C B ) <0272.g2:< D C B )>`.

Again, since :g:`/ C B / <0272.g2:/ C B />` is :eq:`equal <0272.g2:/ C B / = 0272.g2:/ D B />` to :g:`/ D B / <0272.g2:/ D B />`,

.. subclause::

   the angle :g:`< C D B ) <0272.g2:< C D B )>` is also :eq:`equal <0272.g2:< C D B ) = 0272.g2:< D C B )>` to the angle :g:`< D C B ) <0272.g2:< D C B )>`.

But it was also proved much greater than it:

.. assertion::

   which is impossible.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] In an English translation of the enunciation of this proposition it is absolutely necessary, in order to make it intelligible, to insert some words which are not in the Greek. The reason is partly that the Greek enunciation is itself very elliptical, and partly that some words used in it conveyed more meaning than the corresponding words in English do. Particularly is this the case with οὐ συσταθήσονται ἐπί “there shall not be constructed upon,” since συνίστασθαι is the regular word for constructing a *triangle* in particular. Thus a Greek would easily understahd συσταθήσονται ἐπί as meaning the construction of two lines forming *a triangle on a given straight line as base*; whereas to “construct two straight lines on a straight line” is not in English sufficiently definite unless we explain that they are *drawn from the ends of the straight line to meet at a point*. I have had the less hesitation in putting in the words “from its extremities” because they are actually used by :person:`Euclid <euclid>` in the somewhat similar enunciation of I. 21.

.. [#f2] It would be natural to insert here the step “but the angle :g:`< A C D ) <0272.g2:< A C D )>` is greater than the angle :g:`< B C D ) <0272.g2:< B C D )>`. [C. N. 5.]”

.. [#f3] **much greater,** literally “greater by much” (πολλῷ μείζων). :person:`Simson <simson>` and those who follow him translate: “much more then is the angle :g:`< B D C ) <0272.g2:< B D C )>` greater than the angle :g:`< B C D ) <0272.g2:< B C D )>`,” but the Greek for this would have to be πολλῷ (or πολὺ) μᾶλλόν ἐστι...μείζων. πολλῷ μᾶλλον, however, though used by :person:`Apollonius <apollonius>`, is not, apparently, found in :person:`Euclid <euclid>` or :person:`Archimedes <archimedes>`.

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
     "G.14" [label="G.14", tooltip="G.14 (I.7)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
   }

Required for
------------

:ref:`G.15 <G.15>`, :ref:`G.16 <G.16>`, :ref:`G.17 <G.17>`, :ref:`G.19 <G.19>`, :ref:`G.20 <G.20>`, :ref:`G.22 <G.22>`, :ref:`G.24 <G.24>`, :ref:`G.25 <G.25>`, :ref:`G.27 <G.27>`, :ref:`G.28 <G.28>`, :ref:`G.29 <G.29>`, :ref:`G.30 <G.30>`, :ref:`G.31 <G.31>`, :ref:`G.32 <G.32>`, :ref:`G.33 <G.33>`, :ref:`G.34 <G.34>`, :ref:`G.35 <G.35>`, :ref:`G.36 <G.36>`, :ref:`G.37 <G.37>`, :ref:`G.39 <G.39>`, :ref:`G.40 <G.40>`, :ref:`G.42 <G.42>`, :ref:`G.43 <G.43>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.47 <G.47>`, :ref:`G.48 <G.48>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.56 <G.56>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
