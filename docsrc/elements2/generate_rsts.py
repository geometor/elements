import sys
from pathlib import Path

# Adjust the path to include the 'src' directory
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root / 'src'))

from geometor.elements import build_rst_docs

def main():
    xml_dir = project_root / "resources" / "xml" / "split"
    output_dir = project_root / "docsrc" / "elements2"
    build_rst_docs(xml_dir, output_dir)

if __name__ == "__main__":
    main()
