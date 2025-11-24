:order: 5
:original_id: I.1
:type: prop
:dependencies: g.1, g.2, g.3, g.4

.. _g.5:

G.5
===

**Heath ID:** :ref:`I.1`

   On a given finite straight line to construct an equilateral triangle.

Let ``AB`` be the given finite straight line.

Thus it is required to construct an equilateral triangle on the straight line ``AB``. 

With centre ``A`` and distance ``AB`` let the circle ``BCD`` be described; [:ref:`g.4`] again, with centre ``B`` and distance ``BA`` let the circle ``ACE`` be described; [:ref:`g.4`] and from the point ``C``, in which the circles cut one another, to the points ``A``, ``B`` let the straight lines ``CA``, ``CB`` be joined. [:ref:`g.3`] 

Now, since the point ``A`` is the centre of the circle ``CDB``, ``AC`` is equal to ``AB``. [:ref:`g.2`]

Again, since the point ``B`` is the centre of the circle ``CAE``, ``BC`` is equal to ``BA``. [:ref:`g.2`]

But ``CA`` was also proved equal to ``AB``; therefore each of the straight lines ``CA``, ``CB`` is equal to ``AB``.

And things which are equal to the same thing are also equal to one another; [:ref:`g.1`] therefore ``CA`` is also equal to ``CB``.

Therefore the three straight lines ``CA``, ``AB``, ``BC`` are equal to one another. 

Therefore the triangle ``ABC`` is equilateral; and it has been constructed on the given finite straight line ``AB``.


**Q. E. D.**


(Being) what it was required to do.


.. note::


   **1. On a given finite straight line.**

   

   The Greek usage differs from ours in that the definite article is employed in such a phrase as this where we have the indefinite. ἐπὶ τῆς δοθείσης εὐθείας πεπερασμένης, on ``the`` given finite straight line,

    i.e. the finite straight line which we choose to take.


.. note::


   **3. Let AB be the given finite straight line.**

   

   To be strictly literal we should have to translate in the reverse order let the given finite straight line be the (straight line) ``AB``

   ; but this order is inconvenient in other cases where there is more than one datum, e.g. in the ``setting-out`` of :ref:`g.8`, let the given point be ``A``, and the given straight line ``BC``,

    the awkwardness arising from the omission of the verb in the second clause. Hence I have, for clearness' sake, adopted the other order throughout the book.


.. note::


   **8. let the circle BCD be described.**

   

   Two things are here to be noted, (1) the elegant and practically universal use of the perfect passive imperative in constructions, γεγράφθω meaning of course let it ``have been`` described

    or suppose it described,

    (2) the impossibility of expressing shortly in a translation the force of the words in their original order. κύκλος γεγράφθω ὸ ΒΓΔ means literally let a circle have been described, the (circle, namely, which I denote by) ``BCD``.

    Similarly we have lower down let straight lines, (namely) the (straight lines) ``CA``, ``CB``, be joined,

    ἐπεζεύχθωσαν εὐθεῖαι αί ΓΑ, ΓΒ. There seems to be no practicable alternative, in English, but to translate as I have done in the text.


.. note::


   **13. from the point C....**

   

   Euclid is careful to adhere to the phraseology of :ref:`g.3` except that he speaks of joining

    (ἐπεζεύχθωσαν) instead of drawing

    (γράφειν). He does not allow himself to use the shortened expression let the straight line ``FC`` be joined

    (without mention of the points ``F``, ``C``) until :ref:`g.12`.


.. note::


   **20. each of the straight lines CA, CB**

   

   , ἑκατέρα τῶν ΓΑ, ΓΒ and 24. the three straight lines CA, AB, BC, αἱ τρεῖς αἱ ΓΑ, ΑΒ, ΒΓ. I have, here and in all similar expressions, inserted the words straight lines

    which are not in the Greek. The possession of the inflected definite article enables the Greek to omit the words, but this is not possible in English, and it would scarcely be English to write each of ``CA``, ``CB``

    or the three ``CA``, ``AB``, ``BC``.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.5" [label="G.5", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.5/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.5" -> "G.2";
     "G.5" -> "G.1";
     "G.5" -> "G.4";
     "G.5" -> "G.3";
   }



Required for
------------

