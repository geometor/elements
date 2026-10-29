:order: 20
:number: 20
:canonical_id: G.20
:original_id: I.12
:volume: I
:book: I
:type: prop
:subtype: problem
:categories: problem, construction, plane-geometry
:category: problem, construction, plane-geometry
:tags: book-i, point, segment, line, circle, angle, perpendicular, equality
:dependencies: G.3, G.4, G.15, G.17, G.18
:excerpt: To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.

.. _G.20:
.. _I.12:

G.20
====

.. rubric:: `I.12 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/12/>`_

.. enunciation::

   To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.\ [#f1]_

Let :g:`[ A B ] <0285.g1:[ A B ]>` be the given infinite straight line, and :g:`C <0285.g1:C>` the given point which is not on it;

.. picture:: 0285.g1.svg
   :alt: Proposition 12 figure

thus it is required to draw to the given infinite straight line :g:`[ A B ] <0285.g1:[ A B ]>`, from the given point :g:`C <0285.g1:C>` which is not on it, a perpendicular straight line.

For let a point :g:`D <0285.g1:D>` be taken at random on the other side of the straight line :g:`[ A B ] <0285.g1:[ A B ]>`,\ [#f2]_ and with centre :g:`C <0285.g1:C>` and distance :g:`/ C D / <0285.g1:/ C D />` let the circle :g:`( C D ) <0285.g1:( C D )>` be described; :just:`[G.4] <G.4>`

let the straight line :g:`/ E G / <0285.g1:/ E G />` be :eq:`bisected <0285.g1:/ G H / = 0285.g1:/ H E />` at :g:`H <0285.g1:H>`, :just:`[G.17] <G.17>`

and let the straight lines :g:`/ C G / <0285.g1:/ C G />`, :g:`/ C H / <0285.g1:/ C H />`, :g:`/ C E / <0285.g1:/ C E />` be joined. :just:`[G.3] <G.3>`

I say that :g:`/ C H / <0285.g1:/ C H />` has been drawn :eq:`perpendicular <0285.g1:< C H G ) = 0285.g1:< E H C )>` to the given infinite straight line :g:`[ A B ] <0285.g1:[ A B ]>` from the given point :g:`C <0285.g1:C>` which is not on it.

For, since :g:`/ G H / <0285.g1:/ G H />` is :eq:`equal <0285.g1:/ G H / = 0285.g1:/ H E />` to :g:`/ H E / <0285.g1:/ H E />`, and :g:`/ H C / <0285.g1:/ H C />` is common,

.. assertion::

   the two sides :g:`/ G H / <0285.g1:/ G H />`, :g:`/ H C / <0285.g1:/ H C />` are :eq:`equal <0285.g1:/ G H / = 0285.g1:/ E H />` to the two sides :g:`/ E H / <0285.g1:/ E H />`, :g:`/ H C / <0285.g1:/ H C />` respectively;

and the base :g:`/ C G / <0285.g1:/ C G />` is :eq:`equal <0285.g1:/ C G / = 0285.g1:/ C E />` to the base :g:`/ C E / <0285.g1:/ C E />`;

.. assertion:: [G.15] <G.15>

   therefore the angle :g:`< C H G ) <0285.g1:< C H G )>` is :eq:`equal <0285.g1:< C H G ) = 0285.g1:< E H C )>` to the angle :g:`< E H C ) <0285.g1:< E H C )>`.

And they are adjacent angles.

But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is called a perpendicular to that on which it stands. :just:`[G.18] <G.18>`

Therefore :g:`/ C H / <0285.g1:/ C H />` has been drawn :eq:`perpendicular <0285.g1:< C H G ) = 0285.g1:< E H C )>` to the given infinite straight line :g:`[ A B ] <0285.g1:[ A B ]>` from the given point :g:`C <0285.g1:C>` which is not on it.

.. qed::

   Q. E. F.

.. [#f1] **a perpendicular straight line**, κάθετον εὐθεῖαν γραμμήν. This is the full expression for a perpendicular, :term:`κάθετος <kathetos>` meaning *let fall* or *let down*, so that the expression corresponds to our *plumb-line*. ἡ :term:`κάθετος <kathetos>` is however constantly used alone for a perpendicular, :term:`γραμμή <line>` being understood.

.. [#f2] **on the other side of the straight line** :g:`[ A B ] <0285.g1:[ A B ]>`, literally “towards the other parts of the straight line :g:`[ A B ] <0285.g1:[ A B ]>`,” ἐπὶ τὰ ἕτερα μέρη τῆς :g:`[ A B ] <0285.g1:[ A B ]>`. Cf. “on the same side” (ἐπὶ τὰ αὐτὰ μέρη) in Post. 5 and “in both directions” (ἐφ᾽ ἑκάτερα τὰ μέρη) in Def. 23.

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
     "G.20" [label="G.20", tooltip="G.20 (I.12)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.14" -> "G.3";
     "G.20" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.20" -> "G.4";
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
     "G.20" -> "G.15";
     "G.17" -> "G.16";
     "G.20" -> "G.17";
     "G.20" -> "G.18";
   }
