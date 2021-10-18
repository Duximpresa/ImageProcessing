from ImageProcessing import watermark
from datetime import datetime

photo_path = r"I:\2020广西设计周-专业拍摄团队素材\照片素材\5号照片汇总\2020.12.5设计周出图盘\烧鸡出片盘\烧鸡出片无logo"
logo_file = r"F:\Video\2021广西设计周宣传视频\青秀区\logo\2020G广西设计周logo_白.png"
long = 1920


def main():
    start_time = datetime.now()
    watermark.watermark_run(photo_path, logo_file)
    photo_path_ok = photo_path + "/ok"
    watermark.photo_size_long(photo_path_ok, long)
    end_time = datetime.now()
    code_time = end_time - start_time
    print("用时：", code_time)

def main2():
    watermark.photo_size_long(photo_path, long)


if __name__ == '__main__':
    main()
