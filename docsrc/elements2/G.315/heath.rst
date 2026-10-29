:canonical_id: G.315
:original_id: X.2
:volume: III
:book: X
:type: prop

G.315 — Heath
=============

.. rubric:: `X.2 <https://geometor.github.io/euclid/heath/volume_III/book_x/propositions/002/>`_

.. enunciation::

   If, when the less of two unequal magnitudes is continually subtracted in turn from the greater, that which is left never measures the one before it, the magnitudes will be incommensurable.

For, there being two unequal magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`, and :g:`/ A B / <g1:/ A B />` being the less, when the less is continually subtracted in turn from the greater, let that which is left over never measure the one before it; I say that the magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` are incommensurable.

.. picture:: g1.svg
   :alt: Book X, Proposition 2

For, if they are commensurable, some magnitude will measure them.

Let a magnitude measure them, if possible, and let it be :g:`E <g1:E>`; let :g:`/ A B / <g1:/ A B />`, measuring :g:`/ F D / <g1:/ F D />`, leave :g:`/ C F / <g1:/ C F />` less than itself, let :g:`/ C F / <g1:/ C F />` measuring :g:`/ B G / <g1:/ B G />`, leave :g:`/ A G / <g1:/ A G />` less than itself, and let this process be repeated continually, until there is left some magnitude which is less than :g:`E <g1:E>`.

Suppose this done, and let there be left :g:`/ A G / <g1:/ A G />` less than :g:`E <g1:E>`.

.. subclause::

   Then, since :g:`E <g1:E>` measures :g:`/ A B / <g1:/ A B />`, while :g:`/ A B / <g1:/ A B />` measures :g:`/ D F / <g1:/ D F />`,

.. assertion::

   therefore :g:`E <g1:E>` will also measure :g:`/ F D / <g1:/ F D />`.

.. subclause::

   But it measures the whole :g:`/ C D / <g1:/ C D />` also;

.. assertion::

   therefore it will also measure the remainder :g:`/ C F / <g1:/ C F />`.

.. subclause::

   But :g:`/ C F / <g1:/ C F />` measures :g:`/ B G / <g1:/ B G />`;

.. assertion::

   therefore :g:`E <g1:E>` also measures :g:`/ B G / <g1:/ B G />`.

.. subclause::

   But it measures the whole :g:`/ A B / <g1:/ A B />` also;

.. assertion::

   therefore it will also measure the remainder :g:`/ A G / <g1:/ A G />`, the greater the less :

.. assertion::

   which is impossible.

.. assertion::

   Therefore no magnitude will measure the magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />`; therefore the magnitudes :g:`/ A B / <g1:/ A B />`, :g:`/ C D / <g1:/ C D />` are incommensurable. :just:`[G.314] <G.314>`

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
     "G.314" [label="G.314", tooltip="G.314 (X.def.1): Those magnitudes are said to becommensurable which are measured by the same measure, and thoseincommensurable which cannot have any common measure.", fillcolor="#224422", URL="../G.314/index.html", target="_top"];
     "G.315" [label="G.315", tooltip="G.315 (X.2): If, when the less of two unequal magnitudes is continually subtracted in turn from the greater, that which is left never measures the one before it, the magnitudes is incommensurab...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.315" -> "G.314";
   }

Required for
------------

:ref:`G.316 <G.316>`, :ref:`G.317 <G.317>`
