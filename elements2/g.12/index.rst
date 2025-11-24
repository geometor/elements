:order: 12
:original_id: I.5
:type: prop
:dependencies: g.9, g.11, g.3, g.7

.. _g.12:

G.12
====

**Heath ID:** :ref:`I.5`

   In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another.

Let ``ABC`` be an isosceles triangle having the side ``AB``
        equal to the side ``AC``; and let the straight lines ``BD``, ``CE`` be produced further in a straight line with ``AB``, ``AC``. [:ref:`g.7`]

I say that the angle ``ABC`` is equal to the angle ``ACB``, and the angle ``CBD`` to the angle ``BCE``. 

Let a point ``F`` be taken at random on ``BD``;  from ``AE`` the greater let ``AG`` be cut off equal to ``AF`` the less; [:ref:`g.9`] and let the straight lines ``FC``, ``GB`` be joined. [:ref:`g.3`] 

Then, since ``AF`` is equal to ``AG`` and ``AB`` to ``AC``, the two sides ``FA``, ``AC`` are equal to the two sides ``GA``, ``AB``, respectively; and they contain a common angle, the angle ``FAG``. Therefore the base ``FC`` is equal to the base ``GB``, and the triangle ``AFC`` is equal to the triangle ``AGB``, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend, that is, the angle ``ACF`` to the angle ``ABG``, and the angle ``AFC`` to the angle ``AGB``. [:ref:`g.11`]

And, since the whole ``AF`` is equal to the whole ``AG``, and in these ``AB`` is equal to ``AC``, the remainder ``BF`` is equal to the remainder ``CG``.

But ``FC`` was also proved equal to ``GB``; therefore the two sides ``BF``, ``FC`` are equal to the two sides ``CG``, ``GB`` respectively; and the angle ``BFC`` is equal to the angle ``CGB``, while the base ``BC`` is common to them; therefore the triangle ``BFC`` is also equal to the triangle ``CGB``, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend; therefore the angle ``FBC`` is equal to the angle ``GCB``, and the angle ``BCF`` to the angle ``CBG``.
        

Accordingly, since the whole angle ``ABG`` was proved equal to the angle ``ACF``, and in these the angle ``CBG`` is equal to the angle ``BCF``, the remaining angle ``ABC`` is equal to the remaining angle ``ACB``; and they are at the base of the triangle ``ABC``. But the angle ``FBC`` was also proved equal to the angle ``GCB``; and they are under the base.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   **2. the equal straight lines**

   

   (meaning the equal ``sides``). Cf. note on the similar expression in :ref:`g.11`, lines 2, 3.


.. note::


   **10. Let a point F be taken at random on BD**

   

   , εἰλήφθω ἐπὶ τῆς ΒΔ τυχὸν σημεῖον τὸ Ζ, where τυχὸν σημεῖονmeans a chance point.


.. note::


   **17. the two sides FA, AC are equal to the two sides GA, AB respectively,**

   

   δύο αἱ ΖΑ, ΑΓ δυσὶ ταῖς ΗΑ, ΑΒ ἴσαι εἰσὶν ἑκατέρα ἑκατέρᾳ. Here, and in numberless later passages, I have inserted the word sides

    for the reason given in the note on :ref:`g.5`, line 20. It would have been permissible to supply either straight lines

    or sides

   ; but on the whole sides

    seems to be more in accordance with the phraseology of :ref:`g.11`.


.. note::


   **33. the base BC is common to them,**

   

   i.e., apparently, common to the ``angles``, as the αὐτῶν in βάσις αὐτῶν κοινὴ can only refer to γωνία and γωνίᾳ preceding. Simson wrote and the base ``BC`` is common to the two triangles ``BFC``, ``CGB``

   ; Todhunter left out these words as being of no use and tending to perplex a beginner. But Euclid evidently chose to quote the conclusion of :ref:`g.11` exactly; the first phrase of that conclusion is that the bases (of the two triangles) are equal, and, as the equal bases are here the ``same`` base, Euclid naturally substitutes the word common

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
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.12" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.8" -> "G.6";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.8" -> "G.5";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.12" -> "G.11";
     "G.11" -> "G.10";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
   }



Required for
------------

