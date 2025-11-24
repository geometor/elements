:order: 156
:original_id: V.21
:type: prop
:dependencies: g.149, g.152, g.147

.. _g.156:

G.156
=====

**Heath ID:** :ref:`V.21`

   If there be three magnitudes, and others equal to them in multitude, which taken two and two together are in the same ratio, and the proportion of them be perturbed, then, if ex aequali
          the first magnitude is greater than the third, the fourth will also be greater than the sixth; if equal, equal; and if less, less.

Let there be three magnitudes ``A``, ``B``, ``C``, and others ``D``, ``E``, ``F`` equal to them in multitude, which taken two and two are in the same ratio, and let the proportion of them be perturbed, so that,


.. container:: center

   as ``A`` is to ``B``, so is ``E`` to ``F``,


and, as ``B`` is to ``C``, so is ``D`` to ``E``, and let ``A`` be greater than ``C``
ex aequali; I say that ``D`` will also be greater than ``F``; if ``A`` is equal to ``C``, equal; and if less, less.

For, since ``A`` is greater than ``C``, and ``B`` is some other magnitude, therefore ``A`` has to ``B`` a greater ratio than ``C`` has to ``B``. [:ref:`g.147`]

But, as ``A`` is to ``B``, so is ``E`` to ``F``, and, as ``C`` is to ``B``, inversely, so is ``E`` to ``D``. Therefore also ``E`` has to ``F`` a greater ratio than ``E`` has to ``D``. [:ref:`g.152`]

But that to which the same has a greater ratio is less; [:ref:`g.149`]


.. container:: center

   therefore ``F`` is less than ``D``; therefore ``D`` is greater than ``F``.


Similarly we can prove that,


.. container:: center

   if ``A`` be equal to ``C``, ``D`` will also be equal to ``F``;


and if less, less.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.145" [label="G.145", style="rounded,filled", fillcolor=orange, URL="/elements2/g.145/", target="_top"];
     "G.156" [label="G.156", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.156/", target="_top"];
     "G.152" [label="G.152", URL="/elements2/g.152/", target="_top"];
     "G.140" [label="G.140", style="rounded,filled", fillcolor=orange, URL="/elements2/g.140/", target="_top"];
     "G.144" [label="G.144", URL="/elements2/g.144/", target="_top"];
     "G.149" [label="G.149", URL="/elements2/g.149/", target="_top"];
     "G.146" [label="G.146", style="rounded,filled", fillcolor=orange, URL="/elements2/g.146/", target="_top"];
     "G.137" [label="G.137", style="rounded,filled", fillcolor=orange, URL="/elements2/g.137/", target="_top"];
     "G.147" [label="G.147", URL="/elements2/g.147/", target="_top"];
     "G.147" -> "G.145";
     "G.156" -> "G.152";
     "G.144" -> "G.140";
     "G.152" -> "G.140";
     "G.149" -> "G.144";
     "G.156" -> "G.149";
     "G.147" -> "G.146";
     "G.152" -> "G.146";
     "G.147" -> "G.137";
     "G.149" -> "G.147";
     "G.156" -> "G.147";
   }



Required for
------------

:ref:`g.159`, :ref:`g.162`, :ref:`g.164`, :ref:`g.166`, :ref:`g.167`, :ref:`g.177`, :ref:`g.178`, :ref:`g.179`, :ref:`g.182`, :ref:`g.183`, :ref:`g.184`, :ref:`g.185`, :ref:`g.186`, :ref:`g.189`, :ref:`g.168`, :ref:`g.191`, :ref:`g.194`, :ref:`g.195`, :ref:`g.196`, :ref:`g.197`, :ref:`g.198`, :ref:`g.199`, :ref:`g.200`, :ref:`g.201`, :ref:`g.169`, :ref:`g.202`, :ref:`g.203`, :ref:`g.204`, :ref:`g.170`, :ref:`g.171`, :ref:`g.172`, :ref:`g.173`, :ref:`g.175`, :ref:`g.176`, :ref:`g.258`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.483`, :ref:`g.348`, :ref:`g.355`, :ref:`g.356`, :ref:`g.357`, :ref:`g.358`, :ref:`g.361`, :ref:`g.363`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.502`, :ref:`g.509`, :ref:`g.514`, :ref:`g.522`, :ref:`g.524`, :ref:`g.526`, :ref:`g.527`, :ref:`g.530`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.553`, :ref:`g.555`, :ref:`g.531`, :ref:`g.532`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`, :ref:`g.557`, :ref:`g.568`, :ref:`g.569`, :ref:`g.571`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.558`, :ref:`g.560`, :ref:`g.562`, :ref:`g.563`, :ref:`g.565`, :ref:`g.567`
