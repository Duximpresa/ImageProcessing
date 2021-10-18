import os
from PIL import Image
from ImageProcessing import watermark

photo_flie = r"F:\Video\2020广西设计周\Photo\志愿者照片\_MG_0711.JPG"
photo_flie = '/'.join(photo_flie.split('\\'))

watermark.photo_scale_long_only(photo_flie, 1920)
