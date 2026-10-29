:order: 42
:number: 42
:canonical_id: G.42
:original_id: I.29
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, segment, angle, right-angle, parallel, equality
:dependencies: G.1, G.21, G.22, G.25, G.41
:excerpt: A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles.

.. _G.42:
.. _I.29:

G.42
====

.. rubric:: `I.29 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/29/>`_

.. enunciation::

   A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles.

For let the straight line :g:`/ E F / <0325.g1:/ E F />` fall on the parallel straight lines :g:`/ A B / <0325.g1:/ A B />`, :g:`/ C D / <0325.g1:/ C D />`;

I say that it makes the alternate angles :g:`< A G H ) <0325.g1:< A G H )>`, :g:`< G H D ) <0325.g1:< G H D )>` :eq:`equal <0325.g1:< A G H ) = 0325.g1:< G H D )>`, the exterior angle :g:`< E G B ) <0325.g1:< E G B )>` :eq:`equal <0325.g1:< E G B ) = 0325.g1:< G H D )>` to the interior and opposite angle :g:`< G H D ) <0325.g1:< G H D )>`, and the interior angles on the same side, namely :g:`< B G H ) <0325.g1:< B G H )>`, :g:`< G H D ) <0325.g1:< G H D )>`, equal to two right angles.

.. picture:: 0325.g1.svg
   :alt: Folio 0325 Figure 1 - Proposition 29

For, if the angle :g:`< A G H ) <0325.g1:< A G H )>` is unequal to the angle :g:`< G H D ) <0325.g1:< G H D )>`, one of them is greater.

Let the angle :g:`< A G H ) <0325.g1:< A G H )>` be greater.

Let the angle :g:`< B G H ) <0325.g1:< B G H )>` be added to each;

.. assertion::

   therefore the angles :g:`< A G H ) <0325.g1:< A G H )>`, :g:`< B G H ) <0325.g1:< B G H )>` are greater than the angles :g:`< B G H ) <0325.g1:< B G H )>`, :g:`< G H D ) <0325.g1:< G H D )>`.

But the angles :g:`< A G H ) <0325.g1:< A G H )>`, :g:`< B G H ) <0325.g1:< B G H )>` are equal to two right angles; :just:`[G.22] <G.22>`

.. assertion::

   therefore the angles :g:`< B G H ) <0325.g1:< B G H )>`, :g:`< G H D ) <0325.g1:< G H D )>` are less than two right angles.

But straight lines produced indefinitely from angles less than two right angles\ [#f1]_ meet; :just:`[G.41] <G.41>`

.. assertion::

   therefore :g:`/ A B / <0325.g1:/ A B />`, :g:`/ C D / <0325.g1:/ C D />`, if produced indefinitely, will meet;

.. assertion::

   but they do not meet, because they are by hypothesis parallel.\ [#f2]_

.. assertion::

   Therefore the angle :g:`< A G H ) <0325.g1:< A G H )>` is not unequal to the angle :g:`< G H D ) <0325.g1:< G H D )>`,

.. assertion::

   and is therefore :eq:`equal <0325.g1:< A G H ) = 0325.g1:< G H D )>` to it.

Again, the angle :g:`< A G H ) <0325.g1:< A G H )>` is :eq:`equal <0325.g1:< A G H ) = 0325.g1:< E G B )>` to the angle :g:`< E G B ) <0325.g1:< E G B )>`; :just:`[G.25] <G.25>`

.. assertion:: [G.1] <G.1>

   therefore the angle :g:`< E G B ) <0325.g1:< E G B )>` is also :eq:`equal <0325.g1:< E G B ) = 0325.g1:< G H D )>` to the angle :g:`< G H D ) <0325.g1:< G H D )>`.

Let the angle :g:`< B G H ) <0325.g1:< B G H )>` be added to each;

.. assertion:: [G.21] <G.21>

   therefore the angles :g:`< E G B ) <0325.g1:< E G B )>`, :g:`< B G H ) <0325.g1:< B G H )>` are equal to the angles :g:`< B G H ) <0325.g1:< B G H )>`, :g:`< G H D ) <0325.g1:< G H D )>`.

But the angles :g:`< E G B ) <0325.g1:< E G B )>`, :g:`< B G H ) <0325.g1:< B G H )>` are equal to two right angles; :just:`[G.22] <G.22>`

.. assertion::

   therefore the angles :g:`< B G H ) <0325.g1:< B G H )>`, :g:`< G H D ) <0325.g1:< G H D )>` are also equal to two right angles.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **straight lines produced indefinitely from angles less than two right angles,** αἱ δὲ ἀπ᾽ ἐλασσόνων ἢ δύο ὀρθῶν ἐκβαλλόμεναι εἰς ἄπειρον συμπίπτουσιν, a variation from the more explicit language of Postulate 5. A good deal is left to be understood, namely that the straight lines begin from points at which they meet a transversal, and make with it internal angles on the same side the sum of which is less than two right angles.

.. [#f2] **because they are by hypothesis parallel,** literally “because they are supposed parallel,” διὰ τὸ παραλλήλους αὐτὰς ὑποκεῖσθαι.

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
     "G.42" [label="G.42", tooltip="G.42 (I.29)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
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
   }

Required for
------------

:ref:`G.43 <G.43>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.47 <G.47>`, :ref:`G.48 <G.48>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.56 <G.56>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
