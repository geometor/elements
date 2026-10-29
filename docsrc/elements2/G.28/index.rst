:order: 28
:number: 28
:canonical_id: G.28
:original_id: I.17
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, angle, triangle, right-angle
:dependencies: G.7, G.22
:excerpt: In any triangle two angles taken together in any manner are less than two right angles.

.. _G.28:
.. _I.17:

G.28
====

.. rubric:: `I.17 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/17/>`_

.. enunciation::

   In any triangle two angles taken together in any manner\ [#f1]_ are less than two right angles.

Let :g:`< A B C > <0296.g1:< A B C >>` be a triangle;

I say that two angles of the triangle :g:`< A B C > <0296.g1:< A B C >>` taken together in any manner are less than two right angles.

For let :g:`/ B C / <0296.g1:/ B C />` be produced to :g:`D <0296.g1:D>`. :just:`[G.7] <G.7>`

Then, since the angle :g:`< A C D ) <0296.g1:< A C D )>` is an exterior angle of the triangle :g:`< A B C > <0296.g1:< A B C >>`,

.. assertion::

   it is greater than the interior and opposite angle :g:`< A B C ) <0296.g1:< A B C )>`.

.. subclause::

   Let the angle :g:`< A C B ) <0296.g1:< A C B )>` be added to each;

.. assertion::

   therefore the angles :g:`< A C D ) <0296.g1:< A C D )>`, :g:`< A C B ) <0296.g1:< A C B )>` are greater than the angles :g:`< A B C ) <0296.g1:< A B C )>`, :g:`< B C A ) <0296.g1:< B C A )>`.

.. picture:: 0296.g1.svg
   :alt: Proposition 17 figure

But the angles :g:`< A C D ) <0296.g1:< A C D )>`, :g:`< A C B ) <0296.g1:< A C B )>` are equal to two right angles. :just:`[G.22] <G.22>`

.. assertion::

   Therefore the angles :g:`< A B C ) <0296.g1:< A B C )>`, :g:`< B C A ) <0296.g1:< B C A )>` are less than two right angles.

Similarly we can prove that the angles :g:`< B A C ) <0296.g1:< B A C )>`, :g:`< A C B ) <0296.g1:< A C B )>` are also less than two right angles, and so are the angles :g:`< C A B ) <0296.g1:< C A B )>`, :g:`< A B C ) <0296.g1:< A B C )>` as well.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **taken together in any manner,** πάντη μεταλαμβανόμεναι, i.e. any pair added together.

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
     "G.28" [label="G.28", tooltip="G.28 (I.17)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.28" -> "G.7";
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
     "G.28" -> "G.22";
   }
