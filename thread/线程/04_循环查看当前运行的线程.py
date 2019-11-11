import time
import threading

# 如果创建Thread时执行的函数运行结束，意味着这个子线程结束了

def sing():
    """唱歌 5s"""
    for i in range(5):
        print("---%d I'm singing---" % (i + 1))
        time.sleep(1)

def dance():
    """跳舞 5s"""
    for i in range(10):
        print("---%d I'm dancing---" % (i + 1))
        time.sleep(1)

def main():
    t_sing = threading.Thread(target=sing)
    t_dance = threading.Thread(target=dance)
    t_sing.start()
    t_dance.start()

    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)

if __name__ == "__main__":
    main()