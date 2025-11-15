import xml.etree.ElementTree as ET
import os
import re
from pathlib import Path
from xml.sax.saxutils import escape

ROMAN_NUMERALS = {
    '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V',
    '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX', '10': 'X',
    '11': 'XI', '12': 'XII', '13': 'XIII'
}

SECTION_TYPE_MAP = {
    'Def': 'def',
    'Post': 'post',
    'CN': 'cn',
    'Prop': 'prop'
}

def convert_inline_xml_to_rst(element):
    if element is None:
        return ""

    if element.tag == 'term':
        return f" **{''.join(element.itertext()).strip()}** "

    parts = []
    if element.text:
        parts.append(element.text)

    for child in element:
        if child.tag == 'emph':
            parts.append(f" ``{''.join(child.itertext()).strip()}`` ")
        elif child.tag == 'ref':
            target = child.get('target')
            if target:
                target_parts = target.split('.')
                canonical_ref = None # Initialize as None
                if len(target_parts) >= 3 and target_parts[0] == 'elem':
                    book_num_str = target_parts[1]
                    book_num_roman = ROMAN_NUMERALS.get(book_num_str)
                    
                    if book_num_roman:
                        if len(target_parts) == 5 and target_parts[2] == 'c' and target_parts[3] == 'n':
                            section_type_canonical = 'cn'
                            item_num = target_parts[4]
                            canonical_ref = f"{book_num_roman}.{section_type_canonical}.{item_num}"
                        elif len(target_parts) == 4:
                            section_type_str = target_parts[2]
                            item_num = target_parts[3]
                            section_type_canonical = SECTION_TYPE_MAP.get(section_type_str.capitalize())
                            if section_type_canonical:
                                canonical_ref = f"{book_num_roman}.{section_type_canonical}.{item_num}"
                        elif len(target_parts) == 3:
                            item_num = target_parts[2]
                            if book_num_roman:
                                canonical_ref = f"{book_num_roman}.{item_num}"
                
                # If a canonical ref was successfully created, use it. Otherwise, use the original target.
                ref_link = canonical_ref if canonical_ref else target
                parts.append(f" :ref:`{ref_link}` ")
            else:
                # Fallback for refs with no target. Try to parse inner text.
                link_text = ''.join(child.itertext()).strip()
                # Example inner text: "C.N. 1" or "Post. 3"
                temp_split_parts = re.split(r'[\s.]+', link_text) # Use a temporary variable
                canonical_ref = None
                
                # This logic assumes the book number is implicitly the current book.
                # This is a limitation, but better than no link.
                # We don't have access to the current book number here, 
                # so we can't construct a full canonical ref.
                # For now, we will just bold the text as a clear indicator.
                # A more advanced solution would require passing the book context into this function.
                
                # Attempt to find a pattern like C.N. 1, Def. 15, etc.
                if len(temp_split_parts) >= 2:
                    # A very simplified heuristic to guess the ref type
                    ref_type_guess = temp_split_parts[0].lower()
                    ref_num = temp_split_parts[-1]
                    # This is not robust enough to build a link, so we bold it.
                    # A future improvement would be to pass book context here.
                    canonical_ref = f"**{link_text}**" # Revert to bolding as a safe fallback
                else:
                    canonical_ref = f"**{link_text}**"

                parts.append(f" {canonical_ref} ")
        elif child.tag == 'term':
            parts.append(f" **{''.join(child.itertext()).strip()}** ")
        elif child.tag == 'hi':
            # Recursively convert content within <hi> tags
            hi_content = convert_inline_xml_to_rst(child)
            parts.append(f" {hi_content.strip()} ")
        elif child.tag == 'lb':
            parts.append("\n") # Proper newline for inline break
        elif child.tag == 'figure':
            # Block-level directives are handled in the main parsing loop
            pass
        else:
            # For any other tag, just get its text content with padding
            parts.append(f" {''.join(child.itertext()).strip()} ")

        # Process the text that comes after the child tag
        if child.tail:
            parts.append(child.tail)

    # Join all parts and normalize whitespace to single spaces,
    # but preserve intentional newlines from <lb> tags.
    full_text = "".join(parts)
    # Split by newlines, normalize spaces in each line, then rejoin.
    lines = full_text.split('\n')
    cleaned_lines = [re.sub(r'\s+', ' ', line).strip() for line in lines]
    return "\n".join(cleaned_lines)

