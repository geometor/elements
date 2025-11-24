:order: 149
:original_id: V.10
:type: prop
:dependencies: g.144, g.147

.. _g.149:

G.149
=====

**Heath ID:** :ref:`V.10`

   Of magnitudes which have a ratio to the same, that which has a greater ratio is greater; and that to which the same has a greater ratio is less.

For let ``A`` have to ``C`` a greater ratio than ``B`` has to ``C``; I say that ``A`` is greater than ``B``.

For, if not, ``A`` is either equal to ``B`` or less.

Now ``A`` is not equal to ``B``; for in that case each of the magnitudes ``A``, ``B`` would have had the same ratio to ``C``; [:ref:`g.144`] but they have not;


.. container:: center

   therefore ``A`` is not equal to ``B``.


Nor again is ``A`` less than ``B``; for in that case ``A`` would have had to ``C`` a less ratio than ``B`` has to ``C``; [:ref:`g.147`] but it has not;


.. container:: center

   therefore ``A`` is not less than ``B``.


But it was proved not to be equal either;


.. container:: center

   therefore ``A`` is greater than ``B``.


Again, let ``C`` have to ``B`` a greater ratio than ``C`` has to ``A``; I say that ``B`` is less than ``A``.

For, if not, it is either equal or greater.

Now ``B`` is not equal to ``A``; for in that case ``C`` would have had the same ratio to each of the magnitudes ``A``, ``B``; [:ref:`g.144`] but it has not;


.. container:: center

   therefore ``A`` is not equal to ``B``.


Nor again is ``B`` greater than ``A``; for in that case ``C`` would have had to ``B`` a less ratio than it has to ``A``; [:ref:`g.147`] but it has not;


.. container:: center

   therefore ``B`` is not greater than ``A``.


But it was proved that it is not equal either;


.. container:: center

   therefore ``B`` is less than ``A``.


Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.149" [label="G.149", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.149/", target="_top"];
     "G.146" [label="G.146", style="rounded,filled", fillcolor=orange, URL="/elements2/g.146/", target="_top"];
     "G.144" [label="G.144", URL="/elements2/g.144/", target="_top"];
     "G.140" [label="G.140", style="rounded,filled", fillcolor=orange, URL="/elements2/g.140/", target="_top"];
     "G.145" [label="G.145", style="rounded,filled", fillcolor=orange, URL="/elements2/g.145/", target="_top"];
     "G.147" [label="G.147", URL="/elements2/g.147/", target="_top"];
     "G.137" [label="G.137", style="rounded,filled", fillcolor=orange, URL="/elements2/g.137/", target="_top"];
     "G.147" -> "G.146";
     "G.149" -> "G.144";
     "G.144" -> "G.140";
     "G.147" -> "G.145";
     "G.149" -> "G.147";
     "G.147" -> "G.137";
   }



Required for
------------

:ref:`g.153`, :ref:`g.159`, :ref:`g.161`, :ref:`g.162`, :ref:`g.155`, :ref:`g.156`, :ref:`g.163`, :ref:`g.164`, :ref:`g.165`, :ref:`g.166`, :ref:`g.167`, :ref:`g.177`, :ref:`g.178`, :ref:`g.179`, :ref:`g.182`, :ref:`g.183`, :ref:`g.184`, :ref:`g.185`, :ref:`g.186`, :ref:`g.189`, :ref:`g.168`, :ref:`g.191`, :ref:`g.194`, :ref:`g.195`, :ref:`g.196`, :ref:`g.197`, :ref:`g.198`, :ref:`g.199`, :ref:`g.200`, :ref:`g.201`, :ref:`g.169`, :ref:`g.202`, :ref:`g.203`, :ref:`g.204`, :ref:`g.170`, :ref:`g.171`, :ref:`g.172`, :ref:`g.173`, :ref:`g.175`, :ref:`g.176`, :ref:`g.258`, :ref:`g.345`, :ref:`g.466`, :ref:`g.467`, :ref:`g.468`, :ref:`g.469`, :ref:`g.471`, :ref:`g.472`, :ref:`g.473`, :ref:`g.474`, :ref:`g.475`, :ref:`g.476`, :ref:`g.343`, :ref:`g.477`, :ref:`g.478`, :ref:`g.480`, :ref:`g.481`, :ref:`g.482`, :ref:`g.483`, :ref:`g.346`, :ref:`g.347`, :ref:`g.348`, :ref:`g.351`, :ref:`g.353`, :ref:`g.355`, :ref:`g.356`, :ref:`g.357`, :ref:`g.358`, :ref:`g.361`, :ref:`g.363`, :ref:`g.364`, :ref:`g.365`, :ref:`g.366`, :ref:`g.369`, :ref:`g.371`, :ref:`g.373`, :ref:`g.374`, :ref:`g.375`, :ref:`g.376`, :ref:`g.377`, :ref:`g.380`, :ref:`g.381`, :ref:`g.382`, :ref:`g.383`, :ref:`g.385`, :ref:`g.386`, :ref:`g.387`, :ref:`g.388`, :ref:`g.389`, :ref:`g.391`, :ref:`g.392`, :ref:`g.393`, :ref:`g.394`, :ref:`g.395`, :ref:`g.396`, :ref:`g.337`, :ref:`g.397`, :ref:`g.398`, :ref:`g.399`, :ref:`g.400`, :ref:`g.402`, :ref:`g.404`, :ref:`g.406`, :ref:`g.408`, :ref:`g.410`, :ref:`g.411`, :ref:`g.338`, :ref:`g.414`, :ref:`g.416`, :ref:`g.418`, :ref:`g.419`, :ref:`g.420`, :ref:`g.421`, :ref:`g.423`, :ref:`g.425`, :ref:`g.426`, :ref:`g.427`, :ref:`g.339`, :ref:`g.428`, :ref:`g.429`, :ref:`g.430`, :ref:`g.432`, :ref:`g.434`, :ref:`g.435`, :ref:`g.437`, :ref:`g.438`, :ref:`g.439`, :ref:`g.340`, :ref:`g.440`, :ref:`g.441`, :ref:`g.442`, :ref:`g.443`, :ref:`g.444`, :ref:`g.446`, :ref:`g.448`, :ref:`g.450`, :ref:`g.452`, :ref:`g.454`, :ref:`g.342`, :ref:`g.456`, :ref:`g.457`, :ref:`g.458`, :ref:`g.459`, :ref:`g.460`, :ref:`g.461`, :ref:`g.462`, :ref:`g.463`, :ref:`g.464`, :ref:`g.465`, :ref:`g.502`, :ref:`g.509`, :ref:`g.514`, :ref:`g.522`, :ref:`g.524`, :ref:`g.526`, :ref:`g.527`, :ref:`g.530`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.553`, :ref:`g.555`, :ref:`g.531`, :ref:`g.532`, :ref:`g.533`, :ref:`g.535`, :ref:`g.536`, :ref:`g.537`, :ref:`g.538`, :ref:`g.539`, :ref:`g.557`, :ref:`g.568`, :ref:`g.569`, :ref:`g.571`, :ref:`g.574`, :ref:`g.575`, :ref:`g.578`, :ref:`g.558`, :ref:`g.560`, :ref:`g.562`, :ref:`g.563`, :ref:`g.565`, :ref:`g.567`
