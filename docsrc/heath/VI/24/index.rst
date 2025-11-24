:order: 24
:number: 240
:type: prop
:dependencies: V.16, V.18, V.22, VI.2, VI.21, VI.def.1




.. figure:: VI.24.graphic.inverted.png

.. _VI.24:

VI.24
=====

   In any parallelogram the parallelograms about the diameter are similar both to the whole and to one another.

Let ``ABCD`` be a parallelogram, and ``AC`` its diameter, and let ``EG``, ``HK`` be parallelograms about ``AC``; I say that each of the parallelograms ``EG``, ``HK`` is similar both to the whole ``ABCD`` and to the other.

For, since ``EF`` has been drawn parallel to ``BC``, one of the sides of the triangle ``ABC``,


.. container:: center

   proportionally, as ``BE`` is to ``EA``, so is ``CF`` to ``FA``. [:ref:`VI.2`]


Again, since ``FG`` has been drawn parallel to ``CD``, one of the sides of the triangle ``ACD``,


.. container:: center

   proportionally, as ``CF`` is to ``FA``, so is ``DG`` to ``GA``. [:ref:`VI.2`]


But it was proved that,


.. container:: center

   as ``CF`` is to ``FA``, so also is ``BE`` to ``EA``; therefore also, as ``BE`` is to ``EA``, so is ``DG`` to ``GA``,


and therefore, ``componendo``,


.. container:: center

   as ``BA`` is to ``AE``, so is ``DA`` to ``AG``, [:ref:`V.18`]


and, alternately,


.. container:: center

   as ``BA`` is to ``AD``, so is ``EA`` to ``AG``. [:ref:`V.16`]


Therefore in the parallelograms ``ABCD``, ``EG``, the sides about the common angle ``BAD`` are proportional.

And, since ``GF`` is parallel to ``DC``,


.. container:: center

   the angle ``AFG`` is equal to the angle ``DCA``;


and the angle ``DAC`` is common to the two triangles ``ADC``, ``AGF``;


.. container:: center

   therefore the triangle ``ADC`` is equiangular with the triangle ``AGF``.


For the same reason


.. container:: center

   the triangle ``ACB`` is also equiangular with the triangle ``AFE``,


and the whole parallelogram ``ABCD`` is equiangular with the parallelogram ``EG``.

Therefore, proportionally,


.. container:: center

   as ``AD`` is to ``DC``, so is ``AG`` to ``GF``, as ``DC`` is to ``CA``, so is ``GF`` to ``FA``, as ``AC`` is to ``CB``, so is ``AF`` to ``FE``,


and further, as ``CB`` is to ``BA``, so is ``FE`` to ``EA``.

And, since it was proved that,


.. container:: center

   as ``DC`` is to ``CA``, so is ``GF`` to ``FA``,


and, as ``AC`` is to ``CB``, so is ``AF`` to ``FE``, therefore, ex aequali, as ``DC`` is to ``CB``, so is ``GF`` to ``FE``. [:ref:`V.22`]

Therefore in the parallelograms ``ABCD``, ``EG`` the sides about the equal angles are proportional; therefore the parallelogram ``ABCD`` is similar to the parallelogram ``EG``. [:ref:`VI.def.1`]

For the same reason the parallelogram ``ABCD`` is also similar to the parallelogram ``KH``; therefore each of the parallelograms ``EG``, ``HK`` is similar to ``ABCD``.

