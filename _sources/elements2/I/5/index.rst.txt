:order: 5
:number: 38
:type: prop
:tags: line, triangle
:dependencies: I.3, I.4, I.post.1, I.post.2




.. figure:: I.5.jpg
   :width: 50%

.. _I.5:

I.5
===

   In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another.

Let ``ABC`` be an isosceles triangle having the side ``AB``
        equal to the side ``AC``; and let the straight lines ``BD``, ``CE`` be produced further in a straight line with ``AB``, ``AC``. [:ref:`I.post.2`]

I say that the angle ``ABC`` is equal to the angle ``ACB``, and the angle ``CBD`` to the angle ``BCE``. 

Let a point ``F`` be taken at random on ``BD``;  from ``AE`` the greater let ``AG`` be cut off equal to ``AF`` the less; [:ref:`I.3`] and let the straight lines ``FC``, ``GB`` be joined. [:ref:`I.post.1`] 

Then, since ``AF`` is equal to ``AG`` and ``AB`` to ``AC``, the two sides ``FA``, ``AC`` are equal to the two sides ``GA``, ``AB``, respectively; and they contain a common angle, the angle ``FAG``. Therefore the base ``FC`` is equal to the base ``GB``, and the triangle ``AFC`` is equal to the triangle ``AGB``, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend, that is, the angle ``ACF`` to the angle ``ABG``, and the angle ``AFC`` to the angle ``AGB``. [:ref:`I.4`]

And, since the whole ``AF`` is equal to the whole ``AG``, and in these ``AB`` is equal to ``AC``, the remainder ``BF`` is equal to the remainder ``CG``.

But ``FC`` was also proved equal to ``GB``; therefore the two sides ``BF``, ``FC`` are equal to the two sides ``CG``, ``GB`` respectively; and the angle ``BFC`` is equal to the angle ``CGB``, while the base ``BC`` is common to them; therefore the triangle ``BFC`` is also equal to the triangle ``CGB``, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend; therefore the angle ``FBC`` is equal to the angle ``GCB``, and the angle ``BCF`` to the angle ``CBG``.
        

Accordingly, since the whole angle ``ABG`` was proved equal to the angle ``ACF``, and in these the angle ``CBG`` is equal to the angle ``BCF``, the remaining angle ``ABC`` is equal to the remaining angle ``ACB``; and they are at the base of the triangle ``ABC``. But the angle ``FBC`` was also proved equal to the angle ``GCB``; and they are under the base.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **2. the equal straight lines**

   

   (meaning the equal ``sides``). Cf. note on the similar expression in :ref:`I.4`, lines 2, 3.


.. note::


   **10. Let a point F be taken at random on BD**

   

   , εἰλήφθω ἐπὶ τῆς ΒΔ τυχὸν σημεῖον τὸ Ζ, where τυχὸν σημεῖονmeans a chance point.


.. note::


   **17. the two sides FA, AC are equal to the two sides GA, AB respectively,**

   

   δύο αἱ ΖΑ, ΑΓ δυσὶ ταῖς ΗΑ, ΑΒ ἴσαι εἰσὶν ἑκατέρα ἑκατέρᾳ. Here, and in numberless later passages, I have inserted the word sides

    for the reason given in the note on :ref:`I.1`, line 20. It would have been permissible to supply either straight lines

    or sides

   ; but on the whole sides

    seems to be more in accordance with the phraseology of :ref:`I.4`.


.. note::


   **33. the base BC is common to them,**

   

   i.e., apparently, common to the ``angles``, as the αὐτῶν in βάσις αὐτῶν κοινὴ can only refer to γωνία and γωνίᾳ preceding. Simson wrote and the base ``BC`` is common to the two triangles ``BFC``, ``CGB``

   ; Todhunter left out these words as being of no use and tending to perplex a beginner. But Euclid evidently chose to quote the conclusion of :ref:`I.4` exactly; the first phrase of that conclusion is that the bases (of the two triangles) are equal, and, as the equal bases are here the ``same`` base, Euclid naturally substitutes the word common

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
     rankdir="TB";
     node [shape=box, style=rounded];
     "I.2" [URL="/elements2/I/2/", target="_top"];
     "I.1" [URL="/elements2/I/1/", target="_top"];
     "I.cn.4" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.4/", target="_top"];
     "I.cn.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.3/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "I.4" [URL="/elements2/I/4/", target="_top"];
     "I.post.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.1/", target="_top"];
     "I.post.2" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.2/", target="_top"];
     "I.3" [URL="/elements2/I/3/", target="_top"];
     "I.5" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/I/5/", target="_top"];
     "I.cn.1" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/cn.1/", target="_top"];
     "I.post.3" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/post.3/", target="_top"];
     "I.3" -> "I.2";
     "I.2" -> "I.1";
     "I.4" -> "I.cn.4";
     "I.2" -> "I.cn.3";
     "I.1" -> "I.def.15";
     "I.3" -> "I.def.15";
     "I.5" -> "I.4";
     "I.1" -> "I.post.1";
     "I.2" -> "I.post.1";
     "I.5" -> "I.post.1";
     "I.2" -> "I.post.2";
     "I.5" -> "I.post.2";
     "I.5" -> "I.3";
     "I.1" -> "I.cn.1";
     "I.2" -> "I.cn.1";
     "I.3" -> "I.cn.1";
     "I.1" -> "I.post.3";
     "I.2" -> "I.post.3";
     "I.3" -> "I.post.3";
   }



