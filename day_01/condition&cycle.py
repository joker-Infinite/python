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

    # break语句
    for str in 'python':
        if str == 'h':
            break
        print('当前字母', str)

    num = 0
    while num < 10:
        print('当前值', num)
        num += 1
        if num == 10:
            break

    # continue语句
    for st in 'python':
        if st == 'h':
            continue
        print(st)

    nv = 0
    while nv < 10:
        print('当前值', nv)
        nv += 1
        if nv == 10:
            continue

    nm = 0
    while nm < 10:
        nm += 1
        if nm % 2 == 0:
            continue
        print(nm, '是奇数')
