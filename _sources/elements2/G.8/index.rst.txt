:order: 8
:original_id: I.2
:type: prop
:dependencies: G.5, G.1, G.6, G.3, G.7, G.4
:excerpt: To place at a given point (as an extremity) a straight line equal to a given straight line.

**Heath ID:** `I.2 <https://geometor.github.io/euclid/I/2/>`_

.. picture:: G.8.png

.. _G.8:

G.8
===

    To place at a given point (as an extremity) a straight line equal to a given straight line.

Let ``A`` be the given point, and ``BC`` the given straight line.

Thus it is required to place at the point ``A`` (as an extremity) a straight line equal to the given straight line ``BC``. 

From the point ``A`` to the point ``B`` let the straight line ``AB`` be joined; [:ref:`G.3`] and on it let the equilateral triangle ``DAB`` be constructed. [:ref:`G.5`]

Let the straight lines ``AE``, ``BF`` be produced in a straight line with ``DA``, ``DB``; [:ref:`G.7`] with centre ``B`` and distance ``BC`` let the circle ``CGH`` be described; [:ref:`G.4`] and again, with centre ``D`` and distance ``DG`` let the circle ``GKL`` be described. [:ref:`G.4`]

Then, since the point ``B`` is the centre of the circle ``CGH``, ``BC`` is equal to ``BG``.
        

Again, since the point ``D`` is the centre of the circle ``GKL``, ``DL`` is equal to ``DG``.

And in these ``DA`` is equal to ``DB``; therefore the remainder ``AL`` is equal to the remainder ``BG.`` [:ref:`G.6`]
        

But ``BC`` was also proved equal to ``BG``; therefore each of the straight lines ``AL``, ``BC`` is equal to ``BG``.

And things which are equal to the same thing are also equal to one another; [:ref:`G.1`] therefore ``AL`` is also equal to ``BC``.

Therefore at the given point ``A`` the straight line ``AL`` is placed equal to the given straight line ``BC``.


**Q. E. D.**


(Being) what it was required to do.


.. note::


   **1. (as an extremity).**

   

   I have inserted these words because to place a straight line ``at`` a given point

    (πρὸς τῷ δοθέντι σημείῳ) is not quite clear enough, at least in English.


.. note::


   **11. Let the straight lines AE, BF be produced....**

   

   It will be observed that in this first application of :ref:`G.7`, and again in :ref:`G.12`, Euclid speaks of the ``continuation`` of the straight line as that which is produced in such cases, ἐκβεβλήσθωσαν and προσεκβεβλήσθωσαν meaning little more than ``drawing`` straight lines in a straight line with

    the given straight lines. The first place in which Euclid uses phraseology exactly corresponding to ours when speaking of a straight line being produced is in :ref:`G.25`: let one side of it, ``BC``, be produced to ``D``

    (προσεκβεβλήσθω αὐτοῦ μία πλευρὰ ἡ ΒΓ ἐπὶ τὸ Δ).


.. note::


   **23. the remainder AL...the remainder BG.**

   

   The Greek expressions are λοιπὴ ἡ ΑΛ and λοιπῇ τῇ BH, and the literal translation would be ``AL`` (or ``BG``) ``remaining``,

    but the shade of meaning conveyed by the position of the definite article can hardly be expressed in English.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.8" [label="G.8", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.8/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.8" -> "G.5";
     "G.5" -> "G.2";
     "G.8" -> "G.6";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.8" -> "G.7";
   }



Required for
------------

:ref:`G.17`, :ref:`G.19`, :ref:`G.20`, :ref:`G.21`, :ref:`G.23`, :ref:`G.24`, :ref:`G.25`, :ref:`G.26`, :ref:`G.27`, :ref:`G.28`, :ref:`G.30`, :ref:`G.31`, :ref:`G.32`, :ref:`G.33`, :ref:`G.34`, :ref:`G.35`, :ref:`G.36`, :ref:`G.38`, :ref:`G.39`, :ref:`G.42`, :ref:`G.9`, :ref:`G.43`, :ref:`G.44`, :ref:`G.45`, :ref:`G.46`, :ref:`G.47`, :ref:`G.48`, :ref:`G.49`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.56`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`, :ref:`G.12`, :ref:`G.14`, :ref:`G.15`, :ref:`G.16`
