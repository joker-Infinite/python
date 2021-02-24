#!/usr/bin/python
# -*- coding: UTF-8 -*-
if __name__ == '__main__':
    a = 3
    b = 2
    c = 5
    # 算数运算符
    print('算数运算符')
    '''
    加法
    '''
    print(a + b)
    print(a + b + c)
    '''
    减法
    '''
    print(a - b)
    print(a - b - c)
    '''
    乘法
    '''
    print(a * b)
    print(a * b * c)
    '''
    除法
    '''
    print(a / b)
    print(a / b / c)
    '''
    取模
    '''
    print(a % b)
    print(a % b % c)
    '''
    幂
    '''
    print(a ** b)
    print(a ** b ** c)
    '''
    取整
    '''
    print(a // b)
    print(a // b // c)

    # 比较运算符
    print('比较运算符')
    '''
    等于
    '''
    print(c == b)
    '''
    不等于
    '''
    print(c != b)
    '''
    大于
    '''
    print(a > b)
    '''
    小于
    '''
    print(a < b)
    '''
    大于等于
    '''
    print(a >= b)
    '''
    小于等于
    '''
    print(a <= b)

    # 赋值运算符
    print('赋值运算符')
    '''
    简单赋值
    '''
    a = b
    print(a)
    '''
    加法赋值
    '''
    a += b
    print(a)
    '''
    减法赋值
    '''
    a -= b
    print(a)
    '''
    乘法赋值
    '''
    a *= b
    print(a)
    '''
    除法赋值
    '''
    a /= b
    print(a)
    '''
    取模赋值
    '''
    a %= b
    print(a)
    '''
    幂赋值
    '''
    a **= b
    print(a)
    '''
    取整除赋值
    '''
    a //= b
    print(a)

    # 位运算符
    print('位运算符')
    m = 0B00111100
    n = 0B00001101

    '''
    按位与:参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
    '''
    print(m & n)
    '''
    按位或:只要对应的二个二进位有一个为1时，结果位就为1
    '''
    print(m | n)
    '''
    按位异或:当两对应的二进位相异时，结果为1
    '''
    print(m ^ n)
    '''
    按位取反:对数据的每个二进制位取反,即把1变为0,把0变为1
    '''
    print(~m)
    '''
    左移动:运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0
    '''
    print(m << 2)
    '''
    右移动:把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数
    '''
    print(m >> 2)

    # 逻辑运算符
    print('逻辑运算符')
    x = 10
    y = 20
    '''
    布尔“与”:如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值
    '''
    print(x and y)
    '''
    布尔“或”:如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值
    '''
    print(x or y)
    '''
    布尔“非”:如果 x 为 True，返回 False 。如果 x 为 False，它返回 True
    '''
    print(not a)

    # 成员运算符
    print('成员运算符')
    j = 1
    k = 2
    tel = (1, 2, 3, 4, 5, 6)
    '''
    in:如果在指定的序列中找到值返回 True，否则返回 False
    '''
    print(j in tel)
    '''
    not in:如果在指定的序列中没有找到值返回 True，否则返回 False
    '''
    print(j not in tel)

    # 身份运算符
    print('身份运算符')
    '''
    is:是判断两个标识符是不是引用自一个对象
    '''
    s = 20
    l = 20
    print(s is l)
    '''
    is not:是判断两个标识符是不是引用自不同对象
    '''
    l = 30
    print(s is not l)

    # is 与 == 区别：
    # is 用于判断两个变量引用对象是否为同一个(同一块内存空间)， == 用于判断引用变量的值是否相等
