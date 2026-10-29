from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from photon_platform.publish.global_conf import *
import geometor.elements as module

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "elements"
repo_name = "elements"

setup_globals(org, org_name, repo, repo_name)

html_theme = "foundation"

