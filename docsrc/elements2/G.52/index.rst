:order: 52
:number: 52
:canonical_id: G.52
:original_id: I.39
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, triangle, parallel, equality, reductio-ad-absurdum
:dependencies: G.1, G.44, G.50
:excerpt: Equal triangles which are on the same base and on the same side are also in the same parallels.

.. _G.52:
.. _I.39:

G.52
====

.. rubric:: `I.39 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/39/>`_

.. enunciation::

   Equal triangles which are on the same base and on the same side are also in the same parallels.

Let :g:`< A B C > <0350.g2:< A B C >>`, :g:`< D B C > <0350.g2:< D B C >>` be :eq:`equal <0350.g2:< A B C > = 0350.g2:< D B C >>` triangles which are on the same base :g:`/ B C / <0350.g2:/ B C />` and on the same side of it; [I say that they are also in the same parallels.]\ [#f1]_ And [For] let :g:`/ A D / <0350.g2:/ A D />` be joined;

I say that :g:`/ A D / <0350.g2:/ A D />` is parallel to :g:`/ B C / <0350.g2:/ B C />`.

.. picture:: 0350.g2.svg
   :alt: Folio 0350 Figure 2 - Proposition 39

For, if not, let :g:`/ A E / <0350.g2:/ A E />` be drawn through the point :g:`A <0350.g2:A>` parallel to the straight line :g:`/ B C / <0350.g2:/ B C />`, :just:`[G.44] <G.44>`

and let :g:`/ E C / <0350.g2:/ E C />` be joined.

Therefore the triangle :g:`< A B C > <0350.g2:< A B C >>` is :eq:`equal <0350.g2:< A B C > = 0350.g2:< E B C >>` to the triangle :g:`< E B C > <0350.g2:< E B C >>`; for it is on the same base :g:`/ B C / <0350.g2:/ B C />` with it and in the same parallels. :just:`[G.50] <G.50>`

But :g:`< A B C > <0350.g2:< A B C >>` is :eq:`equal <0350.g2:< A B C > = 0350.g2:< D B C >>` to :g:`< D B C > <0350.g2:< D B C >>`;

.. assertion::

   therefore :g:`< D B C > <0350.g2:< D B C >>` is also :eq:`equal <0350.g2:< D B C > = 0350.g2:< E B C >>` to :g:`< E B C > <0350.g2:< E B C >>`, :just:`[G.1] <G.1>` the greater to the less: which is impossible.

.. assertion::

   Therefore :g:`/ A E / <0350.g2:/ A E />` is not parallel to :g:`/ B C / <0350.g2:/ B C />`.

Similarly we can prove that neither is any other straight line except :g:`/ A D / <0350.g2:/ A D />`;

.. assertion::

   therefore :g:`/ A D / <0350.g2:/ A D />` is parallel to :g:`/ B C / <0350.g2:/ B C />`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **[I say that they are also in the same parallels.]** :person:`Heiberg <heiberg>` has proved (*Hermes*, xxxviii., 1903, p. 50) from a recently discovered papyrus-fragment (*Fayūm towns and their papyri*, p. 96, No. ix.) that these words are an interpolation by some one who did not observe that the words “And let :g:`/ A D / <0350.g2:/ A D />` be joined” are part of the *setting-out* (:term:`ἔκθεσις <ekthesis>`), but took them as belonging to the *construction* (:term:`κατασκευή <kataskeue>`) and consequently thought that a :term:`διορισμός <diorismos>` or “definition” (of the thing to be proved) should precede. The interpolator then altered “And” into “For” in the next sentence.

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
     "G.37" [label="G.37", tooltip="G.37 (I.26)", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.38" [label="G.38", tooltip="G.38 (I.def.23)", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27)", fillcolor="#222244", URL="../G.39/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5)", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29)", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.44" [label="G.44", tooltip="G.44 (I.31)", fillcolor="#222244", URL="../G.44/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34)", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.48" [label="G.48", tooltip="G.48 (I.35)", fillcolor="#222244", URL="../G.48/index.html", target="_top"];
     "G.50" [label="G.50", tooltip="G.50 (I.37)", fillcolor="#222244", URL="../G.50/index.html", target="_top"];
     "G.52" [label="G.52", tooltip="G.52 (I.39)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.25" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.52" -> "G.1";
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
     "G.48" -> "G.6";
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
     "G.37" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.14" -> "G.12";
     "G.30" -> "G.12";
     "G.31" -> "G.12";
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
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.48" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.27" -> "G.26";
     "G.31" -> "G.26";
     "G.29" -> "G.27";
     "G.37" -> "G.27";
     "G.39" -> "G.27";
     "G.30" -> "G.29";
     "G.31" -> "G.30";
     "G.33" -> "G.31";
     "G.34" -> "G.33";
     "G.44" -> "G.34";
     "G.47" -> "G.37";
     "G.39" -> "G.38";
     "G.44" -> "G.39";
     "G.42" -> "G.41";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.50" -> "G.44";
     "G.52" -> "G.44";
     "G.48" -> "G.47";
     "G.50" -> "G.47";
     "G.50" -> "G.48";
     "G.52" -> "G.50";
   }
