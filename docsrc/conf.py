from photon_platform.publish.global_conf import *
import geometor.elements as module

version = module.__version__

org = 'geometor'
org_name = 'GEOMETOR'

repo = 'elements'
repo_name = 'elements'

setup_globals(org, org_name, repo, repo_name)

html_theme = "foundation"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sympy': ('https://docs.sympy.org/latest', None),
    'euclid': ('https://geometor.github.io/euclid', None),
}
