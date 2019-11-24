import time
from collections.abc import Iterable
from collections.abc import Iterator

class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个 可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return self # 调用iter(xxobj)的时候 只要 __iter__方法返回一个 迭代器即可，至于是自己还是别的对象都可以，但是要保证是一个迭代器（即实现了 __iter__ __next__方法）

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration

def main():
    classmate = Classmate()
    classmate.add("laowang")
    classmate.add("wanger")
    classmate.add("zhangsan")

    for name in classmate:
        print(name)
        time.sleep(1)

if __name__ == '__main__':
    main()