:canonical_id: G.229
:original_id: VII.28
:volume: II
:book: VII
:type: prop

G.229 — Heath
=============

.. rubric:: `VII.28 <https://geometor.github.io/euclid/heath/volume_II/book_vii/propositions/28/>`_

.. enunciation::

   If two numbers be prime to one another, the sum will also be prime to each of them ; and, if the sum of two numbers be prime to any one of them, the original numbers will also be prime to one another.

For let two numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` prime to one another be added ;

I say that the sum :g:`/ A C / <g1:/ A C />` is also prime to each of the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`.

.. picture:: g1.svg
   :alt: Book VII, Proposition 28

.. subclause::

   For, if :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are not prime to one another, some number will measure :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`.

Let a number measure them, and let it be :g:`D <g1:D>`.

.. subclause::

   Since then :g:`D <g1:D>` measures :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />`,

.. assertion::

   therefore it will also measure the remainder :g:`/ B C / <g1:/ B C />`.

.. subclause::

   But it also measures :g:`/ A B / <g1:/ A B />` ;

.. assertion::

   therefore :g:`D <g1:D>` measures :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` which are prime to one another : which is impossible. :just:`[G.199] <G.199>`

.. assertion::

   Therefore no number will measure the numbers :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` ; therefore :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` are prime to one another.

.. subclause::

   For the same reason

.. assertion::

   :g:`/ A C / <g1:/ A C />`, :g:`/ B C / <g1:/ B C />` are also prime to one another.

.. assertion::

   Therefore :g:`/ A C / <g1:/ A C />` is prime to each of the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`.

Again, let :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` be prime to one another ;

I say that :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are also prime to one another.

.. subclause::

   For, if :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are not prime to one another, some number will measure :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`.

Let a number measure them, and let it be :g:`D <g1:D>`.

.. subclause::

   Now, since :g:`D <g1:D>` measures each of the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`,

.. assertion::

   it will also measure the whole :g:`/ A C / <g1:/ A C />`.

.. subclause::

   But it also measures :g:`/ A B / <g1:/ A B />` ;

.. assertion::

   therefore :g:`D <g1:D>` measures :g:`/ A C / <g1:/ A C />`, :g:`/ A B / <g1:/ A B />` which are prime to one another : which is impossible. :just:`[G.199] <G.199>`

.. assertion::

   Therefore no number will measure the numbers :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />`.

.. assertion::

   Therefore :g:`/ A B / <g1:/ A B />`, :g:`/ B C / <g1:/ B C />` are prime to one another.

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
     "G.229" [label="G.229", tooltip="G.229 (VII.28): If two numbers be prime to one another, the sum is prime to each of them; and, if the sum of two numbers be prime to any one of them, the original numbers is prime to one another.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.229" -> "G.199";
   }

Required for
------------

:ref:`G.286 <G.286>`
