:order: 21
:original_id: I.13
:type: prop
:dependencies: G.19, G.18
:excerpt: If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.

**Heath ID:** `I.13 <https://geometor.github.io/euclid/I/13/>`_

.. picture:: G.21.png

.. _G.21:

G.21
====

    If a straight line set up on a straight line make angles, it will make either two right angles or angles equal to two right angles.

For let any straight line ``AB`` set up on the straight line ``CD`` make the angles ``CBA``, ``ABD``;

I say that the angles ``CBA``, ``ABD`` are either two right angles or equal to two right angles. 

Now, if the angle ``CBA`` is equal to the angle ``ABD``, they are two right angles. [:ref:`G.18`]

But, if not, let ``BE`` be drawn from the point ``B`` at right angles to ``CD``; [:ref:`G.19`] therefore the angles ``CBE``, ``EBD`` are two right angles.
        

Then, since the angle ``CBE`` is equal to the two angles ``CBA``, ``ABE``, let the angle ``EBD`` be added to each; therefore the angles ``CBE``, ``EBD`` are equal to the three angles ``CBA``, ``ABE``, ``EBD``. [C. N. 2]
        

Again, since the angle ``DBA`` is equal to the two angles ``DBE``, ``EBA``, let the angle ``ABC`` be added to each; therefore the angles ``DBA``. ``ABC`` are equal to the three angles ``DBE``, ``EBA``, ``ABC``. [C. N. 2]
        

But the angles ``CBE``, ``EBD`` were also proved equal to the same three angles; and things which are equal to the same thing are also equal to one another; [C. N. 1] therefore the angles ``CBE``, ``EBD`` are also equal to the angles ``DBA``, ``ABC``.
        But the angles ``CBE``, ``EBD`` are two right angles; therefore the angles ``DBA``, ``ABC`` are also equal to two right angles.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **17. let the angle EBD be added to each,**

   

   literally let the angle ``EBD`` be added (so as to be) common,

    κοινὴ προσκείσθω ἡ ὑπὸ ΕΒΔ. Similarly κοινὴ ἀφηρήσθω is used of subtracting a straight line or angle from each of two others. Let the common angle ``EBD`` be added

    is clearly an inaccurate translation, for the angle is not common before it is added, i.e. the κοινὴ is proleptic. Let the common angle be ``subtracted``

    as a translation of κοινὴ ἀφηρήσθω would be less unsatisfactory, it is true, but, as it is desirable to use corresponding words when translating the two expressions, it seems hopeless to attempt to keep the word common,

    and I have therefore said to each

    and from each

    simply.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.21" [label="G.21", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.21/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.8" -> "G.6";
     "G.21" -> "G.19";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.11" -> "G.10";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.19" -> "G.15";
     "G.19" -> "G.5";
     "G.8" -> "G.5";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.14" -> "G.12";
     "G.15" -> "G.14";
     "G.9" -> "G.8";
     "G.19" -> "G.9";
     "G.12" -> "G.9";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.12" -> "G.11";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
   }



Required for
------------

:ref:`G.23`, :ref:`G.24`, :ref:`G.25`, :ref:`G.26`, :ref:`G.27`, :ref:`G.28`, :ref:`G.30`, :ref:`G.31`, :ref:`G.32`, :ref:`G.34`, :ref:`G.35`, :ref:`G.36`, :ref:`G.38`, :ref:`G.39`, :ref:`G.42`, :ref:`G.43`, :ref:`G.44`, :ref:`G.45`, :ref:`G.46`, :ref:`G.47`, :ref:`G.48`, :ref:`G.49`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.56`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`
