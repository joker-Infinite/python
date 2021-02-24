#!/usr/bin/python
# -*- coding:UTF-8 -*-
if __name__ == '__main__':
    a = 1
    # 循环语句
    while a < 11:
        # 条件语句
        if a % 2 == 0:
            print(a, '偶数')
        else:
            print(a, '奇数')
        a += 1

    # while循环语句
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even = []
    odd = []
    while len(numbers) > 0:
        number = numbers.pop()
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    print(even, odd)

    # while循环使用else
    i = 0
    while i == 0:
        print(i, '是0')
        i += 1
    else:
        print(i, '不是0')

    # for循环
    letter = ['a', 'b', 'c', 'd']
    for item in 'number':
        print(item)

    for it in letter:
        print("当前字母是:", it)

    for index in range(len(letter)):
        print(letter[index], index)
