#!/usr/bin/python
# -*- coding:UTF-8 -*-

if __name__ == '__main__':
    import math
    import random

    # 数学函数
    '''
    abs 返回数字的绝对值
    '''
    print(abs(-20))
    '''
    ceil 返回数字的上入整数
    '''
    print(math.ceil(4.2))
    '''
    exp 返回e的x次幂(ex)
    '''
    print(math.exp(1))
    '''
    fabs 返回数字的绝对值
    '''
    print(math.fabs(-10))
    '''
    floor 返回数字的下舍整数
    '''
    print(math.floor(4.9))
    '''
    log 返回数字的自然对数
    '''
    print(math.log(100.12))
    '''
    log10 返回数字以十为基数的对数
    '''
    print(math.log10(100))
    '''
    max 返回给定参数的最大值
    '''
    print(max([0, 1, 2, 3, 22, 33, 55, 21]))
    '''
    min 返回给定参数的最小值
    '''
    print(min([0, 1, 2, 3, 22, 33, -55, 21]))
    '''
    modf 分别返回参数的整数部分和小数部分
    '''
    print(math.modf(3.9))
    '''
    pow 返回a的b次方
    '''
    print(math.pow(2, 3))
    '''
    round 返回浮点数的四舍五入值
    '''
    print(round(3.66, 1))
    '''
    sqrt 返回参数的平方根
    '''
    print(math.sqrt(16))

    # 随机函数
    '''
    choice 从序列的元素中随机挑一个元素
    '''
    print(random.choice(range(10)))  # range:创建一个整数列表
    '''
    randrange 返回指定区间以基数递增的随机数
    '''
    print(random.randrange(0, 10, 5))
    '''
    random 随机生成一个实数，它在[0,1]之间
    '''
    print(random.random())
    '''
    shuffle 将序列的所有元素随机排序
    '''
    ll = [0, 6, 4, 2, 7]
    random.shuffle(ll)
    print(ll)
    random.shuffle(ll)
    print(ll)
    '''
    uniform 随机生成参数一与参数二之间的实数(浮点数)
    '''
    print(random.uniform(1, 5))
