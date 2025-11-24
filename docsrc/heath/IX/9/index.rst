:order: 9
:number: 346
:type: prop
:dependencies: IX.3, IX.8, VIII.22, VIII.23




.. figure:: IX.9.graphic.inverted.png

.. _IX.9:

IX.9
====

   If as many numbers as we please beginning from an unit be in continued proportion, and the number after the unit be square, all the rest will also be square. And, if the number after the unit be cube, all the rest will also be cube.

Let there be as many numbers as we please, A, B, C, D, E, F, beginning from an unit and in continued proportion, and let A, the number after the unit, be square; I say that all the rest will also be square.

Now it has been proved that B, the third from the unit, is square, as are also all those which leave out one; [:ref:`IX.8`] I say that all the rest are also square.

For, since A, B, C are in continued proportion, and A is square, therefore C is also square. [:ref:`VIII.22`]

Again, since B, C, D are in continued proportion, and B is square, D is also square. [:ref:`VIII.22`]

Similarly we can prove that all the rest are also square.

Next, let A be cube; I say that all the rest are also cube.

Now it has been proved that C, the fourth from the unit, is cube, as also are all those which leave out two; [:ref:`IX.8`] I say that all the rest are also cube.

For, since, as the unit is to A, so is A to B, therefore the unit measures A the same number of times as A measures B.

But the unit measures A according to the units in it; therefore A also measures B according to the units in itself; therefore A by multiplying itself has made B.

And A is cube.

But, if a cube number by multiplying itself make some number, the product is cube. [:ref:`IX.3`]

Therefore B is also cube.

And, since the four numbers A, B, C, D are in continued proportion, and A is cube, D also is cube. [:ref:`VIII.23`]

