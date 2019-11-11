def create_num(all_num):

    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        ret = yield a # 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器的模板
        print(">>>ret>>>", ret)
        a, b = b, a + b
        current_num += 1

def main():
    # 如果在调用create_num的时候，发现这个函数中有yield 那么此时，不是调用函数，而是创建一个生成器对象
    obj = create_num(10)

    ret = next(obj)
    print(ret)

    # send里面的数据会传递给第7行，当做yield a的结果，然后ret保存这个结果，，，
    # send的结果是下一次调用yield时 yield后面的值
    ret = obj.send("hahaha")
    print(ret)

if __name__ == '__main__':
    main()