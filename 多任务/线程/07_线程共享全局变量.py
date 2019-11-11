import threading
import time

g_num = 100

def test1():
    global g_num

    g_num += 1
    print("---in test1 g_num=%d---" % g_num)

def test2():
    print("---in test2 g_num=%d---" % g_num)

def main():
    t_test1 = threading.Thread(target=test1)
    t_test2 = threading.Thread(target=test2)

    t_test1.start()
    time.sleep(1)

    t_test2.start()
    time.sleep(1)

    print("---in main g_num=%d---" % g_num)

if __name__ == '__main__':
    main()
