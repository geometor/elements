:order: 29
:number: 62
:type: prop
:tags: line
:dependencies: I.13, I.15, I.cn.1, I.cn.2, I.post.5




.. figure:: I.29.jpg
   :width: 50%

.. _I.29:

I.29
====

   A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles.

For let the straight line ``EF`` fall on the parallel straight lines ``AB``, ``CD``;

I say that it makes the alternate angles ``AGH``, ``GHD`` equal, the exterior angle ``EGB`` equal to the interior and opposite angle ``GHD``, and the interior angles on the same side, namely ``BGH``, ``GHD``, equal to two right angles.

For, if the angle ``AGH`` is unequal to the angle ``GHD``, one of them is greater. 

Let the angle ``AGH`` be greater. 

Let the angle ``BGH`` be added to each; therefore the angles ``AGH``, ``BGH`` are greater than the angles ``BGH``, ``GHD``. 

But the angles ``AGH``, ``BGH`` are equal to two right angles; [:ref:`I.13`] therefore the angles ``BGH``, ``GHD`` are less than two right angles.

But straight lines produced indefinitely from angles less than two right angles meet; [:ref:`I.post.5`] therefore ``AB``, ``CD``, if produced indefinitely, will meet; but they do not meet, because they are by hypothesis parallel.

Therefore the angle ``AGH`` is not unequal to the angle ``GHD``, and is therefore equal to it.
        

Again, the angle ``AGH`` is equal to the angle ``EGB``; [:ref:`I.15`] therefore the angle ``EGB`` is also equal to the angle ``GHD``. [:ref:`I.cn.1`]

Let the angle ``BGH`` be added to each; therefore the angles ``EGB``, ``BGH`` are equal to the angles ``BGH``, ``GHD``. [:ref:`I.cn.2`]

But the angles ``EGB``, ``BGH`` are equal to two right angles; [:ref:`I.13`] therefore the angles ``BGH``, ``GHD`` are also equal to two right angles.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **23. straight lines produced indefinitely from angles less than two right angles,**

   

   αἰ δὲ ἀπ: ὲλασσόνων ἢ δύο ὀρθῶν ἐκβαλλόμεναι εἰς ἄπειπον συμπίπτουσιν, a variation from the more explicit language of :ref:`I.post.5`. A good deal is left to be understood, namely that the straight lines begin from points at which they meet a transversal, and make with it internal angles on the same side the sum of which is less than two right angles.


.. note::


   **26. because they are by hypothesis parallel,**

   

   literally because they are supposed parallel,

    διὰ τὸ παραλλήλους αὐτὰς ὑποκεῖσθαι.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.def.10" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.10/", target="_top"];
     "I.11" [URL="/elements2/I/11/", target="_top"];
     "I.post.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.4/", target="_top"];
     "I.8" [URL="/elements2/I/8/", target="_top"];
     "I.15" [URL="/elements2/I/15/", target="_top"];
     "I.5" [URL="/elements2/I/5/", target="_top"];
     "I.post.5" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.5/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.13" [URL="/elements2/I/13/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.7" [URL="/elements2/I/7/", target="_top"];
     "I.29" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/29/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.cn.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.2/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.11" -> "I.def.10";
     "I.13" -> "I.def.10";
     "I.13" -> "I.11";
     "I.15" -> "I.post.4";
     "I.11" -> "I.8";
     "I.29" -> "I.15";
     "I.7" -> "I.5";
     "I.29" -> "I.post.5";
     "I.5" -> "I.3";
     "I.11" -> "I.3";
     "I.2" -> "I.cn.3";
     "I.15" -> "I.cn.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.15" -> "I.cn.1";
     "I.29" -> "I.cn.1";
     "I.15" -> "I.13";
     "I.29" -> "I.13";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
     "I.5" -> "I.4";
     "I.8" -> "I.7";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.3" -> "I.2";
     "I.2" -> "I.1";
     "I.11" -> "I.1";
     "I.29" -> "I.cn.2";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
   }



Required for
------------

:ref:`I.30`, :ref:`I.32`, :ref:`I.33`, :ref:`I.34`, :ref:`I.35`, :ref:`I.36`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.43`, :ref:`I.44`, :ref:`I.45`, :ref:`I.46`, :ref:`I.47`, :ref:`I.48`, :ref:`II.1`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.8`, :ref:`II.9`, :ref:`III.14`, :ref:`III.15`, :ref:`III.20`, :ref:`III.21`, :ref:`III.22`, :ref:`III.27`, :ref:`III.29`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.15`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.5`, :ref:`IV.6`, :ref:`IV.7`, :ref:`IV.8`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.13`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.33`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`