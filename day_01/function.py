#!/usr/bin/python3
if __name__ == '__main__':
    def MAX(a, b):
        if a > b:
            return a
        else:
            return b


    print(MAX(3, 4))


    def address(a):
        print(id(a))
        a = 20
        print(id(a))


    a = 1
    print(id(a))
    address(a)
    print(id(a))


    def changeList(ls):
        ls.append([1, 2, 3])
        print('函数内：', ls)
        return


    ls = [0, 4, 5, 6]
    print('函数外-前：', ls)
    changeList(ls)
    print('函数外-后：', ls)


    def defaultData(name, age=90):
        print('名字：', name)
        print('年龄：', age)


    defaultData('小明', 30)
    defaultData(name='小李')


    def moreData(a, *arr):
        print(a)
        print(arr)


    moreData(1, 2, 3, 5, 6)


    def dict(d, **dic):
        print('字典：')
        print(d)
        print(dic)


    dict(1, a=2, b=3)
