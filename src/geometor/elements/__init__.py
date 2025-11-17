"""
tools for modeling and rendering geometric constructions
"""



__author__ = "geometor"
__maintainer__ = "geometor"
__email__ = "github@geometor.com"
__version__ = "0.0.14"
__licence__ = "MIT"

__all__ = [
    "parse_element_xml",
    "generate_rst_from_xml",
    "build_rst_docs",
]

from .xml_parser import parse_element_xml
from .rst_generator import generate_rst_from_xml
from .rst_builder import build_rst_docs
