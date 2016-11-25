"""建造者设计模式:
创建一个由多个部分构成的对象，而且它的构成需要一步接一步地完成。
只有当各个部分都创建好，这个对象才算是完整的。

建造者模式将一个复杂对象的构造过程与其表现分离
同一个构造过程可用于创建多个不同的表现

模式中，有两个参与者：建造者 （builder）和指挥者（director）

区分工厂模式和建造者模式,区别在于工厂模式以单个步
骤创建对象，而建造者模式以多个步骤创建对象，并且几乎始终会使用一个指挥者

在工厂模式下，会立即返回一个创建好的对象；而在建造者模式下，仅在需
要时客户端代码才显式地请求指挥者返回最终的对象
"""

"""过程描述：
建立一个模板，在建立比模板更具体的模板时，实例化模板而不是继承，
在具体的模板中添加实例方法对模板实例的数据进行操作。这是一个建
立的过程。而具体的建立地点委托给指挥者。"""



MINI14 = '1.4GHz Mac mini'

class AppleFactory:
    class MacMini14:   
    #inner class 禁止直接实例化一个类的简洁方式
        def __init__(self):
            self.memory = 4
            self.hdd = '1 TB'
            self.gpu = 'NVIDIA GT720M'

        def __str__(self):
            info = ('Model: {}'.format(MINI14),
                    'Memory: {}GB'.format(self.memory),
                    'Hard Disk: {}GB'.format(self.hdd),
                    'Graphics Card: {}'.format(self.gpu))
            return '\n'.join(info)

    def builder(self, model):
        if (model == MINI14):
            return self.MacMini14()
        else:
            print("I dont't know how to build {}".format(model))

#builder pattern
class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('CS2016')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model

class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def constructer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                           self.builder.configure_hdd(hdd),
                           self.builder.configure_gpu(gpu))]

    @property 
    def computer(self):
        return self.builder.computer

def factory_main():
    afac = AppleFactory()
    mac_mini = afac.builder(MINI14)
    print(mac_mini)

def builder_main():
    engineer = HardwareEngineer()
    engineer.constructer(hdd=500, memory=8, gpu='NVIDIA GTX1060M')
    computer = engineer.computer
    print(computer)

#比萨订购的应用示例
from enum import Enum 
import time


"""玛格丽特比萨的配料是双层马苏里拉奶酪（mozzarella）和
牛至（oregano），而奶油熏肉比萨的配料是马苏里拉奶酪（mozzarella）、熏肉（bacon）、火腿（ham）、
蘑菇（mushrooms）、紫洋葱（red onion）和牛至（oregano），如下面的代码所示。"""

#用枚举类型定义Pizza的配方
PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms read_onion oregano')
STEP_DELAY = 3

class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None  #材料
        self.sauce = None  #材料
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print('preparing the {} dough of your {}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))

"""每个建造者都创建一个Pizza实例，并包含遵从比萨制作
流程的方法： prepare_dough()、 add_sauce、 add_topping()和bake()。"""

class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued #制作流程标记
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        print('adding the topping (double mozzarella, oregano) to your margarita')
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella,
            PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (double mozzarella, oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')

class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print('adding the creme fraiche sauce to your creamy bacon')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('done with the creme fraiche sauce')

    def add_topping(self):
        print("adding the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano) to youur creamy bacon")
        self.pizza.topping.append([t for t in (PizzaTopping.mozzarella,
                                               PizzaTopping.bacon,
                                               PizzaTopping.ham,
                                               PizzaTopping.mushrooms,
                                               PizzaTopping.red_onion,
                                               PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')

class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_sauce,
                             builder.add_topping, builder.bake)]

    @property 
    def pizza(self):
        return self.builder.pizza 

def main():
    waiter = Waiter()
    builder = MargaritaBuilder()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza 
    print(pizza)



"""工厂模式相比，建造者模式
是更好的选择。
想要创建一个复杂对象（对象由多个部分构成，且对象的创建要经过多个不同的步骤，
这些步骤也许还需遵从特定的顺序）

要求一个对象能有不同的表现，并希望将对象的构造与表现解耦

想要在某个时间点创建对象，但在稍后的时间点再访问"""
