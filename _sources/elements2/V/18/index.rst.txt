:order: 18
:number: 204
:type: prop
:dependencies: V.11, V.14, V.17


.. _V.18:

V.18
====

   If magnitudes be proportional
          separando, they will also be proportional
          componendo.

Let ``AE``, ``EB``, ``CF``, ``FD`` be magnitudes proportional separando, so that, as ``AE`` is to ``EB``, so is ``CF`` to ``FD``;

I say that they will also be proportional componendo, that is, as ``AB`` is to ``BE``, so is ``CD`` to ``FD``.

For, if ``CD`` be not to ``DF`` as ``AB`` to ``BE``, then, as ``AB`` is to ``BE``, so will ``CD`` be either to some magnitude less than ``DF`` or to a greater.

First, let it be in that ratio to a less magnitude ``DG``.

Then, since, as ``AB`` is to ``BE``, so is ``CD`` to ``DG``, they are magnitudes proportional componendo;


.. container:: center

   so that they will also be proportional separando. [:ref:`V.17`]


Therefore, as ``AE`` is to ``EB``, so is ``CG`` to ``GD``.

But also, by hypothesis,


.. container:: center

   as ``AE`` is to ``EB``, so is ``CF`` to ``FD``.


Therefore also, as ``CG`` is to ``GD``, so is ``CF`` to ``FD``. [:ref:`V.11`]

But the first ``CG`` is greater than the third ``CF``;


.. container:: center

   therefore the second ``GD`` is also greater than the fourth ``FD``. [:ref:`V.14`]


But it is also less: which is impossible.

Therefore, as ``AB`` is to ``BE``, so is not ``CD`` to a less magnitude than ``FD``.

Similarly we can prove that neither is it in that ratio to a greater;


.. container:: center

   it is therefore in that ratio to ``FD`` itself.


Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.5/", target="_top"];
     "V.14" [URL="/elements2/V/14/", target="_top"];
     "V.17" [URL="/elements2/V/17/", target="_top"];
     "V.18" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/V/18/", target="_top"];
     "V.13" [URL="/elements2/V/13/", target="_top"];
     "V.10" [URL="/elements2/V/10/", target="_top"];
     "V.8" [URL="/elements2/V/8/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.4/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/def.7/", target="_top"];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/1/", target="_top"];
     "V.11" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/11/", target="_top"];
     "V.7" [URL="/elements2/V/7/", target="_top"];
     "V.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/V/2/", target="_top"];
     "V.7" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.18" -> "V.14";
     "V.18" -> "V.17";
     "V.14" -> "V.13";
     "V.14" -> "V.10";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.8" -> "V.def.4";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "V.8" -> "V.1";
     "V.17" -> "V.1";
     "V.18" -> "V.11";
     "V.10" -> "V.7";
     "V.17" -> "V.2";
   }



Required for
------------

:ref:`V.24`, :ref:`VI.24`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`