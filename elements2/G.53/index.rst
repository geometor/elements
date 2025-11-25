:order: 53
:original_id: I.40
:type: prop
:dependencies: G.44, G.51, G.1

.. _G.53:

G.53
====

**Heath ID:** :ref:`I.40`

   Equal triangles which are on equal bases and on the same side are also in the same parallels.

Let ``ABC``, ``CDE`` be equal triangles on equal bases ``BC``, ``CE`` and on the same side.

I say that they are also in the same parallels.

For let ``AD`` be joined; I say that ``AD`` is parallel to ``BE``.

For, if not, let ``AF`` be drawn through ``A`` parallel to ``BE`` [:ref:`G.44`], and let ``FE`` be joined.

Therefore the triangle ``ABC`` is equal to the triangle ``FCE``; for they are on equal bases ``BC``, ``CE`` and in the same parallels ``BE``, ``AF``. [:ref:`G.51`]

But the triangle ``ABC`` is equal to the triangle ``DCE``;


.. container:: center

   therefore the triangle ``DCE`` is also equal to the triangle ``FCE``, [:ref:`G.1`] the greater to the less: which is impossible. Therefore ``AF`` is not parallel to ``BE``.


Similarly we can prove that neither is any other straight line except ``AD``;


.. container:: center

   therefore ``AD`` is parallel to ``BE``.


Therefore etc. Q. E. D.]


Dependency Graph
----------------

