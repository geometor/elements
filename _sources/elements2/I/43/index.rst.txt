:order: 43
:number: 76
:type: prop
:dependencies: I.34, I.cn.2, I.cn.3




.. figure:: I.43.jpg
   :width: 50%

.. _I.43:

I.43
====

   In any parallelogram the complements of the parallelograms about the diameter are equal to one another.

Let ``ABCD`` be a parallelogram, and ``AC`` its diameter; and about ``AC`` let ``EH``, ``FG`` be parallelograms, and ``BK``, ``KD``
        the so-called complements;

I say that the complement ``BK`` is equal to the complement ``KD``.

For, since ``ABCD`` is a parallelogram, and ``AC`` its diameter, the triangle ``ABC`` is equal to the triangle ``ACD``. [:ref:`I.34`]

Again, since ``EH`` is a parallelogram, and ``AK`` is its diameter, the triangle ``AEK`` is equal to the triangle ``AHK``.
        
        For the same reason the triangle ``KFC`` is also equal to ``KGC``.

Now, since the triangle ``AEK`` is equal to the triangle ``AHK``, and ``KFC`` to ``KGC``,
        the triangle ``AEK`` together with ``KGC`` is equal to the triangle ``AHK`` together with ``KFC``. [:ref:`I.cn.2`]

And the whole triangle ``ABC`` is also equal to the whole ``ADC``; therefore the complement ``BK`` which remains is equal to the complement ``KD`` which remains. [:ref:`I.cn.3`]

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1**

   

   complements, παραπληρώματα, the figures put in to fill up (interstices).


.. note::


   **4. and about AC....**

   

   Euclid's phraseology here and in the next proposition implies that the complements as well as the other parallelograms are about

    the diagonal. The words are here περὶ δὲ τὴν ΑΓ παραλληλόγραμμα μὲν ἔστω τὰ ΕΘ, ΖΗ, τὰ δὲ λεγόμενα παραπληρώματα τὰ ΒΚ, ΚΔ. The expression the so-called complements

    indicates that this technical use of παραπληρώματα was not new, though it might not be universally known.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.26" [URL="/elements2/I/26/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.34" [URL="/elements2/I/34/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.43" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/43/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.10" [URL="/elements2/I/10/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.29" [URL="/elements2/I/29/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.26" -> "I.16";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.10" -> "I.9";
     "I.3" -> "I.2";
     "I.29" -> "I.cn.2";
     "I.34" -> "I.cn.2";
     "I.43" -> "I.cn.2";
     "I.16" -> "I.15";
     "I.29" -> "I.15";
     "I.34" -> "I.26";
     "I.29" -> "I.post.5";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.43" -> "I.34";
     "I.4" -> "I.cn.4";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.2" -> "I.1";
     "I.10" -> "I.1";
     "I.11" -> "I.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.16" -> "I.post.2";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.16" -> "I.10";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.16" -> "I.post.1";
     "I.8" -> "I.7";
     "I.15" -> "I.post.4";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.43" -> "I.cn.3";
     "I.13" -> "I.11";
     "I.34" -> "I.29";
     "I.7" -> "I.5";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
     "I.26" -> "I.4";
     "I.34" -> "I.4";
   }



Required for
------------

:ref:`I.44`, :ref:`I.45`, :ref:`II.11`, :ref:`II.13`, :ref:`II.14`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.8`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`VI.25`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.30`