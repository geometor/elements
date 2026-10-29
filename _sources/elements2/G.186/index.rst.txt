:order: 186
:number: 186
:canonical_id: G.186
:original_id: VI.21
:volume: II
:book: VI
:type: prop
:subtype: theorem
:categories: theorem, proof, plane-geometry, proportions, similar-figures
:category: theorem, proof, plane-geometry, proportions, similar-figures
:tags: book-vi, point, similar
:dependencies: G.170
:excerpt: Figures which are similar to the same rectilineal figure are also similar to one another.

.. _G.186:
.. _VI.21:

G.186
=====

.. rubric:: `VI.21 <https://geometor.github.io/euclid/heath/volume_II/book_vi/propositions/21/>`_

.. enunciation::

   Figures which are similar to the same rectilineal figure are also similar to one another.

For let each of the rectilineal figures :g:`A <0246.g1:A>`, :g:`B <0246.g1:B>` be similar to :g:`C <0246.g1:C>`;

I say that :g:`A <0246.g1:A>` is also similar to :g:`B <0246.g1:B>`.

.. subclause::

   For, since :g:`A <0246.g1:A>` is similar to :g:`C <0246.g1:C>`,

.. assertion::

   it is equiangular with it and has the sides about the equal angles proportional. :just:`[G.170] <G.170>`

.. picture:: 0246.g1.svg
   :alt: Book VI, Proposition 21

.. subclause::

   Again, since :g:`B <0246.g1:B>` is similar to :g:`C <0246.g1:C>`,

.. assertion::

   it is equiangular with it and has the sides about the equal angles proportional.

.. assertion::

   Therefore each of the figures :g:`A <0246.g1:A>`, :g:`B <0246.g1:B>` is equiangular with :g:`C <0246.g1:C>` and with :g:`C <0246.g1:C>` has the sides about the equal angles proportional;

.. assertion::

   therefore :g:`A <0246.g1:A>` is similar to :g:`B <0246.g1:B>`.

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
     "G.170" [label="G.170", tooltip="G.170 (VI.def.1): Similar rectilineal figures are such as have their angles severally equal and the sides about the equal angles proportional.", fillcolor="#224422", URL="../G.170/index.html", target="_top"];
     "G.186" [label="G.186", tooltip="G.186 (VI.21): Figures which are similar to the same rectilineal figure are also similar to one another.", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.186" -> "G.170";
   }

Required for
------------

:ref:`G.189 <G.189>`, :ref:`G.191 <G.191>`, :ref:`G.192 <G.192>`, :ref:`G.193 <G.193>`, :ref:`G.194 <G.194>`, :ref:`G.195 <G.195>`, :ref:`G.348 <G.348>`, :ref:`G.349 <G.349>`, :ref:`G.354 <G.354>`, :ref:`G.355 <G.355>`, :ref:`G.360 <G.360>`, :ref:`G.361 <G.361>`, :ref:`G.376 <G.376>`, :ref:`G.378 <G.378>`, :ref:`G.383 <G.383>`, :ref:`G.384 <G.384>`, :ref:`G.389 <G.389>`, :ref:`G.390 <G.390>`, :ref:`G.392 <G.392>`, :ref:`G.397 <G.397>`, :ref:`G.398 <G.398>`, :ref:`G.403 <G.403>`, :ref:`G.404 <G.404>`, :ref:`G.418 <G.418>`, :ref:`G.419 <G.419>`, :ref:`G.420 <G.420>`, :ref:`G.421 <G.421>`, :ref:`G.422 <G.422>`, :ref:`G.423 <G.423>`, :ref:`G.427 <G.427>`, :ref:`G.428 <G.428>`, :ref:`G.432 <G.432>`, :ref:`G.433 <G.433>`, :ref:`G.435 <G.435>`, :ref:`G.436 <G.436>`, :ref:`G.437 <G.437>`, :ref:`G.518 <G.518>`, :ref:`G.523 <G.523>`, :ref:`G.525 <G.525>`
