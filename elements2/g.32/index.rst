:order: 32
:original_id: I.22
:type: prop
:dependencies: g.30, g.9

.. _g.32:

G.32
====

**Heath ID:** :ref:`I.22`

   Out of three straight lines, which are equal to three given straight lines, to construct a triangle: thus it is necessary that two of the straight lines taken together in any manner should be greater than the remaining one.

Let the three given straight lines be ``A``, ``B``, ``C``, and of these let two taken together in any manner be greater than the remaining one, namely ``A``, ``B`` greater than ``C``, ``A``, ``C`` greater than ``B``, and ``B``, ``C`` greater than ``A``; thus it is required to construct a triangle out of straight lines equal to ``A``, ``B``, ``C``. [:ref:`g.30`]

Let there be set out a straight line ``DE``, terminated at ``D`` but of infinite length in the direction of ``E``, and let ``DF`` be made equal to ``A``, ``FG`` equal to ``B``, and ``GH`` equal to ``C``. [:ref:`g.9`]

With centre ``F`` and distance ``FD`` let the circle ``DKL`` be described; again, with centre ``G`` and distance ``GH`` let the circle ``KLH`` be described; and let ``KF``, ``KG`` be joined;

I say that the triangle ``KFG`` has been constructed out of three straight lines equal to ``A``, ``B``, ``C``. 

For, since the point ``F`` is the centre of the circle ``DKL``, ``FD`` is equal to ``FK``.

But ``FD`` is equal to ``A``; therefore ``KF`` is also equal to ``A``.

Again, since the point ``G`` is the centre of the circle ``LKH``, ``GH`` is equal to ``GK``.

But ``GH`` is equal to ``C``; therefore ``KG`` is also equal to ``C``. And ``FG`` is also equal to ``B``; therefore the three straight lines ``KF``, ``FG``, ``GK`` are equal to the three straight lines ``A``, ``B``, ``C``.

Therefore out of the three straight lines ``KF``, ``FG``, ``GK``, which are equal to the three given straight lines ``A``, ``B``, ``C``, the triangle ``KFG`` has been constructed.


**Q. E. D.**


Q. E. F.


.. note::


   **2-4**

   

   This is the first case in the Elements of a διορισμός to a problem in the sense of a statement of the conditions or limits of the possibility of a solution. The criterion is of course supplied by the preceding proposition.


.. note::


   **2. thus it is necessary.**

   

   This is usually translated (e.g. by Williamson and Simson) But it is necessary,

    which is however inaccurate, since the Greek is not δεῖ δέ but δεῖ δή. The words are the same as those used to introduce the διορισμός in the other sense of the definition

    or particular statement

    of a construction to be effected. Hence, as in the latter case we say thus it is required

    (e.g. to bisect the finite straight line ``AB``, :ref:`g.17`), we should here translate ``thus`` it is necessary.


.. note::


   **4**

   

   To this enunciation all the MSS. and Boethius add, after the διορισμός, the words because in any triangle two sides taken together in any manner are greater than the remaining one.

    But this explanation has the appearance of a gloss, and it is omitted by Proclus and Campanus. Moreover there is no corresponding addition to the διορισμός of :ref:`g.200`.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.32" [label="G.32", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.32/", target="_top"];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.27" [label="G.27", URL="/elements2/g.27/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.30" [label="G.30", URL="/elements2/g.30/", target="_top"];
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.29" [label="G.29", style="rounded,filled", fillcolor=orange, URL="/elements2/g.29/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.17" -> "G.16";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.28" -> "G.27";
     "G.24" -> "G.21";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.32" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.15" -> "G.14";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.32" -> "G.30";
     "G.30" -> "G.28";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.27" -> "G.25";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.24" -> "G.22";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.11" -> "G.10";
     "G.30" -> "G.29";
     "G.14" -> "G.12";
     "G.28" -> "G.12";
     "G.30" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }
