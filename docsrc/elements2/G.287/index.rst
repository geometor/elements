:order: 287
:number: 287
:canonical_id: G.287
:original_id: IX.16
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, number, prime, reductio-ad-absurdum
:dependencies: G.220, G.221
:excerpt: If two numbers be prime to one another, the second will not be to any other number as the first is to the second.

.. _G.287:
.. _IX.16:

G.287
=====

.. rubric:: `IX.16 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/16/>`_

.. enunciation::

   If two numbers be prime to one another, the second will not be to any other number as the first is to the second.

For let the two numbers :g:`A <0412.g1:A>`, :g:`B <0412.g1:B>` be prime to one another ;

I say that :g:`B <0412.g1:B>` is not to any other number as :g:`A <0412.g1:A>` is to :g:`B <0412.g1:B>`.

.. picture:: 0412.g1.svg
   :alt: Proposition 16

For, if possible, as :g:`A <0412.g1:A>` is to :g:`B <0412.g1:B>`, so let :g:`B <0412.g1:B>` be to :g:`C <0412.g1:C>`.

.. subclause::

   Now :g:`A <0412.g1:A>`, :g:`B <0412.g1:B>` are prime, primes are also least, :just:`[G.221] <G.221>` and the least numbers measure those which have the same ratio the same number of times, the antecedent the antecedent and the consequent the consequent ; :just:`[G.220] <G.220>`

.. assertion::

   therefore :g:`A <0412.g1:A>` measures :g:`B <0412.g1:B>` as antecedent antecedent.

.. subclause::

   But it also measures itself ;

.. assertion::

   therefore :g:`A <0412.g1:A>` measures :g:`A <0412.g1:A>`, :g:`B <0412.g1:B>` which are prime to one another : which is absurd.

.. assertion::

   Therefore :g:`B <0412.g1:B>` will not be to :g:`C <0412.g1:C>`, as :g:`A <0412.g1:A>` is to :g:`B <0412.g1:B>`.

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
     "G.199" [label="G.199", tooltip="G.199 (VII.def.12): Numbers prime to one another are those which are measured by an unit alone as a common measure.", fillcolor="#224422", URL="../G.199/index.html", target="_top"];
     "G.200" [label="G.200", tooltip="G.200 (VII.1): Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is...", fillcolor="#222244", URL="../G.200/index.html", target="_top"];
     "G.201" [label="G.201", tooltip="G.201 (VII.2): Given two numbers not prime to one another, to find their greatest common measure.", fillcolor="#222244", URL="../G.201/index.html", target="_top"];
     "G.203" [label="G.203", tooltip="G.203 (VII.4): Any number is either a part or parts of any number, the less of the greater.", fillcolor="#222244", URL="../G.203/index.html", target="_top"];
     "G.204" [label="G.204", tooltip="G.204 (VII.5): If a number be a part of a number, and another be the same part of another, the sum will also be the same part of the sum that the one is of the one.", fillcolor="#222244", URL="../G.204/index.html", target="_top"];
     "G.205" [label="G.205", tooltip="G.205 (VII.6): If a number be parts of a number, and another be the same parts of another, the sum will also be the same parts of the sum that the one is of the one.", fillcolor="#222244", URL="../G.205/index.html", target="_top"];
     "G.208" [label="G.208", tooltip="G.208 (VII.9): If a number be a part of a number, and another be the same part of another, alternately also, whatever part or parts the first is of the third, the same part, or the same parts, wi...", fillcolor="#222244", URL="../G.208/index.html", target="_top"];
     "G.209" [label="G.209", tooltip="G.209 (VII.10): If a number be parts of a number, and another be the same parts of another, alternately also, whatever parts or part the first is of the third, the same parts or the same part will...", fillcolor="#222244", URL="../G.209/index.html", target="_top"];
     "G.210" [label="G.210", tooltip="G.210 (VII.def.20): **Numbers** are proportional when the first is the same multiple, or the same part, or the same parts, of the second that the third is of the fourth.", fillcolor="#224422", URL="../G.210/index.html", target="_top"];
     "G.212" [label="G.212", tooltip="G.212 (VII.12): If there be as many numbers as we please in proportion, then, as one of the antecedents is to one of the consequents, so are all the antecedents to all the consequents.", fillcolor="#222244", URL="../G.212/index.html", target="_top"];
     "G.213" [label="G.213", tooltip="G.213 (VII.13): If four numbers be proportional, they will also be proportional alternately.", fillcolor="#222244", URL="../G.213/index.html", target="_top"];
     "G.215" [label="G.215", tooltip="G.215 (VII.15): If an unit measure any number, and another number measure any other number the same number of times, alternately also, the unit will measure the third number the same number of tim...", fillcolor="#222244", URL="../G.215/index.html", target="_top"];
     "G.216" [label="G.216", tooltip="G.216 (VII.16): If two numbers by multiplying one another make certain numbers, the numbers so produced will be equal to one another.", fillcolor="#222244", URL="../G.216/index.html", target="_top"];
     "G.220" [label="G.220", tooltip="G.220 (VII.20): The least numbers of those which have the same ratio with them measure those which have the same ratio the same number of times, the greater the greater and the less the less.", fillcolor="#222244", URL="../G.220/index.html", target="_top"];
     "G.221" [label="G.221", tooltip="G.221 (VII.21): Numbers prime to one another are the least of those which have the same ratio with them.", fillcolor="#222244", URL="../G.221/index.html", target="_top"];
     "G.287" [label="G.287", tooltip="G.287 (IX.16): If two numbers be prime to one another, the second will not be to any other number as the first is to the second.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.200" -> "G.199";
     "G.221" -> "G.199";
     "G.201" -> "G.200";
     "G.203" -> "G.201";
     "G.220" -> "G.203";
     "G.205" -> "G.204";
     "G.208" -> "G.204";
     "G.209" -> "G.204";
     "G.212" -> "G.204";
     "G.208" -> "G.205";
     "G.209" -> "G.205";
     "G.212" -> "G.205";
     "G.209" -> "G.208";
     "G.213" -> "G.209";
     "G.212" -> "G.210";
     "G.213" -> "G.210";
     "G.220" -> "G.210";
     "G.215" -> "G.212";
     "G.220" -> "G.212";
     "G.220" -> "G.213";
     "G.216" -> "G.215";
     "G.221" -> "G.216";
     "G.221" -> "G.220";
     "G.287" -> "G.220";
     "G.287" -> "G.221";
   }

Required for
------------

:ref:`G.289 <G.289>`
