import pydenticon
from PIL import Image
import random
import string
from io import BytesIO

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def apply_random_color(image):
    # Generate a random color
    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    width, height = image.size
    pixels = image.load()
    
    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            if pixel == (0, 0, 0, 255):  # Check if the pixel is black
                pixels[x, y] = random_color

def generate_identicon(input_string, output_file):
    generator = pydenticon.Generator(5, 5)
    icon_bytes = generator.generate(input_string, 420, 420)
    
    # Convert the bytes to a PIL Image
    icon_image = Image.open(BytesIO(icon_bytes))

    # Apply a single random color to all the black parts
    apply_random_color(icon_image)

    # Save the PIL Image to the specified output file path
    icon_image.save(output_file)

if __name__ == "__main__":
    custom_output_file_path = input("Enter the output file path (e.g., 'identicon.png'): ")
    if not custom_output_file_path:
        custom_output_file_path = "identicon.png"  # Default file name

    try:
        random_input_string = generate_random_string(10)  # Generates a random 10-character string
        generate_identicon(random_input_string, custom_output_file_path)
        print(f"Random Identicon saved to {custom_output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
