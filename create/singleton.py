"""
单例模式:
下面这个类只能实例化一次,或者多，可以多次调用，但只创建一个实例
它可以看成是缓存模式的一个特例，该缓存模式只能缓存一个对象
"""

#使用元类
class Singleton(type):
    def __init__(self, *args, **kwargs): 
        #初始化类调用
        self.__instance = None
        super().__init__(*args, **kwargs) 

    def __call__(self, *args, **kwargs):
        #从类创建实例时调用
        if self.__instance is None:
            super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

#self.__instance
class Spam(metaclass=Singleton):
    def __init__(self):
        print('creating spam')


print(Spam() is Spam()) #True


#__new__
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            #obj = super(Singleton, cls)
            #issubclass(Singleton, cls) return True
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

class T(Singleton):
    name = "allen"
            
t1 = T()
t2 = T()
t1 is t2 #True


#共享属性
class Singleton(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Singleton, cls).__new__(cls, *args, **Kwargs)
        obj.__dict__ = cls._state
        return obj

class T(Singleton):
    name = "allen"


#decorator method
def singleton(cls, *args, **kwargs):
    instances = {}
    def _instance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _instance



@singleton
class T:
    name = "allen"


#using `import` a natural method
#singleton.py
class Singleton(object):
    def name(self):
        return 'allen'

name = Singleton()

from singleton import name
name.name #



"""实现缓存类"""

class Cached(type):
    def __init__(self, name):
        self._name = name
        self.__cached = {}
        super().__init__(name)

    def __call__(self, *args, **kwargs):
        if self._name in self.__cached:
            return self.__cached[name]
        else:
            super().__call__(*args, **kwargs)


