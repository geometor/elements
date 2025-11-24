:order: 27
:original_id: I.18
:type: prop
:dependencies: g.25, g.9

.. _g.27:

G.27
====

**Heath ID:** :ref:`I.18`

   In any triangle the greater side subtends the greater angle.

For let ``ABC`` be a triangle having the side ``AC`` greater than ``AB``;

I say that the angle ``ABC`` is also greater than the angle ``BCA``.

For, since ``AC`` is greater than ``AB``, let ``AD`` be made equal to ``AB`` [:ref:`g.9`], and let ``BD`` bejoined.

Then, since the angle ``ADB`` is an exterior angle of the triangle ``BCD``, 

it is greater than the interior and opposite angle ``DCB``. [:ref:`g.25`]

But the angle ``ADB`` is equal to the angle ``ABD``, since the side ``AB`` is equal to ``AD``; therefore the angle ``ABD`` is also greater than the angle ``ACB``; therefore the angle ``ABC`` is much greater than the angle ``ACB``.

Therefore etc.


**Q. E. D.**


Q. E. D.


.. note::


   In the enunciation of this number we have ὑποτείνειν (subtend

   ) used with the simple accusative instead of the more usual ὑπό with accusative. The latter construction is used in the enunciation of :ref:`g.28`, which otherwise only differs from that of :ref:`g.27` in the order of the words. The point to remember in order to distinguish the two is that the datum comes first and the quaesitum second, the datum being in this proposition the greater ``side`` and in the next the greater ``angle``. Thus the enunciations are (:ref:`g.27`) παντὸς τριγώνου ἡ μείζων πλευρὰ τὴν μείζονα γωνίαν ὑποτείνει and (:ref:`g.28`) παντὸς τριγώνου ὑπὸ τὴν μείζονα γωνίαν ἡ μείζων πλευρὰ ὑποτείνει. In order to keep the proper order in English we must use the passive of the verb in :ref:`g.28`. Aristotle quotes the result of :ref:`g.28`, using the exact wording, ὑπὸ γὰρ τὴν μείζω γωνίαν ὑποτείνει (Meteorologica III. 5, 376 a 12).


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "G.16" [label="G.16", URL="/elements2/g.16/", target="_top"];
     "G.4" [label="G.4", style="rounded,filled", fillcolor=orange, URL="/elements2/g.4/", target="_top"];
     "G.17" [label="G.17", URL="/elements2/g.17/", target="_top"];
     "G.24" [label="G.24", URL="/elements2/g.24/", target="_top"];
     "G.21" [label="G.21", URL="/elements2/g.21/", target="_top"];
     "G.14" [label="G.14", URL="/elements2/g.14/", target="_top"];
     "G.9" [label="G.9", URL="/elements2/g.9/", target="_top"];
     "G.2" [label="G.2", style="rounded,filled", fillcolor=orange, URL="/elements2/g.2/", target="_top"];
     "G.27" [label="G.27", style="rounded,filled", fillcolor=lightblue, URL="/elements2/g.27/", target="_top"];
     "G.6" [label="G.6", style="rounded,filled", fillcolor=orange, URL="/elements2/g.6/", target="_top"];
     "G.19" [label="G.19", URL="/elements2/g.19/", target="_top"];
     "G.15" [label="G.15", URL="/elements2/g.15/", target="_top"];
     "G.25" [label="G.25", URL="/elements2/g.25/", target="_top"];
     "G.5" [label="G.5", URL="/elements2/g.5/", target="_top"];
     "G.8" [label="G.8", URL="/elements2/g.8/", target="_top"];
     "G.1" [label="G.1", style="rounded,filled", fillcolor=orange, URL="/elements2/g.1/", target="_top"];
     "G.7" [label="G.7", style="rounded,filled", fillcolor=orange, URL="/elements2/g.7/", target="_top"];
     "G.22" [label="G.22", style="rounded,filled", fillcolor=orange, URL="/elements2/g.22/", target="_top"];
     "G.18" [label="G.18", style="rounded,filled", fillcolor=orange, URL="/elements2/g.18/", target="_top"];
     "G.11" [label="G.11", URL="/elements2/g.11/", target="_top"];
     "G.10" [label="G.10", style="rounded,filled", fillcolor=orange, URL="/elements2/g.10/", target="_top"];
     "G.12" [label="G.12", URL="/elements2/g.12/", target="_top"];
     "G.3" [label="G.3", style="rounded,filled", fillcolor=orange, URL="/elements2/g.3/", target="_top"];
     "G.17" -> "G.16";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.25" -> "G.17";
     "G.25" -> "G.24";
     "G.24" -> "G.21";
     "G.15" -> "G.14";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.27" -> "G.9";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.21" -> "G.19";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.27" -> "G.25";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.9" -> "G.8";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.24" -> "G.22";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.11" -> "G.10";
     "G.14" -> "G.12";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
   }



Required for
------------

:ref:`g.28`, :ref:`g.30`, :ref:`g.31`, :ref:`g.32`, :ref:`g.34`, :ref:`g.35`, :ref:`g.88`, :ref:`g.90`, :ref:`g.94`, :ref:`g.95`, :ref:`g.98`, :ref:`g.99`, :ref:`g.77`, :ref:`g.113`, :ref:`g.114`, :ref:`g.115`, :ref:`g.117`, :ref:`g.118`, :ref:`g.82`, :ref:`g.83`, :ref:`g.131`, :ref:`g.132`, :ref:`g.133`, :ref:`g.122`, :ref:`g.120`, :ref:`g.121`, :ref:`g.124`, :ref:`g.128`, :ref:`g.129`, :ref:`g.404`, :ref:`g.429`, :ref:`g.506`, :ref:`g.507`, :ref:`g.508`, :ref:`g.509`, :ref:`g.542`, :ref:`g.543`, :ref:`g.545`, :ref:`g.546`, :ref:`g.547`, :ref:`g.548`, :ref:`g.571`, :ref:`g.578`
