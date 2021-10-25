import random
import requests

# u = 10 #一共多少个
# v = 4 #抽多少个

def lotterying(u, v):
    list = [i for i in range(1, u + 1)]
    print(list)
    for i in range(10):
        random.shuffle(list)
    a = random.sample(list, v)
    a.sort()
    print(a)

    print(f"{v}位幸运鹅：{a}")

    return a

def randomorg(u, v):
    url = f"https://www.random.org/sequences/?min=1&col=1&format=plain&rnd=new&max={u}"
    resp = requests.get(url)
    randlist = list(resp.text.split('\n'))[:-1]
    numlist = []
    for i in randlist:
        numlist.append(int(i))

    numlist = numlist[:v]
    numlist.sort()

    print(f"{v}位幸运鹅：{numlist}")
    return numlist


def main():
    # a = choujiang(u, v)
    list = randomorg(u, v)

if __name__ == '__main__':
    main()