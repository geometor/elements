:canonical_id: G.317
:original_id: X.4
:volume: III
:book: X
:type: prop

G.317 — Heath
=============

.. rubric:: `X.4 <https://geometor.github.io/euclid/heath/volume_III/book_x/propositions/004/>`_

.. enunciation::

   Given three commensurable magnitudes, to find their greatest common measure.

Let :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` be the three given commensurable magnitudes ; thus it is required to find the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

.. picture:: g1.svg
   :alt: Proposition 4 diagram

Let the greatest common measure of the two magnitudes :g:`A <g1:A>`, :g:`B <g1:B>` be taken, and let it be :g:`D <g1:D>` ; :just:`[G.316] <G.316>` then :g:`D <g1:D>` either measures :g:`C <g1:C>`, or does not measure it.

First, let it measure it.

.. subclause::

   Since then :g:`D <g1:D>` measures :g:`C <g1:C>`, while it also measures :g:`A <g1:A>`, :g:`B <g1:B>`,

.. assertion::

   therefore :g:`D <g1:D>` is a common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

.. assertion::

   And it is manifest that it is also the greatest ; for a greater magnitude than the magnitude :g:`D <g1:D>` does not measure :g:`A <g1:A>`, :g:`B <g1:B>`.

Next, let :g:`D <g1:D>` not measure :g:`C <g1:C>`.

I say first that :g:`C <g1:C>`, :g:`D <g1:D>` are commensurable.

.. subclause::

   For, since :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` are commensurable, some magnitude will measure them, and this will of course measure :g:`A <g1:A>`, :g:`B <g1:B>` also ;

.. assertion::

   so that it will also measure the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, namely :g:`D <g1:D>`. :just:`[G.316] <G.316>`

.. subclause::

   But it also measures :g:`C <g1:C>` ;

.. assertion::

   so that the said magnitude will measure :g:`C <g1:C>`, :g:`D <g1:D>` ; therefore :g:`C <g1:C>`, :g:`D <g1:D>` are commensurable.

Now let their greatest common measure be taken, and let it be :g:`E <g1:E>`. :just:`[G.316] <G.316>`

.. subclause::

   Since then :g:`E <g1:E>` measures :g:`D <g1:D>`, while :g:`D <g1:D>` measures :g:`A <g1:A>`, :g:`B <g1:B>`,

.. assertion::

   therefore :g:`E <g1:E>` will also measure :g:`A <g1:A>`, :g:`B <g1:B>`.

.. subclause::

   But it measures :g:`C <g1:C>` also ;

.. assertion::

   therefore :g:`E <g1:E>` measures :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` ; therefore :g:`E <g1:E>` is a common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

I say next that it is also the greatest.

For, if possible, let there be some magnitude :g:`F <g1:F>` greater than :g:`E <g1:E>`, and let it measure :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

.. subclause::

   Now, since :g:`F <g1:F>` measures :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, it will also measure :g:`A <g1:A>`, :g:`B <g1:B>`, and will measure the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`. :just:`[G.316] <G.316>`

.. subclause::

   But the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>` is :g:`D <g1:D>` ;

.. assertion::

   therefore :g:`F <g1:F>` measures :g:`D <g1:D>`.

.. subclause::

   But it measures :g:`C <g1:C>` also ;

.. assertion::

   therefore :g:`F <g1:F>` measures :g:`C <g1:C>`, :g:`D <g1:D>` ; therefore :g:`F <g1:F>` will also measure the greatest common measure of :g:`C <g1:C>`, :g:`D <g1:D>`. :just:`[G.316] <G.316>`

.. subclause::

   But that is :g:`E <g1:E>` ;

.. assertion::

   therefore :g:`F <g1:F>` will measure :g:`E <g1:E>`, the greater the less : which is impossible.

.. assertion::

   Therefore no magnitude greater than the magnitude :g:`E <g1:E>` will measure :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` ; therefore :g:`E <g1:E>` is the greatest common measure of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` if :g:`D <g1:D>` do not measure :g:`C <g1:C>`, and, if it measure it, :g:`D <g1:D>` is itself the greatest common measure.

.. assertion::

   Therefore the greatest common measure of the three given commensurable magnitudes has been found.

.. assertion::

   PORISM. From this it is manifest that, if a magnitude measure three magnitudes, it will also measure their greatest common measure.

.. qed::

   Similarly too, with more magnitudes, the greatest common measure can be found, and the porism can be extended. :just:`Q. E. D.`

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
     "G.316" [label="G.316", tooltip="G.316 (X.3): Given two commensurable magnitudes, to find their greatest common measure.", fillcolor="#222244", URL="../G.316/index.html", target="_top"];
     "G.317" [label="G.317", tooltip="G.317 (X.4): Given three commensurable magnitudes, to find their greatest common measure.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.315" -> "G.314";
     "G.316" -> "G.315";
     "G.317" -> "G.316";
   }
