"""
建造者模式的一种变体实现：
一种有趣的建造者模式变体，这种变体会链式地调用建造者方法，通过将建造者本身
定义为内部类并从其每个设置器方法返回自身来实现。方法build()返回最终的对象。
这个模式被称为流利的建造者

SQLAlchemy中的查询方法也是链式
MongoDB的查询也是如此：
db.collection.find().skip(100).limit(10).sort({_id: -1})

同样，也类似于pymongo模块
db.collection.find({"key": "value"}).sort({"_id": 1}).limit(100).skip(100)

"""



class Pizza_:
    #这是一个绝妙的方法
    def __init__(self, builder):
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese

    def __str__(self):
        garlic = 'yes' if self.garlic else 'no'
        cheese = 'yes' if self.extra_cheese else 'no'
        info = ('Garlic: {}'.format(garlic), 'Extra cheese: {}'.format(cheese))
        return '\n'.join(info)

    class PizzaBuilder:
        def __init__(self):
            self.extra_cheese = False
            self.garlic = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True  #方法可以互换
            return self

        def build(self):
            return Pizza(self)

class LinkList:
    def __init__(self):
        self._list = list()

    def append(self, item):
        self._list.append(item)
        return self


if __name__ == '__main__':
    main()
    pizza = Pizza_.PizzaBuilder().add_garlic().add_extra_cheese().build()
    list_ = LinkList().append(1).append(2).append(3)