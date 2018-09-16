# this code is used to resize the saliency map into the original size (for submitting to the MIT saliency benchmark)
import cv2
import numpy as np 
import scipy.misc as misc
from matplotlib import pyplot as plt
import os

'''
img_unity_path = 'D:\\Paper\\saliency\\Datasets\\BenchmarkIMAGES\\MIT_300_Original\\'
img_benchmark_path = 'D:\\Paper\\saliency\\Datasets\\BenchmarkIMAGES\\mit300\\BenchmarkIMAGES\\'
img_remapping_path = 'D:\\Paper\\saliency\\Datasets\\BenchmarkIMAGES\\mit300\\Submission\\CFS-GAN_1\\'

# img_1 = cv2.imread('D:\\Paper\\saliency\\Datasets\\BenchmarkIMAGES\\MIT_300_Original\\i1.jpg')
# [height_1, width_1, channel_1] = img_1.shape 

for i in range(1, 301, 1):
    # img_1 = cv2.imread(img_unity_path + 'i' + str(i) + '_IMG.jpg')
    img_1 = cv2.imread(img_unity_path + 'i' + str(i) + '_SM.jpg')
    [height_1, width_1, channel_1] = img_1.shape 
    img_2 = cv2.imread(img_benchmark_path + 'i' + str(i) + '.jpg')
    [height_2, width_2, channel_2] = img_2.shape

    ratio_1 = 4 / 3
    ratio_2 = width_2 / height_2

    if (ratio_1 > ratio_2):
        ideal_width = round(height_1 * ratio_2)
        Band = round ((width_1 - ideal_width) / 2)
        img_3 = img_1[:, Band:width_1-Band, :]

    if (ratio_1 < ratio_2):
        ideal_height = round(width_1 / ratio_2)
        Band = round((height_1 - ideal_height) / 2)
        img_3 = img_1[Band:height_1-Band, :, :]

    if (ratio_1 == ratio_2):
        # ideal_height = round(width_1 / ratio_2)
        # Band = round((height_1 - ideal_height) / 2)
        img_3 = img_1

    img_4 = cv2.resize(img_3, (width_2, height_2), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(img_remapping_path + 'i' + str(i) + '.jpg', img_4)
'''

img_unity_path = 'D:\\Paper\\saliency\\Datasets\\BenchmarkIMAGES\\MIT_300_Finetune\\'
img_benchmark_path = 'D:\\Paper\\saliency\\Datasets\\BenchmarkIMAGES\\mit300\\BenchmarkIMAGES\\'
img_remapping_path = 'D:\\Paper\\saliency\\Datasets\\BenchmarkIMAGES\\mit300\\Submission\\CFS-GAN_2\\'

# img_1 = cv2.imread('D:\\Paper\\saliency\\Datasets\\BenchmarkIMAGES\\MIT_300_Original\\i1.jpg')
# [height_1, width_1, channel_1] = img_1.shape 

for i in range(1, 301, 1):
    # img_1 = cv2.imread(img_unity_path + 'i' + str(i) + '_IMG.jpg')
    img_1 = cv2.imread(img_unity_path + 'i' + str(i) + '_SM.jpg')
    [height_1, width_1, channel_1] = img_1.shape 
    img_2 = cv2.imread(img_benchmark_path + 'i' + str(i) + '.jpg')
    [height_2, width_2, channel_2] = img_2.shape

    ratio_1 = 4 / 3
    ratio_2 = width_2 / height_2

    if (ratio_1 > ratio_2):
        ideal_width = round(height_1 * ratio_2)
        Band = round ((width_1 - ideal_width) / 2)
        img_3 = img_1[:, Band:width_1-Band, :]

    if (ratio_1 < ratio_2):
        ideal_height = round(width_1 / ratio_2)
        Band = round((height_1 - ideal_height) / 2)
        img_3 = img_1[Band:height_1-Band, :, :]

    if (ratio_1 == ratio_2):
        # ideal_height = round(width_1 / ratio_2)
        # Band = round((height_1 - ideal_height) / 2)
        img_3 = img_1

    img_4 = cv2.resize(img_3, (width_2, height_2), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(img_remapping_path + 'i' + str(i) + '.jpg', img_4)
 
