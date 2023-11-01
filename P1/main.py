#ALVARO JIMENEZ BARRENO - NIA: 240903
import os
from PIL import Image as img
import numpy as np
import cv2
import struct
import math


# EXERCISE 1
def rgb2yuv(red_c, green_c, blue_c):
    y_c = round(0.257 * red_c + 0.504 * green_c + 0.098 * blue_c + 16, 3)
    u_c = round(-0.148 * red_c - 0.291 * green_c + 0.439 * blue_c + 128, 3)
    v_c = round(0.439 * red_c - 0.368 * green_c - 0.071 * blue_c + 128, 3)
    return [y_c, u_c, v_c]


def yuv2rgb(y_c, u_c, v_c):
    red_c = round(1.164 * (y_c - 16) + 1.596 * (v_c - 128), 3)
    blue_c = round(1.164 * (y_c - 16) + 2.018 * (u_c - 128), 3)
    green_c = round(1.164 * (y_c - 16) - 0.813 * (v_c - 128) - 0.391 * (u_c - 128), 3)
    return [red_c, green_c, blue_c]


def conversorRGB_YUV(val1, val2, val3, val_type):
    '''args of the function
        val1, val2, val3: float values. Components of each system (RGB) or (YUV)
        val_type: color codification system of the input values: RGB if values are
        red, green and blue components or YUV if values are chrominance and color
        data'''
    try:
        converted_values = []
        if val_type == "RGB":
            converted_values = rgb2yuv(val1, val2, val3)
        elif val_type == "YUV":
            converted_values = yuv2rgb(val1, val2, val3)
        else:
            return "Value type incorrect. Must be RGB or YUV"
        return converted_values
    except Exception as e:
        return "Exception error raised: " + str(e)


# EXERCISE 2
def get_imsize(file_image):
    im = img.open(file_image)
    w, h = im.size
    if w <= 0 or h <= 0:
        return "Invalid input"
    return w, h


def lower_quality_image(file_image):
    w_im, h_im = get_imsize(file_image)
    command1 = ('ffmpeg -i ' + file_image + ' -q:v 31 low_quality_image.jpg')
    command2 = ('ffmpeg -i ' + file_image + ' -q:v 31 -vf scale=' +
                str(w_im/2) + ':' + str(h_im/2) + ' low_reduced_image.jpg')
    os.system(command1)
    os.system(command2)


# EXERCISE 3
def get_byte_data(image):
    w, h = get_imsize(image)
    image_pixels = cv2.imread(image)
    pixel_matrix = []
    for y in range(h):
        row = []
        for x in range(w):
            pixel = image_pixels[x, y]
            pixel_byte = struct.pack('BBBB', pixel[0], pixel[1], pixel[2], 255)
            row.append(pixel_byte)
        pixel_matrix.append(row)
    return pixel_matrix


def serpentine(image):
    w, h = get_imsize(image)
    pixel_matrix = get_byte_data(image)
    result = []
    # We iterate for the first half of the image
    for i in range(w):
        if i % 2 == 0:
            for j in range(i + 1):
                result.append(pixel_matrix[j][i - j])
        else:
            for j in range(i + 1):
                result.append(pixel_matrix[i - j][j])
    # We iterate for the second half of the image
    for i in range(w - 1, 0, -1):
        if i % 2 == 0:
            for j in range(i):
                result.append(pixel_matrix[w - 1 - j][w - i + j])
        else:
            for j in range(i):
                result.append(pixel_matrix[w - i + j][w - 1 - j])
    bytes_result = b''.join(result)
    image_serpentine = img.frombytes('RGBA', (w, h), bytes_result)
    image_serpentine.save('serpentine_image.png')
    return result


def test_serpentine_matrix(square_matrix_size):
    if square_matrix_size <= 0:
        return "Invalid input"
    result = []
    for i in range(square_matrix_size):
        if i % 2 == 0:
            for j in range(i + 1):
                result.append((j, i - j))
        else:
            for j in range(i + 1):
                result.append((i - j, j))
    for i in range(square_matrix_size - 1, 0, -1):
        if i % 2 == 0:
            for j in range(i):
                result.append((square_matrix_size - 1 - j, square_matrix_size - i + j))
        else:
            for j in range(i):
                result.append((square_matrix_size - i + j, square_matrix_size - 1 - j))
    return result


