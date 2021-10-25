import os
from PIL import Image
from threading import Thread
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


# logo_file = 'logo/logo.png'
# photo_file = '01/8B2A7406.jpg'
#
# im_logo = Image.open(logo_file)
# im_photo = Image.open(photo_file)
#


def im_composition(width, height):
    w = width
    h = height
    if w < h:
        # print("这是竖构图")
        return 0
    elif w > h:
        # print("这是横构图")
        return 1
    else:
        # print("这是方形构图")
        return 2


def logo_new_size(pw, ph, lw, lh, percen=0.3):  # logo的大小
    w = round(pw * percen)
    h = round(ph * percen)
    lwn = w
    lhn = round(lh * (lwn / lw))
    return lwn, lhn


def logo_resize(im_logo, newsize):
    im_new_logo = im_logo.resize((newsize))
    return im_new_logo


def photo_resize(im_photo, newsize):
    im_new_photo = im_photo.resize(newsize)
    return im_new_photo


def logo_postiton(photo_size, logo_size, percen=0.02):  # logo的边距
    x = photo_size[0] * (1 - percen) - logo_size[0]
    y = photo_size[1] * percen
    return round(x), round(y)


def photo_logo(im_photo, im_logo, postiton):
    im_photo.paste(im_logo, postiton, mask=im_logo)
    return im_photo


def photo_save(im_photo, path, name, format):
    im_photo.save(f'{path}/{name}.{format}')


def file_list(patch):
    file_lists = []
    for i in os.listdir(patch):
        if os.path.isfile(patch + "/" + i):
            file_lists.append(i)
    return file_lists


def file_filter(file_list, name):
    file_lists = []
    for i in file_list:
        if os.path.splitext(i)[-1][1:].lower() == name:
            file_lists.append(i)

    return file_lists


def photo_filter(patch, name):
    file_lists = file_list(patch)
    photo_list = file_filter(file_lists, name)
    return photo_list


def ok_dir(patch):
    if not os.path.exists(patch):
        os.makedirs(patch)


def photologo(patch, logo, name):
    pass


def watermark_run(photo_path, logo_file):
    patch = photo_path
    # patch = r'E:\项目\广西设计生活榜单中海半山壹号\Photo\2021\2021-03-27\04'
    patch = '/'.join(patch.split('\\'))
    logo_file = logo_file
    # logo_file = r'D:\DuximpresaProject\PycharmProjects\ImageProcessing\logo\logo.png'
    jpg_list = photo_filter(patch, "jpg")
    im_logo = Image.open(logo_file)
    ok_dir(patch + '/ok')
    counte = 0
    all = len(jpg_list)
    for i in jpg_list:
        photo_file = patch + "/" + i
        im_photo = Image.open(photo_file)
        newsize = logo_new_size(im_photo.size[0], im_photo.size[1], im_logo.size[0], im_logo.size[1])
        im_new_logo = logo_resize(im_logo, newsize)
        postiton = logo_postiton(im_photo.size, im_new_logo.size)
        im_new_photo = photo_logo(im_photo, im_new_logo, postiton)
        name = os.path.splitext(i)[0] + "_logo"
        format = os.path.splitext(i)[1][1:]
        photo_save(im_new_photo, patch + "/" + 'ok/', name, format)

        counte += 1
        progress = round((counte + 1) / all * 100)
        print(f'\r已完成 {progress}%', end="")
    print(f"已完成 {counte} 张照片")


def watermark_run_only(photo_file, logo_file):
    logo_file = logo_file
    im_logo = Image.open(logo_file)
    patch = os.path.dirname(photo_file)
    patch = '/'.join(patch.split('\\'))
    ok_dir(patch + '/ok')

    photo_file = photo_file
    im_photo = Image.open(photo_file)
    newsize = logo_new_size(im_photo.size[0], im_photo.size[1], im_logo.size[0], im_logo.size[1])
    im_new_logo = logo_resize(im_logo, newsize)
    postiton = logo_postiton(im_photo.size, im_new_logo.size)
    im_new_photo = photo_logo(im_photo, im_new_logo, postiton)
    name = os.path.splitext(os.path.basename(photo_file))[0] + "_logo"
    format = os.path.splitext(photo_file)[1][1:]
    photo_save(im_new_photo, patch + "/" + 'ok/', name, format)
    # counte += 1
    # progress = round((counte + 1) / all * 100)
    print(f'\r打水印:{name}')
    # print(f'\r已完成 {progress}%', end="")

def photo_scale_long_only(photo_file, long):
    # logo_file = logo_file
    # im_logo = Image.open(logo_file)
    patch = os.path.dirname(photo_file)
    patch = '/'.join(patch.split('\\'))
    # ok_dir(patch + '/ok')

    photo_file = photo_file
    im_photo = Image.open(photo_file)
    # newsize = logo_new_size(im_photo.size[0], im_photo.size[1], im_logo.size[0], im_logo.size[1])
    # im_new_logo = logo_resize(im_logo, newsize)
    # postiton = logo_postiton(im_photo.size, im_new_logo.size)
    im_new_photo = im_photo
    photo_scale(im_new_photo, long)
    name = os.path.splitext(os.path.basename(photo_file))[0]
    format = os.path.splitext(photo_file)[1][1:]
    photo_save(im_new_photo, patch, name, format)
    # counte += 1
    # progress = round((counte + 1) / all * 100)
    print(f'\r改尺寸：{name}')
    # print(f'\r已完成 {progress}%', end="")

