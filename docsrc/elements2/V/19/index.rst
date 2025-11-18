:order: 19
:number: 205
:type: prop
:dependencies: V.11, V.16, V.17


.. _V.19:

V.19
====

   If, as a whole is to a whole, so is a part subtracted to a part subtracted, the remainder will also be to the remainder as whole to whole.

For, as the whole ``AB`` is to the whole ``CD``, so let the part ``AE`` subtracted be to the part ``CF`` subtracted; I say that the remainder ``EB`` will also be to the remainder ``FD`` as the whole ``AB`` to the whole ``CD``.

For since, as ``AB`` is to ``CD``, so is ``AE`` to ``CF``, alternately also, as ``BA`` is to ``AE``, so is ``DC`` to ``CF``. [:ref:`V.16`]

And, since the magnitudes are proportional ``componendo``, they will also be proportional ``separando``, [:ref:`V.17`] that is, as ``BE`` is to ``EA``, so is ``DF`` to ``CF``, and, alternately,


.. container:: center

   as ``BE`` is to ``DF``, so is ``EA`` to ``FC``. [:ref:`V.16`]


But, as ``AE`` is to ``CF``, so by hypothesis is the whole ``AB`` to the whole ``CD``.

Therefore also the remainder ``EB`` will be to the remainder ``FD`` as the whole ``AB`` is to the whole ``CD``. [:ref:`V.11`]

Therefore etc.
[


.. _elem.5.19.p.1:


**V.19.p.1**


From this it is manifest that, if magnitudes be proportional componendo, they will also be proportional convertendo.

] Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "V.20" [URL="/elements2/V/20/", target="_top"];
     "V.14" [URL="/elements2/V/14/", target="_top"];
     "V.10" [URL="/elements2/V/10/", target="_top"];
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
     "V.19" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/V/19/", target="_top"];
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
     "V.16" -> "V.15";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "V.21" -> "V.8";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "V.19" -> "V.17";
   }



Required for
------------

:ref:`V.25`