from PIL import Image
import numpy as np

image_path = input("Enter the path to the image (leave blank for input.jpg): ")
if image_path =="":
    image_path = "input.jpg"
    
try:
    image = Image.open(image_path)
except IOError:
    print("Error: Unable to open image file.")
    exit()

image_array = np.array(image)
indices_array = [[0 for i in range(image_array.shape[1])] for j in range(image_array.shape[0])]

# ask for the offset values
while True:
    offset = input("Enter an offset <a b> where a and b are positive integers: ")
    try:
        offset = offset.split()
        offset = [int(i) for i in offset]
        if len(offset) != 2:
            print("Error: Please enter two valid integers.")
        else:
            break
    except ValueError:
        print("Error: Please enter two valid integers.")

# calculate the amount and values of distinct pixels
pixel_values = []

for i in range(image_array.shape[0]):
    for j in range(image_array.shape[1]):
        present = False
        index = 0
        for p in range(len(pixel_values)):
            same = True
            for k in range(len(pixel_values[p])):
                if pixel_values[p][k] != image_array[i][j][k]:
                    same = False
                    break
            if same:
                present = True
                index = p
                break
        if not present:
            pixel_values.append(image_array[i][j])
            index = len(pixel_values) - 1
        indices_array[i][j] = index
        
                

print(f"Amount of distinct pixels: {len(pixel_values)}")

# create gclm matrix with integer zeros
glcm = [[0 for i in range(len(pixel_values))] for j in range(len(pixel_values))]

# calculate the glcm matrix
for i in range(image_array.shape[0]):
    for j in range(image_array.shape[1]):
        if i + offset[0] < image_array.shape[0] and j + offset[1] < image_array.shape[1]:
            glcm[indices_array[i][j]][indices_array[i + offset[0]][j + offset[1]]] += 1

print("\nGLCM matrix:")
for i in range(len(glcm)):
    print(glcm[i])

# calculate the GLDV, by summing the rows of the GLCM matrix
gldv = [sum(row) for row in glcm]
print(f"\nGLDV (transposed):\n{gldv}")