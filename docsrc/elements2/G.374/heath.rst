:canonical_id: G.374
:original_id: X.3
:title: G.374 commensurable magnitudes find
:volume: III
:book: X
:type: prop

G.374 commensurable magnitudes find — Heath
===========================================

.. rubric:: `X.3 <https://geometor.github.io/euclid/heath/volume_III/book_x/propositions/003/>`_

.. enunciation::

   Given two :term:`commensurable <G.372>` magnitudes, to find their greatest common :term:`measure <G.253>`.

Let the two given commensurable magnitudes be :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` of which :g:`/ A B / <g1:/ A B />` is the less ; thus it is required to find the greatest common measure of :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`.

Now the magnitude :g:`/ A B / <g1:/ A B />` either measures :g:`/ C D / <g1:/ C D />` or it does not.

.. assertion::

   If then it measures it—and it measures itself also—:g:`/ A B / <g1:/ A B />` is a common measure of :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`.

.. assertion::

   And it is manifest that it is also the greatest ; for a greater magnitude than the magnitude :g:`/ A B / <g1:/ A B />` will not measure :g:`/ A B / <g1:/ A B />`.

.. picture:: g1.svg
   :alt: Book X, Proposition 3

Next, let :g:`/ A B / <g1:/ A B />` not measure :g:`/ C D / <g1:/ C D />`. Then, if the less be continually subtracted in turn from the greater, that which is left over will sometime measure the one before it, because :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` are not incommensurable ; :just:`[G.373] <G.373>` let :g:`/ A B / <g1:/ A B />`, measuring :g:`/ E D / <g1:/ E D />`, leave :g:`/ E C / <g1:/ E C />` less than itself, let :g:`/ E C / <g1:/ E C />`, measuring :g:`/ F B / <g1:/ F B />`, leave :g:`/ A F / <g1:/ A F />` less than itself, and let :g:`/ A F / <g1:/ A F />` measure :g:`/ C E / <g1:/ C E />`.

.. subclause::

   Since, then, :g:`/ A F / <g1:/ A F />` measures :g:`/ C E / <g1:/ C E />`, while :g:`/ C E / <g1:/ C E />` measures :g:`/ F B / <g1:/ F B />`,

.. assertion::

   therefore :g:`/ A F / <g1:/ A F />` will also measure :g:`/ F B / <g1:/ F B />`.

.. subclause::

   But it measures itself also ;

.. assertion::

   therefore :g:`/ A F / <g1:/ A F />` will also measure the whole :g:`/ A B / <g1:/ A B />`.

.. subclause::

   But :g:`/ A B / <g1:/ A B />` measures :g:`/ D E / <g1:/ D E />` ;

.. assertion::

   therefore :g:`/ A F / <g1:/ A F />` will also measure :g:`/ E D / <g1:/ E D />`.

.. subclause::

   But it measures :g:`/ C E / <g1:/ C E />` also ;

.. assertion::

   therefore it also measures the whole :g:`/ C D / <g1:/ C D />`.

.. assertion::

   Therefore :g:`/ A F / <g1:/ A F />` is a common measure of :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`.

I say next that it is also the greatest.

For, if not, there will be some magnitude greater than :g:`/ A F / <g1:/ A F />` which will measure :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`. Let it be :g:`G <g1:G>`.

.. subclause::

   Since then :g:`G <g1:G>` measures :g:`/ A B / <g1:/ A B />`, while :g:`/ A B / <g1:/ A B />` measures :g:`/ E D / <g1:/ E D />`,

.. assertion::

   therefore :g:`G <g1:G>` will also measure :g:`/ E D / <g1:/ E D />`.

.. subclause::

   But it measures the whole :g:`/ C D / <g1:/ C D />` also ;

.. assertion::

   therefore :g:`G <g1:G>` will also measure the remainder :g:`/ C E / <g1:/ C E />`.

.. subclause::

   But :g:`/ C E / <g1:/ C E />` measures :g:`/ F B / <g1:/ F B />` ;

.. assertion::

   therefore :g:`G <g1:G>` will also measure :g:`/ F B / <g1:/ F B />`.

.. subclause::

   But it measures the whole :g:`/ A B / <g1:/ A B />` also,

.. assertion::

   and it will therefore measure the remainder :g:`/ A F / <g1:/ A F />`, the greater the less : which is impossible.

.. assertion::

   Therefore no magnitude greater than :g:`/ A F / <g1:/ A F />` will measure :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` ; therefore :g:`/ A F / <g1:/ A F />` is the greatest common measure of :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`.

.. qed::

   Therefore the greatest common measure of the two given commensurable magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` has been found. :just:`Q. E. D.`

.. assertion::

   PORISM. From this it is manifest that, if a magnitude measure two magnitudes, it will also measure their greatest common measure.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.372" [label="G.372", tooltip="G.372 (X.def.1): Those magnitudes are said to becommensurable which aremeasured by the same measure, and thoseincommensurable which cannot have any common measure.", fillcolor="#224422", URL="../G.372/index.html", target="_top"];
     "G.373" [label="G.373", tooltip="G.373 (X.2): If, when the less of two unequal magnitudes is continually subtracted in turn from the greater, that which is left never measures the one before it, the magnitudes is incommensurab...", fillcolor="#222244", URL="../G.373/index.html", target="_top"];
     "G.374" [label="G.374", tooltip="G.374 (X.3): Given two commensurable magnitudes, to find their greatest common measure.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.253" -> "G.169";
     "G.372" -> "G.169";
     "G.373" -> "G.169";
     "G.374" -> "G.169";
     "G.248" -> "G.247";
     "G.253" -> "G.248";
     "G.372" -> "G.253";
     "G.373" -> "G.372";
     "G.374" -> "G.372";
     "G.374" -> "G.373";
   }

Required for
------------

:ref:`G.375 <G.375>`
