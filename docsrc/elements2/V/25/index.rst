:order: 25
:number: 211
:type: prop
:dependencies: V.19


.. _V.25:

V.25
====

   If four magnitudes be proportional, the greatest and the least are greater than the remaining two.

``If four magnitudes be proportional``, ``the greatest and the least are greater than the remaining two``.

Let the four magnitudes ``AB``, ``CD``, ``E``, ``F`` be proportional so that, as ``AB`` is to ``CD``, so is ``E`` to ``F``, and let ``AB`` be the greatest of them and ``F`` the least; I say that ``AB``, ``F`` are greater than ``CD``, ``E``.

For let ``AG`` be made equal to ``E``, and ``CH`` equal to ``F``.

Since, as ``AB`` is to ``CD``, so is ``E`` to ``F``, and ``E`` is equal to ``AG``, and ``F`` to ``CH``,


.. container:: center

   therefore, as ``AB`` is to ``CD``, so is ``AG`` to ``CH``.


And since, as the whole ``AB`` is to the whole ``CD``, so is the part ``AG`` subtracted to the part ``CH`` subtracted,


.. container:: center

   the remainder ``GB`` will also be to the remainder ``HD`` as the whole ``AB`` is to the whole ``CD``. [:ref:`V.19`]


But ``AB`` is greater than ``CD``;


.. container:: center

   therefore ``GB`` is also greater than ``HD``.


And, since ``AG`` is equal to ``E``, and ``CH`` to ``F``, therefore ``AG``, ``F`` are equal to ``CH``, ``E``.

And if, ``GB``, ``HD`` being unequal, and ``GB`` greater, ``AG``, ``F`` be added to ``GB`` and ``CH``, ``E`` be added to ``HD``,


.. container:: center

   it follows that ``AB``, ``F`` are greater than ``CD``, ``E``.


Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "V.20" [URL="/elements2/V/20/", target="_top"];
     "V.14" [URL="/elements2/V/14/", target="_top"];
     "V.10" [URL="/elements2/V/10/", target="_top"];
     "V.25" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/V/25/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.5/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.4/", target="_top"];
     "V.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/2/", target="_top"];
     "V.7" [URL="/elements2/V/7/", target="_top"];
     "elem.5.17 elem.5.18" [style="rounded,filled", fillcolor=orange];
     "V.13" [URL="/elements2/V/13/", target="_top"];
     "V.11" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/11/", target="_top"];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/1/", target="_top"];
     "elem.5.20 elem.5.21 elem.5.22 elem.5.23" [style="rounded,filled", fillcolor=orange];
     "V.12" [URL="/elements2/V/12/", target="_top"];
     "V.21" [URL="/elements2/V/21/", target="_top"];
     "V.16" [URL="/elements2/V/16/", target="_top"];
     "V.19" [URL="/elements2/V/19/", target="_top"];
     "V.15" [URL="/elements2/V/15/", target="_top"];
     "V.8" [URL="/elements2/V/8/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.7/", target="_top"];
     "V.17" [URL="/elements2/V/17/", target="_top"];
     "V.16" -> "V.20";
     "V.16" -> "V.14";
     "V.14" -> "V.10";
     "V.20" -> "V.10";
     "V.21" -> "V.10";
     "V.7" -> "V.def.5";
     "V.12" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.16" -> "V.def.5";
     "V.8" -> "V.def.4";
     "V.17" -> "V.2";
     "V.10" -> "V.7";
     "V.15" -> "V.7";
     "V.16" -> "elem.5.17 elem.5.18";
     "V.14" -> "V.13";
     "V.20" -> "V.13";
     "V.21" -> "V.13";
     "V.16" -> "V.11";
     "V.19" -> "V.11";
     "V.8" -> "V.1";
     "V.12" -> "V.1";
     "V.17" -> "V.1";
     "V.16" -> "elem.5.20 elem.5.21 elem.5.22 elem.5.23";
     "V.15" -> "V.12";
     "V.16" -> "V.21";
     "V.19" -> "V.16";
     "V.25" -> "V.19";
     "V.16" -> "V.15";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "V.21" -> "V.8";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "V.19" -> "V.17";
   }
