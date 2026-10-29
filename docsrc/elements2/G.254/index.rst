:order: 254
:number: 254
:canonical_id: G.254
:original_id: VIII.13
:volume: II
:book: VIII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory, proportions
:category: theorem, proof, number-theory, proportions
:tags: book-viii, point, ex-aequali, proportion, number, continued-proportion
:dependencies: G.214
:excerpt: If there be as many numbers as we please in continued proportion, and each by multiplying itself make some number, the products is proportional; and, if the original numbers by multiplying the products make certain numbers, the latter is proportional.

.. _G.254:
.. _VIII.13:

G.254
=====

.. rubric:: `VIII.13 <https://geometor.github.io/euclid/heath/volume_II/book_viii/propositions/13/>`_

.. enunciation::

   If there be as many numbers as we please in continued proportion, and each by multiplying itself make some number, the products is proportional; and, if the original numbers by multiplying the products make certain numbers, the latter is proportional.

.. picture:: g1.svg
   :alt: Book VIII, Proposition 13

.. step:: given

   there be as many numbers as we please, :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, in continued proportion, so that, as :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`B <g1:B>` to :g:`C <g1:C>`

.. step:: assert

   Let :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` by multiplying themselves make :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`F <g1:F>`, and by multiplying :g:`D <g1:D>`, :g:`E <g1:E>`, :g:`F <g1:F>` let them make :g:`G <g1:G>`, :g:`H <g1:H>`, :g:`K <g1:K>`

.. step:: assert

   For let :g:`A <g1:A>` by multiplying :g:`B <g1:B>` make :g:`L <g1:L>`

.. step:: assert

   Let the numbers :g:`A <g1:A>`, :g:`B <g1:B>` by multiplying :g:`L <g1:L>` make :g:`M <g1:M>`, :g:`N <g1:N>` respectively.

.. step:: assert

   Again let :g:`B <g1:B>` by multiplying :g:`C <g1:C>` make :g:`O <g1:O>`

.. step:: assert

   Let the numbers :g:`B <g1:B>`, :g:`C <g1:C>` by multiplying :g:`O <g1:O>` make :g:`P <g1:P>`, :g:`Q <g1:Q>` respectively.

.. step:: assert

   In manner similar to the foregoing, we can prove that :g:`D <g1:D>`, :g:`L <g1:L>`, :g:`E <g1:E>` and :g:`G <g1:G>`, :g:`M <g1:M>`, :g:`N <g1:N>`, :g:`H <g1:H>` are continuously proportional in the ratio of :g:`A <g1:A>` to :g:`B <g1:B>`, and further :g:`E <g1:E>`, :g:`O <g1:O>`, :g:`F <g1:F>` and :g:`H <g1:H>`, :g:`P <g1:P>`, :g:`Q <g1:Q>`, :g:`K <g1:K>` are continuously proportional in the ratio of :g:`B <g1:B>` to :g:`C <g1:C>`.

.. step:: assert

   As :g:`A <g1:A>` is to :g:`B <g1:B>`, so is :g:`B <g1:B>` to :g:`C <g1:C>`;

.. step:: assert

   Therefore :g:`D <g1:D>`, :g:`L <g1:L>`, :g:`E <g1:E>` are also in the same ratio with :g:`E <g1:E>`, :g:`O <g1:O>`, :g:`F <g1:F>`, and further :g:`G <g1:G>`, :g:`M <g1:M>`, :g:`N <g1:N>`, :g:`H <g1:H>` in the same ratio with :g:`H <g1:H>`, :g:`P <g1:P>`, :g:`Q <g1:Q>`, :g:`K <g1:K>`.

.. step:: assert

   The multitude of :g:`D <g1:D>`, :g:`L <g1:L>`, :g:`E <g1:E>` is equal to the multitude of :g:`E <g1:E>`, :g:`O <g1:O>`, :g:`F <g1:F>`, and that of :g:`G <g1:G>`, :g:`M <g1:M>`, :g:`N <g1:N>`, :g:`H <g1:H>` to that of :g:`H <g1:H>`, :g:`P <g1:P>`, :g:`Q <g1:Q>`, :g:`K <g1:K>`;

.. step:: assert [G.214] <G.214>

   Therefore, :term:`*ex aequali* <ex-aequali>`, as :g:`D <g1:D>` is to :g:`E <g1:E>`, so is :g:`E <g1:E>` to :g:`F <g1:F>`, and, as :g:`G <g1:G>` is to :g:`H <g1:H>`, so is :g:`H <g1:H>` to :g:`K <g1:K>`.

.. step:: assert

   If $a, b, c \dots$ be a series in geometrical progression, then

.. step:: assert

   $$\left. \begin{array}{l} a^2,\

.. step:: assert

   B^2,\

.. step:: assert

   C^2 \dots \\ a^3,\

.. step:: assert

   B^3,\

.. step:: assert

   C^3 \dots \end{array} \right\} \text{are also in geometrical progression.}$$

.. step:: assert

   :person:`Heiberg <heiberg>` brackets the words added to the enunciation which extend the theorem to any powers. The words are “and this always occurs with the extremes” (καὶ ἀεὶ περὶ τοὺς ἄκρους τοῦτο συμβαίνει). They seem to be rightly suspected on the same grounds as the same words added to the enunciation of VII. 27. There is no allusion to them in the proof, much less any proof of the extension.

.. step:: assert

   Euclid forms, besides the squares and cubes of the given numbers, the products $ab$, $a^2b$, $ab^2$, $bc$, $b^2c$, $bc^2$. When he says that “we prove in manner similar to the foregoing,” he indicates successive uses of VII. 17, 18 as in VIII. 12.

.. step:: assert

   With our notation the proof is as easy to see for *any* powers as for squares and cubes.

.. step:: assert

   To prove that $a^n, b^n, c^n \dots$ are in geometrical progression.

.. step:: assert

   Form all the means between $a^n, b^n$, and set out the series

.. step:: assert

   $$a^n,\quad a^{n-1}b,\quad a^{n-2}b^2\

.. step:: assert

   \dots\

.. step:: assert

   Ab^{n-1},\quad b^n.$$

.. step:: assert

   The common ratio of one term to the next is $a : b$.

.. step:: assert

   Next take the geometrical progression

.. step:: assert

   $$b^n,\quad b^{n-1}c,\quad b^{n-2}c^2\

.. step:: assert

   \dots\

.. step:: assert

   Bc^{n-1},\quad c^n,$$

.. step:: assert

   The common ratio of which is $b : c$.

.. step:: assert

   Proceed thus for all pairs of consecutive terms.

.. step:: assert

   Now

.. step:: assert

   $$a : b = b : c = \dots$$

.. step:: assert

   Therefore any pair of succeeding terms in one series are in the same ratio as any pair of succeeding terms in any other of the series.

.. step:: assert

   The number of terms in each is the same, namely $(n + 1)$.

.. step:: assert

   Therefore, :term:`*ex aequali* <ex-aequali>`,

.. step:: conclude

   $$a^n : b^n = b^n : c^n = c^n : d^n = \dots$$

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.204" [label="G.204", tooltip="G.204 (VII.5): If a number be a part of a number, and another be the same part of another, the sum is the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.204/index.html", target="_top"];
     "G.205" [label="G.205", tooltip="G.205 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum is the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.205/index.html", target="_top"];
     "G.208" [label="G.208", tooltip="G.208 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.208/index.html", target="_top"];
     "G.209" [label="G.209", tooltip="G.209 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.209/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VII.def.20): **Numbers** areproportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.210/index.html", target="_top"];
     "G.213" [label="G.213", tooltip="G.213 (VII.13): If four numbers be proportional, they is proportional alternately.", fillcolor="#222244", URL="../G.213/index.html", target="_top"];
     "G.214" [label="G.214", tooltip="G.214 (VII.14): If there be as many numbers as we please, and others equal to them in multitude, which taken two and two are in the same ratio, they is in the same ratio ex aequali.", fillcolor="#222244", URL="../G.214/index.html", target="_top"];
     "G.254" [label="G.254", tooltip="G.254 (VIII.13): If there be as many numbers as we please in continued proportion, and each by multiplying itself make some number, the products is proportional; and, if the original numbers by mul...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.205" -> "G.204";
     "G.208" -> "G.204";
     "G.209" -> "G.204";
     "G.208" -> "G.205";
     "G.209" -> "G.205";
     "G.209" -> "G.208";
     "G.213" -> "G.209";
     "G.213" -> "G.210";
     "G.214" -> "G.213";
     "G.254" -> "G.214";
   }

.. toctree::
   :hidden:

   code
   heath
