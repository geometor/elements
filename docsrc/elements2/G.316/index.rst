:order: 316
:number: 316
:canonical_id: G.316
:original_id: X.3
:volume: III
:book: X
:type: prop
:subtype: problem
:categories: problem, finding, incommensurables, magnitudes
:category: problem, finding, incommensurables, magnitudes
:tags: book-x, point, segment, commensurable, greatest-common-measure, reductio-ad-absurdum, porism
:dependencies: G.315
:excerpt: Given two commensurable magnitudes, to find their greatest common measure.

.. _G.316:
.. _X.3:

G.316
=====

.. rubric:: `X.3 <https://geometor.github.io/euclid/heath/volume_III/book_x/propositions/003/>`_

.. enunciation::

   Given two commensurable magnitudes, to find their greatest common measure.

Let the two given commensurable magnitudes be :g:`/ A B / <0024.g1:/ A B />`, :g:`/ C D / <0024.g1:/ C D />` of which :g:`/ A B / <0024.g1:/ A B />` is the less ; thus it is required to find the greatest common measure of :g:`/ A B / <0024.g1:/ A B />`, :g:`/ C D / <0024.g1:/ C D />`.

Now the magnitude :g:`/ A B / <0024.g1:/ A B />` either measures :g:`/ C D / <0024.g1:/ C D />` or it does not.

.. assertion::

   If then it measures it—and it measures itself also—:g:`/ A B / <0024.g1:/ A B />` is a common measure of :g:`/ A B / <0024.g1:/ A B />`, :g:`/ C D / <0024.g1:/ C D />`.

.. assertion::

   And it is manifest that it is also the greatest ; for a greater magnitude than the magnitude :g:`/ A B / <0024.g1:/ A B />` will not measure :g:`/ A B / <0024.g1:/ A B />`.

.. picture:: 0024.g1.svg
   :alt: Book X, Proposition 3

Next, let :g:`/ A B / <0024.g1:/ A B />` not measure :g:`/ C D / <0024.g1:/ C D />`. Then, if the less be continually subtracted in turn from the greater, that which is left over will sometime measure the one before it, because :g:`/ A B / <0024.g1:/ A B />`, :g:`/ C D / <0024.g1:/ C D />` are not incommensurable ; :just:`[G.315] <G.315>` let :g:`/ A B / <0024.g1:/ A B />`, measuring :g:`/ E D / <0024.g1:/ E D />`, leave :g:`/ E C / <0024.g1:/ E C />` less than itself, let :g:`/ E C / <0024.g1:/ E C />`, measuring :g:`/ F B / <0024.g1:/ F B />`, leave :g:`/ A F / <0024.g1:/ A F />` less than itself, and let :g:`/ A F / <0024.g1:/ A F />` measure :g:`/ C E / <0024.g1:/ C E />`.

.. subclause::

   Since, then, :g:`/ A F / <0024.g1:/ A F />` measures :g:`/ C E / <0024.g1:/ C E />`, while :g:`/ C E / <0024.g1:/ C E />` measures :g:`/ F B / <0024.g1:/ F B />`,

.. assertion::

   therefore :g:`/ A F / <0024.g1:/ A F />` will also measure :g:`/ F B / <0024.g1:/ F B />`.

.. subclause::

   But it measures itself also ;

.. assertion::

   therefore :g:`/ A F / <0024.g1:/ A F />` will also measure the whole :g:`/ A B / <0024.g1:/ A B />`.

.. subclause::

   But :g:`/ A B / <0024.g1:/ A B />` measures :g:`/ D E / <0024.g1:/ D E />` ;

.. assertion::

   therefore :g:`/ A F / <0024.g1:/ A F />` will also measure :g:`/ E D / <0024.g1:/ E D />`.

.. subclause::

   But it measures :g:`/ C E / <0024.g1:/ C E />` also ;

.. assertion::

   therefore it also measures the whole :g:`/ C D / <0024.g1:/ C D />`.

.. assertion::

   Therefore :g:`/ A F / <0024.g1:/ A F />` is a common measure of :g:`/ A B / <0024.g1:/ A B />`, :g:`/ C D / <0024.g1:/ C D />`.

I say next that it is also the greatest.

For, if not, there will be some magnitude greater than :g:`/ A F / <0024.g1:/ A F />` which will measure :g:`/ A B / <0024.g1:/ A B />`, :g:`/ C D / <0024.g1:/ C D />`. Let it be :g:`G <0024.g1:G>`.

.. subclause::

   Since then :g:`G <0024.g1:G>` measures :g:`/ A B / <0024.g1:/ A B />`, while :g:`/ A B / <0024.g1:/ A B />` measures :g:`/ E D / <0024.g1:/ E D />`,

.. assertion::

   therefore :g:`G <0024.g1:G>` will also measure :g:`/ E D / <0024.g1:/ E D />`.

.. subclause::

   But it measures the whole :g:`/ C D / <0024.g1:/ C D />` also ;

.. assertion::

   therefore :g:`G <0024.g1:G>` will also measure the remainder :g:`/ C E / <0024.g1:/ C E />`.

.. subclause::

   But :g:`/ C E / <0024.g1:/ C E />` measures :g:`/ F B / <0024.g1:/ F B />` ;

.. assertion::

   therefore :g:`G <0024.g1:G>` will also measure :g:`/ F B / <0024.g1:/ F B />`.

.. subclause::

   But it measures the whole :g:`/ A B / <0024.g1:/ A B />` also,

.. assertion::

   and it will therefore measure the remainder :g:`/ A F / <0024.g1:/ A F />`, the greater the less : which is impossible.

.. assertion::

   Therefore no magnitude greater than :g:`/ A F / <0024.g1:/ A F />` will measure :g:`/ A B / <0024.g1:/ A B />`, :g:`/ C D / <0024.g1:/ C D />` ; therefore :g:`/ A F / <0024.g1:/ A F />` is the greatest common measure of :g:`/ A B / <0024.g1:/ A B />`, :g:`/ C D / <0024.g1:/ C D />`.

.. qed::

   Therefore the greatest common measure of the two given commensurable magnitudes :g:`/ A B / <0024.g1:/ A B />`, :g:`/ C D / <0024.g1:/ C D />` has been found. :just:`Q. E. D.`

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
     "G.314" [label="G.314", tooltip="G.314 (X.def.1): Those magnitudes are said to be commensurable which are measured by the same measure, and those incommensurable which cannot have any common measure.", fillcolor="#224422", URL="../G.314/index.html", target="_top"];
     "G.315" [label="G.315", tooltip="G.315 (X.2): If, when the less of two unequal magnitudes is continually subtracted in turn from the greater, that which is left never measures the one before it, the magnitudes will be incommen...", fillcolor="#222244", URL="../G.315/index.html", target="_top"];
     "G.316" [label="G.316", tooltip="G.316 (X.3): Given two commensurable magnitudes, to find their greatest common measure.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.315" -> "G.314";
     "G.316" -> "G.315";
   }

Required for
------------

:ref:`G.317 <G.317>`
