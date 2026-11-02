:order: 288
:number: 288
:canonical_id: G.288
:original_id: VII.32
:title: G.288 number prime measured
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, number, prime-number, part-aliquot, composite-number, prime
:dependencies: G.169, G.248, G.283, G.287
:excerpt: Any number either is prime or is measured by some prime number.

.. _G.288:
.. _VII.32:

G.288 number prime measured
===========================

.. rubric:: `VII.32 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/32/>`_

.. enunciation::

   Any :term:`number <G.248>` either is :term:`prime <G.283>` or is :term:`measured <G.169>` by some prime number.

.. signature:: theorem

   | :fn:`number_prime_measured <G.288>`\ (:g:`A <g1:A>`)
   | **given** :g:`A <g1:A>` be a number
   | **prove** :g:`A <g1:A>` either is prime or is measured by some prime number

.. picture:: g1.svg
   :alt: Proposition 32 diagram

.. step:: given

   :g:`A <g1:A>` be a number

.. step:: assert

   If now :g:`A <g1:A>` is prime, that which was enjoined will have been done.

.. step:: assert ∵ composite_number_measured <G.287>

   If it is :term:`composite <G.286>`, some prime number will measure it.

.. step:: conclude

   Therefore any number either is prime or is measured by some prime number.

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
     "G.288" [label="G.288", tooltip="G.288 (VII.32): Any number either is prime or is measured by some prime number.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.283" -> "G.169";
     "G.286" -> "G.169";
     "G.287" -> "G.169";
     "G.288" -> "G.169";
     "G.248" -> "G.247";
     "G.283" -> "G.247";
     "G.286" -> "G.248";
     "G.288" -> "G.248";
     "G.287" -> "G.283";
     "G.288" -> "G.283";
     "G.287" -> "G.286";
     "G.288" -> "G.287";
   }

.. toctree::
   :hidden:

   code
   heath
