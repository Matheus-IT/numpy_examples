import numpy as np
import pydicom

import matplotlib
import matplotlib.pyplot as plt


# set the backend
matplotlib.use("TkAgg")


with pydicom.dcmread("pydicom/image5.dcm") as ds:
    img = ds.pixel_array.astype(np.int16)
    img = np.array(img, dtype=np.int16)
    plt.imshow(img, cmap=plt.cm.bone)
    plt.show()
