import xml.etree.ElementTree as ET
from pathlib import Path

def _convert_element_to_rst(element):
    if element is None:
        return ""

    parts = []
    if element.text:
        parts.append(element.text)

    for child in element:
        if child.tag == 'emph':
            parts.append(f"*{''.join(child.itertext()).strip()}*")
        elif child.tag == 'ref':
            target = child.get('target')
            link_text = ''.join(child.itertext()).strip()
            parts.append(f":ref:`{link_text} <{target}>`")
        elif child.tag == 'hi':
            parts.append(f"{''.join(child.itertext()).strip()}")
        else:
            parts.append(''.join(child.itertext()).strip())
        
        if child.tail:
            parts.append(child.tail)

    return ''.join(parts).strip().replace('\n', ' ')

def parse_element_xml(file_path: Path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    element_id = root.get('id')
    element_type = root.get('type')
    element_number = root.get('n')
    
    head = root.find('head').text if root.find('head') is not None else ''
    
    enunciation_p = root.find(".//div4[@type='Enunc']/p")
    enunciation = _convert_element_to_rst(enunciation_p)

    proof_div = root.find(".//div4[@type='Proof']")
    proof_paragraphs = []
    if proof_div is not None:
        for p in proof_div.findall('p'):
            proof_paragraphs.append(_convert_element_to_rst(p))
    
    proof = "\n\n".join(proof_paragraphs)

    qed_p = root.find(".//div4[@type='QED']/p")
    qed = _convert_element_to_rst(qed_p)

    return {
        'id': element_id,
        'type': element_type,
        'number': element_number,
        'head': head,
        'enunciation': enunciation,
        'proof': proof,
        'qed': qed,
    }
