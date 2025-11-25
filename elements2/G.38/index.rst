:order: 38
:original_id: I.27
:type: prop
:dependencies: G.25, G.37

.. _G.38:

G.38
====

**Heath ID:** :ref:`I.27`

   If a straight line falling on two straight lines make the alternate angles equal to one another, the straight lines will be parallel to one another.

For let the straight line ``EF`` falling on the two straight lines ``AB``, ``CD`` make the alternate angles ``AEF``, ``EFD`` equal to one another;

I say that ``AB`` is parallel to ``CD``.

For, if not, ``AB``, ``CD`` when produced will meet either in the direction of ``B``, ``D`` or towards ``A``, ``C``. 

Let them be produced and meet, in the direction of ``B``, ``D``, at ``G``.

Then, in the triangle ``GEF``, the exterior angle ``AEF`` is equal to the interior and opposite angle ``EFG``: which is impossible. [:ref:`G.25`]

Therefore ``AB``, ``CD`` when produced will not meet in the direction of ``B``, ``D``.

Similarly it can be proved that neither will they meet towards ``A``, ``C``. 

But straight lines which do not meet in either direction are parallel; [:ref:`G.37`] therefore ``AB`` is parallel to ``CD``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **1. falling on two straight lines,**

   

   εὶς δύο εὐθείας ἐμπίπτουσα, the phrase being the same as that used in :ref:`G.41`, meaning a ``transversal``.


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
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.38" [label="G.38", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.38/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.37" [label="G.37", fillcolor="#224422", URL="/elements2/G.37/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
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
     "G.25" -> "G.24";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.21" -> "G.19";
     "G.9" -> "G.8";
     "G.24" -> "G.22";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.38" -> "G.37";
     "G.25" -> "G.17";
     "G.38" -> "G.25";
     "G.17" -> "G.16";
     "G.24" -> "G.21";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.11" -> "G.10";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.15" -> "G.14";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.14" -> "G.12";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`G.39`, :ref:`G.44`, :ref:`G.45`, :ref:`G.46`, :ref:`G.49`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`
