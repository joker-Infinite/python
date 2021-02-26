#!/usr/bin/python
# -*-coding:UTF-8-*-
if __name__ == '__main__':
    import operator

    ls = [1, 2, 3, 4, 1, 1]
    ns = []
    obj = (3, 0, 90)
    # 列表方法
    '''
    append 在列表末尾添加新元素
    '''
    ls.append(30)
    print(ls)
    '''
    count 统计某一元素在列表中出现的次数
    '''
    print(ls.count(1))
    '''
    extend 在列表后追加一个新的列表
    '''
    ns.extend(ls)
    print(ns)
    '''
    index 从列表中找出某个值第一个匹配项的位置
    '''
    print(ls.index(3))
    '''
    insert 将指定对象插入列表指定位置
    '''
    ls.insert(0, obj)
    print(ls)
    '''
    pop 移除列表中的一个元素
    '''
    print(ls.pop(5))
    '''
    remove 移除列表中某个值的第一匹配项
    '''
    ls.remove(3)
    print(ls)
    '''
    reverse 反向列表中的元素2
    '''
    ls.reverse()
    print(ls)
    '''
    sort 对列表进行排序
    '''
    arr = [3, 2, 0, 6, 4]
    arr.sort(reverse=True)
    print(arr)
