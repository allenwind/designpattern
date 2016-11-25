"""单例模式:
下面这个类只能实例化一次,或者多，可以多次调用，但只创建一个实例"""


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print('creating spam')


print(Spam() is Spam()) #True
        
