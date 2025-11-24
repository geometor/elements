:order: 6
:number: 316
:type: prop
:dependencies: VII.14, VII.33, VII.def.20, VIII.3




.. figure:: VIII.6.graphic.inverted.png

.. _VIII.6:

VIII.6
======

   If there be as many numbers as we please in continued proportion, and the first do not measure the second, neither will any other measure any other.

Let there be as many numbers as we please, A, B, C, D, E, in continued proportion, and let A not measure B; I say that neither will any other measure any other.

Now it is manifest that A, B, C, D, E do not measure one another in order; for A does not even measure B.

I say, then, that neither will any other measure any other.

For, if possible, let A measure C.

And, however many A, B, C are, let as many numbers F, G, H, the least of those which have the same ratio with A, B, C, be taken. [:ref:`VII.33`]

Now, since F, G, H are in the same ratio with A, B, C, and the multitude of the numbers A, B, C is equal to the multitude of the numbers F, G, H, therefore, ex aequali, as A is to C, so is F to H. [:ref:`VII.14`]

And since, as A is to B, so is F to G, while A does not measure B, therefore neither does F measure G; [:ref:`VII.def.20`] therefore F is not an unit, for the unit measures any number.

Now F, H are prime to one another. [:ref:`VIII.3`]

And, as F is to H, so is A to C; therefore neither does A measure C.

Similarly we can prove that neither will any other measure any other. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.1" [URL="/heath/VII/1/", target="_top"];
     "VII.9" [URL="/heath/VII/9/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.5/", target="_top"];
     "VII.17" [URL="/heath/VII/17/", target="_top"];
     "VII.3" [URL="/heath/VII/3/", target="_top"];
     "elem.7.5 elem.7.6" [style="rounded,filled", fillcolor=orange];
     "V.7" [URL="/heath/V/7/", target="_top"];
     "V.9" [URL="/heath/V/9/", target="_top"];
     "VII.13" [URL="/heath/VII/13/", target="_top"];
     "VII.2" [URL="/heath/VII/2/", target="_top"];
     "VIII.1" [URL="/heath/VIII/1/", target="_top"];
     "VIII.2" [URL="/heath/VIII/2/", target="_top"];
     "VII.12" [URL="/heath/VII/12/", target="_top"];
     "VII.24" [URL="/heath/VII/24/", target="_top"];
     "VIII.6" [style="rounded,filled", fillcolor=lightblue, URL="/heath/VIII/6/", target="_top"];
     "VII.def.12" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.12/", target="_top"];
     "V.8" [URL="/heath/V/8/", target="_top"];
     "VII.33" [URL="/heath/VII/33/", target="_top"];
     "elem.7.2.p.1" [style="rounded,filled", fillcolor=orange];
     "VII.10" [URL="/heath/VII/10/", target="_top"];
     "VII.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.15/", target="_top"];
     "VII.19" [URL="/heath/VII/19/", target="_top"];
     "VII.18" [URL="/heath/VII/18/", target="_top"];
     "VII.16" [URL="/heath/VII/16/", target="_top"];
     "VII.26" [URL="/heath/VII/26/", target="_top"];
     "VII.4" [URL="/heath/VII/4/", target="_top"];
     "VII.25" [URL="/heath/VII/25/", target="_top"];
     "VII.21" [URL="/heath/VII/21/", target="_top"];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/heath/V/1/", target="_top"];
     "VII.20" [URL="/heath/VII/20/", target="_top"];
     "VII.14" [URL="/heath/VII/14/", target="_top"];
     "VII.27" [URL="/heath/VII/27/", target="_top"];
     "VIII.3" [URL="/heath/VIII/3/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.4/", target="_top"];
     "VII.22" [URL="/heath/VII/22/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.7/", target="_top"];
     "VII.23" [URL="/heath/VII/23/", target="_top"];
     "VII.15" [URL="/heath/VII/15/", target="_top"];
     "VII.def.20" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.20/", target="_top"];
     "elem.8.2.p.1" [style="rounded,filled", fillcolor=orange];
     "VII.2" -> "VII.1";
     "VII.10" -> "VII.9";
     "V.7" -> "V.def.5";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.22" -> "VII.17";
     "VIII.2" -> "VII.17";
     "VII.33" -> "VII.3";
     "VII.9" -> "elem.7.5 elem.7.6";
     "VII.10" -> "elem.7.5 elem.7.6";
     "VII.12" -> "elem.7.5 elem.7.6";
     "VII.19" -> "V.7";
     "VII.19" -> "V.9";
     "VII.14" -> "VII.13";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VII.3" -> "VII.2";
     "VII.4" -> "VII.2";
     "VIII.2" -> "VIII.1";
     "VIII.3" -> "VIII.2";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "VII.25" -> "VII.24";
     "VII.26" -> "VII.24";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.23" -> "VII.def.12";
     "VII.24" -> "VII.def.12";
     "V.9" -> "V.8";
     "VIII.3" -> "VII.33";
     "VIII.6" -> "VII.33";
     "VII.3" -> "elem.7.2.p.1";
     "VII.13" -> "VII.10";
     "VII.22" -> "VII.def.15";
     "VII.24" -> "VII.def.15";
     "VII.33" -> "VII.def.15";
     "VII.24" -> "VII.19";
     "VII.33" -> "VII.19";
     "VII.19" -> "VII.18";
     "VIII.2" -> "VII.18";
     "VII.18" -> "VII.16";
     "VII.21" -> "VII.16";
     "VII.24" -> "VII.16";
     "VII.33" -> "VII.16";
     "VII.27" -> "VII.26";
     "VII.20" -> "VII.4";
     "VII.27" -> "VII.25";
     "VII.24" -> "VII.21";
     "VII.33" -> "VII.21";
     "VIII.1" -> "VII.21";
     "V.8" -> "V.1";
     "VII.21" -> "VII.20";
     "VII.24" -> "VII.20";
     "VIII.1" -> "VII.20";
     "VIII.1" -> "VII.14";
     "VIII.6" -> "VII.14";
     "VIII.2" -> "VII.27";
     "VIII.3" -> "VII.27";
     "VIII.6" -> "VIII.3";
     "V.8" -> "V.def.4";
     "VIII.2" -> "VII.22";
     "VIII.3" -> "VII.22";
     "V.8" -> "V.def.7";
     "VII.24" -> "VII.23";
     "VII.16" -> "VII.15";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.33" -> "VII.def.20";
     "VIII.6" -> "VII.def.20";
     "VIII.3" -> "elem.8.2.p.1";
   }



Required for
------------

:ref:`VIII.14`, :ref:`VIII.15`, :ref:`VIII.16`, :ref:`VIII.17`, :ref:`VIII.7`