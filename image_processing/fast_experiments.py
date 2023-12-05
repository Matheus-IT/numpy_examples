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
    MAMMOGRAPHY_DATASET_PATH = "/home/matheuscosta/Documents/mammography-dataset/my_subdataset/subdataset_v4/D3-0051/"
    ds = pydicom.dcmread(MAMMOGRAPHY_DATASET_PATH + "1-1.dcm")
    ic(ds[0x28, 0x2])  # Samples per Pixel
    ic(ds[0x28, 0x10])  # Rows
    ic(ds[0x28, 0x11])  # Columns
    ic(ds[0x28, 0x100])  # Bits Allocated
    ic(ds[0x28, 0x101])  # Bits Stored
    ic(ds[0x28, 0x102])  # High Bit