For the same reason E is also cube, and similarly all the rest are cube. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "VII.1" [URL="/heath/VII/1/", target="_top"];
     "VII.9" [URL="/heath/VII/9/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.5/", target="_top"];
     "VIII.23" [URL="/heath/VIII/23/", target="_top"];
     "VII.17" [URL="/heath/VII/17/", target="_top"];
     "VII.3" [URL="/heath/VII/3/", target="_top"];
     "elem.7.5 elem.7.6" [style="rounded,filled", fillcolor=orange];
     "VIII.21" [URL="/heath/VIII/21/", target="_top"];
     "IX.3" [URL="/heath/IX/3/", target="_top"];
     "V.7" [URL="/heath/V/7/", target="_top"];
     "V.9" [URL="/heath/V/9/", target="_top"];
     "VII.13" [URL="/heath/VII/13/", target="_top"];
     "VII.2" [URL="/heath/VII/2/", target="_top"];
     "VIII.1" [URL="/heath/VIII/1/", target="_top"];
     "IX.9" [style="rounded,filled", fillcolor=lightblue, URL="/heath/IX/9/", target="_top"];
     "VIII.2" [URL="/heath/VIII/2/", target="_top"];
     "VII.12" [URL="/heath/VII/12/", target="_top"];
     "IX.8" [URL="/heath/IX/8/", target="_top"];
     "VII.24" [URL="/heath/VII/24/", target="_top"];
     "VII.def.12" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.12/", target="_top"];
     "V.8" [URL="/heath/V/8/", target="_top"];
     "VII.33" [URL="/heath/VII/33/", target="_top"];
     "VIII.22" [URL="/heath/VIII/22/", target="_top"];
     "elem.7.2.p.1" [style="rounded,filled", fillcolor=orange];
     "VII.10" [URL="/heath/VII/10/", target="_top"];
     "VII.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.15/", target="_top"];
     "VII.18" [URL="/heath/VII/18/", target="_top"];
     "VII.19" [URL="/heath/VII/19/", target="_top"];
     "VII.16" [URL="/heath/VII/16/", target="_top"];
     "VII.26" [URL="/heath/VII/26/", target="_top"];
     "VII.4" [URL="/heath/VII/4/", target="_top"];
     "VII.25" [URL="/heath/VII/25/", target="_top"];
     "VII.21" [URL="/heath/VII/21/", target="_top"];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/heath/V/1/", target="_top"];
     "VII.20" [URL="/heath/VII/20/", target="_top"];
     "VIII.8" [URL="/heath/VIII/8/", target="_top"];
     "VII.14" [URL="/heath/VII/14/", target="_top"];
     "VII.27" [URL="/heath/VII/27/", target="_top"];
     "VIII.3" [URL="/heath/VIII/3/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.4/", target="_top"];
     "VII.22" [URL="/heath/VII/22/", target="_top"];
     "VIII.20" [URL="/heath/VIII/20/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.7/", target="_top"];
     "VII.23" [URL="/heath/VII/23/", target="_top"];
     "VII.15" [URL="/heath/VII/15/", target="_top"];
     "VII.def.20" [style="rounded,filled", fillcolor=orange, URL="/heath/VII/def.20/", target="_top"];
     "elem.8.2.p.1" [style="rounded,filled", fillcolor=orange];
     "VII.2" -> "VII.1";
     "VII.10" -> "VII.9";
     "V.7" -> "V.def.5";
     "IX.3" -> "VIII.23";
     "IX.8" -> "VIII.23";
     "IX.9" -> "VIII.23";
     "VII.18" -> "VII.17";
     "VII.19" -> "VII.17";
     "VII.22" -> "VII.17";
     "VIII.2" -> "VII.17";
     "VIII.20" -> "VII.17";
     "VII.33" -> "VII.3";
     "VII.9" -> "elem.7.5 elem.7.6";
     "VII.10" -> "elem.7.5 elem.7.6";
     "VII.12" -> "elem.7.5 elem.7.6";
     "VIII.23" -> "VIII.21";
     "IX.9" -> "IX.3";
     "VII.19" -> "V.7";
     "VII.19" -> "V.9";
     "VII.14" -> "VII.13";
     "VII.17" -> "VII.13";
     "VII.20" -> "VII.13";
     "VIII.20" -> "VII.13";
     "VII.3" -> "VII.2";
     "VII.4" -> "VII.2";
     "VIII.2" -> "VIII.1";
     "VIII.3" -> "VIII.2";
     "VIII.21" -> "VIII.2";
     "VII.15" -> "VII.12";
     "VII.20" -> "VII.12";
     "IX.9" -> "IX.8";
     "VII.25" -> "VII.24";
     "VII.26" -> "VII.24";
     "VII.1" -> "VII.def.12";
     "VII.21" -> "VII.def.12";
     "VII.23" -> "VII.def.12";
     "VII.24" -> "VII.def.12";
     "V.9" -> "V.8";
     "VIII.3" -> "VII.33";
     "VIII.8" -> "VII.33";
     "VIII.20" -> "VII.33";
     "VIII.21" -> "VII.33";
     "IX.8" -> "VIII.22";
     "IX.9" -> "VIII.22";
     "VII.3" -> "elem.7.2.p.1";
     "VII.13" -> "VII.10";
     "VII.22" -> "VII.def.15";
     "VII.24" -> "VII.def.15";
     "VII.33" -> "VII.def.15";
     "VII.19" -> "VII.18";
     "VIII.2" -> "VII.18";
     "VIII.21" -> "VII.18";
     "VII.24" -> "VII.19";
     "VII.33" -> "VII.19";
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
     "VIII.8" -> "VII.21";
     "VIII.21" -> "VII.21";
     "V.8" -> "V.1";
     "VII.21" -> "VII.20";
     "VII.24" -> "VII.20";
     "VIII.1" -> "VII.20";
     "VIII.8" -> "VII.20";
     "VIII.20" -> "VII.20";
     "VIII.21" -> "VII.20";
     "IX.3" -> "VIII.8";
     "VIII.1" -> "VII.14";
     "VIII.8" -> "VII.14";
     "VIII.21" -> "VII.14";
     "VIII.2" -> "VII.27";
     "VIII.3" -> "VII.27";
     "VIII.8" -> "VIII.3";
     "VIII.21" -> "VIII.3";
     "V.8" -> "V.def.4";
     "VIII.2" -> "VII.22";
     "VIII.3" -> "VII.22";
     "VIII.21" -> "VIII.20";
     "VIII.22" -> "VIII.20";
     "V.8" -> "V.def.7";
     "VII.24" -> "VII.23";
     "VII.16" -> "VII.15";
     "VII.12" -> "VII.def.20";
     "VII.13" -> "VII.def.20";
     "VII.17" -> "VII.def.20";
     "VII.20" -> "VII.def.20";
     "VII.33" -> "VII.def.20";
     "VIII.8" -> "VII.def.20";
     "IX.3" -> "VII.def.20";
     "IX.8" -> "VII.def.20";
     "VIII.3" -> "elem.8.2.p.1";
   }
