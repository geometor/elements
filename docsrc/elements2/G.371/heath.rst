:canonical_id: G.371
:original_id: X.1
:title: G.371 unequal magnitudes set
:volume: III
:book: X
:type: prop

G.371 unequal magnitudes set — Heath
====================================

.. rubric:: `X.1 <https://geometor.github.io/euclid/heath/volume_III/book_x/propositions/001/>`_

.. enunciation::

   Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and if this process be repeated continually, there will be left some magnitude which will be less than the lesser magnitude set out.

Let :g:`/ A B / <g1:/ A B />`, :g:`C <g1:C>` be two unequal magnitudes of which :g:`/ A B / <g1:/ A B />` is the greater : I say that, if from :g:`/ A B / <g1:/ A B />` there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and if this process be repeated continually, there will be left some magnitude which will be less than the magnitude :g:`C <g1:C>`.

.. picture:: g1.svg
   :alt: Book X, Proposition 1

For :g:`C <g1:C>` if :term:`multiplied <G.269>` will sometime be greater than :g:`/ A B / <g1:/ A B />`. :just:`[G.184] <G.184>`

Let it be multiplied, and let :g:`/ D E / <g1:/ D E />` be a :term:`multiple of <G.256>` :g:`C <g1:C>`, and greater than :g:`/ A B / <g1:/ A B />`; let :g:`/ D E / <g1:/ D E />` be divided into the parts :g:`/ D F / <g1:/ D F />`, :g:`/ F G / <g1:/ F G />`, :g:`/ G E / <g1:/ G E />` :eq:`equal <g1:/ D F / = g1:/ F G / = g1:/ G E / = g1:C>` to :g:`C <g1:C>`, from :g:`/ A B / <g1:/ A B />` let there be subtracted :g:`/ B H / <g1:/ B H />` greater than its half, and, from :g:`/ A H / <g1:/ A H />`, :g:`/ H K / <g1:/ H K />` greater than its half, and let this process be repeated continually until the divisions in :g:`/ A B / <g1:/ A B />` are equal in multitude with the divisions in :g:`/ D E / <g1:/ D E />`.

Let, then, :g:`/ A K / <g1:/ A K />`, :g:`/ K H / <g1:/ K H />`, :g:`/ H B / <g1:/ H B />` be divisions which are equal in multitude with :g:`/ D F / <g1:/ D F />`, :g:`/ F G / <g1:/ F G />`, :g:`/ G E / <g1:/ G E />`.

.. subclause::

   Now, since :g:`/ D E / <g1:/ D E />` is greater than :g:`/ A B / <g1:/ A B />`, and from :g:`/ D E / <g1:/ D E />` there has been subtracted :g:`/ E G / <g1:/ E G />` less than its half, and, from :g:`/ A B / <g1:/ A B />`, :g:`/ B H / <g1:/ B H />` greater than its half,

.. assertion::

   therefore the remainder :g:`/ G D / <g1:/ G D />` is greater than the remainder :g:`/ H A / <g1:/ H A />`.

.. subclause::

   And, since :g:`/ G D / <g1:/ G D />` is greater than :g:`/ H A / <g1:/ H A />`, and there has been subtracted, from :g:`/ G D / <g1:/ G D />`, the half :g:`/ G F / <g1:/ G F />`, and, from :g:`/ H A / <g1:/ H A />`, :g:`/ H K / <g1:/ H K />` greater than its half,

.. assertion::

   therefore the remainder :g:`/ D F / <g1:/ D F />` is greater than the remainder :g:`/ A K / <g1:/ A K />`.

.. subclause::

   But :g:`/ D F / <g1:/ D F />` is :eq:`equal <g1:/ D F / = g1:C>` to :g:`C <g1:C>`;

.. assertion::

   therefore :g:`C <g1:C>` is also greater than :g:`/ A K / <g1:/ A K />`.

.. assertion::

   Therefore :g:`/ A K / <g1:/ A K />` is less than :g:`C <g1:C>`.

.. qed::

   Therefore there is left of the magnitude :g:`/ A B / <g1:/ A B />` the magnitude :g:`/ A K / <g1:/ A K />` which is less than the lesser magnitude set out, namely :g:`C <g1:C>`. :just:`Q. E. D.`

.. assertion::

   And the theorem can be similarly proved :term:`even <G.302>` if the parts subtracted be halves.

Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="transparent";
     node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=11, color="#d6d3cd", fontcolor="#ffffff"];
     edge [color="#8c857b", fontcolor="#8c857b", arrowsize=0.75];
     rankdir="TB";
     "G.169" [label="G.169", tooltip="G.169 (V.def.1): A magnitude is apart of a magnitude, the less of the greater, when it measures the greater.", fillcolor="#224422", URL="../G.169/index.html", target="_top"];
     "G.184" [label="G.184", tooltip="G.184 (V.def.4): Magnitudes are said tohave a ratio to one another which are capable, when multiplied, of exceeding one another.", fillcolor="#224422", URL="../G.184/index.html", target="_top"];
     "G.247" [label="G.247", tooltip="G.247 (VII.def.1): Anunit is that by virtue of which each of the things that exist is called one.", fillcolor="#224422", URL="../G.247/index.html", target="_top"];
     "G.248" [label="G.248", tooltip="G.248 (VII.def.2): Anumber is a multitude composed ofunits.", fillcolor="#224422", URL="../G.248/index.html", target="_top"];
     "G.253" [label="G.253", tooltip="G.253 (VII.def.3): Anumber is apart of a number, the less of the greater, when itmeasures the greater;", fillcolor="#224422", URL="../G.253/index.html", target="_top"];
     "G.256" [label="G.256", tooltip="G.256 (VII.def.5): The greaternumber is amultiple of the less when it ismeasured by the less.", fillcolor="#224422", URL="../G.256/index.html", target="_top"];
     "G.269" [label="G.269", tooltip="G.269 (VII.def.15): Anumber is said tomultiply a number when that which is multiplied is added to itself as many times as there areunits in the other, and thus some number is produced.", fillcolor="#224422", URL="../G.269/index.html", target="_top"];
     "G.302" [label="G.302", tooltip="G.302 (VII.def.6): Aneven number is that which is divisible into two equal parts.", fillcolor="#224422", URL="../G.302/index.html", target="_top"];
     "G.371" [label="G.371", tooltip="G.371 (X.1): Two unequal magnitudes being set out, if from the greater there be subtracted a magnitude greater than its half, and from that which is left a magnitude greater than its half, and ...", penwidth=2.5, color="#e8b85a", fillcolor="#4a453b", URL="index.html", target="_top"];
     "G.253" -> "G.169";
     "G.256" -> "G.169";
     "G.371" -> "G.184";
     "G.248" -> "G.247";
     "G.269" -> "G.247";
     "G.253" -> "G.248";
     "G.256" -> "G.248";
     "G.269" -> "G.248";
     "G.256" -> "G.253";
     "G.371" -> "G.256";
     "G.371" -> "G.269";
     "G.371" -> "G.302";
   }

Required for
------------

:ref:`G.556 <G.556>`, :ref:`G.557 <G.557>`, :ref:`G.558 <G.558>`, :ref:`G.559 <G.559>`, :ref:`G.563 <G.563>`, :ref:`G.565 <G.565>`, :ref:`G.570 <G.570>`, :ref:`G.571 <G.571>`, :ref:`G.572 <G.572>`, :ref:`G.573 <G.573>`, :ref:`G.574 <G.574>`, :ref:`G.577 <G.577>`, :ref:`G.578 <G.578>`
