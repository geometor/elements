:order: 88
:original_id: III.12
:type: prop
:dependencies: g.30

.. _g.88:

G.88
====

**Heath ID:** :ref:`III.12`

   If two circles touch one another externally, the straight line joining their centres will pass through the point of contact.

For let the two circles ``ABC``, ``ADE`` touch one another externally at the point ``A``, and let the centre ``F`` of ``ABC``, and the centre ``G`` of ``ADE``, be taken; I say that the straight line joined from ``F`` to ``G`` will pass through the point of contact at ``A``.

For suppose it does not, but, if possible, let it pass as ``FCDG``, and let ``AF``, ``AG`` be joined.

Then, since the point ``F`` is the centre of the circle ``ABC``,


.. container:: center

   ``FA`` is equal to ``FC``.


Again, since the point ``G`` is the centre of the circle ``ADE``,


.. container:: center

   ``GA`` is equal to ``GD``.


But ``FA`` was also proved equal to ``FC``;


.. container:: center

   therefore ``FA``, ``AG`` are equal to ``FC``, ``GD``, so that the whole ``FG`` is greater than ``FA``, ``AG``;


but it is also less [:ref:`g.30`]: which is impossible.

Therefore the straight line joined from ``F`` to ``G`` will not fail to pass through the point of contact at ``A``;


.. container:: center

   therefore it will pass through it.


Therefore etc. Q. E. D.]
will not fail to pass. The Greek has the double negative, οὐκ ἄρα ἡ...εὐθεῖα... οὐκ ἐλεύσεται, literally the straight line...will not ``not``-pass....


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.88" [label="G.88", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.88/", target="_top"];
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
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.15" -> "G.14";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.88" -> "G.30";
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
