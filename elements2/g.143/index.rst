:order: 143
:original_id: V.6
:type: prop
:dependencies: g.138

.. _g.143:

G.143
=====

**Heath ID:** :ref:`V.6`

   If two magnitudes be equimultiples of two magnitudes, and any magnitudes subtracted from them be equimultiples of the same, the remainders also are either equal to the same or equimultiples of them.

For let two magnitudes ``AB``, ``CD`` be equimultiples of two magnitudes ``E``, ``F``, and let ``AG``, ``CH`` subtracted from them be equimultiples of the same two ``E``, ``F``;

I say that the remainders also, ``GB``, ``HD``, are either equal to ``E``, ``F`` or equimultiples of them.

For, first, let ``GB`` be equal to ``E``; I say that ``HD`` is also equal to ``F``.

For let ``CK`` be made equal to ``F``.

Since ``AG`` is the same multiple of ``E`` that ``CH`` is of ``F``, while ``GB`` is equal to ``E`` and ``KC`` to ``F``, therefore ``AB`` is the same multiple of ``E`` that ``KH`` is of ``F``. [:ref:`g.138`]

But, by hypothesis, ``AB`` is the same multiple of ``E`` that ``CD`` is of ``F``; therefore ``KH`` is the same multiple of ``F`` that ``CD`` is of ``F``.

Since then each of the magnitudes ``KH``, ``CD`` is the same multiple of ``F``,


.. container:: center

   therefore ``KH`` is equal to ``CD``.


Let ``CH`` be subtracted from each; therefore the remainder ``KC`` is equal to the remainder ``HD``.

But ``F`` is equal to ``KC``; therefore ``HD`` is also equal to ``F``.

Hence, if ``GB`` is equal to ``E``, ``HD`` is also equal to ``F``.

Similarly we can prove that, even if ``GB`` be a multiple of ``E``, ``HD`` is also the same multiple of ``F``.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.138" [label="G.138", style="rounded,filled", fillcolor=orange, URL="/elements2/g.138/", target="_top"];
     "G.143" [label="G.143", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.143/", target="_top"];
     "G.143" -> "G.138";
   }
