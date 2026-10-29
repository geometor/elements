:order: 39
:number: 39
:canonical_id: G.39
:original_id: I.27
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, angle, triangle, parallel, equality, reductio-ad-absurdum
:dependencies: G.27, G.38
:excerpt: If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.

.. _G.39:
.. _I.27:

G.39
====

.. rubric:: `I.27 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/27/>`_

.. enunciation::

   If a straight line falling on two straight lines\ [#f1]_ make the alternate angles\ [#f2]_ equal to one another, the straight lines will be parallel to one another.

.. picture:: 0321.g1.svg
   :alt: Folio 0321 Figure 1 - Proposition 27

For let the straight line :g:`/ E F / <0321.g1:/ E F />` falling on the two straight lines :g:`/ A B / <0321.g1:/ A B />`, :g:`/ C D / <0321.g1:/ C D />` make the alternate angles :g:`< A E F ) <0321.g1:< A E F )>`, :g:`< E F D ) <0321.g1:< E F D )>` :eq:`equal <0321.g1:< A E F ) = 0321.g1:< E F D )>` to one another;

I say that :g:`/ A B / <0321.g1:/ A B />` is parallel to :g:`/ C D / <0321.g1:/ C D />`.

For, if not, :g:`/ A B / <0321.g1:/ A B />`, :g:`/ C D / <0321.g1:/ C D />` when produced will meet either in the direction of :g:`B <0321.g1:B>`, :g:`D <0321.g1:D>` or towards :g:`A <0321.g1:A>`, :g:`C <0321.g1:C>`.\ [#f3]_ Let them be produced and meet, in the direction of :g:`B <0321.g1:B>`, :g:`D <0321.g1:D>`, at :g:`G <0321.g1:G>`.

Then, in the triangle :g:`< G E F > <0321.g1:< G E F >>`, the exterior angle :g:`< A E F ) <0321.g1:< A E F )>` is :eq:`equal <0321.g1:< A E F ) = 0321.g1:< E F G )>` to the interior and opposite angle :g:`< E F G ) <0321.g1:< E F G )>`:

.. assertion:: [G.27] <G.27>

   which is impossible.

.. assertion::

   Therefore :g:`/ A B / <0321.g1:/ A B />`, :g:`/ C D / <0321.g1:/ C D />` when produced will not meet in the direction of :g:`B <0321.g1:B>`, :g:`D <0321.g1:D>`.

.. assertion::

   Similarly it can be proved that neither will they meet towards :g:`A <0321.g1:A>`, :g:`C <0321.g1:C>`.

But straight lines which do not meet in either direction are parallel; :just:`[G.38] <G.38>`

.. assertion::

   therefore :g:`/ A B / <0321.g1:/ A B />` is parallel to :g:`/ C D / <0321.g1:/ C D />`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. [#f1] **falling on two straight lines,** εἰς δύο εὐθείας ἐμπίπτουσα, the phrase being the same as that used in Post. 5, meaning a *transversal*.

.. [#f2] **the alternate angles,** αἱ ἐναλλὰξ :term:`γωνίαι <angle>`. :person:`Proclus <proclus>` (:cite:`p. 357, 9 <proclus:in-euclid:357.9>`) explains that :person:`Euclid <euclid>` uses the word *alternate* (or, more exactly, *alternately*, ἐναλλάξ) in two connexions, (1) of a certain transformation of a proportion, as in Book **v.** and the arithmetical Books, (2) as here, of certain of the angles formed by parallels with a straight line crossing them. *Alternate angles* are, according to :person:`Euclid <euclid>` as interpreted by :person:`Proclus <proclus>`, those which are not on the same side of the transversal, and are not adjacent, but are separated by the transversal, both being within the parallels but one “above” and the other “below.” The meaning is natural enough if we imagine the four internal angles to be taken in cyclic order and *alternate angles* to be any two of them not successive but separated by one angle of the four.

.. [#f3] **in the direction of B, D or towards A, C,** literally “towards the parts :g:`B <0321.g1:B>`, :g:`D <0321.g1:D>` or towards :g:`A <0321.g1:A>`, :g:`C <0321.g1:C>`,” ἐπὶ τὰ Β, Δ μέρη ἢ ἐπὶ τὰ Α, Γ.

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
     "G.38" [label="G.38", tooltip="G.38 (I.def.23)", fillcolor="#224422", URL="../G.38/index.html", target="_top"];
     "G.39" [label="G.39", tooltip="G.39 (I.27)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.11" -> "G.10";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.27" -> "G.11";
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
     "G.25" -> "G.22";
     "G.25" -> "G.23";
     "G.27" -> "G.25";
     "G.27" -> "G.26";
     "G.39" -> "G.27";
     "G.39" -> "G.38";
   }

Required for
------------

:ref:`G.40 <G.40>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
