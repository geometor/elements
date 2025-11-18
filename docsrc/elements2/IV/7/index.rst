:order: 7
:number: 159
:type: prop
:tags: circle
:dependencies: I.28, I.30, I.34, III.18, elem.3.16.p.1




.. figure:: IV.7.jpg
   :width: 50%

.. _IV.7:

IV.7
====

   About a given circle to circumscribe a square.

Let ``ABCD`` be the given circle; thus it is required to circumscribe a square about the circle ``ABCD``.

Let two diameters ``AC``, ``BD`` of the circle ``ABCD`` be drawn at right angles to one another, and through the points ``A``, ``B``, ``C``, ``D`` let ``FG``, ``GH``, ``HK``, ``KF`` be drawn touching the circle ``ABCD``. [:ref:`elem.3.16.p.1`]

Then, since ``FG`` touches the circle ``ABCD``, and ``EA`` has been joined from the centre ``E`` to the point of contact at ``A``,


.. container:: center

   therefore the angles at ``A`` are right. [:ref:`III.18`]


For the same reason


.. container:: center

   the angles at the points ``B``, ``C``, ``D`` are also right.


Now, since the angle ``AEB`` is right, and the angle ``EBG`` is also right,


.. container:: center

   therefore ``GH`` is parailel to ``AC``. [:ref:`I.28`]


For the same reason


.. container:: center

   ``AC`` is also parallel to ``FK``, so that ``GH`` is also parallel to ``FK``. [:ref:`I.30`]


Similarly we can prove that


.. container:: center

   each of the straight lines ``GF``, ``HK`` is parallel to ``BED``.


Therefore ``GK``, ``GC``, ``AK``, ``FB``, ``BK`` are parallelograms; therefore ``GF`` is equal to ``HK``, and ``GH`` to ``FK``. [:ref:`I.34`]

And, since ``AC`` is equal to ``BD``, and ``AC`` is also equal to each of the straight lines ``GH``, ``FK``,


.. container:: center

   while ``BD`` is equal to each of the straight lines ``GF``, ``HK``, [:ref:`I.34`] therefore the quadrilateral ``FGHK`` is equilateral.


I say next that it is also right-angled.

For, since ``GBEA`` is a parallelogram, and the angle ``AEB`` is right, therefore the angle ``AGB`` is also right. [:ref:`I.34`]

Similarly we can prove that


.. container:: center

   the angles at ``H``, ``K``, ``F`` are also right.


Therefore ``FGHK`` is right-angled.

But it was also proved equilateral;


.. container:: center

   therefore it is a square;


and it has been circumscribed about the circle ``ABCD``.

Therefore about the given circle a square has been circumscribed. Q. E. F.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "III.18" [URL="/elements2/III/18/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.17" [URL="/elements2/I/17/", target="_top"];
     "I.26" [URL="/elements2/I/26/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "elem.3.16.p.1" [style="rounded,filled", fillcolor=orange];
     "I.28" [URL="/elements2/I/28/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.34" [URL="/elements2/I/34/", target="_top"];
     "I.30" [URL="/elements2/I/30/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.19" [URL="/elements2/I/19/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.23/", target="_top"];
     "I.18" [URL="/elements2/I/18/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "IV.7" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/IV/7/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.27" [URL="/elements2/I/27/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "IV.7" -> "III.18";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.16" -> "I.15";
     "I.28" -> "I.15";
     "I.29" -> "I.15";
     "I.7" -> "I.5";
     "I.19" -> "I.5";
     "III.18" -> "I.17";
     "I.34" -> "I.26";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.30" -> "I.cn.1";
     "IV.7" -> "elem.3.16.p.1";
     "IV.7" -> "I.28";
     "I.8" -> "I.7";
     "I.17" -> "I.16";
     "I.18" -> "I.16";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "IV.7" -> "I.34";
     "IV.7" -> "I.30";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "III.18" -> "I.19";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.13" -> "I.11";
     "I.15" -> "I.post.4";
     "I.27" -> "I.def.23";
     "I.19" -> "I.18";
     "I.29" -> "I.post.5";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.18" -> "I.3";
     "I.16" -> "I.10";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.17" -> "I.13";
     "I.28" -> "I.13";
     "I.29" -> "I.13";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.34" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.10" -> "I.9";
     "I.30" -> "I.29";
     "I.34" -> "I.29";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.3" -> "I.2";
     "I.28" -> "I.27";
     "I.4" -> "I.cn.4";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.17" -> "I.post.2";
   }
