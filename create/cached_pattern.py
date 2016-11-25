import weakref

"""缓存模式:
下面这个例子是基于类的名字的缓存
当然，也可以对其他属性进行缓存，但用名字更直观、直接了当

在编程方法上，下面采用的元类方法。单用函数也可以，但用元类这种黑魔法
更能展示Python的强大
"""

class Cached(type):
    """这个类在Spam创建的时候起作用,我们在下面加标记"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #保存值的弱引用, 当引用为零的时候自动垃圾回收
        self.__cache = weakref.WeakValueDictionary()
        print('type.__init__')

    def __call__(self, *args):
        #在Spam实例化时调用
        print('type.__call__')
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj

class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name

