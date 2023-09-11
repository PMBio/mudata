"""Multimodal omics analysis framework"""

from ._core.mudata import MuData
from ._core import utils
from ._core.to_ import to_anndata, to_mudata
from ._core.io import *
from ._core.config import set_options

__version__ = "0.3.0"
__anndataversion__ = "0.1.0"
__mudataversion__ = "0.1.0"
