:order: 20
:original_id: I.12
:type: prop
:dependencies: G.17, G.15, G.18, G.3, G.4

.. _G.20:

G.20
====

**Heath ID:** :ref:`I.12`

   To a given infinite straight line, from a given point which is not on it, to draw a perpendicular straight line.

Let ``AB`` be the given infinite straight line, and ``C`` the given point which is not on it; thus it is required to draw to the given infinite straight line ``AB``, from the given point ``C`` which is not on it, a perpendicular straight line.

For let a point ``D`` be taken at random on the other side of the straight line ``AB``, and with centre ``C`` and distance ``CD`` let the circle ``EFG`` be described; [:ref:`G.4`] 
        let the straight line ``EG``
         be bisected at ``H``, [:ref:`G.17`] and let the straight lines ``CG``, ``CH``, ``CE`` be joined. [:ref:`G.3`]

I say that ``CH`` has been drawn perpendicular to the given infinite straight line ``AB`` from the given point ``C`` which is not on it. 

For, since ``GH`` is equal to ``HE``, and ``HC`` is common, the two sides ``GH``, ``HC`` are equal to the two sides ``EH``, ``HC`` respectively; and the base ``CG`` is equal to the base ``CE``; therefore the angle ``CHG`` is equal to the angle ``EHC``. [:ref:`G.15`] And they are adjacent angles.

But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right, and the straight line standing on the other is called a perpendicular to that on which it stands. [:ref:`G.18`]

Therefore ``CH`` has been drawn perpendicular to the given infinite straight line ``AB`` from the given point ``C`` which is not on it.


**Q. E. D.**


Q. E. F.


.. note::


   **2. a perpendicular straight line**

   

   , κάθετον εὐθεῖαν γραμμἡν. This is the full expression for a ``perpendicular``, κάθετος meaning ``let fall`` or ``let down``, so that the expression corresponds to our ``plumb-line``. ἡ κάθετος is however constantly used alone for a perpendicular, γραμμἡ being understood.


.. note::


   **10. on the other side of the straight line AB**

   

   , literally towards the other parts of the straight line ``AB``,

    ἐπὶ τὰ ἕτερα μέρη τῆς AB. Cf. on the same side

    (ἐπὶ τὰ αὐτὰ μέρη) in :ref:`G.41` and in both directions

    (ἐφ̓ ἑκάτερα τὰ μἑρη) in :ref:`G.37`.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.20" [label="G.20", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.20/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.20" -> "G.17";
     "G.17" -> "G.16";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.11" -> "G.10";
     "G.16" -> "G.15";
     "G.20" -> "G.15";
     "G.8" -> "G.6";
     "G.15" -> "G.14";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.20" -> "G.4";
     "G.20" -> "G.18";
     "G.14" -> "G.12";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.20" -> "G.3";
   }
