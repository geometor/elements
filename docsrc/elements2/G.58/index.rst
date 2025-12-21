:order: 58
:original_id: I.45
:type: prop
:dependencies: G.23, G.42, G.43, G.46, G.47, G.55, G.57, G.1, G.40
:excerpt: To construct, in a given rectilineal angle, a parallelogram equal to a given rectilineal figure.

**Heath ID:** `I.45 <https://geometor.github.io/euclid/I/45/>`_

.. picture:: G.58.png

.. _G.58:

G.58
====

    To construct, in a given rectilineal angle, a parallelogram equal to a given rectilineal figure.

Let ``ABCD`` be the given rectilineal figure and ``E`` the given rectilineal angle; thus it is required to construct, in the given angle ``E``, a parallelogram equal to the rectilineal figure ``ABCD``. 

Let ``DB`` be joined, and let the parallelogram ``FH`` be constructed equal to the triangle ``ABD``, in the angle ``HKF`` which is equal to ``E``; [:ref:`G.55`] let the parallelogram ``GM`` equal to the triangle ``DBC`` be applied to the straight line ``GH``, in the angle ``GHM`` which is equal to ``E``. [:ref:`G.57`]

Then, since the angle ``E`` is equal to each of the angles ``HKF``, ``GHM``, the angle ``HKF`` is also equal to the angle ``GHM``. [:ref:`G.1`]
        

Let the angle ``KHG`` be added to each; therefore the angles ``FKH``, ``KHG`` are equal to the angles ``KHG``, ``GHM``.

But the angles ``FKH``, ``KHG`` are equal to two right angles; [:ref:`G.42`] therefore the angles ``KHG``, ``GHM`` are also equal to two right angles.

Thus, with a straight line ``GH``, and at the point ``H`` on it, two straight lines ``KH``, ``HM`` not lying on the same side make the adjacent angles equal to two right angles; therefore ``KH`` is in a straight line with ``HM``. [:ref:`G.23`]

And, since the straight line ``HG`` falls upon the parallels ``KM``, ``FG``, the alternate angles ``MHG``, ``HGF`` are equal to one another. [:ref:`G.42`]

Let the angle ``HGL`` be added to each; therefore the angles ``MHG``, ``HGL`` are equal to the angles ``HGF``, ``HGL``. [:ref:`G.40`]

But the angles ``MHG``, ``HGL`` are equal to two right angles; [:ref:`G.42`] therefore the angles ``HGF``, ``HGL`` are also equal to two right angles. [:ref:`G.1`] Therefore ``FG`` is in a straight line with ``GL``. [:ref:`G.23`]

And, since ``FK`` is equal and parallel to ``HG``, [:ref:`G.47`] and ``HG`` to ``ML`` also,
        ``KF`` is also equal and parallel to ``ML``; [:ref:`G.1`;:ref:`G.43`] and the straight lines ``KM``, ``FL`` join them (at their extremities); therefore ``KM``, ``FL`` are also equal and parallel. [:ref:`G.46`] Therefore ``KFLM`` is a parallelogram.

And, since the triangle ``ABD`` is equal to the parallelogram ``FH``, and ``DBC`` to ``GM``,
        the whole rectilineal figure ``ABCD`` is equal to the whole parallelogram ``KFLM``.

Therefore the parallelogram ``KFLM`` has been constructed equal to the given rectilineal figure ``ABCD``, in the angle ``FKM`` which is equal to the given angle ``E``.


**Q. E. D.**


Q. E. F.


