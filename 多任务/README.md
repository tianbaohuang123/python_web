# 多任务
线程：threading
创建线程：t_test = threading.Thread(target=FUNC, args=(,))   （target：线程调用的函数名，args：入参，如果没有则不需要填写）
启动线程：t_test.start
数据共享：线程共享全局变量
互斥锁：解决资源竞争问题
       创建互斥锁（默认未上锁）：mutex = threading.Lock()
       上锁：mutex.acquire
       解锁：mutex.release

查看当前正在运行的线程：threading.enumerate()

=======================
进程：multiprocessing

创建进程：p_test = multiprocessing.Process(target=FUNC, args=(,), kwargs={})   （target：进程调用的函数名，args：入参，如果没有则不需要填写, kwargs：字典形式的入参，如果没有则不需要填写）
启动进程：p_test.start
进程pid：os.getpid(), os.getppid()   (pid：子进程pid，ppid：父进程pid)
数据共享：多进程之间不共享全局变量，通过Queue实现数据共享
    创建队列：q_test = multiprocessing.Queue()
    创建线程时，将队列的引用作为实参传递到里面：
    p_test1 = multiprocessing.Process(target=FUNC1, args=(q_test,)))
    p_test2 = multiprocessing.Process(target=FUNC2, args=(q_test,))
    p_test1.start()
    p_test2.start()
进程池：
from multiprocessing import Pool
定义线程池：po = Pool(3)  # 最大进程数3
for i in XX:
    # Pool().apply_async(要调用的目标, (传递给目标的参数元祖,))
    # 每次循环将会用空闲出来的子进程去调用目标
    po.apply_async(FUNC, (,))
关闭进程池：po.close()    # 关闭后po不再接收新的请求
等待po中所有子进程执行完成：po.join()   # 必须放在close语句之后

======================
协程：yield, greenlet, gevent(monkey)
yield:如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器模板
在多个函数中添加yield语句，当执行到yield时，会去执行另一个函数，实现多函数交替运行

例如：task1， task2中均采用while True循环处理数据，并在数据处理完成后执行yield
t1 = task1()
t2 = task2()
while True:
    next(t1)
    next(t2)

======================
greenlet：在两函数数据处理逻辑中交替运行

例如：task1， task2中均采用while True循环处理数据，并在数据处理完成后执行switch(),跳转到另一个函数
gr1 = greenlet(task1)
gr2 = greenlet(task2)

# 切换到gr1中运行
gr1.switch()

======================
gevent:

import gevent
from gevent import monkey
打补丁：monkey.patch_all()
创建gevent: g_test = gevent.spawn(FUNC, ARG)
获取gevnet id: gevent.getcurrent()
等待gevent执行完成: g_test.join()

批量处理：gevent.joinall([gevent.spawn(FUNC1, ARG1), gevent.spawn(FUNC2, ARG2)])