# EXERCISE 4
def bw_compression(image):
    w_im, h_im = get_imsize(image)
    command = ("ffmpeg -i " + image + " -vf format=gray,scale=" + str(w_im/2) +
               ":-1 -q:v 51 image_bw_compressed.jpg")
    os.system(command)


# EXERCISE 5
def run_length_encode(bits_data):
    encoded_data = []
    counter = 0

    for i in bits_data:
        if i == 0:
            counter += 1
        else:
            if counter > 0:
                encoded_data.append(0)
                encoded_data.append(counter)
            encoded_data.append(i)
            counter = 0
    if counter > 0:
        encoded_data.append(0)
        encoded_data.append(counter)
    return encoded_data


# EXERCISE 6
'''To create the methods of this class I have followed the structure of the DCT and IDCT formulas in this entry
https://link.springer.com/referenceworkentry/10.1007/0-387-30038-4_61 but using the values of the theory slides.
The dct_data variable should be a 8x8 matrix of coefficients (pixel values of the 8x8 matrix). Depending on the
values, we would like to perform the DCT or IDCT conversion.'''


class DCTOperations:
    def __init__(self):
        self.matrix_data = None
        self.m = None
        self.n = None

    def dct_conversion(self):
        '''The dct_data variable will determine if we are performing the Discrete Cosine Transform operation
        or the Inverse Cosine Transform Operation.'''
        dct_values = []
        for idx in range(self.m):
            dct_row = []
            for jdx in range(self.n):
                dct_row.append(None)
            dct_values.append(dct_row)

        for u in range(self.m):
            for v in range(self.n):
                if u == 0:
                    cu = np.sqrt(1/self.m)
                else:
                    cu = np.sqrt(2/self.m)
                if v == 0:
                    cv = np.sqrt(1/self.n)
                else:
                    cv = np.sqrt(2/self.n)

                total = 0
                for x in range(self.m):
                    for y in range(self.n):
                        sum_value = (self.matrix_data[x][y] * math.cos((3.1415 / self.m) * (x + 0.5) * u) *
                                     math.cos((3.1415 / self.n) * (y + 0.5) * v))
                        total = total + sum_value
                dct_values[u][v] = cu * cv * total
        return dct_values

    def idct_conversion(self):
        idct_values = []
        for i in range(self.m):
            idct_values.append([None for _ in range(self.n)])

        for x in range(self.m):
            for y in range(self.n):
                total = 0
                for u in range(self.m):
                    for v in range(self.n):
                        if u == 0:
                            cu = np.sqrt(1/self.m)
                        else:
                            cu = np.sqrt(2/self.m)
                        if v == 0:
                            cv = np.sqrt(1/self.n)
                        else:
                            cv = np.sqrt(2/self.n)

                        sum_value = (cu * cv * self.matrix_data[u][v] * math.cos((3.1415 / self.m) * (u + 0.5) * x) *
                                     math.cos((3.1415 / self.n) * (v + 0.5) * y))
                        total = total + sum_value
                idct_values[x][y] = total
        return idct_values


