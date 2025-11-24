:order: 30
:original_id: I.20
:type: prop
:dependencies: g.28, g.12, g.29

.. _g.30:

G.30
====

**Heath ID:** :ref:`I.20`

   In any triangle two sides taken together in any manner are greater than the remaining one.

For let ``ABC`` be a triangle; I say that in the triangle ``ABC`` two sides taken together in any manner are greater than the remaining one, namely ``BA``, ``AC`` greater than ``BC``, ``AB``, ``BC`` greater than ``AC``, ``BC``, ``CA`` greater than ``AB``.

For let ``BA`` be drawn through to the point ``D``, let ``DA`` be made equal to ``CA``, and let ``DC`` be joined.

Then, since ``DA`` is equal to ``AC``, the angle ``ADC`` is also equal to the angle ``ACD``; [:ref:`g.12`] 
        therefore the angle ``BCD`` is greater than the angle ``ADC``. [:ref:`g.29`]

And, since ``DCB`` is a triangle having the angle ``BCD`` greater than the angle ``BDC``, and the greater angle is subtended by the greater side, [:ref:`g.28`] therefore ``DB`` is greater than ``BC``.
        

But ``DA`` is equal to ``AC``; therefore ``BA``, ``AC`` are greater than ``BC``.

Similarly we can prove that ``AB``, ``BC`` are also greater than ``CA``, and ``BC``, ``CA`` than ``AB``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   It was the habit of the Epicureans, says Proclus (p. 322), to ridicule this theorem as being evident even to an ass and requiring no proof, and their allegation that the theorem was known

    (γνώριμον) even to an ass was based on the fact that, if fodder is placed at one angular point and the ass at another, he does not, in order to get to his food, traverse the two sides of the triangle but only the one side separating them (an argument which makes Savile exclaim that its authors were digni ipsi, qui cum Asino foenum essent,

    p. 78). Proclus replies truly that a mere perception of the truth of the theorem is a different thing from a scientific proof of it and a knowledge of the reason ``why`` it is true. Moreover, as Simson says, the number of axioms should not be increased without necessity.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
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
     "G.28" [label="G.28", URL="/elements2/g.28/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.30" [label="G.30", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.30/", target="_top"];
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
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.15" -> "G.14";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.30" -> "G.28";
     "G.27" -> "G.25";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
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



Required for
------------

:ref:`g.31`, :ref:`g.32`, :ref:`g.88`, :ref:`g.94`, :ref:`g.82`, :ref:`g.83`, :ref:`g.506`, :ref:`g.507`, :ref:`g.578`
