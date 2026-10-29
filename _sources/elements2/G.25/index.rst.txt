:order: 25
:number: 25
:canonical_id: G.25
:original_id: I.15
:volume: I
:book: I
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry
:category: theorem, proof, plane-geometry
:tags: book-i, point, segment, angle, equality, porism
:dependencies: G.1, G.6, G.22, G.23
:excerpt: If two straight lines cut one another, they make the vertical angles equal to one another.

.. _G.25:
.. _I.15:

G.25
====

.. rubric:: `I.15 <https://geometor.github.io/euclid/heath/volume_I/book_i/propositions/15/>`_

.. enunciation::

   If two straight lines cut one another, they make the vertical angles\ [#f1]_ equal to one another.

.. picture:: 0291.g2.svg
   :alt: Proposition 15 figure

For let the straight lines :g:`/ A B / <0291.g2:/ A B />`, :g:`/ C D / <0291.g2:/ C D />` cut one another at the point :g:`E <0291.g2:E>`;

I say that the angle :g:`< A E C ) <0291.g2:< A E C )>` is :eq:`equal <0291.g2:< A E C ) = 0291.g2:< D E B ); 0291.g2:< C E B ) = 0291.g2:< A E D )>` to the angle :g:`< D E B ) <0291.g2:< D E B )>`, and the angle :g:`< C E B ) <0291.g2:< C E B )>` to the angle :g:`< A E D ) <0291.g2:< A E D )>`.

For, since the straight line :g:`/ A E / <0291.g2:/ A E />` stands on the straight line :g:`/ C D / <0291.g2:/ C D />`, making the angles :g:`< C E A ) <0291.g2:< C E A )>`, :g:`< A E D ) <0291.g2:< A E D )>`,

.. assertion:: [G.22] <G.22>

   the angles :g:`< C E A ) <0291.g2:< C E A )>`, :g:`< A E D ) <0291.g2:< A E D )>` are equal to two right angles.

Again, since the straight line :g:`/ D E / <0291.g2:/ D E />` stands on the straight line :g:`/ A B / <0291.g2:/ A B />`, making the angles :g:`< A E D ) <0291.g2:< A E D )>`, :g:`< D E B ) <0291.g2:< D E B )>`,

.. assertion:: [G.22] <G.22>

   the angles :g:`< A E D ) <0291.g2:< A E D )>`, :g:`< D E B ) <0291.g2:< D E B )>` are equal to two right angles.

But the angles :g:`< C E A ) <0291.g2:< C E A )>`, :g:`< A E D ) <0291.g2:< A E D )>` were also proved equal to two right angles;

.. assertion:: [G.23, G.1] <G.23, G.1>

   therefore the angles :g:`< C E A ) <0291.g2:< C E A )>`, :g:`< A E D ) <0291.g2:< A E D )>` are equal to the angles :g:`< A E D ) <0291.g2:< A E D )>` :g:`< D E B ) <0291.g2:< D E B )>`.

.. subclause::

   Let the angle :g:`< A E D ) <0291.g2:< A E D )>` be subtracted from each;

therefore the remaining angle :g:`< C E A ) <0291.g2:< C E A )>` is :eq:`equal <0291.g2:< C E A ) = 0291.g2:< B E D )>` to the remaining angle :g:`< B E D ) <0291.g2:< B E D )>`. :just:`[G.6] <G.6>`

Similarly it can be proved that the angles :g:`< C E B ) <0291.g2:< C E B )>`, :g:`< D E A ) <0291.g2:< D E A )>` are also :eq:`equal <0291.g2:< C E B ) = 0291.g2:< D E A )>`.

.. qed::

   Therefore etc. :just:`Q. E. D.`

.. porism::

   From this it is manifest that, if two straight lines cut one another, they will make the angles at the point of section\ [#f2]_ equal to four right angles.

.. [#f1] **the vertical angles.** The difference between adjacent angles (αἱ ἐφεξῆς :term:`γωνίαι <angle>`) and vertical angles (αἱ κατὰ κορυφὴν :term:`γωνίαι <angle>`) is thus explained by :person:`Proclus <proclus>` (:cite:`p. 298, 14—24 <proclus:in-euclid:298.14-24>`). The first term describes the angles made by two straight lines when one only is divided by the other, i.e. when one straight line meets another at a point which is not either of its extremities, but is not itself produced beyond the point of meeting. When the first straight line is produced, so that the lines cross at the point, they make two pairs of vertical angles (which are more clearly described as vertically opposite angles), and which are so called because their convergence is from opposite directions to one point (the intersection of the lines) as vertex (:term:`κορυφή <koryphe>`).

.. [#f2] **at the point of section,** literally “at the section,” πρὸς τῇ τομῇ.

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
     "G.25" [label="G.25", tooltip="G.25 (I.15)", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
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
     "G.25" -> "G.22";
     "G.25" -> "G.23";
   }

Required for
------------

:ref:`G.27 <G.27>`, :ref:`G.29 <G.29>`, :ref:`G.30 <G.30>`, :ref:`G.31 <G.31>`, :ref:`G.32 <G.32>`, :ref:`G.33 <G.33>`, :ref:`G.34 <G.34>`, :ref:`G.35 <G.35>`, :ref:`G.36 <G.36>`, :ref:`G.37 <G.37>`, :ref:`G.39 <G.39>`, :ref:`G.40 <G.40>`, :ref:`G.42 <G.42>`, :ref:`G.43 <G.43>`, :ref:`G.44 <G.44>`, :ref:`G.45 <G.45>`, :ref:`G.46 <G.46>`, :ref:`G.47 <G.47>`, :ref:`G.48 <G.48>`, :ref:`G.49 <G.49>`, :ref:`G.50 <G.50>`, :ref:`G.51 <G.51>`, :ref:`G.52 <G.52>`, :ref:`G.53 <G.53>`, :ref:`G.54 <G.54>`, :ref:`G.55 <G.55>`, :ref:`G.56 <G.56>`, :ref:`G.57 <G.57>`, :ref:`G.58 <G.58>`, :ref:`G.59 <G.59>`, :ref:`G.60 <G.60>`, :ref:`G.61 <G.61>`
