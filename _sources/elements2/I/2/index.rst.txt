:order: 2
:number: 35
:type: prop
:tags: line
:dependencies: I.1, I.cn.1, I.cn.3, I.post.1, I.post.2, I.post.3




.. figure:: I.2.jpg
   :width: 50%

.. _I.2:

I.2
===

   To place at a given point (as an extremity) a straight line equal to a given straight line.

Let ``A`` be the given point, and ``BC`` the given straight line.

Thus it is required to place at the point ``A`` (as an extremity) a straight line equal to the given straight line ``BC``. 

From the point ``A`` to the point ``B`` let the straight line ``AB`` be joined; [:ref:`I.post.1`] and on it let the equilateral triangle ``DAB`` be constructed. [:ref:`I.1`]

Let the straight lines ``AE``, ``BF`` be produced in a straight line with ``DA``, ``DB``; [:ref:`I.post.2`] with centre ``B`` and distance ``BC`` let the circle ``CGH`` be described; [:ref:`I.post.3`] and again, with centre ``D`` and distance ``DG`` let the circle ``GKL`` be described. [:ref:`I.post.3`]

Then, since the point ``B`` is the centre of the circle ``CGH``, ``BC`` is equal to ``BG``.
        

Again, since the point ``D`` is the centre of the circle ``GKL``, ``DL`` is equal to ``DG``.

And in these ``DA`` is equal to ``DB``; therefore the remainder ``AL`` is equal to the remainder ``BG.`` [:ref:`I.cn.3`]
        

But ``BC`` was also proved equal to ``BG``; therefore each of the straight lines ``AL``, ``BC`` is equal to ``BG``.

And things which are equal to the same thing are also equal to one another; [:ref:`I.cn.1`] therefore ``AL`` is also equal to ``BC``.

Therefore at the given point ``A`` the straight line ``AL`` is placed equal to the given straight line ``BC``.


**Q. E. D.**


(Being) what it was required to do.


.. note::


   **1. (as an extremity).**

   

   I have inserted these words because to place a straight line ``at`` a given point

    (πρὸς τῷ δοθέντι σημείῳ) is not quite clear enough, at least in English.


.. note::


   **11. Let the straight lines AE, BF be produced....**

   

   It will be observed that in this first application of :ref:`I.post.2`, and again in :ref:`I.5`, Euclid speaks of the ``continuation`` of the straight line as that which is produced in such cases, ἐκβεβλήσθωσαν and προσεκβεβλήσθωσαν meaning little more than ``drawing`` straight lines in a straight line with

    the given straight lines. The first place in which Euclid uses phraseology exactly corresponding to ours when speaking of a straight line being produced is in :ref:`I.16`: let one side of it, ``BC``, be produced to ``D``

    (προσεκβεβλήσθω αὐτοῦ μία πλευρὰ ἡ ΒΓ ἐπὶ τὸ Δ).


.. note::


   **23. the remainder AL...the remainder BG.**

   

   The Greek expressions are λοιπὴ ἡ ΑΛ and λοιπῇ τῇ BH, and the literal translation would be ``AL`` (or ``BG``) ``remaining``,

    but the shade of meaning conveyed by the position of the definite article can hardly be expressed in English.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.2" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/2/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.2" -> "I.cn.3";
     "I.2" -> "I.1";
     "I.2" -> "I.post.2";
     "I.1" -> "I.def.15";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
   }



Required for
------------

:ref:`I.10`, :ref:`I.11`, :ref:`I.12`, :ref:`I.13`, :ref:`I.14`, :ref:`I.15`, :ref:`I.16`, :ref:`I.17`, :ref:`I.18`, :ref:`I.19`, :ref:`I.20`, :ref:`I.21`, :ref:`I.22`, :ref:`I.23`, :ref:`I.24`, :ref:`I.25`, :ref:`I.26`, :ref:`I.27`, :ref:`I.28`, :ref:`I.29`, :ref:`I.3`, :ref:`I.30`, :ref:`I.31`, :ref:`I.32`, :ref:`I.33`, :ref:`I.34`, :ref:`I.35`, :ref:`I.36`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.43`, :ref:`I.44`, :ref:`I.45`, :ref:`I.46`, :ref:`I.47`, :ref:`I.48`, :ref:`I.5`, :ref:`I.7`, :ref:`I.8`, :ref:`I.9`, :ref:`II.1`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.8`, :ref:`II.9`, :ref:`III.1`, :ref:`III.12`, :ref:`III.13`, :ref:`III.14`, :ref:`III.15`, :ref:`III.16`, :ref:`III.17`, :ref:`III.18`, :ref:`III.19`, :ref:`III.2`, :ref:`III.20`, :ref:`III.21`, :ref:`III.22`, :ref:`III.23`, :ref:`III.24`, :ref:`III.25`, :ref:`III.26`, :ref:`III.27`, :ref:`III.28`, :ref:`III.29`, :ref:`III.3`, :ref:`III.30`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`III.4`, :ref:`III.7`, :ref:`III.8`, :ref:`III.9`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.13`, :ref:`IV.15`, :ref:`IV.16`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.4`, :ref:`IV.5`, :ref:`IV.6`, :ref:`IV.7`, :ref:`IV.8`, :ref:`IV.9`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.13`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.33`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`