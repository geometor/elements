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

.. signature:: problem

   | :fn:`commensurable_magnitudes_find <G.316>`\ (:g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`)
   | **given** the two given commensurable magnitudes be :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` of which :g:`/ A B / <g1:/ A B />` is the less
   | **construct** PORISM. From this it is manifest that, if a magnitude measure two magnitudes, it will also measure their greatest common measure

.. picture:: g1.svg
   :alt: Book X, Proposition 3

.. step:: given

   the two given commensurable magnitudes be :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` of which :g:`/ A B / <g1:/ A B />` is the less

.. step:: assert

   Now the magnitude :g:`/ A B / <g1:/ A B />` either measures :g:`/ C D / <g1:/ C D />` or it does not.

.. step:: assert

   If then it measures it—and it measures itself also—:g:`/ A B / <g1:/ A B />` is a common measure of :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   It is manifest that it is also the greatest ; for a greater magnitude than the magnitude :g:`/ A B / <g1:/ A B />` will not measure :g:`/ A B / <g1:/ A B />`.

.. step:: assert

   Next, let :g:`/ A B / <g1:/ A B />` not measure :g:`/ C D / <g1:/ C D />`

.. step:: assert ∵ less_unequal_magnitudes <G.315>

   If the less be continually subtracted in turn from the greater, that which is left over will sometime measure the one before it, because :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` are not incommensurable

.. step:: assert

   Let :g:`/ A B / <g1:/ A B />`, measuring :g:`/ E D / <g1:/ E D />`, leave :g:`/ E C / <g1:/ E C />` less than itself, let :g:`/ E C / <g1:/ E C />`, measuring :g:`/ F B / <g1:/ F B />`, leave :g:`/ A F / <g1:/ A F />` less than itself, and let :g:`/ A F / <g1:/ A F />` measure :g:`/ C E / <g1:/ C E />`.

.. step:: assert

   Since, then, :g:`/ A F / <g1:/ A F />` measures :g:`/ C E / <g1:/ C E />`, while :g:`/ C E / <g1:/ C E />` measures :g:`/ F B / <g1:/ F B />`,

.. step:: assert

   Therefore :g:`/ A F / <g1:/ A F />` will also measure :g:`/ F B / <g1:/ F B />`.

.. step:: assert

   It measures itself also ;

.. step:: assert

   Therefore :g:`/ A F / <g1:/ A F />` will also measure the whole :g:`/ A B / <g1:/ A B />`.

.. step:: assert

   :g:`/ A B / <g1:/ A B />` measures :g:`/ D E / <g1:/ D E />` ;

.. step:: assert

   Therefore :g:`/ A F / <g1:/ A F />` will also measure :g:`/ E D / <g1:/ E D />`.

.. step:: assert

   It measures :g:`/ C E / <g1:/ C E />` also ;

.. step:: assert

   Therefore it also measures the whole :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   Therefore :g:`/ A F / <g1:/ A F />` is a common measure of :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`.

.. step:: assert

   I say next that it is also the greatest.

.. step:: assert

   If not, there will be some magnitude greater than :g:`/ A F / <g1:/ A F />` which will measure :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`

.. step:: assert

   Let it be :g:`G <g1:G>`.

.. step:: assert

   Since then :g:`G <g1:G>` measures :g:`/ A B / <g1:/ A B />`, while :g:`/ A B / <g1:/ A B />` measures :g:`/ E D / <g1:/ E D />`,

.. step:: assert

   Therefore :g:`G <g1:G>` will also measure :g:`/ E D / <g1:/ E D />`.

.. step:: assert

   It measures the whole :g:`/ C D / <g1:/ C D />` also ;

.. step:: assert

   Therefore :g:`G <g1:G>` will also measure the remainder :g:`/ C E / <g1:/ C E />`.

.. step:: assert

   :g:`/ C E / <g1:/ C E />` measures :g:`/ F B / <g1:/ F B />` ;

.. step:: assert

   Therefore :g:`G <g1:G>` will also measure :g:`/ F B / <g1:/ F B />`.

.. step:: assert

   It measures the whole :g:`/ A B / <g1:/ A B />` also,

.. step:: assert

   And it will therefore measure the remainder :g:`/ A F / <g1:/ A F />`, the greater the less : which is impossible.

.. step:: assert

   Therefore no magnitude greater than :g:`/ A F / <g1:/ A F />` will measure :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` ; therefore :g:`/ A F / <g1:/ A F />` is the greatest common measure of :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`.

.. step:: conclude

   PORISM. From this it is manifest that, if a magnitude measure two magnitudes, it will also measure their greatest common measure.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.314" [label="G.314", tooltip="G.314 (X.def.1): Those magnitudes are said to becommensurable which are measured by the same measure, and thoseincommensurable which cannot have any common measure.", fillcolor="#224422", URL="../G.314/index.html", target="_top"];
     "G.315" [label="G.315", tooltip="G.315 (X.2): If, when the less of two unequal magnitudes is continually subtracted in turn from the greater, that which is left never measures the one before it, the magnitudes is incommensurab...", fillcolor="#222244", URL="../G.315/index.html", target="_top"];
     "G.316" [label="G.316", tooltip="G.316 (X.3): Given two commensurable magnitudes, to find their greatest common measure.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.315" -> "G.314";
     "G.316" -> "G.315";
   }

Required for
------------

:ref:`G.317 <G.317>`

.. toctree::
   :hidden:

   code
   heath
