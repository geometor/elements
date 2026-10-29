:order: 229
:number: 229
:canonical_id: G.229
:original_id: VII.28
:volume: II
:book: VII
:type: prop
:subtype: theorem
:categories: theorem, proof, number-theory
:category: theorem, proof, number-theory
:tags: book-vii, point, segment, number, prime, reductio-ad-absurdum
:dependencies: G.199
:excerpt: If two numbers be prime to one another, the sum is prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers is prime to one another.

.. _G.229:
.. _VII.28:

G.229
=====

.. rubric:: `VII.28 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/28/>`_

.. enunciation::

   If two numbers be prime to one another, the sum is prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers is prime to one another.

.. picture:: g1.svg
   :alt: Book VII, Proposition 28

.. step:: assert

   For let two numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` prime to one another be added

.. step:: assert

   If :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are not prime to one another, some number will measure :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`.

.. step:: assert

   Let a number measure them

.. step:: assert

   Let it be :g:`D <g1:D>`.

.. step:: assert

   Since then :g:`D <g1:D>` measures :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`,

.. step:: assert

   Therefore it will also measure the remainder :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   It also measures :g:`/ A B / <g1:/ A B />` ;

.. step:: assert [G.199] <G.199>

   Therefore :g:`D <g1:D>` measures :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` which are prime to one another : which is impossible.

.. step:: assert

   Therefore no number will measure the numbers :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` ; therefore :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are prime to one another.

.. step:: assert

   For the same reason

.. step:: assert

   :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />` are also prime to one another.

.. step:: assert

   Therefore :g:`/ A C / <g1:/ A C />` is prime to each of the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   Let :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` be prime to one another

.. step:: assert

   If :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are not prime to one another, some number will measure :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`.

.. step:: assert

   Let a number measure them

.. step:: assert

   Let it be :g:`D <g1:D>`.

.. step:: assert

   Since :g:`D <g1:D>` measures each of the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`,

.. step:: assert

   It will also measure the whole :g:`/ A C / <g1:/ A C />`.

.. step:: assert

   It also measures :g:`/ A B / <g1:/ A B />` ;

.. step:: assert [G.199] <G.199>

   Therefore :g:`D <g1:D>` measures :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` which are prime to one another : which is impossible.

.. step:: assert

   Therefore no number will measure the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`.

.. step:: conclude

   Therefore :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are prime to one another.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.199" [label="G.199", tooltip="G.199 (VII.def.12): Numbers prime to one another are those which are measured by an unit alone as a common measure.", fillcolor="#224422", URL="../G.199/index.html", target="_top"];
     "G.229" [label="G.229", tooltip="G.229 (VII.28): If two numbers be prime to one another, the sum is prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers is prime to one another.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.229" -> "G.199";
   }

Required for
------------

:ref:`G.286 <G.286>`

.. toctree::
   :hidden:

   code
   heath
