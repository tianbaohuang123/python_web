import multiprocessing
import time
import os

def sing():
    """唱歌"""
    while True:
        print("---子进程 pid=%d---父进程pid=%d" % (os.getpid(), os.getppid()))
        time.sleep(1)

def main():
    print("---主进程 pid=%d---父进程pid=%d" % (os.getpid(), os.getppid()))
    p_sing = multiprocessing.Process(target=sing)
    p_sing.start()

if __name__ == '__main__':
    main()