def parse_book_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    book_data = {
        "book_number_roman": None,
        "book_number_arabic": None,
        "sections": []
    }

    div1 = root.find(".//div1[@type='book']")
    if div1 is not None:
        book_data["book_number_arabic"] = div1.attrib.get("n")
        book_data["book_number_roman"] = ROMAN_NUMERALS.get(book_data["book_number_arabic"])
        
        entry_number = 0 # Initialize entry_number here
        for div2 in div1.findall(".//div2"):
            section_type_raw = div2.attrib.get("n")
            section_type_canonical = SECTION_TYPE_MAP.get(section_type_raw)
            section_head = div2.find("./head")
            section_title = section_head.text if section_head is not None else section_type_raw

            section_data = {
                "type_raw": section_type_raw,
                "type_canonical": section_type_canonical,
                "title": section_title,
                "entries": []
            }

            for div3 in div2.findall(".//div3"):
                entry_number += 1 # Increment entry_number here
                entry_id = div3.attrib.get("id")
                entry_n = div3.attrib.get("n")
                entry_head = div3.find("./head")
                entry_title = entry_head.text if entry_head is not None else entry_id

                # Generate canonical reference for the entry
                canonical_ref = None
                folder_name = None
                # entry_title will be set to canonical_ref later

                if entry_id:
                    parts = entry_id.split('.')
                    book_num_roman = ROMAN_NUMERALS.get(parts[1])

                    if book_num_roman:
                        if len(parts) == 5 and parts[2] == 'c' and parts[3] == 'n':
                            item_num = parts[4]
                            canonical_ref = f"{book_num_roman}.cn.{item_num}"
                            folder_name = f"cn.{item_num}"
                        elif len(parts) == 4:
                            section_type = SECTION_TYPE_MAP.get(parts[2].capitalize())
                            item_num = parts[3]
                            if section_type:
                                canonical_ref = f"{book_num_roman}.{section_type}.{item_num}"
                                folder_name = f"{section_type}.{item_num}"
                        elif len(parts) == 3:
                            item_num = parts[2]
                            canonical_ref = f"{book_num_roman}.{item_num}"
                            folder_name = item_num
                
                entry_title = canonical_ref if canonical_ref else entry_id # Use canonical_ref as title

                entry_content_rst = []
                
                def format_as_blockquote(text):
                    if not text:
                        return ""
                    lines = text.strip().split('\n')
                    indented_lines = [f"   {line}" for line in lines]
                    return "\n".join(indented_lines)

                # Handle Enunciation: either from div4 or the first p tag
                enunc_div = div3.find("./div4[@type='Enunc']")
                if enunc_div is not None:
                    enunc_p = enunc_div.find('p')
                    if enunc_p is not None:
                        enunc_text = convert_inline_xml_to_rst(enunc_p)
                        entry_content_rst.append(format_as_blockquote(enunc_text))
                else:
                    # If no Enunc div4, treat the first p as enunciation
                    first_p = div3.find('p')
                    if first_p is not None:
                        enunc_text = convert_inline_xml_to_rst(first_p)
                        entry_content_rst.append(format_as_blockquote(enunc_text))
                        # To avoid processing it again, we can remove it or set a flag.
                        # For simplicity, we'll just be careful in the loop below.
                
                # Process remaining elements
                is_first_p = True
                for child in div3:
                    if child.tag == 'head':
                        continue

                    # Skip the enunciation div4 if it exists
                    if child.tag == 'div4' and child.attrib.get('type') == 'Enunc':
                        continue
                    
                    # Skip the first p if it was used as enunciation
                    if child.tag == 'p' and is_first_p and enunc_div is None:
                        is_first_p = False
                        continue
                    is_first_p = False

                    if child.tag == 'div4':
                        div4_type = child.attrib.get('type')
                        if div4_type == 'Proof':
                            entry_content_rst.append("\n**Proof.**\n")
                        elif div4_type == 'QED':
                            entry_content_rst.append("\n**Q. E. D.**\n")
                        
                        # Process content within div4
                        div4_inner_content = []
                        for grand_child in child:
                            if grand_child.tag == 'p':
                                inline_rst = convert_inline_xml_to_rst(grand_child)
                                if inline_rst:
                                    div4_inner_content.append(inline_rst)
                            elif grand_child.tag == 'figure':
                                div4_inner_content.append("\n.. figure:: /_images/placeholder.png\n   :alt: Figure placeholder\n")
                            elif grand_child.tag == 'hi' and grand_child.attrib.get('rend') == 'center':
                                content = ''.join(grand_child.itertext()).strip()
                                if content:
                                    div4_inner_content.append(f"\n.. container:: center\n\n   {content}\n")
                            else:
                                inline_rst = convert_inline_xml_to_rst(grand_child)
                                if inline_rst:
                                    div4_inner_content.append(inline_rst)
                        
                        if div4_inner_content:
                            entry_content_rst.append("\n\n".join(div4_inner_content))

                    elif child.tag == 'p':
                        paragraph_rst_blocks = []
                        current_inline_parts = []

                        def flush_inline_parts():
                            nonlocal current_inline_parts
                            if not current_inline_parts:
                                return
                            full_text = "".join(current_inline_parts)
                            lines = full_text.split('\n')
                            cleaned_lines = [re.sub(r'\s+', ' ', line).strip() for line in lines]
                            final_text = "\n".join(line for line in cleaned_lines if line)
                            if final_text:
                                paragraph_rst_blocks.append(final_text)
                            current_inline_parts = []

                        if child.text:
                            current_inline_parts.append(child.text)

                        for grand_child in child:
                            if grand_child.tag == 'figure':
                                flush_inline_parts()
                                paragraph_rst_blocks.append("\n.. figure:: /_images/placeholder.png\n   :alt: Figure placeholder\n")
                            elif grand_child.tag == 'hi' and grand_child.attrib.get('rend') == 'center':
                                flush_inline_parts()
                                content = convert_inline_xml_to_rst(grand_child)
                                if content:
                                    indented_content = "\n   ".join(content.splitlines())
                                    paragraph_rst_blocks.append(f"\n.. container:: center\n\n   {indented_content}\n")
                            else:
                                inline_rst = convert_inline_xml_to_rst(grand_child)
                                if inline_rst:
                                    current_inline_parts.append(inline_rst)
                            
                            if grand_child.tail:
                                current_inline_parts.append(grand_child.tail)
                        
                        flush_inline_parts()

                        if paragraph_rst_blocks:
                            entry_content_rst.append("\n\n".join(paragraph_rst_blocks))
                    elif child.tag == 'figure':
                        entry_content_rst.append("\n.. figure:: /_images/placeholder.png\n   :alt: Figure placeholder\n")
                    elif child.tag == 'hi' and child.attrib.get('rend') == 'center':
                        content = ''.join(child.itertext()).strip()
                        if content:
                            entry_content_rst.append(f"\n.. container:: center\n\n   {content}\n")
                    elif child.tag == 'note':
                        entry_content_rst.append(f"\n.. raw:: html\n\n   <!-- Note: {child.attrib.get('n', '')} -->\n")
                    else:
                        inline_rst = convert_inline_xml_to_rst(child)
                        if inline_rst:
                            entry_content_rst.append(inline_rst)



                section_data["entries"].append({
                    "id": entry_id,
                    "n": entry_n,
                    "title": entry_title,
                    "canonical_ref": canonical_ref,
                    "folder_name": folder_name,
                    "content_rst": "\n\n".join(filter(None, entry_content_rst)),
                    "order": entry_n,
                    "number": entry_number,
                })
            book_data["sections"].append(section_data)
    return book_data

