"""
理论：
抽象工厂设计模式是抽象方法的一种泛化。可以说，抽象工厂就是工厂方法在逻辑上的组合，
每个工厂方法都负者生产不同类型的实例。它们是不可分割的，在逻辑上实现一些列互相关联
的实例的创建。

应用场景：
1.跟踪对象的创建
2.将对象的创建和使用解耦
3.优化应用性能和减少资源占用

例子：
模仿一个游戏场景

"""

class Frog:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def interact_with(self, obstacle):
		print('{} the Frog encounters {} and {}'.format(
			self.obstacle, obstacle.action()))

class Bug:
	def __str__(self):
		return 'a bug'

	def action(self):
		return 'eats it'

class FrogWorld:
	def __init__(self, name):
		print(self)
		self.palyer_name = name

	def __str__(self):
		return '-----Frog World-----'

	def make_character(self):
		return Frog(self.player_name)

	def make_obstacle(self):
		return Bug()

class Wizard:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def interact_with(self, obstacle):
		print('{} the Wizard battles against {} and {}!'.format(
			self, obstacle, obstacle.action()))
class Ork:
	def __str__(self):
		return 'an evil ork'

	def action(self):
		return 'kills it'

class WizardWorld: #对两个类抽象封装
	def __init__(self, name):
		print(self)
		self.player_name = name

	def __str__(self):
		return '-----Wizard World-----'

	def make_character(self):
		return Wizard(self.player_name)

	def make_obstacle(self):
		return Ork()

class GameEnvironment:
	def __init__(self, factory):
		self.hero = factory.make_character()
		self.obstacle = factory.make_obstacle()

	def play(self):
		self.hero.interact_with(self.obstacle)

def validate_age(name):
	try:
		age = input('How old are you?')
		age = int(age)
	except ValueError as error:
		print('invalid age')
		return (False, age)
	return (True, age)

def main():
	name = input("What's your name?")
	valid_input = False
	while not valid_input:
		valid_input, age = validate_age(name)
	game = FrogWorld if age < 18 else WizardWorld
	environment = GameEnvironment(game(name))
	environment.play()

if __name__ == '__main__':
	main()



