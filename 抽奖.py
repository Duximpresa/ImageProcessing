import random

u = 18 #一共多少个
v = 15 #抽多少个
# list = [i for i in range(1,u +1)]
# print(list)
# for i in range(10):
#     random.shuffle(list)
# a = random.sample(list,v)
# a.sort()
# print(a)
#
# print(f"{v}位幸运鹅：{a}")

def choujiang(u, v):
    list = [i for i in range(1, u + 1)]
    print(list)
    for i in range(10):
        random.shuffle(list)
    a = random.sample(list, v)
    a.sort()
    print(a)

    print(f"{v}位幸运鹅：{a}")

    return a

def main():
    a = choujiang(u, v)

if __name__ == '__main__':
    main()