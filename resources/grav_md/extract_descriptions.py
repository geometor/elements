import os
import re
import json

def extract_info():
    root_dir = "."
    books = []
    
    # regex for book directories
    book_dir_pattern = re.compile(r'^\d+\.book-\d+$')
    
    # List directories and sort them
    dirs = sorted([d for d in os.listdir(root_dir) if os.path.isdir(d) and book_dir_pattern.match(d)])
    
    for d in dirs:
        article_path = os.path.join(root_dir, d, "article.md")
        if os.path.exists(article_path):
            with open(article_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract frontmatter and body
            # Assuming file starts with ---
            parts = re.split(r'^---$', content, maxsplit=2, flags=re.MULTILINE)
            
            if len(parts) >= 3:
                frontmatter = parts[1]
                body = parts[2]
                
                # Extract subtitle from frontmatter
                subtitle = ""
                subtitle_match = re.search(r'^subtitle:\s*(.*)$', frontmatter, re.MULTILINE)
                if subtitle_match:
                    subtitle = subtitle_match.group(1).strip()
                
                # Clean body
                # Remove '===' separator and surrounding whitespace
                description = body.replace('===', '').strip()
                
                books.append({
                    "folder": d,
                    "subtitle": subtitle,
                    "description": description
                })
            else:
                print(f"Warning: Could not parse format of {article_path}")
    
    with open("book_descriptions.json", "w", encoding='utf-8') as f:
        json.dump(books, f, indent=4)
    
    print(f"Extracted descriptions for {len(books)} books to book_descriptions.json")

if __name__ == "__main__":
    extract_info()
