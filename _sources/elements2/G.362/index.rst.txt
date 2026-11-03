:order: 362
:number: 362
:canonical_id: G.362
:original_id: IX.31
:title: G.362 odd number prime
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, odd-number, prime-to-one-another, number, part-aliquot, even-number, prime, reductio-ad-absurdum
:dependencies: G.169, G.248, G.249, G.352, G.361
:excerpt: If an odd number be prime to any number, it is prime to the double of it.

.. _G.362:
.. _IX.31:

G.362 odd number prime
======================

.. rubric:: `IX.31 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/31/>`_

.. enunciation::

   If an :term:`odd number <G.352>` be :term:`prime to <G.249>` any :term:`number <G.248>`, it is prime to the double of it.

.. signature:: theorem

   | :fn:`odd_number_prime <G.362>`\ ()
   | **prove** :g:`A <g1:A>` is prime to :g:`C <g1:C>`

.. picture:: g1.svg
   :alt: Book IX, Proposition 31

.. step:: assert

   Let the odd number :g:`A <g1:A>` be prime to any number :g:`B <g1:B>`, and let :g:`C <g1:C>` be double of :g:`B <g1:B>`

.. step:: assert

   If they are not prime to one another, some number will :term:`measure <G.169>` them

.. step:: assert

   Let a number measure them, and let it be :g:`D <g1:D>`

.. step:: assert

   Now :g:`A <g1:A>` is odd

.. step:: assert

   :g:`D <g1:D>` is also odd

.. step:: assert

   :g:`D <g1:D>` which is odd measures :g:`C <g1:C>`, and :g:`C <g1:C>` is even,

.. step:: assert ∵ odd_number_measure <G.361>

   [:g:`D <g1:D>`] will measure the half of :g:`C <g1:C>` also

.. step:: assert

   :g:`B <g1:B>` is half of :g:`C <g1:C>`

.. step:: assert

   :g:`D <g1:D>` measures :g:`B <g1:B>`

.. step:: assert

   It also measures :g:`A <g1:A>`

.. step:: assert

   :g:`D <g1:D>` measures :g:`A <g1:A>`, :g:`B <g1:B>` which are prime to one another ⇒⇐

.. step:: assert

   :g:`A <g1:A>` cannot but be prime to :g:`C <g1:C>`

.. step:: conclude

   :g:`A <g1:A>`, :g:`C <g1:C>` are prime to one another

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
     "G.249" [label="G.249", tooltip="G.249 (VII.def.12): Numbers prime to one another are those which aremeasured by anunit alone as a common measure.", fillcolor="#224422", URL="../G.249/index.html", target="_top"];
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.351" [label="G.351", tooltip="G.351 (IX.21): If as many even numbers as we please be added together, the whole is even.", fillcolor="#222244", URL="../G.351/index.html", target="_top"];
     "G.352" [label="G.352", tooltip="G.352 (VII.def.7): Anodd number is that which is not divisible into two equal parts, or that which differs by anunit from aneven number.", fillcolor="#224422", URL="../G.352/index.html", target="_top"];
     "G.353" [label="G.353", tooltip="G.353 (IX.22): If as many odd numbers as we please be added together, and their multitude be even, the whole is even.", fillcolor="#222244", URL="../G.353/index.html", target="_top"];
     "G.354" [label="G.354", tooltip="G.354 (IX.23): If as many odd numbers as we please be added together, and their multitude be odd, the whole is odd.", fillcolor="#222244", URL="../G.354/index.html", target="_top"];
     "G.361" [label="G.361", tooltip="G.361 (IX.30): If an odd number measure an even number, it will also measure the half of it.", fillcolor="#222244", URL="../G.361/index.html", target="_top"];
     "G.362" [label="G.362", tooltip="G.362 (IX.31): If an odd number be prime to any number, it is prime to the double of it.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.249" -> "G.169";
     "G.361" -> "G.169";
     "G.362" -> "G.169";
     "G.248" -> "G.247";
     "G.249" -> "G.247";
     "G.269" -> "G.247";
     "G.352" -> "G.247";
     "G.353" -> "G.247";
     "G.354" -> "G.247";
     "G.269" -> "G.248";
     "G.351" -> "G.248";
     "G.353" -> "G.248";
     "G.362" -> "G.248";
     "G.362" -> "G.249";
     "G.361" -> "G.269";
     "G.351" -> "G.302";
     "G.352" -> "G.302";
     "G.353" -> "G.302";
     "G.361" -> "G.302";
     "G.353" -> "G.351";
     "G.354" -> "G.351";
     "G.353" -> "G.352";
     "G.354" -> "G.352";
     "G.361" -> "G.352";
     "G.362" -> "G.352";
     "G.354" -> "G.353";
     "G.361" -> "G.354";
     "G.362" -> "G.361";
   }

.. toctree::
   :hidden:

   code
   heath
