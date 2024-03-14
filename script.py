import PIL.Image

# ascii characters used to represent the pixels
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Resize the image to fit the screen
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert the image to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert the pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]
    return ascii_str

def main():
    # Attempt to open the image input
    path = input("Enter the path to the image: \n")
    try:
        img = PIL.Image.open(path)
    except:
        print(path, "Error: Could not open image.")
        return
    
    # Convert image to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(img)))
    
    # Format the image data
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))


main()
