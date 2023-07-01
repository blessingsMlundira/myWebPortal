from PIL import Image
import os

def reduce_image_size(image_path, output_path, max_size):
    # Open the image
    with Image.open(image_path) as img:
        # Calculate the new width and height while preserving aspect ratio
        width, height = img.size
        aspect_ratio = width / height
        new_width = min(width, max_size)
        new_height = int(new_width / aspect_ratio)

        # Resize the image
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

        # Save the resized image with compression
        img.save(output_path, optimize=True, quality=85)

    # Calculate the percentage reduction in file size
    original_size = os.path.getsize(image_path)
    new_size = os.path.getsize(output_path)
    reduction_percentage = (1 - new_size / original_size) * 100
    print(f"Image file size reduced by {reduction_percentage:.2f}%")

# Example usage
image_path = "my_space_app.png"
output_path = "compressed_image.png"
max_size = 1024  # Maximum width or height in pixels

reduce_image_size(image_path, output_path, max_size)