:ref:`g.17`, :ref:`g.19`, :ref:`g.20`, :ref:`g.21`, :ref:`g.23`, :ref:`g.24`, :ref:`g.25`, :ref:`g.26`, :ref:`g.27`, :ref:`g.28`, :ref:`g.8`, :ref:`g.30`, :ref:`g.31`, :ref:`g.32`, :ref:`g.33`, :ref:`g.34`, :ref:`g.35`, :ref:`g.36`, :ref:`g.38`, :ref:`g.39`, :ref:`g.42`, :ref:`g.9`, :ref:`g.43`, :ref:`g.44`, :ref:`g.45`, :ref:`g.46`, :ref:`g.47`, :ref:`g.48`, :ref:`g.49`, :ref:`g.50`, :ref:`g.51`, :ref:`g.52`, :ref:`g.53`, :ref:`g.54`, :ref:`g.55`, :ref:`g.56`, :ref:`g.57`, :ref:`g.58`, :ref:`g.59`, :ref:`g.60`, :ref:`g.61`, :ref:`g.12`, :ref:`g.14`, :ref:`g.15`, :ref:`g.16`, :ref:`g.62`, :ref:`g.71`, :ref:`g.72`, :ref:`g.73`, :ref:`g.74`, :ref:`g.75`, :ref:`g.63`, :ref:`g.64`, :ref:`g.65`, :ref:`g.66`, :ref:`g.67`, :ref:`g.68`, :ref:`g.69`, :ref:`g.70`, :ref:`g.76`, :ref:`g.88`, :ref:`g.90`, :ref:`g.92`, :ref:`g.94`, :ref:`g.95`, :ref:`g.97`, :ref:`g.98`, :ref:`g.99`, :ref:`g.77`, :ref:`g.100`, :ref:`g.101`, :ref:`g.102`, :ref:`g.104`, :ref:`g.105`, :ref:`g.106`, :ref:`g.107`, :ref:`g.108`, :ref:`g.109`, :ref:`g.110`, :ref:`g.78`, :ref:`g.111`, :ref:`g.112`, :ref:`g.113`, :ref:`g.114`, :ref:`g.115`, :ref:`g.116`, :ref:`g.117`, :ref:`g.118`, :ref:`g.79`, :ref:`g.82`, :ref:`g.83`, :ref:`g.85`, :ref:`g.131`, :ref:`g.132`, :ref:`g.133`, :ref:`g.122`, :ref:`g.135`, :ref:`g.136`, :ref:`g.120`, :ref:`g.121`, :ref:`g.124`, :ref:`g.125`, :ref:`g.127`, :ref:`g.128`, :ref:`g.129`, :ref:`g.130`, :ref:`g.302`, :ref:`g.167`, :ref:`g.177`, :ref:`g.178`, :ref:`g.179`, :ref:`g.181`, :ref:`g.182`, :ref:`g.183`, :ref:`g.184`, :ref:`g.185`, :ref:`g.186`, :ref:`g.189`, :ref:`g.168`, :ref:`g.191`, :ref:`g.194`, :ref:`g.195`, :ref:`g.196`, :ref:`g.197`, :ref:`g.198`, :ref:`g.199`, :ref:`g.200`, :ref:`g.201`, :ref:`g.169`, :ref:`g.202`, :ref:`g.203`, :ref:`g.204`, :ref:`g.205`, :ref:`g.170`, :ref:`g.171`, :ref:`g.172`, :ref:`g.173`, :ref:`g.175`, :ref:`g.176`, :ref:`g.258`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.483`, :ref:`g.347`, :ref:`g.348`, :ref:`g.351`, :ref:`g.353`, :ref:`g.355`, :ref:`g.356`, :ref:`g.357`, :ref:`g.358`, :ref:`g.361`, :ref:`g.363`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.371`, :ref:`g.373`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.381`, :ref:`g.382`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.395`, :ref:`g.396`, :ref:`g.397`, :ref:`g.399`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.432`, :ref:`g.433`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.446`, :ref:`g.448`, :ref:`g.450`, :ref:`g.452`, :ref:`g.454`, :ref:`g.456`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.494`, :ref:`g.495`, :ref:`g.496`, :ref:`g.499`, :ref:`g.500`, :ref:`g.502`, :ref:`g.504`, :ref:`g.506`, :ref:`g.507`, :ref:`g.508`, :ref:`g.509`, :ref:`g.510`, :ref:`g.511`, :ref:`g.512`, :ref:`g.514`, :ref:`g.516`, :ref:`g.518`, :ref:`g.519`, :ref:`g.520`, :ref:`g.521`, :ref:`g.522`, :ref:`g.524`, :ref:`g.525`, :ref:`g.526`, :ref:`g.527`, :ref:`g.528`, :ref:`g.529`, :ref:`g.488`, :ref:`g.489`, :ref:`g.490`, :ref:`g.492`, :ref:`g.493`, :ref:`g.530`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.549`, :ref:`g.553`, :ref:`g.555`, :ref:`g.531`, :ref:`g.532`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`, :ref:`g.557`, :ref:`g.568`, :ref:`g.569`, :ref:`g.570`, :ref:`g.571`, :ref:`g.572`, :ref:`g.573`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.558`, :ref:`g.560`, :ref:`g.562`, :ref:`g.563`, :ref:`g.564`, :ref:`g.565`, :ref:`g.567`
