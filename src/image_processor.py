from PIL import Image

def resize_image(input_path, output_path, size=(100, 100)):
    """Resize an image and save it."""
    img = Image.open(input_path)
    img = img.resize(size)
    img.save(output_path)
    return f"Image saved to {output_path}"
