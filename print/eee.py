import random

import numpy as np
from PIL import Image
from skimage import io
from skimage.transform import resize
import os

mask = Image.open(os.path.join('/home/ziyuz/PycharmProjects/few-shot segmentation/dataloaders/print/print', str('4') + '.png'))
mask1 = mask.load()
pmask = []
for v in range(mask.size[1]):
    for u in range(mask.size[0]):
        if mask1[u, v] == (0, 0, 0,255):
            pmask.append(0)
        else:
            pmask.append(1)


def get_index(lst=None, item=''):
    return [index for (index, value) in enumerate(lst) if value == item]


PT_1 = random.sample(get_index(pmask, item=1), 1024)
PT_0 = random.sample(get_index(pmask, item=0), 1024)
print(len(PT_0))