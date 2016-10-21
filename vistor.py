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
		