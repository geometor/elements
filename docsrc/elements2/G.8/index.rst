:order: 8
:number: 8
:canonical_id: G.8
:original_id: I.2
:volume: I
:book: I
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry
:category: problem, construction, plane-geometry
:tags: book-i, point, segment, circle, triangle, equality
:dependencies: G.1, G.3, G.4, G.5, G.6, G.7
:excerpt: To place at a given point (as an extremity) a straight line equal to a given straight line.

.. _G.8:
.. _I.2:

G.8
===

.. rubric:: `I.2 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/02/>`_

.. enunciation::

   To place at a given point (as an extremity)\ [#f1]_ a straight line equal to a given straight line.

.. picture:: 0258.g1.svg
   :alt: Proposition 2 figure

Let :g:`A <0258.g1:A>` be the given point, and :g:`/ B C / <0258.g1:/ B C />` the given straight line.

Thus it is required to place at the point :g:`A <0258.g1:A>` (as an extremity) a straight line equal to the given straight line :g:`/ B C / <0258.g1:/ B C />`.

From the point :g:`A <0258.g1:A>` to the point :g:`B <0258.g1:B>` let the straight line :g:`/ A B / <0258.g1:/ A B />` be joined; :just:`[G.3] <G.3>`

and on it let the :eq:`equilateral <0258.g1:/ D A / = 0258.g1:/ D B / = 0258.g1:/ A B />` triangle :g:`< D A B > <0258.g1:< D A B >>` be constructed. :just:`[G.5] <G.5>`

Let the straight lines :g:`/ A E / <0258.g1:/ A E />`, :g:`/ B F / <0258.g1:/ B F />` be produced\ [#f2]_ in a straight line with :g:`/ D A / <0258.g1:/ D A />`, :g:`/ D B / <0258.g1:/ D B />`; :just:`[G.7] <G.7>`

with centre :g:`B <0258.g1:B>` and distance :g:`/ B C / <0258.g1:/ B C />` let the circle :g:`( B C ) <0258.g1:( B C )>` be described; :just:`[G.4] <G.4>`

and again, with centre :g:`D <0258.g1:D>` and distance :g:`/ D G / <0258.g1:/ D G />` let the circle :g:`( D G ) <0258.g1:( D G )>` be described. :just:`[G.4] <G.4>`

Then, since the point :g:`B <0258.g1:B>` is the centre of the circle :g:`( B C ) <0258.g1:( B C )>`,

.. assertion::

   :g:`/ B C / <0258.g1:/ B C />` is :eq:`equal <0258.g1:/ B C / = 0258.g1:/ B G />` to :g:`/ B G / <0258.g1:/ B G />`.

Again, since the point :g:`D <0258.g1:D>` is the centre of the circle :g:`( D G ) <0258.g1:( D G )>`,

.. assertion::

   :g:`/ D L / <0258.g1:/ D L />` is :eq:`equal <0258.g1:/ D L / = 0258.g1:/ D G />` to :g:`/ D G / <0258.g1:/ D G />`.

And in these :g:`/ D A / <0258.g1:/ D A />` is :eq:`equal <0258.g1:/ D A / = 0258.g1:/ D B />` to :g:`/ D B / <0258.g1:/ D B />`; therefore the remainder :g:`/ A L / <0258.g1:/ A L />` is :eq:`equal <0258.g1:/ A L / = 0258.g1:/ B G />` to the remainder :g:`/ B G / <0258.g1:/ B G />`.\ [#f3]_ :just:`[G.6] <G.6>`

But :g:`/ B C / <0258.g1:/ B C />` was also proved :eq:`equal <0258.g1:/ B C / = 0258.g1:/ B G />` to :g:`/ B G / <0258.g1:/ B G />`; therefore each of the straight lines :g:`/ A L / <0258.g1:/ A L />`, :g:`/ B C / <0258.g1:/ B C />` is :eq:`equal <0258.g1:/ A L / = 0258.g1:/ B C / = 0258.g1:/ B G />` to :g:`/ B G / <0258.g1:/ B G />`.

And things which are equal to the same thing are also equal to one another; :just:`[G.1] <G.1>`

.. assertion::

   therefore :g:`/ A L / <0258.g1:/ A L />` is also :eq:`equal <0258.g1:/ A L / = 0258.g1:/ B C />` to :g:`/ B C / <0258.g1:/ B C />`.

Therefore at the given point :g:`A <0258.g1:A>` the straight line :g:`/ A L / <0258.g1:/ A L />` is placed :eq:`equal <0258.g1:/ A L / = 0258.g1:/ B C />` to the given straight line :g:`/ B C / <0258.g1:/ B C />`.

.. qed::

   (Being) what it was required to do.

.. [#f1] **(as an extremity).** I have inserted these words because “to place a straight line at a given point” (πρὸς τῷ δοθέντι σημείῳ) is not quite clear enough, at least in English.

.. [#f2] **Let the straight lines AE, BF be produced....** It will be observed that in this first application of Postulate 2, and again in I. 5, :person:`Euclid <euclid>` speaks of the *continuation* of the straight line as that which is produced in such cases, ἐκβεβλήσθωσαν and προσεκβεβλήσθωσαν meaning little more than *drawing* straight lines “in a straight line with” the given straight lines. The first place in which :person:`Euclid <euclid>` uses phraseology exactly corresponding to ours when

.. [#f3] **the remainder AL...the remainder BG.** The Greek expressions are λοιπὴ ἡ ΑΛ and λοιπῇ τῇ ΒΗ, and the literal translation would be “:g:`/ A L / <0258.g1:/ A L />` (or :g:`/ B G / <0258.g1:/ B G />`) *remaining*,” but the shade of meaning conveyed by the position of the definite article can hardly be expressed in English.

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
     "G.8" [label="G.8", tooltip="G.8 (I.2)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.5" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.8" -> "G.5";
     "G.8" -> "G.6";
     "G.8" -> "G.7";
   }

Required for
------------

:ref:`G.9 <G.9>`, :ref:`G.12 <G.12>`, :ref:`G.14 <G.14>`, :ref:`G.15 <G.15>`, :ref:`G.16 <G.16>`, :ref:`G.17 <G.17>`, :ref:`G.19 <G.19>`, :ref:`G.20 <G.20>`, :ref:`G.22 <G.22>`, :ref:`G.24 <G.24>`, :ref:`G.25 <G.25>`, :ref:`G.27 <G.27>`, :ref:`G.28 <G.28>`, :ref:`G.29 <G.29>`, :ref:`G.30 <G.30>`, :ref:`G.31 <G.31>`, :ref:`G.32 <G.32>`, :ref:`G.33 <G.33>`, :ref:`G.34 <G.34>`, :ref:`G.35 <G.35>`, :ref:`G.36 <G.36>`, :ref:`G.37 <G.37>`, :ref:`G.39 <G.39>`, :ref:`G.40 <G.40>`, :ref:`G.42 <G.42>`, :ref:`G.43 <G.43>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.47 <G.47>`, :ref:`G.48 <G.48>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.56 <G.56>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
