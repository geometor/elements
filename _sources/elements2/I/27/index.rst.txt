:order: 27
:number: 60
:type: prop
:tags: line
:dependencies: I.16, I.def.23




.. figure:: I.27.jpg
   :width: 50%

.. _I.27:

I.27
====

   If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.

For let the straight line ``EF`` falling on the two straight lines ``AB``, ``CD`` make the alternate angles ``AEF``, ``EFD`` equal to one another;

I say that ``AB`` is parallel to ``CD``.

For, if not, ``AB``, ``CD`` when produced will meet either in the direction of ``B``, ``D`` or towards ``A``, ``C``. 

Let them be produced and meet, in the direction of ``B``, ``D``, at ``G``.

Then, in the triangle ``GEF``, the exterior angle ``AEF`` is equal to the interior and opposite angle ``EFG``: which is impossible. [:ref:`I.16`]

Therefore ``AB``, ``CD`` when produced will not meet in the direction of ``B``, ``D``.

Similarly it can be proved that neither will they meet towards ``A``, ``C``. 

But straight lines which do not meet in either direction are parallel; [:ref:`I.def.23`] therefore ``AB`` is parallel to ``CD``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. falling on two straight lines,**

   

   εὶς δύο εὐθείας ἐμπίπτουσα, the phrase being the same as that used in :ref:`I.post.5`, meaning a ``transversal``.


.. note::


   **2. the alternate angles,**

   

   αἱ ἐναλλὰξ γωνίαι. Proclus (p. 357, 9) explains that Euclid uses the word ``alternate`` (or, more exactly, ``alternately``, ἐναλλάξ) in two connexions, (1) of a certain transformation of a proportion, as in Book V. and the arithmetical Books, (2) as here, of certain of the angles formed by parallels with a straight line crossing them. Alternate angles are, according to Euclid as interpreted by Proclus, those which are not on the same side of the transversal, and are not adjacent, but are separated by the transversal, both being within the parallels but one above

    and the other below.

    The meaning is natural enough if we imagine the four internal angles to be taken in cyclic order and ``alternate`` angles to be any two of them not successive but separated by one angle of the four.


.. note::


   **9. in the direction of B, D or towards A, C,**

   

   literally towards the ``parts B``, ``D`` or towards ``A``, ``C``,

    ἐπὶ τὰ Β, Δ μέρη ἢ ἐπὶ τὰ Α Γ.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.16" [URL="/elements2/I/16/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.def.23" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.23/", target="_top"];
     "I.9" [URL="/elements2/I/9/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.27" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/27/", target="_top"];
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
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.27" -> "I.16";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.27" -> "I.def.23";
     "I.10" -> "I.9";
     "I.3" -> "I.2";
     "I.9" -> "I.8";
     "I.11" -> "I.8";
     "I.16" -> "I.15";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.4" -> "I.cn.4";
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
     "I.5" -> "I.3";
     "I.9" -> "I.3";
     "I.11" -> "I.3";
     "I.16" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.13" -> "I.11";
     "I.7" -> "I.5";
     "I.5" -> "I.4";
     "I.10" -> "I.4";
     "I.16" -> "I.4";
   }



Required for
------------

:ref:`I.28`, :ref:`I.31`, :ref:`I.32`, :ref:`I.33`, :ref:`I.36`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.44`, :ref:`I.45`, :ref:`I.46`, :ref:`I.47`, :ref:`I.48`, :ref:`II.1`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.8`, :ref:`II.9`, :ref:`III.14`, :ref:`III.15`, :ref:`III.20`, :ref:`III.21`, :ref:`III.22`, :ref:`III.27`, :ref:`III.29`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.15`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.5`, :ref:`IV.6`, :ref:`IV.7`, :ref:`IV.8`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.13`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.33`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`