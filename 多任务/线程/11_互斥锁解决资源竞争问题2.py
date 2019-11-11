import threading
import time

g_num = 0

def test1(num):
    global g_num

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()

    print("---in test1 g_num=%d---" % g_num)

def test2(num):
    global g_num

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()

    print("---in test2 g_num=%d---" % g_num)

# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()

def main():
    t_test1 = threading.Thread(target=test1, args=(1000000,))
    t_test2 = threading.Thread(target=test2, args=(1000000,))

    t_test1.start()
    t_test2.start()

    # 等待上面的2个线程执行完毕...
    time.sleep(10)

    print("---in main g_num=%d---" % g_num)

if __name__ == '__main__':
    main()
