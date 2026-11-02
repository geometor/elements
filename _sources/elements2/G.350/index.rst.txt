:order: 350
:number: 350
:canonical_id: G.350
:original_id: IX.20
:title: G.350 prime numbers more
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, segment, prime-number, number, part-aliquot, unit, prime, reductio-ad-absurdum
:dependencies: G.283, G.287
:excerpt: Prime numbers are more than any assigned multitude of prime numbers.

.. _G.350:
.. _IX.20:

G.350 prime numbers more
========================

.. rubric:: `IX.20 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/20/>`_

.. enunciation::

   :term:`Prime numbers <G.283>` are more than any assigned multitude of prime numbers.

.. signature:: theorem

   | :fn:`prime_numbers_more <G.350>`\ (:g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`)
   | **given** :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` be the assigned prime numbers
   | **prove** there are more prime numbers than :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`; :g:`G <g1:G>` is not the same with any of the numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`

.. picture:: g1.svg
   :alt: Book IX, Proposition 20

.. step:: given

   :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` be the assigned prime numbers

.. step:: construct

   Let the least :term:`number <G.248>` :term:`measured <G.169>` by :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` be taken

.. step:: assert

   Let it be :g:`/ D E / <g1:/ D E />`

.. step:: construct

   Let the :term:`unit <G.247>` :g:`/ D F / <g1:/ D F />` be added to :g:`/ D E / <g1:/ D E />`.

.. step:: assert

   Then :g:`/ E F / <g1:/ E F />` is either prime or not.

.. step:: assert

   First, let it be prime

.. step:: assert

   Then the prime numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`/ E F / <g1:/ E F />` have been found which are more than :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

.. step:: assert

   Next, let :g:`/ E F / <g1:/ E F />` not be prime

.. step:: assert ∵ composite_number_measured <G.287>

   Therefore it is measured by some prime number.

.. step:: construct

   Let it be measured by the prime number :g:`G <g1:G>`.

.. step:: assert

   If possible, let it be so.

.. step:: assert

   Now :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` measure :g:`/ D E / <g1:/ D E />` ;

.. step:: assert

   Therefore :g:`G <g1:G>` also will measure :g:`/ D E / <g1:/ D E />`.

.. step:: assert

   It also measures :g:`/ E F / <g1:/ E F />`.

.. step:: assert

   Therefore :g:`G <g1:G>`, being a number, will measure the remainder, the unit :g:`/ D F / <g1:/ D F />` : which is absurd.

.. step:: assert

   Therefore :g:`G <g1:G>` is not the same with any one of the numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

.. step:: assert

   By hypothesis it is prime.

.. step:: conclude

   Therefore the prime numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`G <g1:G>` have been found which are more than the assigned multitude of :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

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
     "G.283" [label="G.283", tooltip="G.283 (VII.def.11): Aprime number is that which ismeasured by anunit alone.", fillcolor="#224422", URL="../G.283/index.html", target="_top"];
     "G.286" [label="G.286", tooltip="G.286 (VII.def.13): Acomposite number is that which ismeasured by somenumber.", fillcolor="#224422", URL="../G.286/index.html", target="_top"];
     "G.287" [label="G.287", tooltip="G.287 (VII.31): Any composite number is measured by some prime number.", fillcolor="#222244", URL="../G.287/index.html", target="_top"];
     "G.350" [label="G.350", tooltip="G.350 (IX.20): Prime numbers are more than any assigned multitude of prime numbers.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.283" -> "G.169";
     "G.286" -> "G.169";
     "G.287" -> "G.169";
     "G.248" -> "G.247";
     "G.283" -> "G.247";
     "G.286" -> "G.248";
     "G.287" -> "G.283";
     "G.350" -> "G.283";
     "G.287" -> "G.286";
     "G.350" -> "G.287";
   }

.. toctree::
   :hidden:

   code
   heath
