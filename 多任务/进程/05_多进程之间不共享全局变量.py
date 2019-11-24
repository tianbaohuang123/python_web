import  multiprocessing
import time

nums = [11, 22, 33]

def test1():
    nums.append(44)
    print("在进程1中nums=%s" % str(nums))
    time.sleep(3)

def test2():
    print("在进程2中nums=%s" % str(nums))

def main():
    p_test1 = multiprocessing.Process(target=test1)
    p_test1.start()

    # 堵塞进程，直至进程处理结束
    p_test1.join()

    p_test2 = multiprocessing.Process(target=test2)
    p_test2.start()

if __name__ == '__main__':
    main()
