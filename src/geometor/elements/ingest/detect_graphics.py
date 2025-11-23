import json
import os
import argparse
from pathlib import Path
import time
from PIL import Image
import google.generativeai as genai

# Configuration
HEATH_DIR = Path("resources/heath")
PROPOSITIONS_DIR = HEATH_DIR / "propositions"
API_KEY_ENV = "GOOGLE_API_KEY"

def load_json(path):
    if path.exists():
        with open(path, 'r') as f:
            return json.load(f)
    return []

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def detect_graphic(model_instance, image_path):
    """
    Uses Gemini Flash to detect the bounding box of the geometric diagram.
    Returns a list of graphic objects as expected by the index schema:
    [
      {
        "x_offset": int,
        "y_offset": int,
        "crop_box": [width, height]
      }
    ]
    """
    try:
        img = Image.open(image_path)
        
        prompt = """
        Identify the bounding box of the geometric diagram in this image.
        The image contains text and a diagram. Ignore the text.
        Return a JSON object with the keys "ymin", "xmin", "ymax", "xmax" representing the pixel coordinates of the bounding box.
        Ensure the coordinates are integers.
        Example: {"ymin": 100, "xmin": 200, "ymax": 500, "xmax": 600}
        """
        
        response = model_instance.generate_content([prompt, img])
        
        # Parse response
        try:
            # Clean up potential markdown code blocks
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.endswith("```"):
                text = text[:-3]
            
            bbox = json.loads(text)
            
            ymin = int(bbox.get("ymin", 0))
            xmin = int(bbox.get("xmin", 0))
            ymax = int(bbox.get("ymax", 0))
            xmax = int(bbox.get("xmax", 0))
            
            # Validate
            if xmax <= xmin or ymax <= ymin:
                print(f"Invalid bbox detected: {bbox}")
                return None
                
            width = xmax - xmin
            height = ymax - ymin
            
            # Add a small padding (optional, maybe 5-10 pixels)
            padding = 0
            
            return [{
                "x_offset": max(0, xmin - padding),
                "y_offset": max(0, ymin - padding),
                "crop_box": [width + 2*padding, height + 2*padding]
            }]
            
        except json.JSONDecodeError:
            print(f"Failed to parse JSON from model response: {response.text}")
            return None
            
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def process_book(volume, book_slug, book_roman, model_name, model_instance, dry_run=False):
    book_dir = HEATH_DIR / f"volume_{volume}" / book_slug
    index_path = book_dir / "propositions" / "index.json"
    
    if not index_path.exists():
        print(f"No index found at {index_path}")
        return

    propositions = load_json(index_path)
    updated_count = 0
    
    print(f"Processing {book_slug} ({len(propositions)} propositions) using model {model_name}...")
    
    # For a single test, we will only process I.1
    for prop in propositions:
        if prop['id'] == 'I.1': # Only process I.1 for the test
            prop_id = prop['id']
            image_path = PROPOSITIONS_DIR / f"{prop_id}.png"
            
            if not image_path.exists():
                print(f"  Image not found: {image_path}")
                continue
                
            print(f"  Scanning {prop_id} using {model_name}... ", end="", flush=True)
            
            # Call API
            graphics = detect_graphic(model_instance, image_path)
            
            if graphics:
                print(f" Found: {graphics[0]}")
                if not dry_run: # Only update if not dry run
                    prop['graphics'] = graphics
                    updated_count += 1
                # Rate limiting to be safe (free tier limitations)
                time.sleep(4) 
            else:
                print(" No graphic detected or error.")
            break # Exit after processing I.1

    if not dry_run and updated_count > 0:
        save_json(index_path, propositions)
        print(f"Updated {index_path} with {updated_count} new graphic locations.")
    elif dry_run:
        print(f"Dry run: would update {updated_count} propositions for {prop_id}.")
    else:
        print("No updates made.")


def main():
    parser = argparse.ArgumentParser(description="Detect graphics in proposition images using Gemini Flash.")
    parser.add_argument("--volume", "-v", type=str, default="I", help="Volume key (e.g., I)")
    parser.add_argument("--book", "-b", type=str, default="book_i", help="Book directory name (e.g., book_i)")
    parser.add_argument("--roman", "-r", type=str, default="I", help="Book Roman numeral (e.g., I)")
    parser.add_argument("--model", "-m", type=str, default="gemini-1.5-flash", help="Gemini model name (e.g., gemini-1.5-flash)")
    parser.add_argument("--dry-run", action="store_true", help="Do not save changes to index.json")
    
    args = parser.parse_args()
    
    api_key = os.environ.get(API_KEY_ENV)
    if not api_key:
        print(f"Error: {API_KEY_ENV} environment variable not set.")
        return
        
    genai.configure(api_key=api_key)
    model_instance = genai.GenerativeModel(args.model)
    process_book(args.volume, args.book, args.roman, args.model, model_instance, args.dry_run)

if __name__ == "__main__":
    main()
