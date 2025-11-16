import os
import shutil

def int_to_roman(n):
    """Converts an integer to a Roman numeral."""
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "I", "IX", "V", "IV",
        "I"
    ]
    roman_num = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            roman_num += syb[i]
            n -= val[i]
        i += 1
    return roman_num

def organize_images():
    """
    Organizes images from resources/images into a new folder with canonical names.
    """
    images_dir = "resources/images"
    output_dir = "resources/canonical_images"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    for filename in os.listdir(images_dir):
        if filename.endswith(".jpg"):
            parts = filename.split('.')
            
            if len(parts) < 4 or parts[0] != 'elem':
                print(f"Skipping non-standard file: {filename}")
                continue

            book = int(parts[1])
            element_type = parts[2]
            element_number = parts[3]
            
            roman_book = int_to_roman(book)
            
            # Handle variants like 'b' in 'elem.1.prop.47.b.jpg'
            variant = ""
            if len(parts) > 4 and parts[4] != 'jpg':
                variant = f"-{parts[4]}"

            if element_type == "prop":
                new_name = f"{roman_book}.{element_number}{variant}.jpg"
            else:
                new_name = f"{roman_book}.{element_type}.{element_number}{variant}.jpg"

            src_path = os.path.join(images_dir, filename)
            dest_path = os.path.join(output_dir, new_name)
            
            shutil.copy(src_path, dest_path)
            print(f"Copied and renamed {src_path} to {dest_path}")

if __name__ == "__main__":
    organize_images()
