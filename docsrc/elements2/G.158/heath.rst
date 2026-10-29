:canonical_id: G.158
:original_id: V.21
:volume: II
:book: V
:type: prop

G.158 — Heath
=============

.. rubric:: `V.21 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/21/>`_

.. enunciation::

   If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then, if ex aequali the first magnitude is greater than the third, the fourth will also be greater than the sixth; if equal, equal; and if less, less.

Let there be three magnitudes :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, and others :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`F <g1:F>` equal to them in multitude, which taken two and two are in the same ratio, and let the proportion of them be perturbed, so that,

.. assertion::

   as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`,

.. assertion::

   and, as :g:`B <g1:B>` is to :g:`C <g1:C>`, so is :g:`D <g1:D>` to :g:`E <g1:E>`,

and let :g:`A <g1:A>` be greater than :g:`C <g1:C>` :term:`*ex aequali* <ex-aequali>`;

I say that :g:`D <g1:D>` will also be greater than :g:`F <g1:F>`; if :g:`A <g1:A>` is :eq:`equal <g1:A = g1:C>` to :g:`C <g1:C>`, :eq:`equal <g1:D = g1:F>`; and if less, less.

.. picture:: g1.svg
   :alt: Proposition 21

For, since :g:`A <g1:A>` is greater than :g:`C <g1:C>`, and :g:`B <g1:B>` is some other magnitude,

.. assertion:: [G.145] <G.145>

   therefore :g:`A <g1:A>` has to :g:`B <g1:B>` a greater ratio than :g:`C <g1:C>` has to :g:`B <g1:B>`.

But, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`, and, as :g:`C <g1:C>` is to :g:`B <g1:B>`, inversely, so is :g:`E <g1:E>` to :g:`D <g1:D>`.

.. assertion:: [G.150] <G.150>

   Therefore also :g:`E <g1:E>` has to :g:`F <g1:F>` a greater ratio than :g:`E <g1:E>` has to :g:`D <g1:D>`.

.. subclause:: [G.147] <G.147>

   But that to which the same has a greater ratio is less;

.. assertion::

   therefore :g:`F <g1:F>` is less than :g:`D <g1:D>`;

.. assertion::

   therefore :g:`D <g1:D>` is greater than :g:`F <g1:F>`.

Similarly we can prove that, if :g:`A <g1:A>` be :eq:`equal <g1:A = g1:C>` to :g:`C <g1:C>`, :g:`D <g1:D>` will also be :eq:`equal <g1:D = g1:F>` to :g:`F <g1:F>`; and if less, less.

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
     "G.135" [label="G.135", tooltip="G.135 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.135/index.html", target="_top"];
     "G.138" [label="G.138", tooltip="G.138 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if any equimultiples whatever be taken of the first and third, and any equimu...", fillcolor="#224422", URL="../G.138/index.html", target="_top"];
     "G.142" [label="G.142", tooltip="G.142 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.142/index.html", target="_top"];
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.144" [label="G.144", tooltip="G.144 (V.def.7): When, of the equimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then t...", fillcolor="#224422", URL="../G.144/index.html", target="_top"];
     "G.145" [label="G.145", tooltip="G.145 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.145/index.html", target="_top"];
     "G.147" [label="G.147", tooltip="G.147 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", fillcolor="#222244", URL="../G.147/index.html", target="_top"];
     "G.150" [label="G.150", tooltip="G.150 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.150/index.html", target="_top"];
     "G.158" [label="G.158", tooltip="G.158 (V.21): If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then, if ex ae...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.145" -> "G.135";
     "G.142" -> "G.138";
     "G.150" -> "G.138";
     "G.147" -> "G.142";
     "G.145" -> "G.143";
     "G.145" -> "G.144";
     "G.150" -> "G.144";
     "G.147" -> "G.145";
     "G.158" -> "G.145";
     "G.158" -> "G.147";
     "G.158" -> "G.150";
   }

Required for
------------

:ref:`G.160 <G.160>`
