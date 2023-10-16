import pydenticon
from PIL import Image

def generate_identicon(input_string, output_file):
    generator = pydenticon.Generator(5, 5)
    icon = generator.generate(input_string, 420, 420)
    icon.save(output_file)

if __name__ == "__main__":
    input_string = input("Enter the text to create an identicon: ")
    output_file_path = input("Enter the path for the output file (e.g., 'identicon.png'): ")

    try:
        generate_identicon(input_string, output_file_path)
        print(f"Identicon saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
