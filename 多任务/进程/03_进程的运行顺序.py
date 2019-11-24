import multiprocessing
import time
import os

def sing():
    """唱歌"""
    while True:
        print("---子进程sing pid=%d---父进程pid=%d" % (os.getpid(), os.getppid()))
        time.sleep(1)

def dance():
    """跳舞"""
    while True:
        print("---子进程dance pid=%d---父进程pid=%d" % (os.getpid(), os.getppid()))
        time.sleep(1)

def main():
    print("---主进程main pid=%d---父进程pid=%d" % (os.getpid(), os.getppid()))
    p_sing = multiprocessing.Process(target=sing)
    # p_dance = multiprocessing.Process(target=dance)
    p_sing.start()

    p_dance = multiprocessing.Process(target=dance)
    p_dance.start()

if __name__ == '__main__':
    main()