.. graphviz::

   digraph {
     bgcolor="black";
     node [shape=box, style="rounded,filled", fontname="Helvetica", color="white", fontcolor="white"];
     edge [color="white", fontcolor="white"];
     rankdir="TB";
     "G.33" [label="G.33", fillcolor="#222244", URL="/elements2/G.33/", target="_top"];
     "G.24" [label="G.24", fillcolor="#222244", URL="/elements2/G.24/", target="_top"];
     "G.2" [label="G.2", fillcolor="#224422", URL="/elements2/G.2/", target="_top"];
     "G.19" [label="G.19", fillcolor="#222244", URL="/elements2/G.19/", target="_top"];
     "G.22" [label="G.22", fillcolor="#444422", URL="/elements2/G.22/", target="_top"];
     "G.41" [label="G.41", fillcolor="#444422", URL="/elements2/G.41/", target="_top"];
     "G.37" [label="G.37", fillcolor="#224422", URL="/elements2/G.37/", target="_top"];
     "G.40" [label="G.40", fillcolor="#442222", URL="/elements2/G.40/", target="_top"];
     "G.25" [label="G.25", fillcolor="#222244", URL="/elements2/G.25/", target="_top"];
     "G.21" [label="G.21", fillcolor="#222244", URL="/elements2/G.21/", target="_top"];
     "G.6" [label="G.6", fillcolor="#442222", URL="/elements2/G.6/", target="_top"];
     "G.14" [label="G.14", fillcolor="#222244", URL="/elements2/G.14/", target="_top"];
     "G.36" [label="G.36", fillcolor="#222244", URL="/elements2/G.36/", target="_top"];
     "G.47" [label="G.47", fillcolor="#222244", URL="/elements2/G.47/", target="_top"];
     "G.4" [label="G.4", fillcolor="#444422", URL="/elements2/G.4/", target="_top"];
     "G.49" [label="G.49", fillcolor="#222244", URL="/elements2/G.49/", target="_top"];
     "G.12" [label="G.12", fillcolor="#222244", URL="/elements2/G.12/", target="_top"];
     "G.44" [label="G.44", fillcolor="#222244", URL="/elements2/G.44/", target="_top"];
     "G.9" [label="G.9", fillcolor="#222244", URL="/elements2/G.9/", target="_top"];
     "G.51" [label="G.51", fillcolor="#222244", URL="/elements2/G.51/", target="_top"];
     "G.53" [label="G.53", penwidth=3, color="white", fillcolor="#555555", URL="/elements2/G.53/", target="_top"];
     "G.5" [label="G.5", fillcolor="#222244", URL="/elements2/G.5/", target="_top"];
     "G.38" [label="G.38", fillcolor="#222244", URL="/elements2/G.38/", target="_top"];
     "G.46" [label="G.46", fillcolor="#222244", URL="/elements2/G.46/", target="_top"];
     "G.1" [label="G.1", fillcolor="#442222", URL="/elements2/G.1/", target="_top"];
     "G.8" [label="G.8", fillcolor="#222244", URL="/elements2/G.8/", target="_top"];
     "G.7" [label="G.7", fillcolor="#444422", URL="/elements2/G.7/", target="_top"];
     "G.17" [label="G.17", fillcolor="#222244", URL="/elements2/G.17/", target="_top"];
     "G.42" [label="G.42", fillcolor="#222244", URL="/elements2/G.42/", target="_top"];
     "G.16" [label="G.16", fillcolor="#222244", URL="/elements2/G.16/", target="_top"];
     "G.11" [label="G.11", fillcolor="#222244", URL="/elements2/G.11/", target="_top"];
     "G.10" [label="G.10", fillcolor="#442222", URL="/elements2/G.10/", target="_top"];
     "G.15" [label="G.15", fillcolor="#222244", URL="/elements2/G.15/", target="_top"];
     "G.18" [label="G.18", fillcolor="#224422", URL="/elements2/G.18/", target="_top"];
     "G.3" [label="G.3", fillcolor="#444422", URL="/elements2/G.3/", target="_top"];
     "G.48" [label="G.48", fillcolor="#222244", URL="/elements2/G.48/", target="_top"];
     "G.44" -> "G.33";
     "G.25" -> "G.24";
     "G.42" -> "G.24";
     "G.5" -> "G.2";
     "G.9" -> "G.2";
     "G.21" -> "G.19";
     "G.24" -> "G.22";
     "G.42" -> "G.41";
     "G.38" -> "G.37";
     "G.42" -> "G.40";
     "G.47" -> "G.40";
     "G.48" -> "G.40";
     "G.36" -> "G.25";
     "G.38" -> "G.25";
     "G.24" -> "G.21";
     "G.42" -> "G.21";
     "G.8" -> "G.6";
     "G.24" -> "G.6";
     "G.48" -> "G.6";
     "G.15" -> "G.14";
     "G.47" -> "G.36";
     "G.48" -> "G.47";
     "G.49" -> "G.47";
     "G.51" -> "G.47";
     "G.5" -> "G.4";
     "G.8" -> "G.4";
     "G.9" -> "G.4";
     "G.51" -> "G.49";
     "G.14" -> "G.12";
     "G.51" -> "G.44";
     "G.53" -> "G.44";
     "G.12" -> "G.9";
     "G.16" -> "G.9";
     "G.19" -> "G.9";
     "G.25" -> "G.9";
     "G.53" -> "G.51";
     "G.8" -> "G.5";
     "G.17" -> "G.5";
     "G.19" -> "G.5";
     "G.44" -> "G.38";
     "G.46" -> "G.38";
     "G.49" -> "G.46";
     "G.5" -> "G.1";
     "G.8" -> "G.1";
     "G.9" -> "G.1";
     "G.24" -> "G.1";
     "G.42" -> "G.1";
     "G.48" -> "G.1";
     "G.49" -> "G.1";
     "G.53" -> "G.1";
     "G.9" -> "G.8";
     "G.8" -> "G.7";
     "G.12" -> "G.7";
     "G.25" -> "G.7";
     "G.25" -> "G.17";
     "G.46" -> "G.42";
     "G.47" -> "G.42";
     "G.48" -> "G.42";
     "G.17" -> "G.16";
     "G.12" -> "G.11";
     "G.17" -> "G.11";
     "G.25" -> "G.11";
     "G.36" -> "G.11";
     "G.46" -> "G.11";
     "G.47" -> "G.11";
     "G.48" -> "G.11";
     "G.11" -> "G.10";
     "G.16" -> "G.15";
     "G.19" -> "G.15";
     "G.33" -> "G.15";
     "G.19" -> "G.18";
     "G.21" -> "G.18";
     "G.5" -> "G.3";
     "G.8" -> "G.3";
     "G.12" -> "G.3";
     "G.25" -> "G.3";
     "G.49" -> "G.48";
   }