if __name__ == "__main__":
    #Load the images
    jigglypuff = 'jigglypuff.jpg'
    sillycat = 'silly_cat.jpg'
    squirtle = 'squirtle.jpg'

    # Exercise 1
    yuv_val = conversorRGB_YUV(16.389, 127.825, 127.904, "YUV")
    print(yuv_val)

    rgb_val = conversorRGB_YUV(0.3, 0.6, 0.1, "RGB")
    print(rgb_val)

    # Exercise 2
    lower_quality_image(jigglypuff)

    # Exercise 3
    # It should be done with a square image.
    sillycat_serpentine_bits = serpentine(sillycat)

    # Simplified algorithm to test the path of the iterations
    matrix_size = 8
    serpentine_algorithm = test_serpentine_matrix(matrix_size)
    print(serpentine_algorithm)

    # Exercise 4
    bw_compression(sillycat)

    # Exercise 5
    list_data_bits = [0, 1, 2, 3, 3, 2, 1, 0, 0, 48, 13, 66, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    run_length_data_bits = run_length_encode(list_data_bits)
    print(run_length_data_bits)

    # Exercise 6
    value_matrix = [[255, 255, 255, 255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255, 255, 255, 255]]

    dct_value_matrix = DCTOperations()
    dct_value_matrix.m = 8
    dct_value_matrix.n = 8
    dct_value_matrix.matrix_data = value_matrix
    dct_data_matrix = dct_value_matrix.dct_conversion()

    dct_value_matrix.matrix_data = dct_data_matrix
    idct_data_matrix = dct_value_matrix.idct_conversion()

    print('Original Matrix: \n', value_matrix)
    print('DCT Matrix: \n', dct_data_matrix)
    print('IDCT Matrix: \n', idct_data_matrix)


    #This part of the code tried to get the DCT Image from the squirtle.jpg image.
    #Since it lasts nearly 15 minutes, I decided to comment this part and show the example
    #with a 8x8 matrix.
    
    w_squirtle, h_squirtle = get_imsize(squirtle)
    sillycat_matrix = get_byte_data(squirtle)

    image_pixels_squirtle = cv2.imread(squirtle)
    mat_r = []
    mat_g = []
    mat_b = []
    for i_m in range(h_squirtle):
        row_r = []
        row_g = []
        row_b = []
        for j_m in range(w_squirtle):
            row_r.append(image_pixels_squirtle[i_m][j_m][0])
            row_g.append(image_pixels_squirtle[i_m][j_m][1])
            row_b.append(image_pixels_squirtle[i_m][j_m][2])
        mat_r.append(row_r)
        mat_g.append(row_g)
        mat_b.append(row_b)

    dct_r = DCTOperations()
    dct_g = DCTOperations()
    dct_b = DCTOperations()

    dct_r.matrix_data = mat_r
    dct_g.matrix_data = mat_g
    dct_b.matrix_data = mat_b

    dct_r.m = w_squirtle
    dct_r.n = h_squirtle
    dct_g.m = w_squirtle
    dct_g.n = h_squirtle
    dct_b.m = w_squirtle
    dct_b.n = h_squirtle

    dct_r_mat = dct_r.dct_conversion()
    dct_g_mat = dct_g.dct_conversion()
    dct_b_mat = dct_b.dct_conversion()

    dct_total_matrix = np.dstack((dct_r_mat, dct_g_mat, dct_b_mat))
    rgb_matrix = np.array(dct_total_matrix)
    dct_image = cv2.cvtColor(rgb_matrix.astype(np.uint8), cv2.COLOR_RGB2BGR)
    
    cv2.imwrite('dct_squirtle.jpg', dct_image)

    '''
    COMMENTS:
    EX4. In order to make the image BW, we use the ffmpeg command using format=gray to convert
    the image input into grayscale. Then I use scale=width_of_the_image/2 to resize it half of the
    original width and -1 so that the height is resized automatically. as for the -q:v 51 is for the
    quality video. JPG quality images' range go from 0 being the best quality to 51 being the worst. 
    Then, since I want the image to have less quality, I set the value to 51. 
    As for the output, I obtain the sillycat image with some changes. Its dimensions are half the original, 
    the quality is worse, and its color scale is not RGB (3 channels) but grayscale (1 channel).
    
    EX6. I do not think that the expected DCT result of the image is OK. It should give me
    the components of a 8x8 matrix DCT transform applied to the image. But I do not know how
    can check the expected result. It might have something to do with the fact that I separated
    the RGB channels and performed the DCT conversion independently. However, I also performed the
    DCT operation with the 8x8 matrices because I think my code is generally OK but I am not getting something
    conceptually.
    '''