:order: 23
:original_id: I.14
:type: prop
:dependencies: g.21, g.1, g.6, g.22

.. _g.23:

G.23
====

**Heath ID:** :ref:`I.14`

   If with any straight line, and at a point on it, two straight lines not lying on the same side make the adjacent angles equal to two right angles, the two straight lines will be in a straight line with one another.

For with any straight line ``AB``, and at the point ``B`` on it, let the two straight lines ``BC``, ``BD`` not lying on the same side make the adjacent angles ``ABC``, ``ABD`` equal to two right angles;

I say that ``BD`` is in a straight line with ``CB``. 

For, if ``BD`` is not in a straight line with ``BC``, let ``BE`` be in a straight line with ``CB``.

Then, since the straight line ``AB`` stands on the straight line ``CBE``, 
        the angles ``ABC``, ``ABE`` are equal to two right angles. [:ref:`g.21`] But the angles ``ABC``, ``ABD`` are also equal to two right angles; therefore the angles ``CBA``, ``ABE`` are equal to the angles ``CBA``, ``ABD``. [:ref:`g.22` and :ref:`g.1`]

Let the angle ``CBA`` be subtracted from each; therefore the remaining angle ``ABE`` is equal to the remaining angle ``ABD``, [:ref:`g.6`] the less to the greater: which is impossible. Therefore ``BE`` is not in a straight line with ``CB``.

Similarly we can prove that neither is any other straight line except ``BD``. Therefore ``CB`` is in a straight line with ``BD``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. If with any straight line....**

   

   There is no greater difficulty in translating the works of the Greek geometers than that of accurately giving the force of prepositions. πρός, for instance, is used in all sorts of expressions with various shades of meaning. The present enunciation begins ἐὰν πρός τινι εὐθείᾳ καὶ τῷ πρὸς αὐτῆ σημείῳ, and it is really necessary in this one sentence to translate πρός by three different words, ``with``, ``at``, and ``on``. The first πρός must be translated by ``with`` because two straight lines make

    an angle ``with`` one another. On the other hand, where the similar expression πρὸς τῇ δοθείση εὐθείᾳ occurs in :ref:`g.33`, but it is a question of constructing

    an angle (συστἡσασθαι), we have to say to construct ``on`` a given straight line.

    Against would perhaps be the English word coming nearest to expressing all these meanings of πρός, but it would be intolerable as a translation.


.. note::


   **17**

   

   Todhunter points out that for the inference in this line :ref:`g.22`, that all right angles are equal, is necessary as well as the Common Notion that things which are equal to the same thing (or rather, here, to ``equal things``) are equal. A similar remark applies to steps in the proofs of :ref:`g.24` and :ref:`g.39`.


.. note::


   **24. we can prove.**

   

   The Greek expresses this by the future of the verb, δείξομεν, we shall prove,

    which however would perhaps be misleading in English.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.23" [label="G.23", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.23/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.23" -> "G.21";
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.19" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.8" -> "G.6";
     "G.23" -> "G.6";
     "G.21" -> "G.19";
     "G.19" -> "G.15";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.23" -> "G.1";
     "G.8" -> "G.5";
     "G.19" -> "G.5";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.23" -> "G.22";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.12" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
   }



Required for
------------

:ref:`g.58`, :ref:`g.60`, :ref:`g.61`, :ref:`g.71`, :ref:`g.72`, :ref:`g.73`, :ref:`g.74`, :ref:`g.75`, :ref:`g.70`, :ref:`g.92`, :ref:`g.94`, :ref:`g.116`, :ref:`g.117`, :ref:`g.118`, :ref:`g.131`, :ref:`g.132`, :ref:`g.133`, :ref:`g.182`, :ref:`g.183`, :ref:`g.184`, :ref:`g.185`, :ref:`g.189`, :ref:`g.191`, :ref:`g.197`, :ref:`g.200`, :ref:`g.201`, :ref:`g.202`, :ref:`g.204`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.347`, :ref:`g.353`, :ref:`g.358`, :ref:`g.361`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.371`, :ref:`g.373`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.381`, :ref:`g.382`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.395`, :ref:`g.396`, :ref:`g.397`, :ref:`g.399`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.509`, :ref:`g.521`, :ref:`g.522`, :ref:`g.524`, :ref:`g.525`, :ref:`g.526`, :ref:`g.527`, :ref:`g.528`, :ref:`g.530`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.553`, :ref:`g.555`, :ref:`g.531`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`, :ref:`g.557`, :ref:`g.568`, :ref:`g.569`, :ref:`g.570`, :ref:`g.571`, :ref:`g.572`, :ref:`g.573`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.560`, :ref:`g.562`, :ref:`g.563`