Required for
------------

:ref:`I.10`, :ref:`I.11`, :ref:`I.12`, :ref:`I.13`, :ref:`I.14`, :ref:`I.15`, :ref:`I.16`, :ref:`I.17`, :ref:`I.18`, :ref:`I.19`, :ref:`I.20`, :ref:`I.21`, :ref:`I.22`, :ref:`I.23`, :ref:`I.24`, :ref:`I.25`, :ref:`I.26`, :ref:`I.27`, :ref:`I.28`, :ref:`I.29`, :ref:`I.30`, :ref:`I.31`, :ref:`I.32`, :ref:`I.33`, :ref:`I.34`, :ref:`I.35`, :ref:`I.36`, :ref:`I.37`, :ref:`I.38`, :ref:`I.39`, :ref:`I.40`, :ref:`I.41`, :ref:`I.42`, :ref:`I.43`, :ref:`I.44`, :ref:`I.45`, :ref:`I.46`, :ref:`I.47`, :ref:`I.48`, :ref:`I.7`, :ref:`I.8`, :ref:`I.9`, :ref:`II.1`, :ref:`II.10`, :ref:`II.11`, :ref:`II.12`, :ref:`II.13`, :ref:`II.14`, :ref:`II.2`, :ref:`II.3`, :ref:`II.4`, :ref:`II.5`, :ref:`II.6`, :ref:`II.7`, :ref:`II.8`, :ref:`II.9`, :ref:`III.1`, :ref:`III.12`, :ref:`III.13`, :ref:`III.14`, :ref:`III.15`, :ref:`III.16`, :ref:`III.17`, :ref:`III.18`, :ref:`III.19`, :ref:`III.2`, :ref:`III.20`, :ref:`III.21`, :ref:`III.22`, :ref:`III.23`, :ref:`III.24`, :ref:`III.25`, :ref:`III.26`, :ref:`III.27`, :ref:`III.28`, :ref:`III.29`, :ref:`III.3`, :ref:`III.30`, :ref:`III.31`, :ref:`III.32`, :ref:`III.33`, :ref:`III.34`, :ref:`III.35`, :ref:`III.36`, :ref:`III.37`, :ref:`III.4`, :ref:`III.7`, :ref:`III.8`, :ref:`III.9`, :ref:`IV.10`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.13`, :ref:`IV.15`, :ref:`IV.16`, :ref:`IV.2`, :ref:`IV.3`, :ref:`IV.4`, :ref:`IV.5`, :ref:`IV.6`, :ref:`IV.7`, :ref:`IV.8`, :ref:`IV.9`, :ref:`VI.1`, :ref:`VI.10`, :ref:`VI.11`, :ref:`VI.12`, :ref:`VI.13`, :ref:`VI.14`, :ref:`VI.15`, :ref:`VI.16`, :ref:`VI.17`, :ref:`VI.18`, :ref:`VI.19`, :ref:`VI.2`, :ref:`VI.20`, :ref:`VI.22`, :ref:`VI.23`, :ref:`VI.24`, :ref:`VI.25`, :ref:`VI.26`, :ref:`VI.27`, :ref:`VI.28`, :ref:`VI.29`, :ref:`VI.3`, :ref:`VI.30`, :ref:`VI.31`, :ref:`VI.32`, :ref:`VI.33`, :ref:`VI.4`, :ref:`VI.5`, :ref:`VI.6`, :ref:`VI.7`, :ref:`VI.8`, :ref:`VI.9`