def generate_rst_files(book_data, output_dir):
    book_roman = book_data["book_number_roman"]
    book_dir = Path(output_dir) / book_roman
    book_dir.mkdir(parents=True, exist_ok=True)

    # Create book index.rst
    book_index_content = [
        f"Book {book_roman}",
        f"==============\n",
        ".. toctree::",
        "   :maxdepth: 1\n"
    ]
    
    for section in book_data["sections"]:
        for entry in section["entries"]:
            if entry["folder_name"]:
                entry_dir = book_dir / entry["folder_name"]
                entry_dir.mkdir(exist_ok=True)

                # Create entry index.rst
                title = entry['canonical_ref']
                underline = "=" * len(title)
                entry_index_content = [
                    f":order: {entry['order']}",
                    f":number: {entry['number']}\n",
                    f".. _{entry['canonical_ref']}:\n",
                    title,
                    underline + "\n",
                    entry['content_rst']
                ]
                with open(entry_dir / "index.rst", "w") as f:
                    f.write("\n".join(entry_index_content))
                
                book_index_content.append(f"   {entry['folder_name']}/index")

    with open(book_dir / "index.rst", "w") as f:
        f.write("\n".join(book_index_content))
    print(f"Generated RST files for Book {book_roman}")

def main():
    print("RST transformation tool")
    output_dir = "docsrc/elements2"
    
    for i in range(1, 3):
        xml_file_path = f"resources/xml/books/{i:02d}.xml"
        if os.path.exists(xml_file_path):
            book_data = parse_book_xml(xml_file_path)
            generate_rst_files(book_data, output_dir)
        else:
            print(f"Warning: XML file not found at {xml_file_path}")

    # Create the main index.rst for elements2
    main_index_content = [
        ":navigation: header",
        ":order: 2\n",
        "Elements 2.0",
        "============\n",
        ".. toctree::",
        "   :maxdepth: 1\n"
    ]
    for i in range(1, 3):
        book_roman = ROMAN_NUMERALS.get(str(i))
        if book_roman:
            main_index_content.append(f"   {book_roman}/index.rst")
            
    with open(Path(output_dir) / "index.rst", "w") as f:
        f.write("\n".join(main_index_content))
    print("Generated main index.rst for elements2")

if __name__ == "__main__":
    main()
