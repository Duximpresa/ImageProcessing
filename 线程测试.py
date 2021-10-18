from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(count):
    print(1)
    print(f'以完成{count}')


if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(1) as t:
        for i in range(100):
            t.submit(fn, name=f'i')
    # 等待线程池中的任务全部执行完毕. 才继续执行(守护)
    print("123")
