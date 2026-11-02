:canonical_id: G.368
:original_id: IX.35
:title: G.368 many numbers please
:volume: II
:book: IX
:type: prop

G.368 many numbers please — Heath
=================================

.. rubric:: `IX.35 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/35/>`_

.. enunciation::

   If as many :term:`numbers <G.248>` as we please be in :term:`continued proportion <G.180>`, and there be subtracted from the second and the last numbers equal to the first, then, as the excess of the second is to the first, so will the excess of the last be to all those before it.

Let there be as many numbers as we please in continued proportion, :g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />`, :g:`D <g1:D>`, :g:`/ E F / <g1:/ E F />`, beginning from :g:`A <g1:A>` as least, and let there be subtracted from :g:`/ B C / <g1:/ B C />` and :g:`/ E F / <g1:/ E F />` the numbers :g:`/ B G / <g1:/ B G />`, :g:`/ F H / <g1:/ F H />`, each :eq:`equal <g1:/ B G / = g1:/ F H / = g1:A>` to :g:`A <g1:A>`;

I say that, as :g:`/ C G / <g1:/ C G />` is to :g:`A <g1:A>`, so is :g:`/ E H / <g1:/ E H />` to :g:`A <g1:A>`, :g:`/ B C / <g1:/ B C />`, :g:`D <g1:D>`.

.. picture:: g1.svg
   :alt: Proposition 35 Diagram

For let :g:`/ F K / <g1:/ F K />` be made :eq:`equal <g1:/ F K / = g1:/ B C />` to :g:`/ B C / <g1:/ B C />`, and :g:`/ F L / <g1:/ F L />` :eq:`equal <g1:/ F L / = g1:D>` to :g:`D <g1:D>`.

.. subclause::

   Then, since :g:`/ F K / <g1:/ F K />` is :eq:`equal <g1:/ F K / = g1:/ B C />` to :g:`/ B C / <g1:/ B C />`, and of these the part :g:`/ F H / <g1:/ F H />` is :eq:`equal <g1:/ F H / = g1:/ B G />` to the part :g:`/ B G / <g1:/ B G />`,

.. assertion::

   therefore the remainder :g:`/ H K / <g1:/ H K />` is :eq:`equal <g1:/ H K / = g1:/ C G />` to the remainder :g:`/ C G / <g1:/ C G />`.

.. subclause::

   And since, as :g:`/ E F / <g1:/ E F />` is to :g:`D <g1:D>`, so is :g:`D <g1:D>` to :g:`/ B C / <g1:/ B C />`, and :g:`/ B C / <g1:/ B C />` to :g:`A <g1:A>`, while :g:`D <g1:D>` is :eq:`equal <g1:D = g1:/ F L /; g1:/ B C / = g1:/ F K /; g1:A = g1:/ F H />` to :g:`/ F L / <g1:/ F L />`, :g:`/ B C / <g1:/ B C />` to :g:`/ F K / <g1:/ F K />`, and :g:`A <g1:A>` to :g:`/ F H / <g1:/ F H />`,

.. assertion::

   therefore, as :g:`/ E F / <g1:/ E F />` is to :g:`/ F L / <g1:/ F L />`, so is :g:`/ F L / <g1:/ F L />` to :g:`/ F K / <g1:/ F K />`, and :g:`/ F K / <g1:/ F K />` to :g:`/ F H / <g1:/ F H />`.

.. assertion::

   :term:`Separando <G.197>`, as :g:`/ E L / <g1:/ E L />` is to :g:`/ F L / <g1:/ F L />`, so is :g:`/ K L / <g1:/ K L />` to :g:`/ F K / <g1:/ F K />`, and :g:`/ H K / <g1:/ H K />` to :g:`/ F H / <g1:/ F H />`. :just:`[G.264, G.266] <G.264, G.266>`

.. assertion::

   Therefore also, as one of the :term:`antecedents <G.181>` is to one of the consequents, so are all the antecedents to all the consequents; :just:`[G.265] <G.265>` therefore, as :g:`/ H K / <g1:/ H K />` is to :g:`/ F H / <g1:/ F H />`, so are :g:`/ E L / <g1:/ E L />`, :g:`/ K L / <g1:/ K L />`, :g:`/ H K / <g1:/ H K />` to :g:`/ F L / <g1:/ F L />`, :g:`/ F K / <g1:/ F K />`, :g:`/ F H / <g1:/ F H />`.

.. subclause::

   But :g:`/ H K / <g1:/ H K />` is :eq:`equal <g1:/ H K / = g1:/ C G /; g1:/ F H / = g1:A; g1:/ F L / = g1:D; g1:/ F K / = g1:/ B C />` to :g:`/ C G / <g1:/ C G />`, :g:`/ F H / <g1:/ F H />` to :g:`A <g1:A>`, and :g:`/ F L / <g1:/ F L />`, :g:`/ F K / <g1:/ F K />`, :g:`/ F H / <g1:/ F H />` to :g:`D <g1:D>`, :g:`/ B C / <g1:/ B C />`, :g:`A <g1:A>`;

.. assertion::

   therefore, as :g:`/ C G / <g1:/ C G />` is to :g:`A <g1:A>`, so is :g:`/ E H / <g1:/ E H />` to :g:`D <g1:D>`, :g:`/ B C / <g1:/ B C />`, :g:`A <g1:A>`.

.. assertion::

   Therefore, as the excess of the second is to the first, so is the excess of the last to all those before it.

.. qed::

   :just:`Q. E. D.`

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.170" [label="G.170", tooltip="G.170 (V.def.2): The greater is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.176" [label="G.176", tooltip="G.176 (V.def.5): Magnitudes are said tobe in the same ratio, the first to the second and the third to the fourth, when, if anyequimultiples whatever be taken of the first and third, and any equimul...", fillcolor="#224422", URL="../G.176/index.html", target="_top"];
     "G.180" [label="G.180", tooltip="G.180 (V.def.6): Let magnitudes which have thesame ratio be calledproportional.", fillcolor="#224422", URL="../G.180/index.html", target="_top"];
     "G.181" [label="G.181", tooltip="G.181 (V.def.11): The termcorresponding magnitudes is used of antecedents in relation to antecedents, and of consequents in relation to consequents.", fillcolor="#224422", URL="../G.181/index.html", target="_top"];
     "G.194" [label="G.194", tooltip="G.194 (V.def.12): Alternate ratio means taking theantecedent in relation to the antecedent and the consequent in relation to the consequent.", fillcolor="#224422", URL="../G.194/index.html", target="_top"];
     "G.197" [label="G.197", tooltip="G.197 (V.def.15): Separation of a ratio means taking the excess by which theantecedent exceeds the consequent in relation to the consequent by itself.", fillcolor="#224422", URL="../G.197/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.254" [label="G.254", tooltip="G.254 (VII.def.4): Butparts when it does notmeasure it.", fillcolor="#224422", URL="../G.254/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.257" [label="G.257", tooltip="G.257 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.257/index.html", target="_top"];
     "G.258" [label="G.258", tooltip="G.258 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.258/index.html", target="_top"];
     "G.259" [label="G.259", tooltip="G.259 (VII.7): If a number be that part of a number, which a number subtracted is of a number subtracted, the remainder is the same part of the remainder that the whole is of the whole.", fillcolor="#222244", URL="../G.259/index.html", target="_top"];
     "G.260" [label="G.260", tooltip="G.260 (VII.8): If a number be the same parts of a number that a number subtracted is of a number subtracted, the remainder is the same parts of the remainder that the whole is of the whole.", fillcolor="#222244", URL="../G.260/index.html", target="_top"];
     "G.261" [label="G.261", tooltip="G.261 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.261/index.html", target="_top"];
     "G.262" [label="G.262", tooltip="G.262 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.262/index.html", target="_top"];
     "G.263" [label="G.263", tooltip="G.263 (VII.def.20): Numbers areproportional when the first is thesame multiple, or thesame part, or thesame parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.263/index.html", target="_top"];
     "G.264" [label="G.264", tooltip="G.264 (VII.11): If, as whole is to whole, so is a number subtracted to a number subtracted, the remainder is to the remainder as whole to whole.", fillcolor="#222244", URL="../G.264/index.html", target="_top"];
     "G.265" [label="G.265", tooltip="G.265 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.265/index.html", target="_top"];
     "G.266" [label="G.266", tooltip="G.266 (VII.13): If four numbers be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.266/index.html", target="_top"];
     "G.368" [label="G.368", tooltip="G.368 (IX.35): If as many numbers as we please be in continued proportion, and there be subtracted from the second and the last numbers equal to the first, then, as the excess of the second is to...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.170" -> "G.169";
     "G.253" -> "G.169";
     "G.254" -> "G.169";
     "G.256" -> "G.169";
     "G.176" -> "G.170";
     "G.257" -> "G.170";
     "G.180" -> "G.176";
     "G.266" -> "G.180";
     "G.368" -> "G.180";
     "G.194" -> "G.181";
     "G.197" -> "G.181";
     "G.265" -> "G.181";
     "G.261" -> "G.194";
     "G.262" -> "G.194";
     "G.266" -> "G.194";
     "G.368" -> "G.197";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.256" -> "G.248";
     "G.257" -> "G.248";
     "G.258" -> "G.248";
     "G.259" -> "G.248";
     "G.260" -> "G.248";
     "G.261" -> "G.248";
     "G.262" -> "G.248";
     "G.264" -> "G.248";
     "G.265" -> "G.248";
     "G.266" -> "G.248";
     "G.368" -> "G.248";
     "G.257" -> "G.253";
     "G.259" -> "G.253";
     "G.261" -> "G.253";
     "G.262" -> "G.253";
     "G.263" -> "G.253";
     "G.258" -> "G.254";
     "G.260" -> "G.254";
     "G.261" -> "G.254";
     "G.262" -> "G.254";
     "G.263" -> "G.254";
     "G.257" -> "G.256";
     "G.263" -> "G.256";
     "G.258" -> "G.257";
     "G.259" -> "G.257";
     "G.261" -> "G.257";
     "G.262" -> "G.257";
     "G.265" -> "G.257";
     "G.261" -> "G.258";
     "G.262" -> "G.258";
     "G.265" -> "G.258";
     "G.260" -> "G.259";
     "G.264" -> "G.259";
     "G.264" -> "G.260";
     "G.262" -> "G.261";
     "G.266" -> "G.262";
     "G.264" -> "G.263";
     "G.265" -> "G.263";
     "G.266" -> "G.263";
     "G.368" -> "G.264";
     "G.368" -> "G.265";
     "G.368" -> "G.266";
   }

Required for
------------

:ref:`G.370 <G.370>`
