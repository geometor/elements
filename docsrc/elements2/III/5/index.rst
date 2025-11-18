:order: 5
:number: 113
:type: prop
:tags: circle
:dependencies: I.def.15




.. figure:: III.5.jpg
   :width: 50%

.. _III.5:

III.5
=====

   If two circles cut one another, they will not have the same centre.

For let the circles ``ABC``, ``CDG`` cut one another at the points ``B``, ``C``; I say that they will not have the same centre.

For, if possible, let it be ``E``; let ``EC`` be joined, and let ``EFG`` be drawn through at random.

Then, since the point ``E`` is the centre of the circle ``ABC``,


.. container:: center

   ``EC`` is equal to ``EF``. [:ref:`I.def.15`]


Again, since the point ``E`` is the centre of the circle ``CDG``,


.. container:: center

   ``EC`` is equal to ``EG``.


But ``EC`` was proved equal to ``EF`` also;


.. container:: center

   therefore ``EF`` is also equal to ``EG``, the less to the greater : which is impossible.


Therefore the point ``E`` is not the centre of the circles ``ABC``, ``CDG``.

Therefore etc. Q. E. D.


Dependency Graph
----------------

.. graphviz::

   digraph {
     rankdir="TB";
     node [shape=box, style=rounded];
     "III.5" [style="rounded,filled", fillcolor=lightblue, URL="/elements2/III/5/", target="_top"];
     "I.def.15" [style="rounded,filled", fillcolor=orange, URL="/elements2/I/def.15/", target="_top"];
     "III.5" -> "I.def.15";
   }



Required for
------------

:ref:`III.10`, :ref:`III.24`, :ref:`III.26`, :ref:`III.27`, :ref:`III.28`, :ref:`III.29`, :ref:`III.30`, :ref:`IV.11`, :ref:`IV.12`, :ref:`IV.15`, :ref:`IV.16`, :ref:`VI.33`