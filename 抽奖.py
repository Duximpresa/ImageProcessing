from ImageProcessing import lottery

u = 10 #一共多少个
v = 3 #抽多少个

def main():
    list = lottery.randomorg(u, v)
    with open("luckylist.txt", 'w') as f:
        f.write(f"{v}位幸运鹅：")
        for i in list:
            f.write(str(i) + ",")
        f.close()


if __name__ == '__main__':
    main()