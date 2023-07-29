import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_voi_lut
from utils.presentation import (
    show_pixel_info,
    show_voi_lut_module,
    show_file_dataset_info,
    show_pixel_array_info,
    display_side_by_side,
)
import cv2 as cv
from utils.image_normalization import normalize, denormalize
from utils.filters import opening_filter, closing_filter, high_pass_filter
from icecream import ic
import numpy as np
from utils.elapsed_time import Timer
from PIL import Image
import pydicom


with Timer():
    # MAMMOGRAPHY_DATASET_PATH = "/home/matheuscosta/Documents/mammography-dataset/nbia/CMMD/D2-0001/07-18-2011-NA-NA-75485/1.000000-NA-12786/"
    # original = pydicom.dcmread(MAMMOGRAPHY_DATASET_PATH + "1-1.dcm").pixel_array
    original = cv.imread("image_processing/images/mammography2.png")
    original = cv.cvtColor(original, cv.COLOR_BGRA2GRAY)
    modified = original.copy()

    modified = normalize(modified)

    height, width = modified.shape

    kernel_size = (5, 5)
    modified = cv.GaussianBlur(modified, kernel_size, 0)

    # Convert the new image to binary
    ret, modified = cv.threshold(modified, 0, 255, cv.THRESH_OTSU)

    # get largest contour
    contours, hierarchy = cv.findContours(
        modified, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE
    )
    big_contour = max(contours, key=cv.contourArea)

    # draw largest contour as white filled on black background as mask
    mask = np.zeros((height, width), dtype=np.uint8)
    cv.drawContours(mask, [big_contour], 0, 255, cv.FILLED)

    modified = cv.bitwise_and(original, original, mask=mask)

    modified = high_pass_filter(modified)

    Image.fromarray(modified).show()
