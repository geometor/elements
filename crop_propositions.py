import os
import json
from PIL import Image

def process_propositions(instructions_file):
    """
    Crops proposition text, stitches multi-page propositions,
    and extracts the graphic from the stitched image.
    """
    if not os.path.exists(instructions_file):
        print(f"Error: Instructions file not found at {instructions_file}")
        return

    try:
        with open(instructions_file, 'r') as f:
            instructions = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {instructions_file}: {e}")
        return

    # Load global settings
    gs = instructions.get("global_settings", {})
    page_width = gs.get("page_width", 755)
    page_header_end = gs.get("page_header_end", 125)
    page_footer_start = gs.get("page_footer_start", 1115)
    crop_width = gs.get("crop_width", 640)

    # Calculate centered horizontal crop coordinates
    left = (page_width - crop_width) // 2
    right = left + crop_width

    # Prepare output directories
    cropped_dir = os.path.join("resources", "cropped")
    graphics_dir = os.path.join("resources", "graphics")
    os.makedirs(cropped_dir, exist_ok=True)
    os.makedirs(graphics_dir, exist_ok=True)

    for prop_key, prop_data in instructions.items():
        if prop_key == "global_settings":
            continue

        cropped_images = []
        prop_pages = prop_data.get("pages", [])

        # Step 1: Crop individual pages
        for page in prop_pages:
            input_filename = page.get("input_file")
            start_offset = page.get("start_offset")
            end_offset = page.get("end_offset")

            if not all([input_filename, start_offset is not None, end_offset is not None]):
                print(f"Skipping malformed page instruction in {prop_key}")
                continue

            input_path = os.path.join("resources", "heath", input_filename)
            if not os.path.exists(input_path):
                print(f"Error: Input file not found at {input_path}. Skipping.")
                continue

            try:
                img = Image.open(input_path)
                upper = page_header_end + start_offset
                lower = page_footer_start - end_offset
                box = (left, max(0, upper), right, min(img.height, lower))

                if box[2] <= box[0] or box[3] <= box[1]:
                    print(f"Warning: Invalid crop box for {input_filename}. Skipping.")
                    continue
                
                cropped_images.append(img.crop(box))
            except Exception as e:
                print(f"An error occurred while cropping {input_filename}: {e}")

        if not cropped_images:
            print(f"No pages cropped for {prop_key}. Skipping.")
            continue

        # Step 2: Stitch cropped pages
        if len(cropped_images) > 1:
            total_height = sum(img.height for img in cropped_images)
            stitched_image = Image.new('RGB', (crop_width, total_height), (255, 255, 255))
            current_y = 0
            for img in cropped_images:
                stitched_image.paste(img, (0, current_y))
                current_y += img.height
        else:
            stitched_image = cropped_images[0]
        
        # Save the final stitched proposition image
        prop_output_path = os.path.join(cropped_dir, f"{prop_key}.png")
        stitched_image.save(prop_output_path)
        print(f"Saved stitched proposition to {prop_output_path}")

        # Step 3: Extract the graphic from the stitched image
        gx = prop_data.get("graphic_x_offset")
        gy = prop_data.get("graphic_y_offset")
        g_box = prop_data.get("graphic_crop_box")

        if not all([gx is not None, gy is not None, g_box is not None and len(g_box) == 2]):
            print(f"Warning: Incomplete graphic info for {prop_key}. Skipping graphic extraction.")
            continue
        
        graphic_width, graphic_height = g_box
        graphic_box = (gx, gy, gx + graphic_width, gy + graphic_height)

        if graphic_box[2] > stitched_image.width or graphic_box[3] > stitched_image.height:
            print(f"Warning: Graphic crop box is outside the bounds of the stitched image for {prop_key}. Skipping.")
            continue

        try:
            graphic_img = stitched_image.crop(graphic_box)
            graphic_output_path = os.path.join(graphics_dir, f"{prop_key}_graphic.png")
            graphic_img.save(graphic_output_path)
            print(f"Saved extracted graphic to {graphic_output_path}")
        except Exception as e:
            print(f"An error occurred during graphic extraction for {prop_key}: {e}")

if __name__ == "__main__":
    process_propositions("resources/cropping_instructions.json")