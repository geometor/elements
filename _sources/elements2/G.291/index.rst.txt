:order: 291
:number: 291
:canonical_id: G.291
:original_id: IX.20
:volume: II
:book: IX
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-ix, point, segment, number, prime, reductio-ad-absurdum
:dependencies: G.232
:excerpt: Prime numbers are more than any assigned multitude of prime numbers.

.. _G.291:
.. _IX.20:

G.291
=====

.. rubric:: `IX.20 <https://geometor.github.io/euclid/heath/volume_II/book_ix/propositions/20/>`_

.. enunciation::

   Prime numbers are more than any assigned multitude of prime numbers.

.. picture:: g1.svg
   :alt: Book IX, Proposition 20

.. step:: given

   :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` be the assigned prime numbers

.. step:: construct

   For let the least number measured by :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>` be taken

.. step:: assert

   Let it be :g:`/ D E / <g1:/ D E />`

.. step:: assert

   Let the unit :g:`/ D F / <g1:/ D F />` be added to :g:`/ D E / <g1:/ D E />`.

.. step:: assert

   Then :g:`/ E F / <g1:/ E F />` is either prime or not.

.. step:: assert

   First, let it be prime

.. step:: assert

   Then the prime numbers :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`, :g:`/ E F / <g1:/ E F />` have been found which are more than :g:`A <g1:A>`, :g:`B <g1:B>`, :g:`C <g1:C>`.

.. step:: assert

   Next, let :g:`/ E F / <g1:/ E F />` not be prime

.. step:: assert [G.232] <G.232>

   Therefore it is measured by some prime number.

.. step:: assert

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
     "G.232" [label="G.232", tooltip="G.232 (VII.31): Any composite number is measured by some prime number.", fillcolor="#222244", URL="../G.232/index.html", target="_top"];
     "G.291" [label="G.291", tooltip="G.291 (IX.20): Prime numbers are more than any assigned multitude of prime numbers.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.291" -> "G.232";
   }

.. toctree::
   :hidden:

   code
   heath
