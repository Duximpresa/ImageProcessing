from ImageProcessing import watermark
from datetime import datetime

photo_path = r"F:\Video\2021广西设计周记录\photo\10_24\10-24-开会合影"
photo_file = r"I:\2020广西设计周-专业拍摄团队素材\照片素材\5号照片汇总\2020.12.5设计周出图盘\烧鸡出片盘\烧鸡出片无logo\D75_6168.jpg"
logo_file = r"F:\Video\2021广西设计周宣传视频\logo\2021创意生活节x广西设计周_白_阴影.png"
long = 1920
angle = int(-90)


def main():
    start_time = datetime.now()
    watermark.watermark_run(photo_path, logo_file)
    photo_path_ok = photo_path + "/ok"
    watermark.photo_scale_long(photo_path_ok, long)
    # watermark.photo_rot_list(photo_path_ok, -90)

    end_time = datetime.now()
    code_time = end_time - start_time
    print("用时：", code_time)


def main2():
    watermark.photo_size_long(photo_path, long)


def main3():
    start_time = datetime.now()

    watermark.watermark_run_cpu(photo_path, logo_file)
    photo_path_ok = photo_path  # + "/ok"
    watermark.photo_scale_long_cpu(photo_path_ok, long)

    end_time = datetime.now()
    code_time = end_time - start_time
    print("用时：", code_time)


if __name__ == '__main__':
    main3()
