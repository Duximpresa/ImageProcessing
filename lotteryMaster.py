from ImageProcessing import lottery

u = int(input("请输入参加抽奖的人数:"))
v = int(input("请输入幸运鹅的人数:"))

def main():
    list = lottery.randomorg(u, v)
    with open("luckylist.txt", 'w') as f:
        f.write(f"{v}位幸运鹅：")
        for i in list:
            f.write(str(i) + ",")
        f.close()

main()