:order: 27
:original_id: I.18
:type: prop
:dependencies: G.25, G.9
:excerpt: In any triangle the greater side subtends the greater angle.

**Heath ID:** `I.18 <https://geometor.github.io/euclid/I/18/>`_

.. picture:: G.27.png

.. _G.27:

G.27
====

    In any triangle the greater side subtends the greater angle.

For let ``ABC`` be a triangle having the side ``AC`` greater than ``AB``;

I say that the angle ``ABC`` is also greater than the angle ``BCA``.

For, since ``AC`` is greater than ``AB``, let ``AD`` be made equal to ``AB`` [:ref:`G.9`], and let ``BD`` bejoined.

Then, since the angle ``ADB`` is an exterior angle of the triangle ``BCD``, 

it is greater than the interior and opposite angle ``DCB``. [:ref:`G.25`]

But the angle ``ADB`` is equal to the angle ``ABD``, since the side ``AB`` is equal to ``AD``; therefore the angle ``ABD`` is also greater than the angle ``ACB``; therefore the angle ``ABC`` is much greater than the angle ``ACB``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   In the enunciation of this number we have ὑποτείνειν (subtend

   ) used with the simple accusative instead of the more usual ὑπό with accusative. The latter construction is used in the enunciation of :ref:`G.28`, which otherwise only differs from that of :ref:`G.27` in the order of the words. The point to remember in order to distinguish the two is that the datum comes first and the quaesitum second, the datum being in this proposition the greater ``side`` and in the next the greater ``angle``. Thus the enunciations are (:ref:`G.27`) παντὸς τριγώνου ἡ μείζων πλευρὰ τὴν μείζονα γωνίαν ὑποτείνει and (:ref:`G.28`) παντὸς τριγώνου ὑπὸ τὴν μείζονα γωνίαν ἡ μείζων πλευρὰ ὑποτείνει. In order to keep the proper order in English we must use the passive of the verb in :ref:`G.28`. Aristotle quotes the result of :ref:`G.28`, using the exact wording, ὑπὸ γὰρ τὴν μείζω γωνίαν ὑποτείνει (Meteorologica III. 5, 376 a 12).


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.27" [label="G.27", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.27/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.24" -> "G.6";
     "G.8" -> "G.6";
     "G.21" -> "G.19";
     "G.25" -> "G.24";
     "G.24" -> "G.21";
     "G.11" -> "G.10";
     "G.25" -> "G.7";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.17";
     "G.5" -> "G.3";
     "G.25" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.19" -> "G.15";
     "G.16" -> "G.15";
     "G.19" -> "G.5";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.5" -> "G.1";
     "G.24" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.14" -> "G.12";
     "G.24" -> "G.22";
     "G.15" -> "G.14";
     "G.9" -> "G.8";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.16" -> "G.9";
     "G.27" -> "G.9";
     "G.12" -> "G.9";
     "G.27" -> "G.25";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.25" -> "G.11";
     "G.17" -> "G.11";
     "G.12" -> "G.11";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.17" -> "G.16";
   }



Required for
------------

:ref:`G.28`, :ref:`G.30`, :ref:`G.31`, :ref:`G.32`, :ref:`G.34`, :ref:`G.35`
