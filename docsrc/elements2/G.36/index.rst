:order: 36
:number: 36
:canonical_id: G.36
:original_id: I.25
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, segment, angle, triangle, equality, reductio-ad-absurdum
:dependencies: G.11, G.35
:excerpt: If two triangles have the two sides equal to two sides respectively, but have the base greater than the base, they will also have the one of the angles contained by the equal straight lines greater than the other.

.. _G.36:
.. _I.25:

G.36
====

.. rubric:: `I.25 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/25/>`_

.. enunciation::

   If two triangles have the two sides equal to two sides respectively, but have the base greater than the base, they will also have the one of the angles contained by the equal straight lines greater than the other.

Let :g:`< A B C > <0313.g1:< A B C >>`, :g:`< D E F > <0313.g1:< D E F >>` be two triangles having the two sides :g:`/ A B / <0313.g1:/ A B />`, :g:`/ A C / <0313.g1:/ A C />` :eq:`equal <0313.g1:/ A B / = 0313.g1:/ D E /; 0313.g1:/ A C / = 0313.g1:/ D F />` to the two sides :g:`/ D E / <0313.g1:/ D E />`, :g:`/ D F / <0313.g1:/ D F />` respectively, namely :g:`/ A B / <0313.g1:/ A B />` to :g:`/ D E / <0313.g1:/ D E />`, and :g:`/ A C / <0313.g1:/ A C />` to :g:`/ D F / <0313.g1:/ D F />`; and let the base :g:`/ B C / <0313.g1:/ B C />` be greater than the base :g:`/ E F / <0313.g1:/ E F />`;

I say that the angle :g:`< B A C ) <0313.g1:< B A C )>` is also greater than the angle :g:`< E D F ) <0313.g1:< E D F )>`.

.. picture:: 0313.g1.svg
   :alt: Folio 0313 Figure 1 - Proposition 25

For, if not, it is either :eq:`equal <0313.g1:< B A C ) = 0313.g1:< E D F )>` to it or less.

Now the angle :g:`< B A C ) <0313.g1:< B A C )>` is not :eq:`equal <0313.g1:< B A C ) = 0313.g1:< E D F )>` to the angle :g:`< E D F ) <0313.g1:< E D F )>`;

.. subclause:: [G.11] <G.11>

   for then the base :g:`/ B C / <0313.g1:/ B C />` would also have been :eq:`equal <0313.g1:/ B C / = 0313.g1:/ E F />` to the base :g:`/ E F / <0313.g1:/ E F />`,

.. subclause::

   but it is not;

.. assertion::

   therefore the angle :g:`< B A C ) <0313.g1:< B A C )>` is not :eq:`equal <0313.g1:< B A C ) = 0313.g1:< E D F )>` to the angle :g:`< E D F ) <0313.g1:< E D F )>`.

Neither again is the angle :g:`< B A C ) <0313.g1:< B A C )>` less than the angle :g:`< E D F ) <0313.g1:< E D F )>`;

.. subclause:: [G.35] <G.35>

   for then the base :g:`/ B C / <0313.g1:/ B C />` would also have been less than the base :g:`/ E F / <0313.g1:/ E F />`,

.. subclause::

   but it is not;

.. assertion::

   therefore the angle :g:`< B A C ) <0313.g1:< B A C )>` is not less than the angle :g:`< E D F ) <0313.g1:< E D F )>`.

But it was proved that it is not :eq:`equal <0313.g1:< B A C ) = 0313.g1:< E D F )>` either;

.. assertion::

   therefore the angle :g:`< B A C ) <0313.g1:< B A C )>` is greater than the angle :g:`< E D F ) <0313.g1:< E D F )>`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

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
     "G.27" [label="G.27", tooltip="G.27 (I.16)", fillcolor="#222244", URL="../G.27/index.html", target="_top"];
     "G.29" [label="G.29", tooltip="G.29 (I.18)", fillcolor="#222244", URL="../G.29/index.html", target="_top"];
     "G.30" [label="G.30", tooltip="G.30 (I.19)", fillcolor="#222244", URL="../G.30/index.html", target="_top"];
     "G.31" [label="G.31", tooltip="G.31 (I.20)", fillcolor="#222244", URL="../G.31/index.html", target="_top"];
     "G.33" [label="G.33", tooltip="G.33 (I.22)", fillcolor="#222244", URL="../G.33/index.html", target="_top"];
     "G.34" [label="G.34", tooltip="G.34 (I.23)", fillcolor="#222244", URL="../G.34/index.html", target="_top"];
     "G.35" [label="G.35", tooltip="G.35 (I.24)", fillcolor="#222244", URL="../G.35/index.html", target="_top"];
     "G.36" [label="G.36", tooltip="G.36 (I.25)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.29" -> "G.9";
     "G.33" -> "G.9";
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
     "G.35" -> "G.11";
     "G.36" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
     "G.35" -> "G.12";
     "G.15" -> "G.14";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.34" -> "G.15";
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
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.35" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.35" -> "G.34";
     "G.36" -> "G.35";
   }
