:order: 23
:number: 333
:type: prop
:dependencies: VIII.21




.. figure:: VIII.23.graphic.inverted.png

.. _VIII.23:

VIII.23
=======

   If four numbers be in continued proportion, and the first be cube, the fourth will also be cube.

Let A, B, C, D be four numbers in continued proportion, and let A be cube; I say that D is also cube.

For, since between A, D there are two mean proportional numbers B, C, therefore A, D are similar solid numbers. [:ref:`VIII.21`]

But A is cube; therefore D is also cube. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.33" [URL="/heath/VII/33/", target="_top"];
     "VII.12" [URL="/heath/VII/12/", target="_top"];
     "elem.7.5 elem.7.6" [style="rounded,filled", fillcolor=orange];
     "VIII.20" [URL="/heath/VIII/20/", target="_top"];
     "VII.9" [URL="/heath/VII/9/", target="_top"];
     "VIII.2" [URL="/heath/VIII/2/", target="_top"];
     "VII.18" [URL="/heath/VII/18/", target="_top"];
     "VII.16" [URL="/heath/VII/16/", target="_top"];
     "V.7" [URL="/heath/V/7/", target="_top"];
     "VII.26" [URL="/heath/VII/26/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.5/", target="_top"];
     "V.9" [URL="/heath/V/9/", target="_top"];
     "VII.10" [URL="/heath/VII/10/", target="_top"];
     "VIII.3" [URL="/heath/VIII/3/", target="_top"];
     "VII.13" [URL="/heath/VII/13/", target="_top"];
     "VIII.23" [style="rounded,filled", fillcolor=lightblue, URL="/heath/VIII/23/", target="_top"];
     "VII.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.15/", target="_top"];
     "VII.17" [URL="/heath/VII/17/", target="_top"];
     "VII.19" [URL="/heath/VII/19/", target="_top"];
     "VIII.2.p.1" [style="rounded,filled", fillcolor=orange];
     "VII.2" [URL="/heath/VII/2/", target="_top"];
     "VII.def.20" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.20/", target="_top"];
     "VII.2.p.1" [style="rounded,filled", fillcolor=orange];
     "VII.15" [URL="/heath/VII/15/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.4/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.7/", target="_top"];
     "VII.14" [URL="/heath/VII/14/", target="_top"];
     "VIII.21" [URL="/heath/VIII/21/", target="_top"];
     "VII.27" [URL="/heath/VII/27/", target="_top"];
     "VII.21" [URL="/heath/VII/21/", target="_top"];
     "VII.22" [URL="/heath/VII/22/", target="_top"];
     "VII.25" [URL="/heath/VII/25/", target="_top"];
     "VIII.1" [URL="/heath/VIII/1/", target="_top"];
     "VII.1" [URL="/heath/VII/1/", target="_top"];
     "V.8" [URL="/heath/V/8/", target="_top"];
     "VII.23" [URL="/heath/VII/23/", target="_top"];
     "VII.4" [URL="/heath/VII/4/", target="_top"];
     "VII.def.12" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.12/", target="_top"];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/heath/V/1/", target="_top"];
     "VII.3" [URL="/heath/VII/3/", target="_top"];
     "VII.24" [URL="/heath/VII/24/", target="_top"];
     "VII.20" [URL="/heath/VII/20/", target="_top"];
     "VIII.3" -> "VII.33";
     "VIII.20" -> "VII.33";
     "VIII.21" -> "VII.33";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.9" -> "elem.7.5 elem.7.6";
     "VII.10" -> "elem.7.5 elem.7.6";
     "VII.12" -> "elem.7.5 elem.7.6";
     "VIII.21" -> "VIII.20";
     "VII.10" -> "VII.9";
     "VIII.3" -> "VIII.2";
     "VIII.21" -> "VIII.2";
     "VII.19" -> "VII.18";
     "VIII.2" -> "VII.18";
     "VIII.21" -> "VII.18";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.24" -> "VII.16";
     "VII.33" -> "VII.16";
     "VII.19" -> "V.7";
     "VII.27" -> "VII.26";
     "V.7" -> "V.def.5";
     "VII.19" -> "V.9";
     "VII.13" -> "VII.10";
     "VIII.21" -> "VIII.3";
     "VII.14" -> "VII.13";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VIII.20" -> "VII.13";
     "VII.22" -> "VII.def.15";
     "VII.24" -> "VII.def.15";
     "VII.33" -> "VII.def.15";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.22" -> "VII.17";
     "VIII.2" -> "VII.17";
     "VIII.20" -> "VII.17";
     "VII.24" -> "VII.19";
     "VII.33" -> "VII.19";
     "VIII.3" -> "VIII.2.p.1";
     "VII.3" -> "VII.2";
     "VII.4" -> "VII.2";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.33" -> "VII.def.20";
     "VII.3" -> "VII.2.p.1";
     "VII.16" -> "VII.15";
     "V.8" -> "V.def.4";
     "V.8" -> "V.def.7";
     "VIII.1" -> "VII.14";
     "VIII.21" -> "VII.14";
     "VIII.23" -> "VIII.21";
     "VIII.2" -> "VII.27";
     "VIII.3" -> "VII.27";
     "VII.24" -> "VII.21";
     "VII.33" -> "VII.21";
     "VIII.1" -> "VII.21";
     "VIII.21" -> "VII.21";
     "VIII.2" -> "VII.22";
     "VIII.3" -> "VII.22";
     "VII.27" -> "VII.25";
     "VIII.2" -> "VIII.1";
     "VII.2" -> "VII.1";
     "V.9" -> "V.8";
     "VII.24" -> "VII.23";
     "VII.20" -> "VII.4";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.23" -> "VII.def.12";
     "VII.24" -> "VII.def.12";
     "V.8" -> "V.1";
     "VII.33" -> "VII.3";
     "VII.25" -> "VII.24";
     "VII.26" -> "VII.24";
     "VII.21" -> "VII.20";
     "VII.24" -> "VII.20";
     "VIII.1" -> "VII.20";
     "VIII.20" -> "VII.20";
     "VIII.21" -> "VII.20";
   }



Required for
------------

:ref:`IX.10`, :ref:`IX.12`, :ref:`IX.13`, :ref:`IX.3`, :ref:`IX.32`, :ref:`IX.36`, :ref:`IX.4`, :ref:`IX.5`, :ref:`IX.6`, :ref:`IX.8`, :ref:`IX.9`, :ref:`VIII.25`