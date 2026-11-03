:order: 282
:number: 282
:canonical_id: G.282
:original_id: VII.28
:title: G.282 numbers prime sum
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, segment, number, prime-to-one-another, part-aliquot, prime, reductio-ad-absurdum
:dependencies: G.169, G.248, G.249
:excerpt: If two numbers be prime to one another, the sum is prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers is prime to one another.

.. _G.282:
.. _VII.28:

G.282 numbers prime sum
=======================

.. rubric:: `VII.28 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/28/>`_

.. enunciation::

   If two :term:`numbers <G.248>` be :term:`prime to one another <G.249>`, the sum is prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers is prime to one another.

.. signature:: theorem

   | :fn:`numbers_prime_sum <G.282>`\ ()
   | **prove** the sum :g:`/ A C / <g1:/ A C />` is also prime to each of the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`; :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are also prime to one another

.. picture:: g1.svg
   :alt: Book VII, Proposition 28

.. step:: construct

   Let two numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` prime to one another be added

.. step:: assert

   If :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are not prime to one another, some number will :term:`measure <G.169>` :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`

.. step:: assert

   Let a number measure them, and let it be :g:`D <g1:D>`

.. step:: assert

   then :g:`D <g1:D>` measures :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`,

.. step:: assert

   it will also measure :g:`/ B C / <g1:/ B C />`

.. step:: assert

   It also measures :g:`/ A B / <g1:/ A B />`

.. step:: assert ∵ numbers_prime_measured_def <G.249>

   :g:`D <g1:D>` measures :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` which are prime to one another ⇒⇐

.. step:: assert

   no number will measure the numbers :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` ; therefore :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are prime to one another

.. step:: assert

   For the same reason

.. step:: assert

   :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />` are also prime to one another

.. step:: assert

   :g:`/ A C / <g1:/ A C />` is prime to each of the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`

.. step:: assert

   Let :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` be prime to one another

.. step:: assert

   If :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are not prime to one another, some number will measure :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`

.. step:: assert

   Let a number measure them, and let it be :g:`D <g1:D>`

.. step:: assert

   :g:`D <g1:D>` measures each of the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`,

.. step:: assert

   It will also measure :g:`/ A C / <g1:/ A C />`

.. step:: assert

   It also measures :g:`/ A B / <g1:/ A B />`

.. step:: assert ∵ numbers_prime_measured_def <G.249>

   :g:`D <g1:D>` measures :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` which are prime to one another ⇒⇐

.. step:: assert

   no number will measure the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`

.. step:: conclude

   :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are prime to one another

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
     "G.282" [label="G.282", tooltip="G.282 (VII.28): If two numbers be prime to one another, the sum is prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers is prime to one another.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.249" -> "G.169";
     "G.282" -> "G.169";
     "G.248" -> "G.247";
     "G.249" -> "G.247";
     "G.282" -> "G.248";
     "G.282" -> "G.249";
   }

Required for
------------

:ref:`G.345 <G.345>`

.. toctree::
   :hidden:

   code
   heath