def watermark_run_cpu(photo_path, logo_file):
    patch = photo_path
    patch = '/'.join(patch.split('\\'))
    logo_file = logo_file
    jpg_list = photo_filter(patch, "jpg")
    # im_logo = Image.open(logo_file)
    ok_dir(patch + '/ok')
    counte = 0
    all = len(jpg_list)

    with ThreadPoolExecutor(8) as t:
        for i in jpg_list:
            t.submit(watermark_run_only, patch + "/" + i, logo_file)

    # print(f"已完成 {counte} 张照片")

def photo_scale_long_cpu(photo_path, long):
    patch = photo_path
    patch = '/'.join(patch.split('\\'))
    # logo_file = logo_file
    jpg_list = photo_filter(patch, "jpg")
    # im_logo = Image.open(logo_file)
    # ok_dir(patch + '/ok')
    # counte = 0
    # all = len(jpg_list)

    with ThreadPoolExecutor(8) as t:
        for i in jpg_list:
            t.submit(photo_scale_long_only, patch + "/" + i, long)

    # print(f"已完成 {counte} 张照片")


def size_1080p(size, long):
    hw = im_composition(size[0], size[1])
    if hw == 1:
        a = size[1] / (size[0] / long)
        return (long, round(a))
    else:
        a = size[0] / (size[1] / long)
        return (round(a), long)


def photo_size_long(photo_path, long):
    patch = photo_path
    patch = '/'.join(patch.split('\\'))
    jpg_list = photo_filter(patch, "jpg")
    counte = 0
    all = len(jpg_list)
    for i in jpg_list:
        photo_file = patch + "/" + i
        im_photo = Image.open(photo_file)
        original_size = im_photo.size
        newsize = size_1080p(original_size, long)
        im_new_photo = photo_resize(im_photo, newsize)
        name = os.path.splitext(i)[0]
        format = os.path.splitext(i)[1][1:]
        photo_save(im_new_photo, patch, name, format)
        counte += 1
        progress = round((counte + 1) / all * 100)
        print(f'\r已完成 {progress}%', end="")
    print(f"已完成 {counte} 张照片")


def photo_rot(im, angle):  # 弃用，直接调用pillow的方法
    im = im.rotate(angle, expand=True)
    return im


def photo_scale(im, long):  # 旋转图片，返回一个Image对象
    im.thumbnail((long, long))
    # return im


def photo_scale_long(photo_path, long):
    patch = photo_path
    patch = '/'.join(patch.split('\\'))
    jpg_list = photo_filter(patch, "jpg")
    counte = 0
    all = len(jpg_list)
    for i in jpg_list:
        photo_file = patch + "/" + i
        im_photo = Image.open(photo_file)
        im_new_photo = im_photo
        photo_scale(im_new_photo, long)
        name = os.path.splitext(i)[0]
        format = os.path.splitext(i)[1][1:]
        photo_save(im_new_photo, patch, name, format)
        counte += 1
        progress = round((counte + 1) / all * 100)
        print(f'\r已完成 {progress}%', end="")
    print(f"已完成 {counte} 张照片")


def photo_rot_list(photo_path, angle):
    patch = photo_path
    patch = '/'.join(patch.split('\\'))
    jpg_list = photo_filter(patch, "jpg")
    counte = 0
    all = len(jpg_list)
    for i in jpg_list:
        photo_file = patch + "/" + i
        im_photo = Image.open(photo_file)
        im_new_photo = im_photo.rotate(angle, expand=True)
        name = os.path.splitext(i)[0]
        format = os.path.splitext(i)[1][1:]
        photo_save(im_new_photo, patch, name, format)
        counte += 1
        progress = round((counte + 1) / all * 100)
        print(f'\r已完成 {progress}%', end="")
    print(f"已完成 {counte} 张照片")


# Image.thumbnail(1920, 1920)  图像缩放，代开发

def main():
    patch = r'E:\项目\广西设计生活榜单中海半山壹号\Photo\2021\2021-03-27\04'
    patch = '/'.join(patch.split('\\'))
    logo_file = r'D:\DuximpresaProject\PycharmProjects\ImageProcessing\logo\logo.png'
    jpg_list = photo_filter(patch, "jpg")
    im_logo = Image.open(logo_file)
    ok_dir(patch + '/ok')
    counte = 0
    all = len(jpg_list)
    for i in jpg_list:
        photo_file = patch + "/" + i
        im_photo = Image.open(photo_file)
        newsize = logo_new_size(im_photo.size[0], im_photo.size[1], im_logo.size[0], im_logo.size[1])
        im_new_logo = logo_resize(im_logo, newsize)
        postiton = logo_postiton(im_photo.size, im_new_logo.size)
        im_new_photo = photo_logo(im_photo, im_new_logo, postiton)
        name = os.path.splitext(i)[0] + "_logo"
        format = os.path.splitext(i)[1][1:]
        photo_save(im_new_photo, patch + "/" + 'ok/', name, format)

        counte += 1
        progress = round((counte + 1) / all * 100)
        print(f'\r已完成 {progress}%', end="")
    print(f"已完成 {counte} 张照片")


def main2():
    photo_path = r"J:\DuximpresaProject\PychramProject\ImageProcessing\01"
    size = 1920
    photo_size_long(photo_path, size)


if __name__ == "__main__":
    main2()
