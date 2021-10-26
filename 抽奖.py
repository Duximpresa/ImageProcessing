from ImageProcessing import lottery

u = 15  # 一共多少个
v = 6  # 抽多少个


def main():
    list = lottery.randomorg(u, v)
    with open("luckylist.txt", 'w', encoding='utf-8') as f:
        f.write(f"{v}位幸运鹅：")
        for i in list:
            f.write(str(i) + ",")
        f.close()


if __name__ == '__main__':
    main()
