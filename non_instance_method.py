from urllib.request import Request

class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("can't instanced")

class Grom(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print('grok {}'.format(x))

