import xml.etree.ElementTree as ET
import os
import re
import shutil
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

CATEGORIES_KEYWORDS = ['construct', 'describe', 'bisect']
TAGS_KEYWORDS = ['line', 'circle', 'triangle']

def get_taxonomy(enunciation_text):
    categories = []
    tags = []
    
    lower_text = enunciation_text.lower()
    
    for keyword in CATEGORIES_KEYWORDS:
        if keyword in lower_text:
            categories.append(keyword)
            
    for keyword in TAGS_KEYWORDS:
        if keyword in lower_text:
            tags.append(keyword)
            
    return categories, tags

def convert_inline_xml_to_rst(element, is_enunciation=False):
    if element is None:
        return ""

    # Handle non-recursive tags first
    if element.tag == 'ref':
        target = element.get('target')
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
            
            ref_link = canonical_ref if canonical_ref else target
            return f":ref:`{ref_link}`"
        else:
            link_text = ''.join(element.itertext()).strip()
            temp_split_parts = re.split(r'[\s.]+', link_text)
            canonical_ref = f"**{link_text}**"
            return f"{canonical_ref}"
    
    if element.tag == 'lb' or element.tag == 'pb':
        return ""
        
    if element.tag == 'figure':
        return "" # Handled by the p-handler which deals with block-level elements

    # Handle container-like tags recursively
    parts = []
    if element.text:
        parts.append(element.text)

    for child in element:
        parts.append(convert_inline_xml_to_rst(child, is_enunciation))
        if child.tail:
            parts.append(child.tail)
    
    content = "".join(parts)

    # Apply formatting based on the container's tag
    if element.tag == 'emph':
        if is_enunciation:
            return f"{content.strip()}"
        else:
            return f"``{content.strip()}``"
    elif element.tag == 'term':
        return f"**{content.strip()}**"

    # For other tags (like p, hi, div), just return the processed content
    # Final whitespace cleanup is handled by the caller (flush_inline_parts)
    return content

def parse_book_xml(file_path, entry_number_start=0):
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
        
        entry_number = entry_number_start # Initialize entry_number here
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
                enunc_text = ""
                
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
                        enunc_text = convert_inline_xml_to_rst(enunc_p, is_enunciation=True)
                        entry_content_rst.append(format_as_blockquote(enunc_text))
                else:
                    # If no Enunc div4, treat the first p as enunciation
                    first_p = div3.find('p')
                    if first_p is not None:
                        enunc_text = convert_inline_xml_to_rst(first_p, is_enunciation=True)
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
                            pass
                        elif div4_type == 'QED':
                            entry_content_rst.append("\n**Q. E. D.**\n")
                        elif div4_type == 'porism':
                            porism_id = child.attrib.get('id')
                            
                            # Create canonical title like III.1.p.1
                            porism_title = "Porism" # Default
                            if porism_id:
                                parts = porism_id.split('.')
                                if len(parts) == 5:
                                    book_roman = ROMAN_NUMERALS.get(parts[1])
                                    prop_num = parts[2]
                                    p_literal = parts[3]
                                    porism_num = parts[4]
                                    if book_roman:
                                        porism_title = f"{book_roman}.{prop_num}.{p_literal}.{porism_num}"

                            porism_content = []
                            for grand_child in child:
                                if grand_child.tag == 'p':
                                    inline_rst = convert_inline_xml_to_rst(grand_child)
                                    if inline_rst:
                                        porism_content.append(inline_rst)

                            if porism_id and porism_content:
                                entry_content_rst.append(f"\n.. _{porism_id}:\n")
                                entry_content_rst.append(f"**{porism_title}**\n")
                                entry_content_rst.append("\n".join(porism_content))
                            continue

                        
                        # Process content within div4
                        div4_inner_content = []
                        for grand_child in child:
                            if grand_child.tag == 'p':
                                inline_rst = convert_inline_xml_to_rst(grand_child)
                                if inline_rst:
                                    div4_inner_content.append(inline_rst)
                            elif grand_child.tag == 'figure':
                                pass
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
                        pass
                    elif child.tag == 'hi' and child.attrib.get('rend') == 'center':
                        content = ''.join(child.itertext()).strip()
                        if content:
                            entry_content_rst.append(f"\n.. container:: center\n\n   {content}\n")
                    elif child.tag == 'note':
                        note_title = child.attrib.get('n', '')
                        note_content = []
                        if note_title:
                            note_content.append(f"**{note_title}**")

                        for grand_child in child:
                            if grand_child.tag == 'p':
                                inline_rst = convert_inline_xml_to_rst(grand_child)
                                if inline_rst:
                                    note_content.append(inline_rst)
                        
                        if note_content:
                            entry_content_rst.append(f"\n.. note::\n")
                            full_note_content = "\n\n".join(note_content)
                            for line in full_note_content.splitlines():
                                entry_content_rst.append(f"   {line}")
                        entry_content_rst.append("") # Add an empty line after the note
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
                    "type": section_type_canonical,
                    "enunciation": enunc_text,
                })
            book_data["sections"].append(section_data)
    return book_data, entry_number

