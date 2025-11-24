:order: 86
:original_id: III.10
:type: prop
:dependencies: g.2, g.80, g.84

.. _g.86:

G.86
====

**Heath ID:** :ref:`III.10`

   A circle does not cut a circle at more points than two.

``A circle does not cut a circle at more points than two``.

For, if possible, let the circle ``ABC`` cut the circle ``DEF`` at more points than two, namely ``B``, ``C``, ``F``, ``H``;

let ``BH``, ``BG`` be joined and bisected at the points ``K``, ``L``, and from ``K``, ``L`` let ``KC``, ``LM`` be drawn at right angles to ``BH``, ``BG`` and carried through to the points ``A``, ``E``.

Then, since in the circle ``ABC`` a straight line ``AC`` cuts a straight line ``BH`` into two equal parts and at right angles,


.. container:: center

   the centre of the circle ``ABC`` is on ``AC``. [:ref:`g.84`]


Again, since in the same circle ``ABC`` a straight line ``NO`` cuts a straight line ``BG`` into two equal parts and at right angles,


.. container:: center

   the centre of the circle ``ABC`` is on ``NO``.


But it was also proved to be on ``AC``, and the straight lines ``AC``, ``NO`` meet at no point except at ``P``;


.. container:: center

   therefore the point ``P`` is the centre of the circle ``ABC``.


Similarly we can prove that ``P`` is also the centre of the circle ``DEF``;


.. container:: center

   therefore the two circles ``ABC``, ``DEF`` which cut one another have the same centre ``P``: which is impossible. [:ref:`g.80`]


Therefore etc. Q. E. D.
The word circle (κύκλος) is here employed in the unusual sense of the ``circumference`` (περιφέρεια) of a circle. Cf. note on :ref:`g.2`.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.84" [label="G.84", style="rounded,filled", fillcolor=orange, URL="/elements2/g.84/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.86" [label="G.86", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.86/", target="_top"];
     "G.80" [label="G.80", URL="/elements2/g.80/", target="_top"];
     "G.86" -> "G.84";
     "G.80" -> "G.2";
     "G.86" -> "G.2";
     "G.86" -> "G.80";
   }



Required for
------------

:ref:`g.105`, :ref:`g.107`, :ref:`g.108`, :ref:`g.109`, :ref:`g.110`, :ref:`g.111`, :ref:`g.132`, :ref:`g.133`, :ref:`g.135`, :ref:`g.136`, :ref:`g.205`, :ref:`g.530`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.553`, :ref:`g.555`, :ref:`g.531`, :ref:`g.568`, :ref:`g.569`, :ref:`g.574`, :ref:`g.578`, :ref:`g.565`, :ref:`g.567`
