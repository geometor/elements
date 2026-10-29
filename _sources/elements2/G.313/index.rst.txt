:order: 313
:number: 313
:canonical_id: G.313
:original_id: X.1
:volume: III
:book: X
:type: prop
:subtype: theorem
:categories: theorem, proof, incommensurables, magnitudes
:category: theorem, proof, incommensurables, magnitudes
:tags: book-x, point, segment, equality
:dependencies: G.143
:excerpt: Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and if this process be repeated continually, there will be left some magnitude which will be less than the lesser magnitude set out.

.. _G.313:
.. _X.1:

G.313
=====

.. rubric:: `X.1 <https://geometor.github.io/euclid/heath/volume_III/book_x/propositions/001/>`_

.. enunciation::

   Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and if this process be repeated continually, there will be left some magnitude which will be less than the lesser magnitude set out.

Let :g:`/ A B / <0018.g1:/ A B />`, :g:`C <0018.g1:C>` be two unequal magnitudes of which :g:`/ A B / <0018.g1:/ A B />` is the greater : I say that, if from :g:`/ A B / <0018.g1:/ A B />` there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and if this process be repeated continually, there will be left some magnitude which will be less than the magnitude :g:`C <0018.g1:C>`.

.. picture:: 0018.g1.svg
   :alt: Book X, Proposition 1

For :g:`C <0018.g1:C>` if multiplied will sometime be greater than :g:`/ A B / <0018.g1:/ A B />`. :just:`[G.143] <G.143>`

Let it be multiplied, and let :g:`/ D E / <0018.g1:/ D E />` be a multiple of :g:`C <0018.g1:C>`, and greater than :g:`/ A B / <0018.g1:/ A B />`; let :g:`/ D E / <0018.g1:/ D E />` be divided into the parts :g:`/ D F / <0018.g1:/ D F />`, :g:`/ F G / <0018.g1:/ F G />`, :g:`/ G E / <0018.g1:/ G E />` :eq:`equal <0018.g1:/ D F / = 0018.g1:/ F G / = 0018.g1:/ G E / = 0018.g1:C>` to :g:`C <0018.g1:C>`, from :g:`/ A B / <0018.g1:/ A B />` let there be subtracted :g:`/ B H / <0018.g1:/ B H />` greater than its half, and, from :g:`/ A H / <0018.g1:/ A H />`, :g:`/ H K / <0018.g1:/ H K />` greater than its half, and let this process be repeated continually until the divisions in :g:`/ A B / <0018.g1:/ A B />` are equal in multitude with the divisions in :g:`/ D E / <0018.g1:/ D E />`.

Let, then, :g:`/ A K / <0018.g1:/ A K />`, :g:`/ K H / <0018.g1:/ K H />`, :g:`/ H B / <0018.g1:/ H B />` be divisions which are equal in multitude with :g:`/ D F / <0018.g1:/ D F />`, :g:`/ F G / <0018.g1:/ F G />`, :g:`/ G E / <0018.g1:/ G E />`.

.. subclause::

   Now, since :g:`/ D E / <0018.g1:/ D E />` is greater than :g:`/ A B / <0018.g1:/ A B />`, and from :g:`/ D E / <0018.g1:/ D E />` there has been subtracted :g:`/ E G / <0018.g1:/ E G />` less than its half, and, from :g:`/ A B / <0018.g1:/ A B />`, :g:`/ B H / <0018.g1:/ B H />` greater than its half,

.. assertion::

   therefore the remainder :g:`/ G D / <0018.g1:/ G D />` is greater than the remainder :g:`/ H A / <0018.g1:/ H A />`.

.. subclause::

   And, since :g:`/ G D / <0018.g1:/ G D />` is greater than :g:`/ H A / <0018.g1:/ H A />`, and there has been subtracted, from :g:`/ G D / <0018.g1:/ G D />`, the half :g:`/ G F / <0018.g1:/ G F />`, and, from :g:`/ H A / <0018.g1:/ H A />`, :g:`/ H K / <0018.g1:/ H K />` greater than its half,

.. assertion::

   therefore the remainder :g:`/ D F / <0018.g1:/ D F />` is greater than the remainder :g:`/ A K / <0018.g1:/ A K />`.

.. subclause::

   But :g:`/ D F / <0018.g1:/ D F />` is :eq:`equal <0018.g1:/ D F / = 0018.g1:C>` to :g:`C <0018.g1:C>`;

.. assertion::

   therefore :g:`C <0018.g1:C>` is also greater than :g:`/ A K / <0018.g1:/ A K />`.

.. assertion::

   Therefore :g:`/ A K / <0018.g1:/ A K />` is less than :g:`C <0018.g1:C>`.

.. qed::

   Therefore there is left of the magnitude :g:`/ A B / <0018.g1:/ A B />` the magnitude :g:`/ A K / <0018.g1:/ A K />` which is less than the lesser magnitude set out, namely :g:`C <0018.g1:C>`. :just:`Q. E. D.`

.. assertion::

   And the theorem can be similarly proved even if the parts subtracted be halves.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.143" [label="G.143", tooltip="G.143 (V.def.4): Magnitudes are said to have a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.143/index.html", target="_top"];
     "G.313" [label="G.313", tooltip="G.313 (X.1): Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and ...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.313" -> "G.143";
   }

Required for
------------

:ref:`G.491 <G.491>`, :ref:`G.492 <G.492>`, :ref:`G.493 <G.493>`, :ref:`G.494 <G.494>`, :ref:`G.496 <G.496>`, :ref:`G.497 <G.497>`, :ref:`G.499 <G.499>`, :ref:`G.500 <G.500>`, :ref:`G.501 <G.501>`, :ref:`G.502 <G.502>`, :ref:`G.503 <G.503>`, :ref:`G.505 <G.505>`, :ref:`G.506 <G.506>`
