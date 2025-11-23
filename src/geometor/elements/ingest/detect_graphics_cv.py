import cv2
import json
import argparse
import numpy as np
from pathlib import Path
import os

# Configuration
HEATH_DIR = Path("resources/heath")
PROPOSITIONS_DIR = HEATH_DIR / "propositions"
INDEX_PATH = HEATH_DIR / "volume_I/book_i/propositions/index.json"

def load_json(path):
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return []

def detect_graphic_cv(image_path, debug=False):
    # Load image
    img = cv2.imread(str(image_path))
    if img is None:
        return {"error": "Could not load image"}
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 1. Binarize (Invert so ink is white, paper is black)
    # Otsu's thresholding
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # 2. Remove Text (Heuristic)
    # We assume text characters are small.
    # We can use connected components analysis.
    
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)
    
    # stats: [x, y, width, height, area]
    
    # We will create a mask of "potential graphic components"
    graphics_mask = np.zeros_like(binary)
    
    # Heuristics for text vs graphic
    # Text characters usually have:
    # - Small height (e.g., < 50 px)
    # - Small width 
    # - Small area
    
    # Diagram parts (like a long line) might have small height OR small width, but usually not both.
    # A circle has large width AND height.
    
    # Let's try filtering out "small" components.
    min_dimension = 40  # If both width and height are smaller than this, it's likely text
    
    # Also, we want to keep the labels (A, B, C) which are near the graphic.
    # This is tricky.
    
    # Alternative approach:
    # 1. Identify the "main" graphic elements (large lines, circles).
    # 2. Create a bounding box around them.
    # 3. Expand that bounding box to include nearby "small" elements (labels).
    
    large_components = []
    for i in range(1, num_labels): # Skip background (0)
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        area = stats[i, cv2.CC_STAT_AREA]
        
        # Criteria for a "Graphic Anchor" (main lines/circles)
        # Must be reasonably large in at least one dimension
        if w > 100 or h > 100: 
            large_components.append(i)
            graphics_mask[labels == i] = 255
            
    # If no large components found, maybe the threshold is too high?
    if not large_components:
        return {"error": "No large graphic components found"}
        
    # Find the bounding box of all large components combined
    points = cv2.findNonZero(graphics_mask)
    if points is None:
         return {"error": "Mask empty"}
         
    rect = cv2.boundingRect(points)
    gx, gy, gw, gh = rect
    
    # 3. Include nearby labels
    # Now we look for small components that are close to this bounding box.
    # Expand the search region
    margin = 50
    search_x = max(0, gx - margin)
    search_y = max(0, gy - margin)
    search_w = gw + 2*margin
    search_h = gh + 2*margin
    search_rect = (search_x, search_y, search_x + search_w, search_y + search_h)
    
    final_mask = graphics_mask.copy()
    
    for i in range(1, num_labels):
        if i in large_components:
            continue
            
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        
        # Center of component
        cx = x + w/2
        cy = y + h/2
        
        # Check if inside the expanded search rect
        if (search_x <= cx <= search_x + search_w) and (search_y <= cy <= search_y + search_h):
            # It's close to the graphic, likely a label
            final_mask[labels == i] = 255
            
    # Recalculate bounding box
    points = cv2.findNonZero(final_mask)
    gx, gy, gw, gh = cv2.boundingRect(points)
    
    if debug:
        # Draw rectangle and save debug image
        debug_img = img.copy()
        cv2.rectangle(debug_img, (gx, gy), (gx + gw, gy + gh), (0, 0, 255), 2)
        debug_path = f"debug_{Path(image_path).name}"
        cv2.imwrite(debug_path, debug_img)
        print(f"Saved debug image to {debug_path}")

    return {
        "x_offset": int(gx),
        "y_offset": int(gy),
        "crop_box": [int(gw), int(gh)]
    }

def run_test():
    print("Running OpenCV Graphic Detection Test")
    propositions = load_json(INDEX_PATH)
    prop_map = {p['id']: p for p in propositions}
    
    target_props = ["I.1", "I.2", "I.3"]
    
    for prop_id in target_props:
        print(f"\nProcessing {prop_id}...")
        prop_data = prop_map.get(prop_id)
        
        # Ground Truth
        gt_graphics = prop_data.get('graphics', [{}])[0]
        print(f"  Ground Truth: {gt_graphics}")
        
        image_path = PROPOSITIONS_DIR / f"{prop_id}.png"
        if not image_path.exists():
            print("  Image not found")
            continue
            
        result = detect_graphic_cv(image_path, debug=True)
        print(f"  CV Detected:  {result}")
        
        if "error" not in result:
            gt_x = gt_graphics.get('x_offset', 0)
            gt_y = gt_graphics.get('y_offset', 0)
            gt_w, gt_h = gt_graphics.get('crop_box', [0, 0])
            
            d_x = result['x_offset'] - gt_x
            d_y = result['y_offset'] - gt_y
            d_w = result['crop_box'][0] - gt_w
            d_h = result['crop_box'][1] - gt_h
            
            print(f"  Diff (CV - GT): x={d_x:+d}, y={d_y:+d}, w={d_w:+d}, h={d_h:+d}")

if __name__ == "__main__":
    run_test()
