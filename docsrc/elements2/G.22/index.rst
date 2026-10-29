:order: 22
:number: 22
:canonical_id: G.22
:original_id: I.13
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, angle, right-angle, equality
:dependencies: G.1, G.18, G.19, G.21
:excerpt: If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.

.. _G.22:
.. _I.13:

G.22
====

.. rubric:: `I.13 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/13/>`_

.. enunciation::

   If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.

.. picture:: 0289.g1.svg
   :alt: Proposition 13 figure

For let any straight line :g:`/ A B / <0289.g1:/ A B />` set up on the straight line :g:`/ C D / <0289.g1:/ C D />` make the angles :g:`< C B A ) <0289.g1:< C B A )>`, :g:`< A B D ) <0289.g1:< A B D )>`;

I say that the angles :g:`< C B A ) <0289.g1:< C B A )>`, :g:`< A B D ) <0289.g1:< A B D )>` are either two right angles or equal to two right angles.

Now, if the angle :g:`< C B A ) <0289.g1:< C B A )>` is :eq:`equal <0289.g1:< C B A ) = 0289.g1:< A B D )>` to the angle :g:`< A B D ) <0289.g1:< A B D )>`,

.. assertion:: [G.18] <G.18>

   they are :eq:`two right angles <0289.g1:< C B A ) = 0289.g1:< A B D )>`.

But, if not, let :g:`/ B E / <0289.g1:/ B E />` be drawn from the point :g:`B <0289.g1:B>` at right angles to :g:`/ C D / <0289.g1:/ C D />`; :just:`[G.19] <G.19>`

.. assertion::

   therefore the angles :g:`< C B E ) <0289.g1:< C B E )>`, :g:`< E B D ) <0289.g1:< E B D )>` are :eq:`two right angles <0289.g1:< C B E ) = 0289.g1:< E B D )>`.

Then, since the angle :g:`< C B E ) <0289.g1:< C B E )>` is equal to the two angles :g:`< C B A ) <0289.g1:< C B A )>`, :g:`< A B E ) <0289.g1:< A B E )>`,

.. subclause::

   let the angle :g:`< E B D ) <0289.g1:< E B D )>` be added to each;\ [#f1]_

.. assertion:: [G.21] <G.21>

   therefore the angles :g:`< C B E ) <0289.g1:< C B E )>`, :g:`< E B D ) <0289.g1:< E B D )>` are equal to the three angles :g:`< C B A ) <0289.g1:< C B A )>`, :g:`< A B E ) <0289.g1:< A B E )>`, :g:`< E B D ) <0289.g1:< E B D )>`.

Again, since the angle :g:`< D B A ) <0289.g1:< D B A )>` is equal to the two angles :g:`< D B E ) <0289.g1:< D B E )>`, :g:`< E B A ) <0289.g1:< E B A )>`,

.. subclause::

   let the angle :g:`< A B C ) <0289.g1:< A B C )>` be added to each;

.. assertion:: [G.21] <G.21>

   therefore the angles :g:`< D B A ) <0289.g1:< D B A )>`, :g:`< A B C ) <0289.g1:< A B C )>` are equal to the three angles :g:`< D B E ) <0289.g1:< D B E )>`, :g:`< E B A ) <0289.g1:< E B A )>`, :g:`< A B C ) <0289.g1:< A B C )>`.

But the angles :g:`< C B E ) <0289.g1:< C B E )>`, :g:`< E B D ) <0289.g1:< E B D )>` were also proved equal to the same three angles; and things which are equal to the same thing are also equal to one another; :just:`[G.1] <G.1>`

.. assertion::

   therefore the angles :g:`< C B E ) <0289.g1:< C B E )>`, :g:`< E B D ) <0289.g1:< E B D )>` are also equal to the angles :g:`< D B A ) <0289.g1:< D B A )>`, :g:`< A B C ) <0289.g1:< A B C )>`.

But the angles :g:`< C B E ) <0289.g1:< C B E )>`, :g:`< E B D ) <0289.g1:< E B D )>` are :eq:`two right angles <0289.g1:< C B E ) = 0289.g1:< E B D )>`;

.. assertion::

   therefore the angles :g:`< D B A ) <0289.g1:< D B A )>`, :g:`< A B C ) <0289.g1:< A B C )>` are also equal to two right angles.

Therefore etc.

.. qed::

   Q. E. D.

.. [#f1] **let the angle** :g:`< E B D ) <0289.g1:< E B D )>` **be added to each**, literally “let the angle :g:`< E B D ) <0289.g1:< E B D )>` be added (so as to be) common,” κοινὴ προσκείσθω ἡ ὑπὸ ΕΒΔ. Similarly κοινὴ ἀφηρήσθω is used of subtracting a straight line or angle from each of two others. “Let the common angle :g:`< E B D ) <0289.g1:< E B D )>` be added” is clearly an inaccurate translation, for the angle is not common before it is added, i.e. the κοινὴ is proleptic. “Let the common angle be subtracted” as a translation of κοινὴ ἀφηρήσθω would be less unsatisfactory, it is true, but, as it is desirable to use corresponding words when translating the two expressions, it seems hopeless to attempt to keep the word “common,” and I have therefore said “to each” and “from each” simply.

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
     "G.22" [label="G.22", tooltip="G.22 (I.13)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
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
     "G.22" -> "G.18";
     "G.22" -> "G.19";
     "G.22" -> "G.21";
   }

Required for
------------

:ref:`G.24 <G.24>`, :ref:`G.25 <G.25>`, :ref:`G.27 <G.27>`, :ref:`G.28 <G.28>`, :ref:`G.29 <G.29>`, :ref:`G.30 <G.30>`, :ref:`G.31 <G.31>`, :ref:`G.32 <G.32>`, :ref:`G.33 <G.33>`, :ref:`G.34 <G.34>`, :ref:`G.35 <G.35>`, :ref:`G.36 <G.36>`, :ref:`G.37 <G.37>`, :ref:`G.39 <G.39>`, :ref:`G.40 <G.40>`, :ref:`G.42 <G.42>`, :ref:`G.43 <G.43>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.47 <G.47>`, :ref:`G.48 <G.48>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.56 <G.56>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
