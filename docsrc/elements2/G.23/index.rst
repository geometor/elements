:order: 23
:original_id: I.14
:type: prop
:dependencies: G.21, G.1, G.6, G.22
:excerpt: If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

**Heath ID:** `I.14 <https://geometor.github.io/euclid/I/14/>`_

.. picture:: G.23.png

.. _G.23:

G.23
====

    If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

For with any straight line ``AB``, and at the point ``B`` on it, let the two straight lines ``BC``, ``BD`` not lying on the same side make the adjacent angles ``ABC``, ``ABD`` equal to two right angles;

I say that ``BD`` is in a straight line with ``CB``. 

For, if ``BD`` is not in a straight line with ``BC``, let ``BE`` be in a straight line with ``CB``.

Then, since the straight line ``AB`` stands on the straight line ``CBE``, 
        the angles ``ABC``, ``ABE`` are equal to two right angles. [:ref:`G.21`] But the angles ``ABC``, ``ABD`` are also equal to two right angles; therefore the angles ``CBA``, ``ABE`` are equal to the angles ``CBA``, ``ABD``. [:ref:`G.22` and :ref:`G.1`]

Let the angle ``CBA`` be subtracted from each; therefore the remaining angle ``ABE`` is equal to the remaining angle ``ABD``, [:ref:`G.6`] the less to the greater: which is impossible. Therefore ``BE`` is not in a straight line with ``CB``.

Similarly we can prove that neither is any other straight line except ``BD``. Therefore ``CB`` is in a straight line with ``BD``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. If with any straight line....**

   

   There is no greater difficulty in translating the works of the Greek geometers than that of accurately giving the force of prepositions. πρός, for instance, is used in all sorts of expressions with various shades of meaning. The present enunciation begins ἐὰν πρός τινι εὐθείᾳ καὶ τῷ πρὸς αὐτῆ σημείῳ, and it is really necessary in this one sentence to translate πρός by three different words, ``with``, ``at``, and ``on``. The first πρός must be translated by ``with`` because two straight lines make

    an angle ``with`` one another. On the other hand, where the similar expression πρὸς τῇ δοθείση εὐθείᾳ occurs in :ref:`G.33`, but it is a question of constructing

    an angle (συστἡσασθαι), we have to say to construct ``on`` a given straight line.

    Against would perhaps be the English word coming nearest to expressing all these meanings of πρός, but it would be intolerable as a translation.


.. note::


   **17**

   

   Todhunter points out that for the inference in this line :ref:`G.22`, that all right angles are equal, is necessary as well as the Common Notion that things which are equal to the same thing (or rather, here, to ``equal things``) are equal. A similar remark applies to steps in the proofs of :ref:`G.24` and :ref:`G.39`.


.. note::


   **24. we can prove.**

   

   The Greek expresses this by the future of the verb, δείξομεν, we shall prove,

    which however would perhaps be misleading in English.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.23" [label="G.23", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.23/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.8" -> "G.6";
     "G.23" -> "G.6";
     "G.21" -> "G.19";
     "G.23" -> "G.21";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.11" -> "G.10";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.19" -> "G.15";
     "G.19" -> "G.5";
     "G.8" -> "G.5";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.23" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.14" -> "G.12";
     "G.23" -> "G.22";
     "G.15" -> "G.14";
     "G.9" -> "G.8";
     "G.19" -> "G.9";
     "G.12" -> "G.9";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.12" -> "G.11";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
   }



Required for
------------

:ref:`G.58`, :ref:`G.60`, :ref:`G.61`