.. note::


   **2, 3, 6, 45, 48. rectilineal figure, in the Greek**

   

   rectilineal

    simply, without figure,

    εὐθύγραμμον being here used as a substantive, like the similarly formed παραλληλόγραμμον.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.50" [label="G.50", fillcolor="#222244", URL="/elements2/G.50/", target="_top"];
     "G.55" [label="G.55", fillcolor="#222244", URL="/elements2/G.55/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.46" [label="G.46", fillcolor="#222244", URL="/elements2/G.46/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.57" [label="G.57", fillcolor="#222244", URL="/elements2/G.57/", target="_top"];
     "G.42" [label="G.42", fillcolor="#222244", URL="/elements2/G.42/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.54" [label="G.54", fillcolor="#222244", URL="/elements2/G.54/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.49" [label="G.49", fillcolor="#222244", URL="/elements2/G.49/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.40" [label="G.40", fillcolor="#442222", URL="/elements2/G.40/", target="_top"];
     "G.58" [label="G.58", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.58/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.38" [label="G.38", fillcolor="#222244", URL="/elements2/G.38/", target="_top"];
     "G.48" [label="G.48", fillcolor="#222244", URL="/elements2/G.48/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.23" [label="G.23", fillcolor="#222244", URL="/elements2/G.23/", target="_top"];
     "G.41" [label="G.41", fillcolor="#444422", URL="/elements2/G.41/", target="_top"];
     "G.51" [label="G.51", fillcolor="#222244", URL="/elements2/G.51/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.36" [label="G.36", fillcolor="#222244", URL="/elements2/G.36/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.43" [label="G.43", fillcolor="#222244", URL="/elements2/G.43/", target="_top"];
     "G.37" [label="G.37", fillcolor="#224422", URL="/elements2/G.37/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.44" [label="G.44", fillcolor="#222244", URL="/elements2/G.44/", target="_top"];
     "G.33" [label="G.33", fillcolor="#222244", URL="/elements2/G.33/", target="_top"];
     "G.56" [label="G.56", fillcolor="#222244", URL="/elements2/G.56/", target="_top"];
     "G.47" [label="G.47", fillcolor="#222244", URL="/elements2/G.47/", target="_top"];
     "G.54" -> "G.50";
     "G.57" -> "G.55";
     "G.58" -> "G.55";
     "G.21" -> "G.19";
     "G.49" -> "G.46";
     "G.58" -> "G.46";
     "G.24" -> "G.21";
     "G.23" -> "G.21";
     "G.42" -> "G.21";
     "G.57" -> "G.24";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.11" -> "G.10";
     "G.58" -> "G.57";
     "G.47" -> "G.42";
     "G.43" -> "G.42";
     "G.46" -> "G.42";
     "G.48" -> "G.42";
     "G.57" -> "G.42";
     "G.58" -> "G.42";
     "G.25" -> "G.17";
     "G.19" -> "G.15";
     "G.16" -> "G.15";
     "G.33" -> "G.15";
     "G.5" -> "G.3";
     "G.25" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.19" -> "G.5";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.5" -> "G.1";
     "G.43" -> "G.1";
     "G.24" -> "G.1";
     "G.49" -> "G.1";
     "G.48" -> "G.1";
     "G.57" -> "G.1";
     "G.8" -> "G.1";
     "G.58" -> "G.1";
     "G.23" -> "G.1";
     "G.42" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.14" -> "G.12";
     "G.24" -> "G.22";
     "G.23" -> "G.22";
     "G.55" -> "G.54";
     "G.9" -> "G.8";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.51" -> "G.49";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.47" -> "G.40";
     "G.48" -> "G.40";
     "G.58" -> "G.40";
     "G.56" -> "G.40";
     "G.42" -> "G.40";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.17" -> "G.16";
     "G.24" -> "G.6";
     "G.48" -> "G.6";
     "G.8" -> "G.6";
     "G.56" -> "G.6";
     "G.23" -> "G.6";
     "G.46" -> "G.38";
     "G.44" -> "G.38";
     "G.49" -> "G.48";
     "G.50" -> "G.48";
     "G.25" -> "G.7";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.58" -> "G.23";
     "G.57" -> "G.41";
     "G.42" -> "G.41";
     "G.55" -> "G.51";
     "G.15" -> "G.14";
     "G.47" -> "G.36";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.16" -> "G.9";
     "G.12" -> "G.9";
     "G.58" -> "G.43";
     "G.38" -> "G.37";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.46" -> "G.11";
     "G.48" -> "G.11";
     "G.25" -> "G.11";
     "G.17" -> "G.11";
     "G.12" -> "G.11";
     "G.57" -> "G.44";
     "G.51" -> "G.44";
     "G.55" -> "G.44";
     "G.50" -> "G.44";
     "G.44" -> "G.33";
     "G.55" -> "G.33";
     "G.57" -> "G.56";
     "G.54" -> "G.47";
     "G.49" -> "G.47";
     "G.48" -> "G.47";
     "G.51" -> "G.47";
     "G.58" -> "G.47";
     "G.56" -> "G.47";
     "G.50" -> "G.47";
   }
