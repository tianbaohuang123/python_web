import time
from collections.abc import Iterable
from collections.abc import Iterator

class Classmate(object):
    def __init__(self):
        self.name = list()

    def add(self, name):
        self.name.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个 可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return ClassIterator(self)

class ClassIterator(object):

    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        pass

    def __next__(self):
        return self.obj.name[0]

def main():
    classmate = Classmate()
    classmate.add("laowang")
    classmate.add("wanger")
    classmate.add("zhangsan")

    # print("判断classmate是否是可以迭代的对象：", isinstance(classmate, Iterable))
    #
    # classmate_iterator = iter(classmate)
    # print("判断classmate_iterator是否是可以迭代的对象：", isinstance(classmate_iterator, Iterable))
    # print(next(classmate_iterator))

    for name in classmate:
        print(name)
        time.sleep(1)

if __name__ == '__main__':
    main()