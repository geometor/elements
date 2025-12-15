:order: 56
:original_id: I.43
:type: prop
:dependencies: G.47, G.40, G.6

.. _G.56:

G.56
====

**Heath ID:** :ref:`I.43`

   In any parallelogram the complements of the parallelograms about the diameter are equal to one another.

Let ``ABCD`` be a parallelogram, and ``AC`` its diameter; and about ``AC`` let ``EH``, ``FG`` be parallelograms, and ``BK``, ``KD``
        the so-called complements;

I say that the complement ``BK`` is equal to the complement ``KD``.

For, since ``ABCD`` is a parallelogram, and ``AC`` its diameter, the triangle ``ABC`` is equal to the triangle ``ACD``. [:ref:`G.47`]

Again, since ``EH`` is a parallelogram, and ``AK`` is its diameter, the triangle ``AEK`` is equal to the triangle ``AHK``.
        
        For the same reason the triangle ``KFC`` is also equal to ``KGC``.

Now, since the triangle ``AEK`` is equal to the triangle ``AHK``, and ``KFC`` to ``KGC``,
        the triangle ``AEK`` together with ``KGC`` is equal to the triangle ``AHK`` together with ``KFC``. [:ref:`G.40`]

And the whole triangle ``ABC`` is also equal to the whole ``ADC``; therefore the complement ``BK`` which remains is equal to the complement ``KD`` which remains. [:ref:`G.6`]

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
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.40" [label="G.40", fillcolor="#442222", URL="/elements2/G.40/", target="_top"];
     "G.42" [label="G.42", fillcolor="#222244", URL="/elements2/G.42/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.36" [label="G.36", fillcolor="#222244", URL="/elements2/G.36/", target="_top"];
     "G.47" [label="G.47", fillcolor="#222244", URL="/elements2/G.47/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.56" [label="G.56", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.56/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
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
     "G.25" -> "G.7";
     "G.42" -> "G.41";
     "G.25" -> "G.17";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.56" -> "G.40";
     "G.47" -> "G.42";
     "G.36" -> "G.25";
     "G.17" -> "G.16";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.47" -> "G.11";
     "G.11" -> "G.10";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.56" -> "G.6";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.15" -> "G.14";
     "G.47" -> "G.36";
     "G.56" -> "G.47";
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

:ref:`G.57`, :ref:`G.58`
