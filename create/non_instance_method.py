"""控制类不能实例化"""

class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("can't instanced")

class Grom(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print('grok {}'.format(x))

