elements.ingest.compare_models
==============================

.. py:module:: elements.ingest.compare_models


Attributes
----------

.. autoapisummary::

   elements.ingest.compare_models.HEATH_DIR
   elements.ingest.compare_models.PROPOSITIONS_DIR
   elements.ingest.compare_models.INDEX_PATH
   elements.ingest.compare_models.API_KEY_ENV
   elements.ingest.compare_models.REPORT_FILE
   elements.ingest.compare_models.MODELS_TO_TEST
   elements.ingest.compare_models.TARGET_MODELS
   elements.ingest.compare_models.TARGET_PROPS
   elements.ingest.compare_models.api_key


Functions
---------

.. autoapisummary::

   elements.ingest.compare_models.load_json
   elements.ingest.compare_models.detect_graphic_with_usage
   elements.ingest.compare_models.run_comparison


Module Contents
---------------

.. py:data:: HEATH_DIR

.. py:data:: PROPOSITIONS_DIR

.. py:data:: INDEX_PATH

.. py:data:: API_KEY_ENV
   :value: 'GOOGLE_API_KEY'


.. py:data:: REPORT_FILE
   :value: 'comparison_report.txt'


.. py:data:: MODELS_TO_TEST
   :value: ['gemini-flash-latest', 'gemini-2.5-pro']


.. py:data:: TARGET_MODELS
   :value: ['gemini-flash-latest', 'gemini-2.5-pro']


.. py:data:: TARGET_PROPS
   :value: ['I.1', 'I.2', 'I.3']


.. py:function:: load_json(path)

.. py:function:: detect_graphic_with_usage(model_name, image_path)

.. py:function:: run_comparison()

.. py:data:: api_key

