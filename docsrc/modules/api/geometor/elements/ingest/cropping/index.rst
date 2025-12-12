geometor.elements.ingest.cropping
=================================

.. py:module:: geometor.elements.ingest.cropping


Attributes
----------

.. autoapisummary::

   geometor.elements.ingest.cropping.CROPPED_DIR


Functions
---------

.. autoapisummary::

   geometor.elements.ingest.cropping.ensure_dir
   geometor.elements.ingest.cropping.calculate_crop_box
   geometor.elements.ingest.cropping.process_propositions
   geometor.elements.ingest.cropping.run_cropping


Module Contents
---------------

.. py:data:: CROPPED_DIR

.. py:function:: ensure_dir(path)

.. py:function:: calculate_crop_box(img_height, total_lines, start_line=0, end_line=None)

   Calculates the crop box based on line indices.
   Assumes linear distribution of lines within the text area.


.. py:function:: process_propositions()

   Automated cropping of propositions based on analysis data.


.. py:function:: run_cropping()

