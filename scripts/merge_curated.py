"""Merge per-proposition curated.json files into CURATED_PROPOSITIONS in pseudocode.py."""

import json
import pathlib
import re


def main() -> None:
    p = pathlib.Path("src/geometor/elements/pseudocode.py")
    txt = p.read_text(encoding="utf-8")
    lines = []
    merged_keys = []
    for cpath in sorted(pathlib.Path("resources/videos").glob("book_*/*/curated.json")):
        raw = cpath.read_text(encoding="utf-8")
        cleaned = re.sub(r'\\{2,}(?= )', r'\\\\', raw)
        cleaned = re.sub(r'(?<!\\)\\(?![/\"\\bfnrtu])', r'\\\\', cleaned)
        if cleaned != raw:
            cpath.write_text(cleaned, encoding="utf-8")
        cj = json.loads(cleaned)
        for k, v in cj.items():
            if f'    "{k}": {{' in txt:
                continue
            merged_keys.append(k)
            lines.append(f"    {json.dumps(k)}: {{")
            lines.append(f'        "subtype": {json.dumps(v["subtype"])},')
            lines.append(f'        "args": {json.dumps(v.get("args", []), ensure_ascii=False)},')
            lines.append(f'        "returns": {json.dumps(v.get("returns", []), ensure_ascii=False)},')
            lines.append(f'        "given": {json.dumps(v.get("given", ""), ensure_ascii=False)},')
            lines.append(f'        "contract": {json.dumps(v.get("contract", ""), ensure_ascii=False)},')
            lines.append('        "steps": [')
            for st in v.get("steps", []):
                lines.append(
                    f"            ({json.dumps(st[0])}, {json.dumps(st[1])}, {json.dumps(st[2], ensure_ascii=False)}),"
                )
            lines.append("        ],")
            lines.append("    },")

    if not lines:
        print("All propositions already merged.")
        return

    block = "\n".join(lines)
    marker = "}\n\n\ndef _render_curated_proposition("
    assert marker in txt, "Marker not found in pseudocode.py"
    p.write_text(txt.replace(marker, block + "\n" + marker, 1), encoding="utf-8")
    print(f"Merged {len(merged_keys)} propositions ({', '.join(merged_keys)}) into pseudocode.py")


if __name__ == "__main__":
    main()
