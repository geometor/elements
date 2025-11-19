:order: 23
:number: 209
:type: prop
:dependencies: V.11, V.15, V.16, V.21


.. _V.23:

V.23
====

   If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, they will also be in the same ratio
          ex aequali.

Let there be three magnitudes ``A``, ``B``, ``C``, and others equal to them in multitude, which, taken two and two together, are in the same proportion, namely ``D``, ``E``, ``F``; and let the proportion of them be perturbed, so that,


.. container:: center

   as ``A`` is to ``B``, so is ``E`` to ``F``,


and, as ``B`` is to ``C``, so is ``D`` to ``E``; I say that, as ``A`` is to ``C``, so is ``D`` to ``F``.

Of ``A``, ``B``, ``D`` let equimultiples ``G``, ``H``, ``K`` be taken, and of ``C``, ``E``, ``F`` other, chance, equimultiples ``L``, ``M``, ``N``.

Then, since ``G``, ``H`` are equimultiples of ``A``, ``B``, and parts have the same ratio as the same multiples of them, [:ref:`V.15`]


.. container:: center

   therefore, as ``A`` is to ``B``, so is ``G`` to ``H``.


For the same reason also,


.. container:: center

   as ``E`` is to ``F``, so is ``M`` to ``N``.


And, as ``A`` is to ``B``, so is ``E`` to ``F``;


.. container:: center

   therefore also, as ``G`` is to ``H``, so is ``M`` to ``N``. [:ref:`V.11`]


Next, since, as ``B`` is to ``C``, so is ``D`` to ``E``, alternately, also, as ``B`` is to ``D``, so is ``C`` to ``E``. [:ref:`V.16`]

And, since ``H``, ``K`` are equimultiples of ``B``, ``D``, and parts have the same ratio as their equimultiples,


.. container:: center

   therefore, as ``B`` is to ``D``, so is ``H`` to ``K``. [:ref:`V.15`]


But, as ``B`` is to ``D``, so is ``C`` to ``E``;


.. container:: center

   therefore also, as ``H`` is to ``K``, so is ``C`` to ``E``. [:ref:`V.11`]


Again, since ``L``, ``M`` are equimultiples of ``C``, ``E``,


.. container:: center

   therefore, as ``C`` is to ``E``, so is ``L`` to ``M``. [:ref:`V.15`]


But, as ``C`` is to ``E``, so is ``H`` to ``K``;


.. container:: center

   therefore also, as ``H`` is to ``K``, so is ``L`` to ``M``, [:ref:`V.11`]


and, alternately, as ``H`` is to ``L``, so is ``K`` to ``M``. [:ref:`V.16`]

But it was also proved that,


.. container:: center

   as ``G`` is to ``H``, so is ``M`` to ``N``.


Since, then, there are three magnitudes ``G``, ``H``, ``L``, and others equal to them in multitude ``K``, ``M``, ``N``, which taken two and two together are in the same ratio, and the proportion of them is perturbed, therefore, ex aequali, if ``G`` is in excess of ``L``, ``K`` is also in excess of ``N``; if equal, equal; and if less, less. [:ref:`V.21`]

And ``G``, ``K`` are equimultiples of ``A``, ``D``, and ``L``, ``N`` of ``C``, ``F``.

Therefore, as ``A`` is to ``C``, so is ``D`` to ``F``.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "V.14" [URL="/elements2/V/14/", target="_top"];
     "elem.5.17 elem.5.18" [style="rounded,filled", fillcolor=orange];
     "V.21" [URL="/elements2/V/21/", target="_top"];
     "V.20" [URL="/elements2/V/20/", target="_top"];
     "V.16" [URL="/elements2/V/16/", target="_top"];
     "V.10" [URL="/elements2/V/10/", target="_top"];
     "V.8" [URL="/elements2/V/8/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.7/", target="_top"];
     "V.12" [URL="/elements2/V/12/", target="_top"];
     "V.11" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/11/", target="_top"];
     "elem.5.20 elem.5.21 elem.5.22 elem.5.23" [style="rounded,filled", fillcolor=orange];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.5/", target="_top"];
     "V.13" [URL="/elements2/V/13/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.4/", target="_top"];
     "V.23" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/V/23/", target="_top"];
     "V.15" [URL="/elements2/V/15/", target="_top"];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/1/", target="_top"];
     "V.7" [URL="/elements2/V/7/", target="_top"];
     "V.16" -> "V.14";
     "V.16" -> "elem.5.17 elem.5.18";
     "V.16" -> "V.21";
     "V.23" -> "V.21";
     "V.16" -> "V.20";
     "V.23" -> "V.16";
     "V.14" -> "V.10";
     "V.20" -> "V.10";
     "V.21" -> "V.10";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "V.21" -> "V.8";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "V.15" -> "V.12";
     "V.16" -> "V.11";
     "V.23" -> "V.11";
     "V.16" -> "elem.5.20 elem.5.21 elem.5.22 elem.5.23";
     "V.7" -> "V.def.5";
     "V.12" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.16" -> "V.def.5";
     "V.14" -> "V.13";
     "V.20" -> "V.13";
     "V.21" -> "V.13";
     "V.8" -> "V.def.4";
     "V.16" -> "V.15";
     "V.23" -> "V.15";
     "V.8" -> "V.1";
     "V.12" -> "V.1";
     "V.10" -> "V.7";
     "V.15" -> "V.7";
   }
