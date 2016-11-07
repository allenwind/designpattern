"""观察者模式:

在一个对象的状态改变时更新另外一组对象
在两个视图同时应用相同的模板的情况，当模板数据改变时候，两个视图同时改变

因此，这这个结构中，这两个视图在监控（观察）模板的变化"""

#关注点分离原则背后的思想
"""例子：
RSS、MVC

观察者模式描述单个对象（发布者，又称为主持者或可观察者）与一个或多个对象（订阅者，
又称为观察者）之间的发布—订阅关系。在MVC例子中，发布者是模型，订阅者是视图。然而，
MVC并非是仅有的发布—订阅例子。信息聚合订阅（比如， RSS或Atom）是另一种例子。许多读
者通常会使用一个信息聚合阅读器订阅信息流，每当增加一条新信息时，他们就能自动地获取到
更新。

拍卖会、RabbitMQ可用于为应用添加异步消息支持，支持多种消息协议（比如， HTTP和AMQP），可
在Python应用中用于实现发布—订阅模式，也就是观察者设计模式

社交网络、事件驱动系统、系统终端（DMA）
"""














































class Node:
	pass

class UnaryOperator(Node):
	def __init__(self, operand):
		self.operand = operand

class BinaryOperator(Node):
	def __init__(self, left, right):
		self.left = left
		self.right = right 

class Add(BinaryOperator):
	pass

class Sub(BinaryOperator):
	pass

class Mul(BinaryOperator):
	pass

class Div(BinaryOperator):
	pass

class Negate(UnaryOperator):
	pass

class Number(Node):
	def __init__(self, value):
		self.value = value
		