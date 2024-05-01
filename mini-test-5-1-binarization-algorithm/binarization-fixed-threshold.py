from PIL import Image
import numpy as np

# Read the black and white image
image_path = input("Enter the path to the black and white image (leave blank for input.jpg): ")
if image_path =="":
    image_path = "input.jpg"
    
try:
    image = Image.open(image_path)
except IOError:
    print("Error: Unable to open image file.")
    exit()

# Convert the image to a numpy array
image_array = np.array(image)

# Ask for the threshold value
while True:
    threshold = input("Enter a threshold value (between 1 and 254 inclusive): ")
    try:
        threshold = int(threshold)
        if threshold < 1 or threshold > 254:
            print("Error: Threshold value must be between 1 and 254 inclusive.")
        else:
            break
    except ValueError:
        print("Error: Please enter a valid integer.")

# Binarize the image array using the threshold and convert it back to an image
binarized_image = np.where(image_array > threshold, 255, 0)
binarized_image = Image.fromarray(binarized_image.astype(np.uint8))

# Save the binarized image
output_path = input("Enter the path to save the binarized image (leave blank for output_{threshold}.jpg): ")
if output_path == "":
    output_path = "output_" + str(threshold) + ".jpg"
binarized_image.save(output_path)

print(f"Binarized image saved as '{output_path}'.")