def generate_rst_files(book_data, output_dir):
    book_roman = book_data["book_number_roman"]
    book_dir = Path(output_dir) / book_roman
    book_dir.mkdir(parents=True, exist_ok=True)

    canonical_images_dir = Path("resources/canonical_images")

    # Create book index.rst
    book_index_content = [
        f":order: {book_data["book_number_arabic"]}",
        ":type: book\n",
        f"Book {book_roman}",
        f"==============\n",
    ]

    entry_types_in_book = set()
    
    for section in book_data["sections"]:
        for entry in section["entries"]:
            if entry["folder_name"]:
                entry_dir = book_dir / entry["folder_name"]
                entry_types_in_book.add(entry['type'])
                entry_dir.mkdir(exist_ok=True)

                # Create entry index.rst
                title = entry['canonical_ref']
                underline = "=" * len(title)

                categories, tags = get_taxonomy(entry['enunciation'])

                entry_index_content = [
                    f":order: {entry['order']}",
                    f":number: {entry['number']}",
                    f":type: {entry['type']}",
                ]
                if categories:
                    entry_index_content.append(f":categories: {', '.join(categories)}")
                if tags:
                    entry_index_content.append(f":tags: {', '.join(tags)}")
                entry_index_content.append('\n')

                # Copy images and add figure directives
                if canonical_images_dir.exists() and entry['canonical_ref']:
                    image_stem = entry['canonical_ref']
                    
                    # Find all images for this entry (including variants like -b)
                    image_files = []
                    # Exact match
                    exact_match = canonical_images_dir / f"{image_stem}.jpg"
                    if exact_match.exists():
                        image_files.append(exact_match)
                    # Variant matches (e.g., I.1-b.jpg)
                    image_files.extend(sorted(canonical_images_dir.glob(f"{image_stem}-*.jpg")))

                    for image_path in image_files:
                        shutil.copy(image_path, entry_dir)
                        entry_index_content.append(f"\n\n.. figure:: {image_path.name}\n   :width: 50%\n")
                
                entry_index_content.extend([
                    f".. _{entry['canonical_ref']}:\n",
                    title,
                    underline + "\n",
                    entry['content_rst']
                ])

                with open(entry_dir / "index.rst", "w") as f:
                    f.write("\n".join(entry_index_content))
                
    # Add collections for each type
    type_titles = {
        'def': 'Definitions',
        'post': 'Postulates',
        'cn': 'Common Notions',
        'prop': 'Propositions'
    }

    for entry_type in sorted(list(entry_types_in_book)):
        if entry_type:
            book_index_content.append(f".. collection::")
            book_index_content.append(f"   :type: {entry_type}")
            book_index_content.append(f"   :title: {type_titles.get(entry_type, entry_type.capitalize())}")
            book_index_content.append(f"   :sort: number\n")

    with open(book_dir / "index.rst", "w") as f:
        f.write("\n".join(book_index_content))
    print(f"Generated RST files for Book {book_roman}")

def main():
    print("RST transformation tool")
    output_dir = "docsrc/elements2"

    # Clean up existing book directories to prevent orphans
    output_path = Path(output_dir)
    if output_path.exists():
        for i in range(1, 7):
            book_roman = ROMAN_NUMERALS.get(str(i))
            if book_roman:
                book_dir = output_path / book_roman
                if book_dir.exists() and book_dir.is_dir():
                    shutil.rmtree(book_dir)
                    print(f"Removed directory: {book_dir}")

    entry_number = 0
    for i in range(1, 7):
        xml_file_path = f"resources/xml/books/{i:02d}.xml"
        if os.path.exists(xml_file_path):
            print(f"Processing {xml_file_path}")
            book_data, entry_number = parse_book_xml(xml_file_path, entry_number)
            generate_rst_files(book_data, output_dir)

        else:
            print(f"Warning: XML file not found at {xml_file_path}")

    # Create the main index.rst for elements2
    main_index_content = [
        ":navigation: header",
        ":order: 2\n",
        "Elements 2.0",
        "============\n",
        ".. collection::",
        "   :type: book",
        "   :title: Books",
        "   :sort: order\n",
    ]
            
    with open(Path(output_dir) / "index.rst", "w") as f:
        f.write("\n".join(main_index_content))
    print("Generated main index.rst for elements2")

if __name__ == "__main__":
    main()
