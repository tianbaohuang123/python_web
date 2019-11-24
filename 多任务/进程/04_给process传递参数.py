import multiprocessing
import os

def test(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


def main():
    print("---主进程main pid=%d---父进程pid=%d" % (os.getpid(), os.getppid()))
    p_test = multiprocessing.Process(target=test, args=(11, 22, 33, 44, 55, 66, 77, 88), kwargs={"name":"tb"})
    p_test.start()

if __name__ == '__main__':
    main()