from ImageProcessing import watermark

photo_path = r"F:\Video\2021广西设计周记录\photo\10_17\临时选片"
logo_file = r"F:\Video\2021广西设计周宣传视频\青秀区\logo\2020G广西设计周logo_白.png"
long = 1920


def main():
    watermark.watermark_run(photo_path, logo_file)
    photo_path_ok = photo_path + "/ok"
    watermark.photo_size_long(photo_path_ok, long)

def main2():
    watermark.photo_size_long(photo_path, long)


if __name__ == '__main__':
    main()
