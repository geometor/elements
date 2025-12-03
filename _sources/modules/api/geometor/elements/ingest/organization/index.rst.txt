geometor.elements.ingest.organization
=====================================

.. py:module:: geometor.elements.ingest.organization


Functions
---------

.. autoapisummary::

   geometor.elements.ingest.organization.ensure_dir
   geometor.elements.ingest.organization.get_max_page
   geometor.elements.ingest.organization.assign_ranges
   geometor.elements.ingest.organization.run_organization


Module Contents
---------------

.. py:function:: ensure_dir(path)

.. py:function:: get_max_page(pages)

.. py:function:: assign_ranges(toc_entries, start_page, end_page, parent_path, assignments)

   Recursive function to assign page ranges to paths.
   assignments: dict mapping page_num -> path


.. py:function:: run_organization()

