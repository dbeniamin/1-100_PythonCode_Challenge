import numpy as np
import matplotlib.pyplot as plt
from scipy import misc  # contains an image of a racoon
from PIL import Image  # used for reading image files

my_array = np.array([1.1, 9.2, 8.1, 4.7])
print(my_array.shape)

# TODO 1 - check the dimensions of my_array with the ndim attribute
print(my_array.ndim)

# TODO 2 - create a 2-dimensional array (i.e., a “matrix”)
array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

# TODO 3 - access an entire row and all the values therein, you can use the : operator
print(f"entire row access is {array_2d[0, :]}")

# TODO 4 - mystery array working
mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],

                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

print(f'We have {mystery_array.ndim} dimensions')
print(f'The shape is {mystery_array.shape}')

# The shape is (3, 2, 4), so we have 3 elements along axis #0, 2 elements along axis #1 and 4 elements along axis #3.

# TODO 5 - Generating and Manipulating arrays
# random generates an array from 10 to 29
a = np.arange(10, 30)
print(a)

# The last 3 values in the array
print(a[-3:])

# An interval between two values
print(a[3:6])

# All the values except the first 12
print(a[12:])

# Every second value (i.e., all the even values in our case)
print(a[::2])

# reverse the order of an array
# method 1 - use .flip() method
print(np.flip(a))
# method 2 - use slicing
print(a[::-1])

# vector
x = np.linspace(0, 100, num=9)
print(x)
y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x, y)
plt.show()

# noise
noise = np.random.random((128, 128, 3))
# print(noise.shape)
plt.imshow(noise)
plt.show()

# TODO 6 - Broadcasting, Scalars and Matrix Multiplication
# adding arrays is very different from adding lists
v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
print(v1 + v2)

# arrays can be multiplied - lists cant
print(v1 * v2)

# Broadcasting Now, oftentimes you'll want to do some sort of operation between an array and a single number. In
# mathematics, this single number is often called a scalar. For example, you might want to multiply every value in
# your NumPy array by 2

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

# multiplication of matrix's
c = np.matmul(a1, b1)
print(c)

# TODO 7 - Manipulating Images as arrays
img = misc.face()
plt.imshow(img)
plt.show()

sRGB_array = img / 255
grey_vals = np.array([0.2126, 0.7152, 0.0722])
img_gray = sRGB_array @ grey_vals

img_gray = np.matmul(sRGB_array, grey_vals)
plt.imshow(img_gray, cmap='gray')
plt.show()

# adding an image as array
file_name = "yummy_macarons.jpg"
test_img = Image.open(file_name)
test_array = np.array(test_img)
plt.imshow(test_array)
plt.show()
