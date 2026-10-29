:order: 56
:number: 56
:canonical_id: G.56
:original_id: I.43
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, segment, triangle, quadrilateral, parallelogram, equality
:dependencies: G.6, G.21, G.47
:excerpt: In any parallelogram the complements of the parallelograms about the diameter are equal to one another.

.. _G.56:
.. _I.43:

G.56
====

.. rubric:: `I.43 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/43/>`_

.. enunciation::

   In any parallelogram the complements\ [#f1]_ of the parallelograms about the diameter are equal to one another.

Let :g:`< A B C D > <0354.g1:< A B C D >>` be a parallelogram, and :g:`/ A C / <0354.g1:/ A C />` its diameter; and about :g:`/ A C / <0354.g1:/ A C />`\ [#f2]_ let :g:`< A E K H > <0354.g1:< A E K H >>`, :g:`< K F C G > <0354.g1:< K F C G >>` be parallelograms, and :g:`< E B F K > <0354.g1:< E B F K >>`, :g:`< H K G D > <0354.g1:< H K G D >>` the so-called complements;

I say that the complement :g:`< E B F K > <0354.g1:< E B F K >>` is :eq:`equal <0354.g1:< E B F K > = 0354.g1:< H K G D >>` to the complement :g:`< H K G D > <0354.g1:< H K G D >>`.

.. picture:: 0354.g1.svg
   :alt: Folio 0354 Figure 1 - Proposition 43

For, since :g:`< A B C D > <0354.g1:< A B C D >>` is a parallelogram, and :g:`/ A C / <0354.g1:/ A C />` its diameter, the triangle :g:`< A B C > <0354.g1:< A B C >>` is :eq:`equal <0354.g1:< A B C > = 0354.g1:< A C D >>` to the triangle :g:`< A C D > <0354.g1:< A C D >>`. :just:`[G.47] <G.47>`

Again, since :g:`< A E K H > <0354.g1:< A E K H >>` is a parallelogram, and :g:`/ A K / <0354.g1:/ A K />` is its diameter, the triangle :g:`< A E K > <0354.g1:< A E K >>` is :eq:`equal <0354.g1:< A E K > = 0354.g1:< A H K >>` to the triangle :g:`< A H K > <0354.g1:< A H K >>`.

For the same reason the triangle :g:`< K F C > <0354.g1:< K F C >>` is also :eq:`equal <0354.g1:< K F C > = 0354.g1:< K G C >>` to :g:`< K G C > <0354.g1:< K G C >>`.

Now, since the triangle :g:`< A E K > <0354.g1:< A E K >>` is :eq:`equal <0354.g1:< A E K > = 0354.g1:< A H K >; 0354.g1:< K F C > = 0354.g1:< K G C >>` to the triangle :g:`< A H K > <0354.g1:< A H K >>`, and :g:`< K F C > <0354.g1:< K F C >>` to :g:`< K G C > <0354.g1:< K G C >>`,

.. assertion:: [G.21] <G.21>

   the triangle :g:`< A E K > <0354.g1:< A E K >>` together with :g:`< K G C > <0354.g1:< K G C >>` is equal to the triangle :g:`< A H K > <0354.g1:< A H K >>` together with :g:`< K F C > <0354.g1:< K F C >>`.

And the whole triangle :g:`< A B C > <0354.g1:< A B C >>` is also :eq:`equal <0354.g1:< A B C > = 0354.g1:< A D C >>` to the whole :g:`< A D C > <0354.g1:< A D C >>`;

.. assertion::

   therefore the complement :g:`< E B F K > <0354.g1:< E B F K >>` which remains is :eq:`equal <0354.g1:< E B F K > = 0354.g1:< H K G D >>` to the complement :g:`< H K G D > <0354.g1:< H K G D >>` which remains. :just:`[G.6] <G.6>`

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **complements**, :term:`παραπληρώματα <parapleroma>`, the figures put in to fill up (interstices).

.. [#f2] **and about** :g:`/ A C / <0354.g1:/ A C />`.... Euclid's phraseology here and in the next proposition implies that the complements as well as the other parallelograms are “about” the diagonal. The words are here περὶ δὲ τὴν ΑΓ παραλληλόγραμμα μὲν ἔστω τὰ ΕΘ, ΖΗ, τὰ δὲ λεγόμενα :term:`παραπληρώματα <parapleroma>` τὰ ΒΚ, ΚΔ. The expression “the so-called complements” indicates that this technical use of :term:`παραπληρώματα <parapleroma>` was not new, though it might not be universally known.

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
     "G.37" [label="G.37", tooltip="G.37 (I.26)", fillcolor="#222244", URL="../G.37/index.html", target="_top"];
     "G.41" [label="G.41", tooltip="G.41 (I.post.5)", fillcolor="#444422", URL="../G.41/index.html", target="_top"];
     "G.42" [label="G.42", tooltip="G.42 (I.29)", fillcolor="#222244", URL="../G.42/index.html", target="_top"];
     "G.47" [label="G.47", tooltip="G.47 (I.34)", fillcolor="#222244", URL="../G.47/index.html", target="_top"];
     "G.56" [label="G.56", tooltip="G.56 (I.43)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.27" -> "G.3";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.8" -> "G.6";
     "G.25" -> "G.6";
     "G.56" -> "G.6";
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
     "G.37" -> "G.11";
     "G.47" -> "G.11";
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
     "G.42" -> "G.21";
     "G.47" -> "G.21";
     "G.56" -> "G.21";
     "G.25" -> "G.22";
     "G.42" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.42" -> "G.25";
     "G.27" -> "G.26";
     "G.37" -> "G.27";
     "G.47" -> "G.37";
     "G.42" -> "G.41";
     "G.47" -> "G.42";
     "G.56" -> "G.47";
   }

Required for
------------

:ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`