:ref:`g.17`, :ref:`g.19`, :ref:`g.20`, :ref:`g.21`, :ref:`g.23`, :ref:`g.24`, :ref:`g.25`, :ref:`g.26`, :ref:`g.27`, :ref:`g.28`, :ref:`g.30`, :ref:`g.31`, :ref:`g.32`, :ref:`g.33`, :ref:`g.34`, :ref:`g.35`, :ref:`g.36`, :ref:`g.38`, :ref:`g.39`, :ref:`g.42`, :ref:`g.43`, :ref:`g.44`, :ref:`g.45`, :ref:`g.46`, :ref:`g.47`, :ref:`g.48`, :ref:`g.49`, :ref:`g.50`, :ref:`g.51`, :ref:`g.52`, :ref:`g.53`, :ref:`g.54`, :ref:`g.55`, :ref:`g.56`, :ref:`g.57`, :ref:`g.58`, :ref:`g.59`, :ref:`g.60`, :ref:`g.61`, :ref:`g.14`, :ref:`g.15`, :ref:`g.16`, :ref:`g.62`, :ref:`g.71`, :ref:`g.72`, :ref:`g.73`, :ref:`g.74`, :ref:`g.75`, :ref:`g.63`, :ref:`g.64`, :ref:`g.65`, :ref:`g.66`, :ref:`g.67`, :ref:`g.68`, :ref:`g.69`, :ref:`g.70`, :ref:`g.76`, :ref:`g.88`, :ref:`g.90`, :ref:`g.92`, :ref:`g.94`, :ref:`g.95`, :ref:`g.97`, :ref:`g.98`, :ref:`g.99`, :ref:`g.77`, :ref:`g.100`, :ref:`g.101`, :ref:`g.102`, :ref:`g.104`, :ref:`g.105`, :ref:`g.106`, :ref:`g.107`, :ref:`g.108`, :ref:`g.109`, :ref:`g.110`, :ref:`g.78`, :ref:`g.111`, :ref:`g.112`, :ref:`g.113`, :ref:`g.114`, :ref:`g.115`, :ref:`g.116`, :ref:`g.117`, :ref:`g.118`, :ref:`g.79`, :ref:`g.82`, :ref:`g.83`, :ref:`g.85`, :ref:`g.131`, :ref:`g.132`, :ref:`g.133`, :ref:`g.122`, :ref:`g.135`, :ref:`g.136`, :ref:`g.120`, :ref:`g.121`, :ref:`g.124`, :ref:`g.125`, :ref:`g.127`, :ref:`g.128`, :ref:`g.129`, :ref:`g.130`, :ref:`g.302`, :ref:`g.167`, :ref:`g.177`, :ref:`g.178`, :ref:`g.179`, :ref:`g.181`, :ref:`g.182`, :ref:`g.183`, :ref:`g.184`, :ref:`g.185`, :ref:`g.186`, :ref:`g.189`, :ref:`g.168`, :ref:`g.191`, :ref:`g.194`, :ref:`g.195`, :ref:`g.196`, :ref:`g.197`, :ref:`g.198`, :ref:`g.199`, :ref:`g.200`, :ref:`g.201`, :ref:`g.169`, :ref:`g.202`, :ref:`g.203`, :ref:`g.204`, :ref:`g.205`, :ref:`g.170`, :ref:`g.171`, :ref:`g.172`, :ref:`g.173`, :ref:`g.175`, :ref:`g.176`, :ref:`g.258`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.483`, :ref:`g.347`, :ref:`g.348`, :ref:`g.351`, :ref:`g.353`, :ref:`g.355`, :ref:`g.356`, :ref:`g.357`, :ref:`g.358`, :ref:`g.361`, :ref:`g.363`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.371`, :ref:`g.373`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.381`, :ref:`g.382`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.395`, :ref:`g.396`, :ref:`g.397`, :ref:`g.399`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.432`, :ref:`g.433`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.446`, :ref:`g.448`, :ref:`g.450`, :ref:`g.452`, :ref:`g.454`, :ref:`g.456`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.494`, :ref:`g.495`, :ref:`g.496`, :ref:`g.499`, :ref:`g.500`, :ref:`g.502`, :ref:`g.504`, :ref:`g.506`, :ref:`g.507`, :ref:`g.508`, :ref:`g.509`, :ref:`g.510`, :ref:`g.511`, :ref:`g.512`, :ref:`g.514`, :ref:`g.516`, :ref:`g.518`, :ref:`g.519`, :ref:`g.520`, :ref:`g.521`, :ref:`g.522`, :ref:`g.524`, :ref:`g.525`, :ref:`g.526`, :ref:`g.527`, :ref:`g.528`, :ref:`g.529`, :ref:`g.488`, :ref:`g.489`, :ref:`g.490`, :ref:`g.492`, :ref:`g.493`, :ref:`g.530`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.549`, :ref:`g.553`, :ref:`g.555`, :ref:`g.531`, :ref:`g.532`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`, :ref:`g.557`, :ref:`g.568`, :ref:`g.569`, :ref:`g.570`, :ref:`g.571`, :ref:`g.572`, :ref:`g.573`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.558`, :ref:`g.560`, :ref:`g.562`, :ref:`g.563`, :ref:`g.564`, :ref:`g.565`, :ref:`g.567`
