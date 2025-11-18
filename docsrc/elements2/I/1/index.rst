:order: 1
:number: 34
:type: prop
:categories: construct
:tags: line, triangle
:dependencies: I.cn.1, I.def.15, I.post.1, I.post.3




.. figure:: I.1.jpg
   :width: 50%

.. _I.1:

I.1
===

   On a given finite straight line to construct an equilateral triangle.

Let ``AB`` be the given finite straight line.

Thus it is required to construct an equilateral triangle on the straight line ``AB``. 

With centre ``A`` and distance ``AB`` let the circle ``BCD`` be described; [:ref:`I.post.3`] again, with centre ``B`` and distance ``BA`` let the circle ``ACE`` be described; [:ref:`I.post.3`] and from the point ``C``, in which the circles cut one another, to the points ``A``, ``B`` let the straight lines ``CA``, ``CB`` be joined. [:ref:`I.post.1`] 

Now, since the point ``A`` is the centre of the circle ``CDB``, ``AC`` is equal to ``AB``. [:ref:`I.def.15`]

Again, since the point ``B`` is the centre of the circle ``CAE``, ``BC`` is equal to ``BA``. [:ref:`I.def.15`]

But ``CA`` was also proved equal to ``AB``; therefore each of the straight lines ``CA``, ``CB`` is equal to ``AB``.

And things which are equal to the same thing are also equal to one another; [:ref:`I.cn.1`] therefore ``CA`` is also equal to ``CB``.

Therefore the three straight lines ``CA``, ``AB``, ``BC`` are equal to one another. 

Therefore the triangle ``ABC`` is equilateral; and it has been constructed on the given finite straight line ``AB``.


**Q. E. D.**


(Being) what it was required to do.


.. note::


   **1. On a given finite straight line.**

   

   The Greek usage differs from ours in that the definite article is employed in such a phrase as this where we have the indefinite. ἐπὶ τῆς δοθείσης εὐθείας πεπερασμένης, on ``the`` given finite straight line,

    i.e. the finite straight line which we choose to take.


.. note::


   **3. Let AB be the given finite straight line.**

   

   To be strictly literal we should have to translate in the reverse order let the given finite straight line be the (straight line) ``AB``

   ; but this order is inconvenient in other cases where there is more than one datum, e.g. in the ``setting-out`` of :ref:`I.2`, let the given point be ``A``, and the given straight line ``BC``,

    the awkwardness arising from the omission of the verb in the second clause. Hence I have, for clearness' sake, adopted the other order throughout the book.


.. note::


   **8. let the circle BCD be described.**

   

   Two things are here to be noted, (1) the elegant and practically universal use of the perfect passive imperative in constructions, γεγράφθω meaning of course let it ``have been`` described

    or suppose it described,

    (2) the impossibility of expressing shortly in a translation the force of the words in their original order. κύκλος γεγράφθω ὸ ΒΓΔ means literally let a circle have been described, the (circle, namely, which I denote by) ``BCD``.

    Similarly we have lower down let straight lines, (namely) the (straight lines) ``CA``, ``CB``, be joined,

    ἐπεζεύχθωσαν εὐθεῖαι αί ΓΑ, ΓΒ. There seems to be no practicable alternative, in English, but to translate as I have done in the text.


.. note::


   **13. from the point C....**

   

   Euclid is careful to adhere to the phraseology of :ref:`I.post.1` except that he speaks of joining

    (ἐπεζεύχθωσαν) instead of drawing

    (γράφειν). He does not allow himself to use the shortened expression let the straight line ``FC`` be joined

    (without mention of the points ``F``, ``C``) until :ref:`I.5`.


.. note::


   **20. each of the straight lines CA, CB**

   

   , ἑκατέρα τῶν ΓΑ, ΓΒ and 24. the three straight lines CA, AB, BC, αἱ τρεῖς αἱ ΓΑ, ΑΒ, ΒΓ. I have, here and in all similar expressions, inserted the words straight lines

    which are not in the Greek. The possession of the inflected definite article enables the Greek to omit the words, but this is not possible in English, and it would scarcely be English to write each of ``CA``, ``CB``

    or the three ``CA``, ``AB``, ``BC``.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.1" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/1/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.1" -> "I.post.1";
     "I.1" -> "I.def.15";
     "I.1" -> "I.cn.1";
     "I.1" -> "I.post.3";
   }



Required for
------------

:ref:`I.10`, :ref:`I.11`, :ref:`I.12`, :ref:`I.13`, :ref:`I.14`, :ref:`I.15`, :ref:`I.16`, :ref:`I.17`, :ref:`I.18`, :ref:`I.19`, :ref:`I.2`, :ref:`I.20`, :ref:`I.21`, :ref:`I.22`, :ref:`I.23`, :ref:`I.24`, :ref:`I.25`, :ref:`I.26`, :ref:`I.27`, :ref:`I.28`, :ref:`I.29`, :ref:`I.3`, :ref:`I.30`, :ref:`I.31`, :ref:`I.32`, :ref:`I.33`, :ref:`I.34`, :ref:`I.35`, :ref:`I.36`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.43`, :ref:`I.44`, :ref:`I.45`, :ref:`I.46`, :ref:`I.47`, :ref:`I.48`, :ref:`I.5`, :ref:`I.7`, :ref:`I.8`, :ref:`I.9`, :ref:`II.1`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.8`, :ref:`II.9`, :ref:`III.1`, :ref:`III.12`, :ref:`III.13`, :ref:`III.14`, :ref:`III.15`, :ref:`III.16`, :ref:`III.17`, :ref:`III.18`, :ref:`III.19`, :ref:`III.2`, :ref:`III.20`, :ref:`III.21`, :ref:`III.22`, :ref:`III.23`, :ref:`III.24`, :ref:`III.25`, :ref:`III.26`, :ref:`III.27`, :ref:`III.28`, :ref:`III.29`, :ref:`III.3`, :ref:`III.30`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`III.4`, :ref:`III.7`, :ref:`III.8`, :ref:`III.9`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.13`, :ref:`IV.15`, :ref:`IV.16`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.4`, :ref:`IV.5`, :ref:`IV.6`, :ref:`IV.7`, :ref:`IV.8`, :ref:`IV.9`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.13`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.33`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`