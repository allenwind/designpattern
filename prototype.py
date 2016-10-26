#copy
#prototype design pattern


import copy

class A:
"just a test for using deepcopy"
    def __init__(self):
        self.year = 2016
        self.status = 'great'

class B(A):
    def __init__(self):
        A.__init__(self)
        self.month = 10

    def __str__(self):
        return '{}, {}, {}'.format(self.year, self.month, self.status)

"""可视化工具套件（Visualization Toolkit， VTK)是原型模式的一
个应用。 VTK是一个开源的跨平台系统，用于三维计算机图形/图片处理以及可视化。 VTK使用
原型模式来创建几何元素的克隆"""

#当我们已有一个对象，并希望创建该对象的一个完整副本时，原型模式就派上用场了
#我们知道对象的某些部分会被变更但又希望保持原有对象不变之时，通常需要对象的一个副本。在
#这样的案例中，重新创建原有对象是没有意义的

#浅副本构造一个新的复合对象后，（会尽可能地）将在原始对象中找到的对象的引用插入新对象中。

#深副本构造一个新的复合对象后，会递归地将在原始对象中找到的对象的副本插入新对象中
from collections import OrderedDict


class Book:
    def __init__(self, name, authors, price, **rest):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        list_ = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            list_.append('{}: {}'.format(i, ordered[i]))
            if i == 'prices':
                list_.append('$')

            list_.append('\n')
        return ''.join(list_)

class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        target = self.objects.get(identifier)
        if not target:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))

        obj = copy.deepcopy(target)
        obj.__dict__.update(attr)
        return obj

        