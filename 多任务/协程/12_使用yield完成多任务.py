import time

def task_1():
    while True:
        print("---task 1---")
        time.sleep(0.1)
        yield

def task_2():
    while True:
        print("---task 2---")
        time.sleep(0.1)
        yield

def main():
    t1 = task_1()
    t2 = task_2()

    # 先让t1运行一会，当t1中遇到yield的时候，再返回到22行，然后
    # 执行t2，当它遇到yield的时候，再次切换到t1中
    # 这样循环交替运行，最终实现了多任务...协程
    while True:
        next(t1)
        next(t2)

if __name__ == '__main__':
    main()