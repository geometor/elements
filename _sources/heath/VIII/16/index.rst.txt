:order: 16
:number: 326
:type: prop
:dependencies: VIII.14




.. figure:: VIII.16.graphic.inverted.png

.. _VIII.16:

VIII.16
=======

   If a square number do not measure a square number, neither will the side measure the side; and, if the side do not measure the side, neither will the square measure the square.

Let A, B be square numbers, and let C, D be their sides; and let A not measure B; I say that neither does C measure D.

For, if C measures D, A will also measure B. [:ref:`VIII.14`]

But A does not measure B; therefore neither will C measure D.

Again, let C not measure D; I say that neither will A measure B.

For, if A measures B, C will also measure D. [:ref:`VIII.14`]

But C does not measure D; therefore neither will A measure B. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.33" [URL="/heath/VII/33/", target="_top"];
     "VII.12" [URL="/heath/VII/12/", target="_top"];
     "VIII.6" [URL="/heath/VIII/6/", target="_top"];
     "elem.7.5 elem.7.6" [style="rounded,filled", fillcolor=orange];
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
     "VII.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.15/", target="_top"];
     "VIII.14" [URL="/heath/VIII/14/", target="_top"];
     "VII.17" [URL="/heath/VII/17/", target="_top"];
     "VII.19" [URL="/heath/VII/19/", target="_top"];
     "VIII.11" [URL="/heath/VIII/11/", target="_top"];
     "VIII.2.p.1" [style="rounded,filled", fillcolor=orange];
     "VII.def.20" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.20/", target="_top"];
     "VII.2" [URL="/heath/VII/2/", target="_top"];
     "VII.15" [URL="/heath/VII/15/", target="_top"];
     "VII.2.p.1" [style="rounded,filled", fillcolor=orange];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.4/", target="_top"];
     "VIII.7" [URL="/heath/VIII/7/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.7/", target="_top"];
     "VIII.16" [style="rounded,filled", fillcolor=lightblue, URL="/heath/VIII/16/", target="_top"];
     "VII.14" [URL="/heath/VII/14/", target="_top"];
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
     "V.def.9" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.9/", target="_top"];
     "VII.3" [URL="/heath/VII/3/", target="_top"];
     "VII.24" [URL="/heath/VII/24/", target="_top"];
     "VII.20" [URL="/heath/VII/20/", target="_top"];
     "VIII.3" -> "VII.33";
     "VIII.6" -> "VII.33";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VIII.7" -> "VIII.6";
     "VII.9" -> "elem.7.5 elem.7.6";
     "VII.10" -> "elem.7.5 elem.7.6";
     "VII.12" -> "elem.7.5 elem.7.6";
     "VII.10" -> "VII.9";
     "VIII.3" -> "VIII.2";
     "VII.19" -> "VII.18";
     "VIII.2" -> "VII.18";
     "VIII.11" -> "VII.18";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.24" -> "VII.16";
     "VII.33" -> "VII.16";
     "VII.19" -> "V.7";
     "VII.27" -> "VII.26";
     "V.7" -> "V.def.5";
     "VII.19" -> "V.9";
     "VII.13" -> "VII.10";
     "VIII.6" -> "VIII.3";
     "VII.14" -> "VII.13";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VII.22" -> "VII.def.15";
     "VII.24" -> "VII.def.15";
     "VII.33" -> "VII.def.15";
     "VIII.16" -> "VIII.14";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.22" -> "VII.17";
     "VIII.2" -> "VII.17";
     "VIII.11" -> "VII.17";
     "VII.24" -> "VII.19";
     "VII.33" -> "VII.19";
     "VIII.14" -> "VIII.11";
     "VIII.3" -> "VIII.2.p.1";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.33" -> "VII.def.20";
     "VIII.6" -> "VII.def.20";
     "VIII.14" -> "VII.def.20";
     "VII.3" -> "VII.2";
     "VII.4" -> "VII.2";
     "VII.16" -> "VII.15";
     "VII.3" -> "VII.2.p.1";
     "V.8" -> "V.def.4";
     "VIII.14" -> "VIII.7";
     "V.8" -> "V.def.7";
     "VIII.1" -> "VII.14";
     "VIII.6" -> "VII.14";
     "VIII.2" -> "VII.27";
     "VIII.3" -> "VII.27";
     "VII.24" -> "VII.21";
     "VII.33" -> "VII.21";
     "VIII.1" -> "VII.21";
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
     "VIII.11" -> "V.def.9";
     "VII.33" -> "VII.3";
     "VII.25" -> "VII.24";
     "VII.26" -> "VII.24";
     "VII.21" -> "VII.20";
     "VII.24" -> "VII.20";
     "VIII.1" -> "VII.20";
   }
