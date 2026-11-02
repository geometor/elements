:canonical_id: G.204
:original_id: V.21
:title: G.204 there magnitudes others
:volume: II
:book: V
:type: prop

G.204 there magnitudes others — Heath
=====================================

.. rubric:: `V.21 <https://geometor.github.io/euclid/heath/volume_II/book_v/propositions/21/>`_

.. enunciation::

   If there be three magnitudes, and others equal to them in multitude, which taken two and two together are :term:`in the same ratio <G.176>`, and the :term:`proportion of them be perturbed <G.203>`, then, if ex aequali the first magnitude is greater than the third, the fourth will also be greater than the sixth; if equal, equal; and if less, less.

Let there be three magnitudes :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, and others :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`F <g1:F>` equal to them in multitude, which taken two and two are in the same ratio, and let the proportion of them be perturbed, so that,

.. assertion::

   as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`,

.. assertion::

   and, as :g:`B <g1:B>` is to :g:`C <g1:C>`, so is :g:`D <g1:D>` to :g:`E <g1:E>`,

and let :g:`A <g1:A>` be greater than :g:`C <g1:C>` :term:`*ex aequali* <G.174>`;

I say that :g:`D <g1:D>` will also be greater than :g:`F <g1:F>`; if :g:`A <g1:A>` is :eq:`equal <g1:A = g1:C>` to :g:`C <g1:C>`, :eq:`equal <g1:D = g1:F>`; and if less, less.

.. picture:: g1.svg
   :alt: Proposition 21

For, since :g:`A <g1:A>` is greater than :g:`C <g1:C>`, and :g:`B <g1:B>` is some other magnitude,

.. assertion:: [G.186] <G.186>

   therefore :g:`A <g1:A>` has to :g:`B <g1:B>` a :term:`greater ratio <G.185>` than :g:`C <g1:C>` has to :g:`B <g1:B>`.

But, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`, and, as :g:`C <g1:C>` is to :g:`B <g1:B>`, :term:`inversely <G.182>`, so is :g:`E <g1:E>` to :g:`D <g1:D>`.

.. assertion:: [G.191] <G.191>

   Therefore also :g:`E <g1:E>` has to :g:`F <g1:F>` a greater ratio than :g:`E <g1:E>` has to :g:`D <g1:D>`.

.. subclause:: [G.188] <G.188>

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
     "G.1" [label="G.1", tooltip="G.1 (I.def.1): A point A is that which has no part.", fillcolor="#224422", URL="../G.1/index.html", target="_top"];
     "G.2" [label="G.2", tooltip="G.2 (I.def.2): A line [ A B ] is a projection of a relationship of two points A, B.", fillcolor="#224422", URL="../G.2/index.html", target="_top"];
     "G.3" [label="G.3", tooltip="G.3 (I.def.3): The extremities of a segment / A B / are points A, B.", fillcolor="#224422", URL="../G.3/index.html", target="_top"];
     "G.8" [label="G.8", tooltip="G.8 (I.def.13): A boundary is the extremity of anything.", fillcolor="#224422", URL="../G.8/index.html", target="_top"];
     "G.9" [label="G.9", tooltip="G.9 (I.def.14): A figure is that which is contained by any boundary or boundaries.", fillcolor="#224422", URL="../G.9/index.html", target="_top"];
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.171" [label="G.171", tooltip="G.171 (V.1): If there be any number of magnitudes whatever which are, respectively, equimultiples of any magnitudes equal in multitude, then, whatever multiple one of the magnitudes is of one, ...", fillcolor="#222244", URL="../G.171/index.html", target="_top"];
     "G.173" [label="G.173", tooltip="G.173 (V.def.3): Aratio is a sort of relation in respect of size between two magnitudes of the same kind.", fillcolor="#224422", URL="../G.173/index.html", target="_top"];
     "G.174" [label="G.174", tooltip="G.174 (V.def.17): Aratioex aequali arises when, there being several magnitudes and another set equal to them in multitude which taken two and two are in the same proportion, as the first is to the l...", fillcolor="#224422", URL="../G.174/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.182" [label="G.182", tooltip="G.182 (V.def.13): Inverse ratio means taking theconsequent as antecedent in relation to the antecedent as consequent.", fillcolor="#224422", URL="../G.182/index.html", target="_top"];
     "G.183" [label="G.183", tooltip="G.183 (V.7): Equal magnitudes have to the same the same ratio, as also has the same to equal magnitudes.", fillcolor="#222244", URL="../G.183/index.html", target="_top"];
     "G.184" [label="G.184", tooltip="G.184 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.184/index.html", target="_top"];
     "G.185" [label="G.185", tooltip="G.185 (V.def.7): When, of theequimultiples, the multiple of the first magnitude exceeds the multiple of the second, but the multiple of the third does not exceed the multiple of the fourth, then th...", fillcolor="#224422", URL="../G.185/index.html", target="_top"];
     "G.186" [label="G.186", tooltip="G.186 (V.8): Of unequal magnitudes, the greater has to the same a greater ratio than the less has; and the same has to the less a greater ratio than it has to the greater.", fillcolor="#222244", URL="../G.186/index.html", target="_top"];
     "G.188" [label="G.188", tooltip="G.188 (V.10): Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.", fillcolor="#222244", URL="../G.188/index.html", target="_top"];
     "G.191" [label="G.191", tooltip="G.191 (V.13): If a first magnitude have to a second the same ratio as a third to a fourth, and the third have to the fourth a greater ratio than a fifth has to a sixth, the first will also have ...", fillcolor="#222244", URL="../G.191/index.html", target="_top"];
     "G.203" [label="G.203", tooltip="G.203 (V.def.18): Aperturbed proportion arises when, there being three magnitudes and another set equal to them in multitude, asantecedent is to consequent among the first magnitudes, so is antecede...", fillcolor="#224422", URL="../G.203/index.html", target="_top"];
     "G.204" [label="G.204", tooltip="G.204 (V.21): If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then, if ex ae...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.2" -> "G.1";
     "G.3" -> "G.1";
     "G.3" -> "G.2";
     "G.8" -> "G.3";
     "G.9" -> "G.8";
     "G.188" -> "G.9";
     "G.170" -> "G.169";
     "G.171" -> "G.170";
     "G.176" -> "G.170";
     "G.185" -> "G.170";
     "G.186" -> "G.171";
     "G.174" -> "G.173";
     "G.188" -> "G.173";
     "G.204" -> "G.174";
     "G.180" -> "G.176";
     "G.183" -> "G.176";
     "G.191" -> "G.176";
     "G.204" -> "G.176";
     "G.183" -> "G.180";
     "G.182" -> "G.181";
     "G.203" -> "G.181";
     "G.183" -> "G.182";
     "G.188" -> "G.183";
     "G.186" -> "G.184";
     "G.188" -> "G.184";
     "G.186" -> "G.185";
     "G.188" -> "G.185";
     "G.191" -> "G.185";
     "G.188" -> "G.186";
     "G.204" -> "G.186";
     "G.204" -> "G.188";
     "G.204" -> "G.191";
     "G.204" -> "G.203";
   }

Required for
------------

:ref:`G.206 <G.206>`
