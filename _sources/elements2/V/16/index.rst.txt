:order: 16
:number: 202
:type: prop
:dependencies: V.11, V.14, V.15, V.20, V.21, V.def.5, elem.5.17 elem.5.18, elem.5.20 elem.5.21 elem.5.22 elem.5.23


.. _V.16:

V.16
====

   If four magnitudes be proportional, they will also be proportional alternately.

Let ``A``, ``B``, ``C``, ``D`` be four proportional magnitudes, so that, as ``A`` is to ``B``, so is ``C`` to ``D``; I say that they will also be so alternately, that is, as ``A`` is to ``C``, so is ``B`` to ``D``.

For of ``A``, ``B`` let equimultiples ``E``, ``F`` be taken, and of ``C``, ``D`` other, chance, equimultiples ``G``, ``H``.

Then, since ``E`` is the same multiple of ``A`` that ``F`` is of ``B``, and parts have the same ratio as the same multiples of them, [:ref:`V.15`] therefore, as ``A`` is to ``B``, so is ``E`` to ``F``.

But as ``A`` is to ``B``, so is ``C`` to ``D``; therefore also, as ``C`` is to ``D``, so is ``E`` to ``F``. [:ref:`V.11`]

Again, since ``G``, ``H`` are equimultiples of ``C``, ``D``, therefore, as ``C`` is to ``D``, so is ``G`` to ``H``. [:ref:`V.15`]

But, as ``C`` is to ``D``, so is ``E`` to ``F``; therefore also, as ``E`` is to ``F``, so is ``G`` to ``H``. [:ref:`V.11`]

But, if four magnitudes be proportional, and the first be greater than the third,


.. container:: center

   the second will also be greater than the fourth;


if equal, equal; and if less, less. [:ref:`V.14`]

Therefore, if ``E`` is in excess of ``G``, ``F`` is also in excess of ``H``, if equal, equal, and if less, less.

Now ``E``, ``F`` are equimultiples of ``A``, ``B``, and ``G``, ``H`` other, chance, equimultiples of ``C``, ``D``;


.. container:: center

   therefore, as ``A`` is to ``C``, so is ``B`` to ``D``. [:ref:`V.def.5`]


Therefore etc. Q. E. D.
Let A, B, C, D be four proportional magnitudes, so that, as A is to B, so is C to D.
In a number of expressions like this it is absolutely necessary, when translating into English, to interpolate words which are not in the Greek. Thus the Greek here is: Ἕστω τέσσαρα μεγέθη ἀνάλογον τὰ Α, Β, Γ, Δ, ὡς τὸ Α πρὸς τὸ Β, οὕτως τὸ Γ πρὸς τὸ Δ, literally Let ``A``, ``B``, ``C``, ``D`` be four proportional magnitudes, as ``A`` to ``B``, so ``C`` to ``D``.
The same remark applies to the corresponding expressions in the next propositions, :ref:`elem.5.17 elem.5.18`, and to other forms of expression in :ref:`elem.5.20 elem.5.21 elem.5.22 elem.5.23` and later propositions: e.g. in :ref:`V.20` we have a phrase meaning literally Let there be magnitudes...which taken two and two are in the same ratio, as ``A`` to ``B``, so ``D`` to ``E``,
etc.: in :ref:`V.21` (magnitudes)...which taken two and two are in the same ratio, and let the proportion of them be perturbed, as ``A`` to ``B``, so ``E`` to ``F``,
etc. In all such cases (where the Greek is so terse as to be almost ungrammatical) I shall insert the words necessary in English, without further remark.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "elem.5.17 elem.5.18" [style="rounded,filled", fillcolor=orange];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/1/", target="_top"];
     "V.16" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/V/16/", target="_top"];
     "V.7" [URL="/elements2/V/7/", target="_top"];
     "V.21" [URL="/elements2/V/21/", target="_top"];
     "elem.5.20 elem.5.21 elem.5.22 elem.5.23" [style="rounded,filled", fillcolor=orange];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.5/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.7/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.4/", target="_top"];
     "V.11" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/11/", target="_top"];
     "V.10" [URL="/elements2/V/10/", target="_top"];
     "V.12" [URL="/elements2/V/12/", target="_top"];
     "V.13" [URL="/elements2/V/13/", target="_top"];
     "V.14" [URL="/elements2/V/14/", target="_top"];
     "V.15" [URL="/elements2/V/15/", target="_top"];
     "V.8" [URL="/elements2/V/8/", target="_top"];
     "V.20" [URL="/elements2/V/20/", target="_top"];
     "V.16" -> "elem.5.17 elem.5.18";
     "V.8" -> "V.1";
     "V.12" -> "V.1";
     "V.10" -> "V.7";
     "V.15" -> "V.7";
     "V.16" -> "V.21";
     "V.16" -> "elem.5.20 elem.5.21 elem.5.22 elem.5.23";
     "V.7" -> "V.def.5";
     "V.12" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.16" -> "V.def.5";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "V.8" -> "V.def.4";
     "V.16" -> "V.11";
     "V.14" -> "V.10";
     "V.20" -> "V.10";
     "V.21" -> "V.10";
     "V.15" -> "V.12";
     "V.14" -> "V.13";
     "V.20" -> "V.13";
     "V.21" -> "V.13";
     "V.16" -> "V.14";
     "V.16" -> "V.15";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "V.21" -> "V.8";
     "V.16" -> "V.20";
   }



Required for
------------

:ref:`V.19`, :ref:`V.23`, :ref:`V.25`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`