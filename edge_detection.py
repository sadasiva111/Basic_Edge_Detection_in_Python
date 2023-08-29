from helper_functions import *

# -----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "images/"
imgpath = datafolder + "3.jpg"
# ----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
# ----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information
new_pixel_values = [[0 for i in range(numb_colns)] for j in range(numb_rows)]
# Define the 3 x 3 mask as a tuple of tuples
mask = ((-1, 0, 1), (-2, 0, 2), (-1, 0, 1))




# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(pixel_values, i, j):
    return [pixel_values[row][j-1: j+2] for row in range(i-1, i+2)]
    # return np.asarray(pixel_values)[i - 1:i + 2, j - 1:j + 2]


# Implement a function to flatten a 2D list or a 2D tuple
def flatten(l):
    return [single_pixel for i in l for single_pixel in i]


# For each of the pixel values, excluding the boundary values
flatten_mask = flatten(mask)
for i in range(1, numb_rows + 1):
    for j in range(1, numb_colns + 1):
        # Create little local 3x3 box using list slicing
        neighbour_pixels = get_slice_2d_list(pixel_values, i, j)
        flatten_np = flatten(neighbour_pixels)
        # Apply the mask
        mult_result = list(map(lambda x, y: x * y, flatten_np, flatten_mask))
        # Sum all the multiplied values and set the new pixel value
        new_pixel_values[i - 1][j - 1] = sum(mult_result)
#
# ----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)
