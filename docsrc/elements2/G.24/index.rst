:order: 24
:number: 24
:canonical_id: G.24
:original_id: I.14
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, angle, right-angle, equality, reductio-ad-absurdum
:dependencies: G.1, G.6, G.22, G.23
:excerpt: If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

.. _G.24:
.. _I.14:

G.24
====

.. rubric:: `I.14 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/14/>`_

.. enunciation::

   If with any straight line,\ [#f1]_ and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

.. picture:: 0290.g1.svg
   :alt: Proposition 14 figure

For with any straight line :g:`/ A B / <0290.g1:/ A B />`, and at the point :g:`B <0290.g1:B>` on it, let the two straight lines :g:`/ B C / <0290.g1:/ B C />`, :g:`/ B D / <0290.g1:/ B D />` not lying on the same side make the adjacent angles :g:`< A B C ) <0290.g1:< A B C )>`, :g:`< A B D ) <0290.g1:< A B D )>` equal to two right angles;

I say that :g:`/ B D / <0290.g1:/ B D />` is in a straight line with :g:`/ C B / <0290.g1:/ C B />`.

For, if :g:`/ B D / <0290.g1:/ B D />` is not in a straight line with :g:`/ B C / <0290.g1:/ B C />`, let :g:`/ B E / <0290.g1:/ B E />` be in a straight line with :g:`/ C B / <0290.g1:/ C B />`.

Then, since the straight line :g:`/ A B / <0290.g1:/ A B />` stands on the straight line :g:`/ C B E / <0290.g1:/ C B E />`,

.. assertion:: [G.22] <G.22>

   the angles :g:`< A B C ) <0290.g1:< A B C )>`, :g:`< A B E ) <0290.g1:< A B E )>` are equal to two right angles.

But the angles :g:`< A B C ) <0290.g1:< A B C )>`, :g:`< A B D ) <0290.g1:< A B D )>` are also equal to two right angles;

.. assertion:: [G.23, G.1] <G.23, G.1>

   therefore the angles :g:`< C B A ) <0290.g1:< C B A )>`, :g:`< A B E ) <0290.g1:< A B E )>` are equal to the angles :g:`< C B A ) <0290.g1:< C B A )>`, :g:`< A B D ) <0290.g1:< A B D )>`.\ [#f2]_

.. subclause::

   Let the angle :g:`< C B A ) <0290.g1:< C B A )>` be subtracted from each;

therefore the remaining angle :g:`< A B E ) <0290.g1:< A B E )>` is :eq:`equal <0290.g1:< A B E ) = 0290.g1:< A B D )>` to the remaining angle :g:`< A B D ) <0290.g1:< A B D )>`, :just:`[G.6] <G.6>`

.. assertion::

   the less to the greater: which is impossible.

Therefore :g:`/ B E / <0290.g1:/ B E />` is not in a straight line with :g:`/ C B / <0290.g1:/ C B />`.

Similarly we can prove\ [#f3]_ that neither is any other straight line except :g:`/ B D / <0290.g1:/ B D />`.

Therefore :g:`/ C B / <0290.g1:/ C B />` is in a straight line with :g:`/ B D / <0290.g1:/ B D />`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **If with any straight line....** There is no greater difficulty in translating the works of the Greek geometers than that of accurately giving the force of prepositions. πρός, for instance, is used in all sorts of expressions with various shades of meaning. The present enunciation begins Ἐὰν πρός τινι εὐθείᾳ καὶ τῷ πρὸς αὐτῇ σημείῳ, and it is really necessary in this one sentence to translate πρός by three different words, *with*, *at*, and *on*. The first πρός must be translated by *with* because two straight lines “make” an angle *with* one another. On the other hand, where the similar expression πρὸς τῇ δοθείσῃ εὐθείᾳ occurs in I. 23, but it is a question of “constructing” an angle (συστήσασθαι), we have to say “to construct *on* a given straight line.” *Against* would perhaps be the English word coming nearest to expressing all these meanings of πρός, but it would be intolerable as a translation.

.. [#f2] :person:`Todhunter <todhunter>` points out that for the inference in this line Post. 4, that all right angles are equal, is necessary as well as the Common Notion that things which are equal to the same thing (or rather, here, to equal things) are equal. A similar remark applies to steps in the proofs of I. 15 and I. 28.

.. [#f3] **we can prove.** The Greek expresses this by the future of the verb, δείξομεν, “we shall prove,” which however would perhaps be misleading in English.

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
     "G.24" [label="G.24", tooltip="G.24 (I.14)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.22" -> "G.1";
     "G.24" -> "G.1";
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
     "G.24" -> "G.6";
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
     "G.24" -> "G.22";
     "G.24" -> "G.23";
   }

Required for
------------

:ref:`G.58 <G.58>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
