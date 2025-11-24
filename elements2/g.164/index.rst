:order: 164
:original_id: V.23
:type: prop
:dependencies: g.150, g.154, g.159, g.156

.. _g.164:

G.164
=====

**Heath ID:** :ref:`V.23`

   If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, they will also be in the same ratio
          ex aequali.

Let there be three magnitudes ``A``, ``B``, ``C``, and others equal to them in multitude, which, taken two and two together, are in the same proportion, namely ``D``, ``E``, ``F``; and let the proportion of them be perturbed, so that,


.. container:: center

   as ``A`` is to ``B``, so is ``E`` to ``F``,


and, as ``B`` is to ``C``, so is ``D`` to ``E``; I say that, as ``A`` is to ``C``, so is ``D`` to ``F``.

Of ``A``, ``B``, ``D`` let equimultiples ``G``, ``H``, ``K`` be taken, and of ``C``, ``E``, ``F`` other, chance, equimultiples ``L``, ``M``, ``N``.

Then, since ``G``, ``H`` are equimultiples of ``A``, ``B``, and parts have the same ratio as the same multiples of them, [:ref:`g.154`]


.. container:: center

   therefore, as ``A`` is to ``B``, so is ``G`` to ``H``.


For the same reason also,


.. container:: center

   as ``E`` is to ``F``, so is ``M`` to ``N``.


And, as ``A`` is to ``B``, so is ``E`` to ``F``;


.. container:: center

   therefore also, as ``G`` is to ``H``, so is ``M`` to ``N``. [:ref:`g.150`]


Next, since, as ``B`` is to ``C``, so is ``D`` to ``E``, alternately, also, as ``B`` is to ``D``, so is ``C`` to ``E``. [:ref:`g.159`]

And, since ``H``, ``K`` are equimultiples of ``B``, ``D``, and parts have the same ratio as their equimultiples,


.. container:: center

   therefore, as ``B`` is to ``D``, so is ``H`` to ``K``. [:ref:`g.154`]


But, as ``B`` is to ``D``, so is ``C`` to ``E``;


.. container:: center

   therefore also, as ``H`` is to ``K``, so is ``C`` to ``E``. [:ref:`g.150`]


Again, since ``L``, ``M`` are equimultiples of ``C``, ``E``,


.. container:: center

   therefore, as ``C`` is to ``E``, so is ``L`` to ``M``. [:ref:`g.154`]


But, as ``C`` is to ``E``, so is ``H`` to ``K``;


.. container:: center

   therefore also, as ``H`` is to ``K``, so is ``L`` to ``M``, [:ref:`g.150`]


and, alternately, as ``H`` is to ``L``, so is ``K`` to ``M``. [:ref:`g.159`]

But it was also proved that,


.. container:: center

   as ``G`` is to ``H``, so is ``M`` to ``N``.


Since, then, there are three magnitudes ``G``, ``H``, ``L``, and others equal to them in multitude ``K``, ``M``, ``N``, which taken two and two together are in the same ratio, and the proportion of them is perturbed, therefore, ex aequali, if ``G`` is in excess of ``L``, ``K`` is also in excess of ``N``; if equal, equal; and if less, less. [:ref:`g.156`]

And ``G``, ``K`` are equimultiples of ``A``, ``D``, and ``L``, ``N`` of ``C``, ``F``.

Therefore, as ``A`` is to ``C``, so is ``D`` to ``F``.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.159" [label="G.159", URL="/elements2/g.159/", target="_top"];
     "G.151" [label="G.151", URL="/elements2/g.151/", target="_top"];
     "G.157" [label="G.157", style="rounded,filled", fillcolor=orange, URL="/elements2/g.157/", target="_top"];
     "G.156" [label="G.156", URL="/elements2/g.156/", target="_top"];
     "G.140" [label="G.140", style="rounded,filled", fillcolor=orange, URL="/elements2/g.140/", target="_top"];
     "G.144" [label="G.144", URL="/elements2/g.144/", target="_top"];
     "G.149" [label="G.149", URL="/elements2/g.149/", target="_top"];
     "G.137" [label="G.137", style="rounded,filled", fillcolor=orange, URL="/elements2/g.137/", target="_top"];
     "G.155" [label="G.155", URL="/elements2/g.155/", target="_top"];
     "G.145" [label="G.145", style="rounded,filled", fillcolor=orange, URL="/elements2/g.145/", target="_top"];
     "G.150" [label="G.150", style="rounded,filled", fillcolor=orange, URL="/elements2/g.150/", target="_top"];
     "G.154" [label="G.154", URL="/elements2/g.154/", target="_top"];
     "G.152" [label="G.152", URL="/elements2/g.152/", target="_top"];
     "G.146" [label="G.146", style="rounded,filled", fillcolor=orange, URL="/elements2/g.146/", target="_top"];
     "G.153" [label="G.153", URL="/elements2/g.153/", target="_top"];
     "G.164" [label="G.164", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.164/", target="_top"];
     "G.158" [label="G.158", style="rounded,filled", fillcolor=orange, URL="/elements2/g.158/", target="_top"];
     "G.147" [label="G.147", URL="/elements2/g.147/", target="_top"];
     "G.164" -> "G.159";
     "G.154" -> "G.151";
     "G.159" -> "G.157";
     "G.159" -> "G.156";
     "G.164" -> "G.156";
     "G.144" -> "G.140";
     "G.151" -> "G.140";
     "G.152" -> "G.140";
     "G.159" -> "G.140";
     "G.149" -> "G.144";
     "G.154" -> "G.144";
     "G.153" -> "G.149";
     "G.155" -> "G.149";
     "G.156" -> "G.149";
     "G.147" -> "G.137";
     "G.151" -> "G.137";
     "G.159" -> "G.155";
     "G.147" -> "G.145";
     "G.159" -> "G.150";
     "G.164" -> "G.150";
     "G.159" -> "G.154";
     "G.164" -> "G.154";
     "G.153" -> "G.152";
     "G.155" -> "G.152";
     "G.156" -> "G.152";
     "G.147" -> "G.146";
     "G.152" -> "G.146";
     "G.159" -> "G.153";
     "G.159" -> "G.158";
     "G.149" -> "G.147";
     "G.153" -> "G.147";
     "G.155" -> "G.147";
     "G.156" -> "G.147";
   }
