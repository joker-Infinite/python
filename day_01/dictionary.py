#!/usr/bin/python
# -*- coding:UTF-8 -*-
if __name__ == '__main__':
    dict = {0: 'a', 1: 'b', 2: 'c'}
    '''
    copy 返回对一个字典的浅复制
    '''
    print(dict.copy())
    '''
    fromkeys 创建一个新的字典
    '''
    bd = {9: '', 8: '', 7: ''}
    nbd = bd.fromkeys((0, 1, 2), 20)
    print(nbd)
    '''
    get 返回字典中指定key的value，没有则返回默认值
    '''
    print(dict.get(1))
    print(dict.get(6, 'nonono'))
    '''
    items 以列表的形式将字典返回
    '''
    print(dict.items())
    '''
    keys 以列表返回所有的键
    '''
    print(dict.keys())
    '''
    setdefault 与get方法类似，如果所查键不存在，将会将所查键及默认参数加入
    '''
    dict.setdefault(3, 'd')
    print(dict)
    '''
    update 将一个字典的参数导入另一个字典
    '''
    dict.update(nbd)
    print(dict)
    '''
    values 以列表的形式返回字典的value值
    '''
    print(dict.values())
    '''
    pop 删除字典中指定的key,返回被删除key的value
    '''
    print(dict.pop(0))
    print(dict)
    '''
    popitem 返回并删除字典中的最后一对键值
    '''
    print(dict.popitem())
