:order: 165
:original_id: V.24
:type: prop
:dependencies: g.161, g.163

.. _g.165:

G.165
=====

**Heath ID:** :ref:`V.24`

   If a first magnitude have to a second the same ratio as a third has to a fourth, and also a fifth have to the second the same ratio as a sixth to the fourth, the first and fifth added together will have to the second the same ratio as the third and sixth have to the fourth.

Let a first magnitude ``AB`` have to a second ``C`` the same ratio as a third ``DE`` has to a fourth ``F``; and let also a fifth ``BG`` have to

the second ``C`` the same ratio as a sixth ``EH`` has to the fourth ``F``; I say that the first and fifth added together, ``AG``, will have to the second ``C`` the same ratio as the third and sixth, ``DH``, has to the fourth ``F``.

For since, as ``BG`` is to ``C``, so is ``EH`` to ``F``, inversely, as ``C`` is to ``BG``, so is ``F`` to ``EH``.

Since, then, as ``AB`` is to ``C``, so is ``DE`` to ``F``,


.. container:: center

   and, as ``C`` is to ``BG``, so is ``F`` to ``EH``,


therefore, ex aequali, as ``AB`` is to ``BG``, so is ``DE`` to ``EH``. [:ref:`g.163`]

And, since the magnitudes are proportional separando, they will also be proportional componendo; [:ref:`g.161`]


.. container:: center

   therefore, as ``AG`` is to ``GB``, so is ``DH`` to ``HE``.


But also, as ``BG`` is to ``C``, so is ``EH`` to ``F``; therefore, ex aequali, as ``AG`` is to ``C``, so is ``DH`` to ``F``. [:ref:`g.163`]

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.163" [label="G.163", URL="/elements2/g.163/", target="_top"];
     "G.161" [label="G.161", URL="/elements2/g.161/", target="_top"];
     "G.140" [label="G.140", style="rounded,filled", fillcolor=orange, URL="/elements2/g.140/", target="_top"];
     "G.137" [label="G.137", style="rounded,filled", fillcolor=orange, URL="/elements2/g.137/", target="_top"];
     "G.149" [label="G.149", URL="/elements2/g.149/", target="_top"];
     "G.144" [label="G.144", URL="/elements2/g.144/", target="_top"];
     "G.160" [label="G.160", URL="/elements2/g.160/", target="_top"];
     "G.139" [label="G.139", URL="/elements2/g.139/", target="_top"];
     "G.141" [label="G.141", URL="/elements2/g.141/", target="_top"];
     "G.155" [label="G.155", URL="/elements2/g.155/", target="_top"];
     "G.145" [label="G.145", style="rounded,filled", fillcolor=orange, URL="/elements2/g.145/", target="_top"];
     "G.150" [label="G.150", style="rounded,filled", fillcolor=orange, URL="/elements2/g.150/", target="_top"];
     "G.138" [label="G.138", style="rounded,filled", fillcolor=orange, URL="/elements2/g.138/", target="_top"];
     "G.165" [label="G.165", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.165/", target="_top"];
     "G.152" [label="G.152", URL="/elements2/g.152/", target="_top"];
     "G.146" [label="G.146", style="rounded,filled", fillcolor=orange, URL="/elements2/g.146/", target="_top"];
     "G.153" [label="G.153", URL="/elements2/g.153/", target="_top"];
     "G.147" [label="G.147", URL="/elements2/g.147/", target="_top"];
     "G.165" -> "G.163";
     "G.165" -> "G.161";
     "G.141" -> "G.140";
     "G.144" -> "G.140";
     "G.152" -> "G.140";
     "G.163" -> "G.140";
     "G.147" -> "G.137";
     "G.160" -> "G.137";
     "G.153" -> "G.149";
     "G.155" -> "G.149";
     "G.149" -> "G.144";
     "G.161" -> "G.160";
     "G.141" -> "G.139";
     "G.163" -> "G.141";
     "G.163" -> "G.155";
     "G.147" -> "G.145";
     "G.161" -> "G.150";
     "G.139" -> "G.138";
     "G.160" -> "G.138";
     "G.153" -> "G.152";
     "G.155" -> "G.152";
     "G.147" -> "G.146";
     "G.152" -> "G.146";
     "G.161" -> "G.153";
     "G.149" -> "G.147";
     "G.153" -> "G.147";
     "G.155" -> "G.147";
   }
