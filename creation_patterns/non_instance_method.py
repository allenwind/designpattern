"""控制类不能实例化
这中方法这设计模式上展示没有称呼，但控制类不能实例化
某些情况还是必要的。



"""

class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("can't instanced")

class Grom(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print('grok {}'.format(x))

