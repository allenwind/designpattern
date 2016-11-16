"""
如果合理，可以直接将功能添加到对象所属的类（例如，添加一个新的方法）
使用组合
使用继承

与继承相比，通常应该优先选择组合，因为继承使得代码更难复用，继承关系是静态的，并
且应用于整个类以及这个类的所有实例"""



"""设计模式为我们提供第四种可选方法，以支持动态地（运行时）扩展一个对象的功能，这种
方法就是修饰器。 修饰器（Decorator）模式能够以透明的方式（不会影响其他对象）动态地将功
能添加到一个对象中"""

#Python修饰器能做的实际上比修饰器模式多得多
"""
def func():
    pass

@decorator1
@decorator2
@decorator3
def func():
    pass

use this pattern to add function in func"""

"""应用：
数据校验
事务处理（这里的事务类似于数据库事务，意味着要么所有步骤都成功完成，要么事务失败）
缓存
日志
监控
调试
业务规则
压缩
加密"""

"""使用修饰器模式的另一个常见例子是图形用户界面（Graphical User Interface， GUI）工具集。
在一个GUI工具集中，我们希望能够将一些特性，比如边框、阴影、颜色以及滚屏，添加到单个
组件/部件"""

#修饰器模式是实现横切关注点的绝佳方案，因为横切关注点通用但不太适合使用面向对象编程范式来实现
import timeit
import functools

def memory(func):
    cache = dict()
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wrapper

@memory
def fibonacci_naive(n):
    assert (n >= 0), 'n must be >=0'
    return n if n in (0, 1) else fibonacci_naive(n-1) + fibonacci_naive(n-2)

known = {0: 0, 1: 1}
def fibonacci(n):
    assert (n >= 0), 'n must be >= 0'
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

#use decorator design pattern
def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('I am decorator1')
        result = func(*args, **kwargs)
        return result
    return wrapper

def decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('I am decorator2')
        result = func(*args, **kwargs)
        return result
    return wrapper

def decorator3(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('I am decorator3')
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator1
@decorator2
@decorator3
def func():
    pass

if __name__ == '__main__':
    t_navie = timeit.Timer('fibonacci_naive(8)', 'from __main__ import fibonacci_naive')
    
    t = timeit.Timer('fibonacci(8)', 'from __main__ import fibonacci')


    print(t.timeit())
    print(t_navie.timeit())

    func()

























