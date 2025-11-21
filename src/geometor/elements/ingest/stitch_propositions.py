import json
import os
from pathlib import Path
from PIL import Image

# Configuration
HEATH_DIR = Path("resources/heath")
PROPOSITION_INDEX_PATH = HEATH_DIR / "proposition_index.json"
CROPPED_DIR = HEATH_DIR / "propositions"
GRAPHICS_DIR = HEATH_DIR / "graphics"

# Constants
PAGE_WIDTH = 755
CROP_WIDTH = 640

def ensure_dir(path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

def load_json(path):
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return []

def stitch_propositions():
    propositions = load_json(PROPOSITION_INDEX_PATH)
    
    ensure_dir(CROPPED_DIR)
    ensure_dir(GRAPHICS_DIR)
    
    print(f"Stitching {len(propositions)} propositions...")
    
    for prop in propositions:
        prop_id = prop['id']
        # print(f"Processing {prop_id}...")
        
        cropped_segments = []
        
        for page_info in prop['pages']:
            file_rel_path = page_info['file']
            input_path = HEATH_DIR / file_rel_path
            
            if not input_path.exists():
                # Try to find it if the path is slightly off (e.g. duplicate 'resources/heath' prefix)
                # The path in JSON is relative to HEATH_DIR? Let's check.
                # JSON: "resources/heath/volume_I/..." 
                # HEATH_DIR is "resources/heath".
                # So HEATH_DIR / file_rel_path would be "resources/heath/resources/heath/..." -> Wrong.
                
                # The scan_propositions script wrote full relative paths from project root (e.g. "resources/heath/...")
                # We should resolve relative to PROJECT ROOT, not HEATH_DIR if it starts with "resources/heath"
                
                project_root = Path(".") # Assuming running from project root
                input_path = project_root / file_rel_path
                
                if not input_path.exists():
                    print(f"  Error: Image not found: {file_rel_path}")
                    continue
            
            try:
                img = Image.open(input_path)
                
                start_px = page_info['start_offset_px']
                end_margin_px = page_info['end_offset_px']
                
                # Calculate crop box
                top = start_px
                bottom = img.height - end_margin_px
                
                # Horizontal center crop
                # If image width differs from expected, center on actual image width
                img_width = img.width
                left = (img_width - CROP_WIDTH) // 2
                right = left + CROP_WIDTH
                
                # Validate vertical bounds
                if top >= bottom:
                    # This can happen if offsets are too aggressive or page is small
                    # Fallback: take whole page or skip?
                    # If it's a very small sliver, maybe skip.
                    # But usually this implies an error in offset calculation or standard height assumption.
                    # Let's try to salvage if possible, or skip.
                    # print(f"  Warning: Invalid vertical crop for {prop_id} page {page_info['page']} (top {top} >= bottom {bottom}). Skipping page.")
                    continue
                
                # Validate horizontal
                if left < 0: left = 0
                if right > img_width: right = img_width
                
                crop_box = (left, top, right, bottom)
                segment = img.crop(crop_box)
                cropped_segments.append(segment)
                
            except Exception as e:
                print(f"  Error processing image {input_path}: {e}")
        
        if not cropped_segments:
            print(f"  No segments for {prop_id}. Skipping.")
            continue
            
        # Stitch
        total_height = sum(seg.height for seg in cropped_segments)
        max_width = max(seg.width for seg in cropped_segments) # Should be CROP_WIDTH usually
        
        stitched_image = Image.new('RGB', (max_width, total_height), (255, 255, 255))
        
        current_y = 0
        for seg in cropped_segments:
            # Center segment if widths vary (unlikely with fixed crop width but good practice)
            x_offset = (max_width - seg.width) // 2
            stitched_image.paste(seg, (x_offset, current_y))
            current_y += seg.height
            
        # Save Stitched
        output_filename = f"{prop_id}.png"
        stitched_image.save(CROPPED_DIR / output_filename)
        
        # Extract Graphic (if defined)
        if 'graphics' in prop and prop['graphics']:
            # Use the first graphic entry (assuming one per prop for now)
            g_info = prop['graphics'][0]
            gx = g_info.get('x_offset')
            gy = g_info.get('y_offset')
            g_box = g_info.get('crop_box') # [width, height]
            
            if gx is not None and gy is not None and g_box:
                gw, gh = g_box
                
                # Graphic coordinates are relative to the stitched image?
                # The manual tool likely worked on the stitched image or the first page?
                # Usually relative to the top-left of the stitched result (or the first page's crop).
                # Let's assume stitched image coordinates.
                
                # Validate bounds
                if gx + gw <= stitched_image.width and gy + gh <= stitched_image.height:
                    graphic_crop = (gx, gy, gx + gw, gy + gh)
                    graphic_img = stitched_image.crop(graphic_crop)
                    graphic_img.save(GRAPHICS_DIR / f"{prop_id}_graphic.png")
                else:
                    # print(f"  Warning: Graphic box out of bounds for {prop_id}")
                    pass

    print(f"Stitching complete. Check {CROPPED_DIR}")

if __name__ == "__main__":
    stitch_propositions()
