elements.ingest.cleanup
=======================

.. py:module:: elements.ingest.cleanup


Functions
---------

.. autoapisummary::

   elements.ingest.cleanup.clean_image


Module Contents
---------------

.. py:function:: clean_image(pil_image, white_point=226)

   Applies a linear levels adjustment to the image, setting the white point.
   This effectively removes light gray bleed-through by mapping the 
   white_point (default 226) and everything above it to pure white (255).

   Args:
       pil_image (PIL.Image): The input image.
       white_point (int): The pixel value (0-255) to map to pure white (255).
                          
   Returns:
       PIL.Image: The cleaned image.


