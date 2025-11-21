elements.ingest.organization
============================

.. py:module:: elements.ingest.organization


Functions
---------

.. autoapisummary::

   elements.ingest.organization.ensure_dir
   elements.ingest.organization.get_max_page
   elements.ingest.organization.assign_ranges
   elements.ingest.organization.run_organization


Module Contents
---------------

.. py:function:: ensure_dir(path)

.. py:function:: get_max_page(pages)

.. py:function:: assign_ranges(toc_entries, start_page, end_page, parent_path, assignments)

   Recursive function to assign page ranges to paths.
   assignments: dict mapping page_num -> path


.. py:function:: run_organization()

