import json
import glob
import os
import yaml

def extract_metadata():
    """
    Extracts metadata from book-level article.md files and saves it to a JSON file.
    The content of these files is used to create an intro.rst file.
    """
    metadata = {}
    files = glob.glob('resources/grav_md/*/article.md')

    # Sort files to ensure consistent order
    files.sort()

    intro_content = ""

    for file_path in files:
        with open(file_path, 'r') as f:
            content = f.read()
            
            if content.startswith('---'):
                parts = content.split('---', 2)
                if len(parts) > 2:
                    try:
                        front_matter = yaml.safe_load(parts[1])
                        # Use a key relative to the resources/grav_md directory
                        key = os.path.relpath(file_path, 'resources/grav_md')
                        metadata[key] = front_matter
                        
                        # The rest of the file is the content for the intro
                        intro_content += f'.. _{front_matter.get("title", key)}:\n\n'
                        intro_content += f'{front_matter.get("title", key)}\n'
                        intro_content += "=" * len(front_matter.get('title', key)) + "\n"
                        if front_matter.get('subtitle'):
                            intro_content += f'{front_matter.get("subtitle")}\n'
                            intro_content += "-" * len(front_matter.get('subtitle')) + "\n"
                        intro_content += parts[2].strip().replace('===', '')
                        intro_content += "\n\n"

                    except yaml.YAMLError as e:
                        print(f"Error parsing YAML in {file_path}: {e}")

    with open('resources/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)

    # Create intro.rst
    with open('docsrc/intro.rst', 'w') as f:
        f.write(".. _intro:\n\n")
        f.write("Introduction\n")
        f.write("============\n\n")
        f.write(intro_content)


if __name__ == '__main__':
    extract_metadata()