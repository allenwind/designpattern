"""一般而言，我们想要创建的是一种领域特定语言（Domain Specific Language， DSL）。 DSL
是一种针对一个特定领域的有限表达能力的计算机语言。很多不同的事情都使用DSL，比如，战
斗模拟、记账、可视化、配置、通信协议等。 DSL分为内部DSL和外部DSL"""

"""内部DSL构建在一种宿主编程语言之上。内部DSL的一个例子是，使用Python解决线性方程
组的一种语言。使用内部DSL的优势是我们不必担心创建、编译及解析语法，因为这些已经被宿
主语言解决掉了。劣势是会受限于宿主语言的特性。如果宿主语言不具备这些特性，构建一种表
达能力强、简洁而且优美的内部DSL是富有挑战性的


外部DSL不依赖某种宿主语言。 DSL的创建者可以决定语言的方方面面（语法、句法等），
但也要负责为其创建一个解析器和编译器。为一种新语言创建解析器和编译器是一个非常复杂、
长期而又痛苦的过程"""

"""在某种意义上，五线谱是音乐的语言，音
乐演奏者是这种语言的解释器。"""

#使用巴科斯-诺尔形式（Backus-Naur Form， BNF）表示法来定义语法:

"""
语法定义
event ::= command token receiver token arguments
command ::= word+
word ::= a collection of one or more alphanumeric characters
token ::= ->
receiver ::= word+
arguments ::= word+

"""


"""解析器模式负责把特定的符号序列进行解析，转换到宿主语言的具体操作上
相当于翻译的过程，把一种符号翻译到另外一种符号，但语义相同

"""


from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums

class Gate:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' is self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True

    def close(self):
        print('closing the gate')
        self.is_open = False

class Garage:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the garage')
        self.is_open = True

    def close(self):
        print('closing the garage')
        self.is_open = False

class Aircondition:
    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the aircondition')
        self.is_on = True

    def turn_off(self):
        print('turning off the aircondition')
        self.is_on = False

class Heating:
    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the heating')
        self.is_on = True

    def turn_off(self):
        print('turning off the heading')
        self.is_on = False

class Boiler:
    def __init__(self):
        self.temperature = 83

    def __str__(self):
        return 'boiler temperature: {}'.format(self.temperature)

    def increase_temperature(self, amount):
        print("increasing the boiler's temperature by {} degrees".format(amount))
        self.temperature += 1

    def decrease_temperature(self, amount):
        print("decreasing the boiler's temperature by {}".format(amount))
        self.temperature -= amount


class Fridge:
    def __init__(self):
        self.temperature = 2

    def __str__(self):
        return 'fridge temperature: {}'.format(self.temperature)

    def increase_temperature(self, amount):
        print("increasing the fridge's temperature by {} degrees".format(amount))
        self.temperature += amount

    def decrease_temperature(self, amount):
        print("decreasing the fridge's temperature by {}".format(amount))
        self.temperature -= amount

def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress('->')
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token+argument)

    gate = Gate()
    garage = Garage()
    airco = Aircondition()
    heating = Heating()
    boiler = Boilder()
    fridge = Fridge()

    tests = ('open -> gate',
             'close -> garage',
             'turn on -> aircondition',
             'turn off -> heating',
             'increase -> boiler temperature -> 5 degrees',
             'decrease -> fridge temperature -> 2 degrees')

    open_actions = {'gate': gate.open,
                    'garage': garage.open,
                    'aircondition': airo.turn_on,
                    'heating': heating.turn_on,
                    'boiler temperature': boilder.increase_temperature,
                    'fridge temperature': fridge.increase_temperature}
    close_actions = {'gate': gate.close,
                     'garage': garage.close,
                     'aircondition': airco.turn_off,
                     'heating': heating.turn_off,
                     'boiler temperature': boiler.decrease_temperature,
                     'fridge temperature': fridge.decrease_temperature}

    


















































