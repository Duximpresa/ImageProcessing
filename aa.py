import os
from PIL import Image
from ImageProcessing import watermark

photo_flie = r"F:\Photo\X100V\2021"
photo_flie = '/'.join(photo_flie.split('\\'))
photo_path = r"F:\Photo\X100V\2021"

# watermark.photo_scale_long_only(photo_flie, 1920)


def getFlist(file_dir):
    roots = []
    dirs = []
    flist = []
    for root, dir, file in os.walk(file_dir):
        # print(root)
        # print(dir)
        # print(file)
        root = '/'.join(root.split('\\'))
        print(root)
        for i in file:
            print(i)
            flpath = os.path.join(root, i)
            flpath = '/'.join(flpath.split('\\'))
            flist.append(flpath)
        # roots.append(root)
        # dirs.append(dir)
        # files.append(flpath)
    return flist

flist = getFlist(photo_path)
print(flist)