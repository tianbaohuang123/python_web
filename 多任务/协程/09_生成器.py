def create_num(all_num):

    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        yield a # 如果一个函数中有yield语句，那么这个就不再是函数，而是一个生成器的模板
        a, b = b, a + b
        current_num += 1

def main():
    obj = create_num(10)

    ret = next(obj)
    print(ret)

    ret = next(obj)
    print(ret)

    obj2 = create_num(2)
    ret = next(obj2)
    print(ret)

    for num in obj:
        print(num)

if __name__ == '__main__':
    main()