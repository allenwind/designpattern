


"""抽象工厂设计模式是抽象方法的一种泛化。概括来说，
一个抽象工厂是（逻辑上的）一组工厂方法，其中的每个
工厂方法负责产生不同种类的对象

(a)想要追踪对象的创建时， (b)想要将对象的创建与使用解耦时， (c)想要优化应用的性能
和资源占用时"""

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

class WizardWorld:
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



