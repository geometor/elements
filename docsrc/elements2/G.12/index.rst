:order: 12
:original_id: I.5
:type: prop
:dependencies: G.9, G.11, G.3, G.7
:excerpt: In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another.

**Heath ID:** `I.5 <https://geometor.github.io/euclid/I/5/>`_

.. picture:: G.12.png

.. _G.12:

G.12
====

    In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another.

Let ``ABC`` be an isosceles triangle having the side ``AB``
        equal to the side ``AC``; and let the straight lines ``BD``, ``CE`` be produced further in a straight line with ``AB``, ``AC``. [:ref:`G.7`]

I say that the angle ``ABC`` is equal to the angle ``ACB``, and the angle ``CBD`` to the angle ``BCE``. 

Let a point ``F`` be taken at random on ``BD``;  from ``AE`` the greater let ``AG`` be cut off equal to ``AF`` the less; [:ref:`G.9`] and let the straight lines ``FC``, ``GB`` be joined. [:ref:`G.3`] 

Then, since ``AF`` is equal to ``AG`` and ``AB`` to ``AC``, the two sides ``FA``, ``AC`` are equal to the two sides ``GA``, ``AB``, respectively; and they contain a common angle, the angle ``FAG``. Therefore the base ``FC`` is equal to the base ``GB``, and the triangle ``AFC`` is equal to the triangle ``AGB``, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend, that is, the angle ``ACF`` to the angle ``ABG``, and the angle ``AFC`` to the angle ``AGB``. [:ref:`G.11`]

And, since the whole ``AF`` is equal to the whole ``AG``, and in these ``AB`` is equal to ``AC``, the remainder ``BF`` is equal to the remainder ``CG``.

But ``FC`` was also proved equal to ``GB``; therefore the two sides ``BF``, ``FC`` are equal to the two sides ``CG``, ``GB`` respectively; and the angle ``BFC`` is equal to the angle ``CGB``, while the base ``BC`` is common to them; therefore the triangle ``BFC`` is also equal to the triangle ``CGB``, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend; therefore the angle ``FBC`` is equal to the angle ``GCB``, and the angle ``BCF`` to the angle ``CBG``.
        

Accordingly, since the whole angle ``ABG`` was proved equal to the angle ``ACF``, and in these the angle ``CBG`` is equal to the angle ``BCF``, the remaining angle ``ABC`` is equal to the remaining angle ``ACB``; and they are at the base of the triangle ``ABC``. But the angle ``FBC`` was also proved equal to the angle ``GCB``; and they are under the base.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **2. the equal straight lines**

   

   (meaning the equal ``sides``). Cf. note on the similar expression in :ref:`G.11`, lines 2, 3.


.. note::


   **10. Let a point F be taken at random on BD**

   

   , εἰλήφθω ἐπὶ τῆς ΒΔ τυχὸν σημεῖον τὸ Ζ, where τυχὸν σημεῖονmeans a chance point.


.. note::


   **17. the two sides FA, AC are equal to the two sides GA, AB respectively,**

   

   δύο αἱ ΖΑ, ΑΓ δυσὶ ταῖς ΗΑ, ΑΒ ἴσαι εἰσὶν ἑκατέρα ἑκατέρᾳ. Here, and in numberless later passages, I have inserted the word sides

    for the reason given in the note on :ref:`G.5`, line 20. It would have been permissible to supply either straight lines

    or sides

   ; but on the whole sides

    seems to be more in accordance with the phraseology of :ref:`G.11`.


.. note::


   **33. the base BC is common to them,**

   

   i.e., apparently, common to the ``angles``, as the αὐτῶν in βάσις αὐτῶν κοινὴ can only refer to γωνία and γωνίᾳ preceding. Simson wrote and the base ``BC`` is common to the two triangles ``BFC``, ``CGB``

   ; Todhunter left out these words as being of no use and tending to perplex a beginner. But Euclid evidently chose to quote the conclusion of :ref:`G.11` exactly; the first phrase of that conclusion is that the bases (of the two triangles) are equal, and, as the equal bases are here the ``same`` base, Euclid naturally substitutes the word common

    for equal.


.. note::


   **48**

   

   As (Being) what it was required to prove

    (or do

   ) is somewhat long, I shall henceforth write the time-honoured Q. E. D.

    and Q. E. F.

    for ὅπερ ἔδει δεῖξαι and ὅπερ ἔδει ποιῆσαι.


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.12" [label="G.12", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.12/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.8" -> "G.6";
     "G.9" -> "G.8";
     "G.12" -> "G.9";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.11" -> "G.10";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.12" -> "G.11";
     "G.8" -> "G.5";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
   }



Required for
------------

:ref:`G.17`, :ref:`G.19`, :ref:`G.20`, :ref:`G.21`, :ref:`G.23`, :ref:`G.24`, :ref:`G.25`, :ref:`G.26`, :ref:`G.27`, :ref:`G.28`, :ref:`G.30`, :ref:`G.31`, :ref:`G.32`, :ref:`G.33`, :ref:`G.34`, :ref:`G.35`, :ref:`G.36`, :ref:`G.38`, :ref:`G.39`, :ref:`G.42`, :ref:`G.43`, :ref:`G.44`, :ref:`G.45`, :ref:`G.46`, :ref:`G.47`, :ref:`G.48`, :ref:`G.49`, :ref:`G.50`, :ref:`G.51`, :ref:`G.52`, :ref:`G.53`, :ref:`G.54`, :ref:`G.55`, :ref:`G.56`, :ref:`G.57`, :ref:`G.58`, :ref:`G.59`, :ref:`G.60`, :ref:`G.61`, :ref:`G.14`, :ref:`G.15`, :ref:`G.16`