But figures similar to the same rectilineal figure are also similar to one another; [:ref:`VI.21`] therefore the parallelogram ``EG`` is also similar to the parallelogram ``HK``.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.10/", target="_top"];
     "I.11" [URL="/heath/I/11/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.4/", target="_top"];
     "I.1" [URL="/heath/I/1/", target="_top"];
     "VI.21" [URL="/heath/VI/21/", target="_top"];
     "V.def.5" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.5/", target="_top"];
     "V.13" [URL="/heath/V/13/", target="_top"];
     "V.11" [style="rounded,filled", fillcolor=orange, URL="/heath/V/11/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.3/", target="_top"];
     "VI.1" [URL="/heath/VI/1/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.3/", target="_top"];
     "V.16" [URL="/heath/V/16/", target="_top"];
     "V.3" [URL="/heath/V/3/", target="_top"];
     "V.8" [URL="/heath/V/8/", target="_top"];
     "I.36" [URL="/heath/I/36/", target="_top"];
     "I.41" [URL="/heath/I/41/", target="_top"];
     "I.27" [URL="/heath/I/27/", target="_top"];
     "I.37" [URL="/heath/I/37/", target="_top"];
     "I.34" [URL="/heath/I/34/", target="_top"];
     "I.2" [URL="/heath/I/2/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.23/", target="_top"];
     "I.33" [URL="/heath/I/33/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.2/", target="_top"];
     "VI.def.1" [style="rounded,filled", fillcolor=orange, URL="/heath/VI/def.1/", target="_top"];
     "elem.5.20 elem.5.21 elem.5.22 elem.5.23" [style="rounded,filled", fillcolor=orange];
     "I.9" [URL="/heath/I/9/", target="_top"];
     "V.def.4" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.4/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.4/", target="_top"];
     "I.15" [URL="/heath/I/15/", target="_top"];
     "I.38" [URL="/heath/I/38/", target="_top"];
     "V.def.7" [style="rounded,filled", fillcolor=orange, URL="/heath/V/def.7/", target="_top"];
     "I.5" [URL="/heath/I/5/", target="_top"];
     "V.21" [URL="/heath/V/21/", target="_top"];
     "I.39" [URL="/heath/I/39/", target="_top"];
     "I.26" [URL="/heath/I/26/", target="_top"];
     "V.14" [URL="/heath/V/14/", target="_top"];
     "I.29" [URL="/heath/I/29/", target="_top"];
     "V.22" [URL="/heath/V/22/", target="_top"];
     "V.12" [URL="/heath/V/12/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.2/", target="_top"];
     "V.20" [URL="/heath/V/20/", target="_top"];
     "V.10" [URL="/heath/V/10/", target="_top"];
     "VI.2" [URL="/heath/VI/2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/heath/I/def.15/", target="_top"];
     "V.15" [URL="/heath/V/15/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/cn.1/", target="_top"];
     "V.7" [URL="/heath/V/7/", target="_top"];
     "V.18" [URL="/heath/V/18/", target="_top"];
     "V.9" [URL="/heath/V/9/", target="_top"];
     "I.23" [URL="/heath/I/23/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.1/", target="_top"];
     "I.35" [URL="/heath/I/35/", target="_top"];
     "I.7" [URL="/heath/I/7/", target="_top"];
     "I.3" [URL="/heath/I/3/", target="_top"];
     "I.4" [URL="/heath/I/4/", target="_top"];
     "V.17" [URL="/heath/V/17/", target="_top"];
     "I.13" [URL="/heath/I/13/", target="_top"];
     "V.4" [URL="/heath/V/4/", target="_top"];
     "I.31" [URL="/heath/I/31/", target="_top"];
     "V.1" [style="rounded,filled", fillcolor=orange, URL="/heath/V/1/", target="_top"];
     "I.16" [URL="/heath/I/16/", target="_top"];
     "VI.24" [style="rounded,filled", fillcolor=lightblue, URL="/heath/VI/24/", target="_top"];
     "elem.5.17 elem.5.18" [style="rounded,filled", fillcolor=orange];
     "I.8" [URL="/heath/I/8/", target="_top"];
     "V.2" [style="rounded,filled", fillcolor=orange, URL="/heath/V/2/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/heath/I/post.5/", target="_top"];
     "I.10" [URL="/heath/I/10/", target="_top"];
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.13" -> "I.11";
     "I.15" -> "I.post.4";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "VI.24" -> "VI.21";
     "V.4" -> "V.def.5";
     "V.7" -> "V.def.5";
     "V.12" -> "V.def.5";
     "V.13" -> "V.def.5";
     "V.16" -> "V.def.5";
     "V.22" -> "V.def.5";
     "VI.1" -> "V.def.5";
     "V.14" -> "V.13";
     "V.20" -> "V.13";
     "V.21" -> "V.13";
     "V.16" -> "V.11";
     "V.18" -> "V.11";
     "VI.1" -> "V.11";
     "VI.2" -> "V.11";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "VI.2" -> "VI.1";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "VI.1" -> "V.16";
     "VI.24" -> "V.16";
     "V.4" -> "V.3";
     "V.9" -> "V.8";
     "V.10" -> "V.8";
     "V.14" -> "V.8";
     "V.20" -> "V.8";
     "V.21" -> "V.8";
     "I.38" -> "I.36";
     "VI.1" -> "I.41";
     "I.31" -> "I.27";
     "I.33" -> "I.27";
     "I.39" -> "I.37";
     "I.41" -> "I.37";
     "I.35" -> "I.34";
     "I.36" -> "I.34";
     "I.37" -> "I.34";
     "I.38" -> "I.34";
     "I.41" -> "I.34";
     "I.3" -> "I.2";
     "I.27" -> "I.def.23";
     "I.36" -> "I.33";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "VI.21" -> "VI.def.1";
     "VI.24" -> "VI.def.1";
     "V.16" -> "elem.5.20 elem.5.21 elem.5.22 elem.5.23";
     "I.10" -> "I.9";
     "V.8" -> "V.def.4";
     "I.4" -> "I.cn.4";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "VI.1" -> "I.38";
     "VI.2" -> "I.38";
     "V.8" -> "V.def.7";
     "V.13" -> "V.def.7";
     "I.7" -> "I.5";
     "V.16" -> "V.21";
     "VI.2" -> "I.39";
     "I.34" -> "I.26";
     "V.16" -> "V.14";
     "V.18" -> "V.14";
     "I.33" -> "I.29";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "VI.24" -> "V.22";
     "V.15" -> "V.12";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "V.16" -> "V.20";
     "V.22" -> "V.20";
     "V.14" -> "V.10";
     "V.20" -> "V.10";
     "V.21" -> "V.10";
     "VI.24" -> "VI.2";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "V.16" -> "V.15";
     "VI.1" -> "V.15";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.36" -> "I.cn.1";
     "I.39" -> "I.cn.1";
     "V.10" -> "V.7";
     "V.15" -> "V.7";
     "VI.2" -> "V.7";
     "VI.24" -> "V.18";
     "VI.2" -> "V.9";
     "I.31" -> "I.23";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.36" -> "I.35";
     "I.37" -> "I.35";
     "I.8" -> "I.7";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.33" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "V.18" -> "V.17";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "V.22" -> "V.4";
     "I.37" -> "I.31";
     "I.38" -> "I.31";
     "I.39" -> "I.31";
     "V.8" -> "V.1";
     "V.12" -> "V.1";
     "V.17" -> "V.1";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "V.16" -> "elem.5.17 elem.5.18";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "V.3" -> "V.2";
     "V.17" -> "V.2";
     "I.29" -> "I.post.5";
     "I.16" -> "I.10";
   }



Required for
------------

:ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`, :ref:`X.100`, :ref:`X.101`, :ref:`X.105`, :ref:`X.106`, :ref:`X.108`, :ref:`X.109`, :ref:`X.110`, :ref:`X.33`, :ref:`X.34`, :ref:`X.39`, :ref:`X.40`, :ref:`X.45`, :ref:`X.46`, :ref:`X.57`, :ref:`X.58`, :ref:`X.63`, :ref:`X.64`, :ref:`X.68`, :ref:`X.69`, :ref:`X.71`, :ref:`X.76`, :ref:`X.77`, :ref:`X.82`, :ref:`X.83`, :ref:`X.91`, :ref:`X.92`, :ref:`X.93`, :ref:`X.94`, :ref:`X.95`, :ref:`X.96`, :ref:`XIII.11`, :ref:`XIII.16`, :ref:`XIII.18`