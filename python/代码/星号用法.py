# -*- coding: utf-8 -*-
#!/usr/bin/env python



# 一个星号*的时候，表示传的参数个数是可变的
# 参数类型：全部    返回值类型：元组def fish1(*x):
def fish1(*x):
    print 'fish1',x
if __name__ == '__main__':
    fish1(1==9, (2,3), [1,'2',{'3':'4'}], {'a':'s'}, 'x')


# 两个星号**的时候，表示是可变的关键字参数
# 参数类型：关键字参数    返回值类型：字典
def fish2(**x):
    print 'fish2',x
if __name__ == '__main__':
    fish2(a=1, b=2, c=3)

# 可变参数总结
def fish3(*x,**y):
    print 'fish3',x,y
if __name__ == '__main__':
    fish3(1==9, 2*2, 'x', a=1, b=2, c=3)


# 参数传递逆过程，一个星号*的时候，可以自动解包
# 参数类型：可解包参数    返回值类型：解包后的参数
# 解包字典返回的是 字典的键
def fish4(x,y):
    print 'fish4',x,y
if __name__ == '__main__':
    data_source = [1,2]
    fish4(data_source,0)
    fish4(*data_source)
    data_source2 = ['a',['s','d']]
    fish4(*data_source2)
    data_source3 ={'fish_1': 'abc_1', 'fish_2': 'abc_2'}
    fish4(*data_source3)

# 参数传递逆过程，两个星号**的时候，只能解包字典
# 参数类型：字典    返回值类型：字典的键对应的值
def fish5(fish_1,fish_2):
    print 'fish5',fish_1,fish_2,type(fish_1)
if __name__ == '__main__':
    data_source = {'fish_1': 'abc_1', 'fish_2': 'abc_2'}
    fish5(**data_source)
    
# 总结1, 先将字典解包，然后再组合成字典
def fish6(**x):
    print 'fish6',x
if __name__ == '__main__':
    data_source = {'fish_1': 'abc_1', 'fish_2': 'abc_2'}
    fish6(**data_source)

# 总结2，解包后，传可变参数个数,将返回值组合成元组
def fish7(*x):
    print 'fish7',x
if __name__ == '__main__':
    data_source = [1,'a',[5,'s'],{'asd':'fgh'}]
    fish7(*data_source)
