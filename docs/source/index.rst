Say hello to MuData
===================

``MuData`` is a format for annotated multimodal datasets. ``MuData`` is native to Python but provides cross-language functionality via HDF5-based ``.h5mu`` files.


MuData objects as containers
----------------------------

``mudata`` package introduces multimodal data objects (:class:`mudata.MuData` class) allowing Python users to work with increasigly complex datasets efficiently and to build new workflows and computational tools around it.
::
	MuData object with n_obs × n_vars = 10110 × 110101
	 2 modalities
	  atac: 10110 x 100001
	  rna: 10110 x 10100

``MuData`` objects enable multimodal information to be stored & accessed naturally, embrace `AnnData <https://github.com/theislab/anndata>`_ for the individual modalities, and can be serialized to ``.h5mu`` files. :doc:`Learn more about multimodal objects </io/mudata>` as well as :doc:`file formats for storing & sharing them </io/output>`. 

Handling MuData objects
-----------------------

A flagship framework for multimodal omics analysis — ``muon`` — has been built around the ``MuData`` format. Find more information on it `in its documentation <https://muon.readthedocs.io/en/latest/>`_ and `on the tutorials page <https://muon-tutorials.readthedocs.io/en/latest/>`_.


.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Getting started

   notebooks/quickstart_mudata.ipynb
   nuances.rst

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Documentation

   install
   io/input
   io/mudata
   io/output
   api/index
   changelog

