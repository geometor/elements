:order: 39
:number: 72
:type: prop
:tags: triangle
:dependencies: I.31, I.37, I.cn.1




.. figure:: I.39.jpg
   :width: 50%

.. _I.39:

I.39
====

   Equal triangles which are on the same base and on the same side are also in the same parallels.

Let ``ABC``, ``DBC`` be equal triangles which are on the same base ``BC`` and on the same side of it; [I say that they are also in the same parallels.]

And [For] let ``AD`` be joined; I say that ``AD`` is parallel to ``BC``.

For, if not, let ``AE`` be drawn through the point ``A`` parallel to the straight line ``BC``, [:ref:`I.31`] and let ``EC`` be joined. 

Therefore the triangle ``ABC`` is equal to the triangle ``EBC``; for it is on the same base ``BC`` with it and in the same parallels. [:ref:`I.37`]

But ``ABC`` is equal to ``DBC``; therefore ``DBC`` is also equal to ``EBC``, [:ref:`I.cn.1`] the greater to the less: which is impossible.

Therefore ``AE`` is not parallel to ``BC``. 

Similarly we can prove that neither is any other straight line except ``AD``; therefore ``AD`` is parallel to ``BC``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **5**

   

   [I say that they are also in the same parallels.] Heiberg has proved (Hermes, XXXVIII., 1903, p. 50) from a recently discovered papyrus-fragment (Fayūm towns and their papyri, p. 96, No. IX.) that these words are an interpolation by some one who did not observe that the words And let ``AD`` be joined

    are part of the ``setting-out`` (ἔκθεσις), but took them as belonging to the ``construction`` (κατασκευή) and consequently thought that a διορισμός or definition

    (of the thing to be proved) should precede. The interpolator then altered And

    into For

    in the next sentence.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.37" [URL="/elements2/I/37/", target="_top"];
     "I.31" [URL="/elements2/I/31/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.26" [URL="/elements2/I/26/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.23" [URL="/elements2/I/23/", target="_top"];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.35" [URL="/elements2/I/35/", target="_top"];
     "I.34" [URL="/elements2/I/34/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.23/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.39" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/39/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.27" [URL="/elements2/I/27/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.39" -> "I.37";
     "I.37" -> "I.31";
     "I.39" -> "I.31";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.23" -> "I.8";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.7" -> "I.5";
     "I.34" -> "I.26";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.35" -> "I.cn.1";
     "I.39" -> "I.cn.1";
     "I.8" -> "I.7";
     "I.31" -> "I.23";
     "I.26" -> "I.16";
     "I.27" -> "I.16";
     "I.37" -> "I.35";
     "I.35" -> "I.34";
     "I.37" -> "I.34";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.15" -> "I.post.4";
     "I.27" -> "I.def.23";
     "I.13" -> "I.11";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.29" -> "I.post.5";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.16" -> "I.10";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.35" -> "I.cn.3";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.34" -> "I.4";
     "I.35" -> "I.4";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.10" -> "I.9";
     "I.34" -> "I.29";
     "I.35" -> "I.29";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.3" -> "I.2";
     "I.31" -> "I.27";
     "I.4" -> "I.cn.4";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.35" -> "I.cn.2";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
   }



Required for
------------

:ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`