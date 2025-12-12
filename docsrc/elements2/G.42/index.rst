:order: 42
:original_id: I.29
:type: prop
:dependencies: G.21, G.24, G.1, G.40, G.41

.. _G.42:

G.42
====

**Heath ID:** :ref:`I.29`

   A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles.

For let the straight line ``EF`` fall on the parallel straight lines ``AB``, ``CD``;

I say that it makes the alternate angles ``AGH``, ``GHD`` equal, the exterior angle ``EGB`` equal to the interior and opposite angle ``GHD``, and the interior angles on the same side, namely ``BGH``, ``GHD``, equal to two right angles.

For, if the angle ``AGH`` is unequal to the angle ``GHD``, one of them is greater. 

Let the angle ``AGH`` be greater. 

Let the angle ``BGH`` be added to each; therefore the angles ``AGH``, ``BGH`` are greater than the angles ``BGH``, ``GHD``. 

But the angles ``AGH``, ``BGH`` are equal to two right angles; [:ref:`G.21`] therefore the angles ``BGH``, ``GHD`` are less than two right angles.

But straight lines produced indefinitely from angles less than two right angles meet; [:ref:`G.41`] therefore ``AB``, ``CD``, if produced indefinitely, will meet; but they do not meet, because they are by hypothesis parallel.

Therefore the angle ``AGH`` is not unequal to the angle ``GHD``, and is therefore equal to it.
        

Again, the angle ``AGH`` is equal to the angle ``EGB``; [:ref:`G.24`] therefore the angle ``EGB`` is also equal to the angle ``GHD``. [:ref:`G.1`]

Let the angle ``BGH`` be added to each; therefore the angles ``EGB``, ``BGH`` are equal to the angles ``BGH``, ``GHD``. [:ref:`G.40`]

But the angles ``EGB``, ``BGH`` are equal to two right angles; [:ref:`G.21`] therefore the angles ``BGH``, ``GHD`` are also equal to two right angles.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **23. straight lines produced indefinitely from angles less than two right angles,**

   

   αἰ δὲ ἀπ: ὲλασσόνων ἢ δύο ὀρθῶν ἐκβαλλόμεναι εἰς ἄπειπον συμπίπτουσιν, a variation from the more explicit language of :ref:`G.41`. A good deal is left to be understood, namely that the straight lines begin from points at which they meet a transversal, and make with it internal angles on the same side the sum of which is less than two right angles.


.. note::


   **26. because they are by hypothesis parallel,**

   

   literally because they are supposed parallel,

    διὰ τὸ παραλλήλους αὐτὰς ὑποκεῖσθαι.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.41" [label="G.41", fillcolor="#444422", URL="/elements2/G.41/", target="_top"];
     "G.40" [label="G.40", fillcolor="#442222", URL="/elements2/G.40/", target="_top"];
     "G.42" [label="G.42", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.42/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.42" -> "G.24";
     "G.8" -> "G.5";
     "G.19" -> "G.5";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.21" -> "G.19";
     "G.9" -> "G.8";
     "G.24" -> "G.22";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.42" -> "G.41";
     "G.42" -> "G.40";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.12" -> "G.11";
     "G.11" -> "G.10";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.19" -> "G.15";
     "G.15" -> "G.14";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.14" -> "G.12";
     "G.12" -> "G.9";
     "G.19" -> "G.9";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
   }



Required for
------------

:ref:`G.43`, :ref:`G.45`, :ref:`G.46`, :ref:`G.47`, :ref:`G.48`, :ref:`G.49`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.56`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`
