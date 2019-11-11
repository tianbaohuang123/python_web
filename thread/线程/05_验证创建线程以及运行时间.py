import time
import threading

# 如果创建Thread时执行的函数运行结束，意味着这个子线程结束了

def sing():
    """唱歌 5s"""
    for i in range(5):
        print("---%d I'm singing---" % (i + 1))
        time.sleep(1)

def main():
    # 在调用Thread之前先打印当前线程信息
    print(threading.enumerate())
    t_sing = threading.Thread(target=sing)

    # 在调用Thread之后打印
    print(threading.enumerate())
    t_sing.start()

    # 在调用start之后打印
    print(threading.enumerate())


if __name__ == "__main__":
    main()