:order: 21
:number: 207
:type: prop
:dependencies: V.10, V.13, V.8


.. _V.21:

V.21
====

   If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then, if ex aequali
          the first magnitude is greater than the third, the fourth will also be greater than the sixth; if equal, equal; and if less, less.

Let there be three magnitudes ``A``, ``B``, ``C``, and others ``D``, ``E``, ``F`` equal to them in multitude, which taken two and two are in the same ratio, and let the proportion of them be perturbed, so that,


.. container:: center

   as ``A`` is to ``B``, so is ``E`` to ``F``,


and, as ``B`` is to ``C``, so is ``D`` to ``E``, and let ``A`` be greater than ``C``
ex aequali; I say that ``D`` will also be greater than ``F``; if ``A`` is equal to ``C``, equal; and if less, less.

For, since ``A`` is greater than ``C``, and ``B`` is some other magnitude, therefore ``A`` has to ``B`` a greater ratio than ``C`` has to ``B``. [:ref:`V.8`]

But, as ``A`` is to ``B``, so is ``E`` to ``F``, and, as ``C`` is to ``B``, inversely, so is ``E`` to ``D``. Therefore also ``E`` has to ``F`` a greater ratio than ``E`` has to ``D``. [:ref:`V.13`]

But that to which the same has a greater ratio is less; [:ref:`V.10`]


.. container:: center

   therefore ``F`` is less than ``D``; therefore ``D`` is greater than ``F``.


Similarly we can prove that,


.. container:: center

   if ``A`` be equal to ``C``, ``D`` will also be equal to ``F``;


and if less, less.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/1/", target="_top"];
     "V.10" [URL="/elements2/V/10/", target="_top"];
     "V.7" [URL="/elements2/V/7/", target="_top"];
     "V.21" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/V/21/", target="_top"];
     "V.13" [URL="/elements2/V/13/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.5/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.7/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.4/", target="_top"];
     "V.8" [URL="/elements2/V/8/", target="_top"];
     "V.8" -> "V.1";
     "V.21" -> "V.10";
     "V.10" -> "V.7";
     "V.21" -> "V.13";
     "V.7" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "V.8" -> "V.def.4";
     "V.10" -> "V.8";
     "V.21" -> "V.8";
   }



Required for
------------

:ref:`V.16`, :ref:`V.19`, :ref:`V.23`, :ref:`V.25`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`