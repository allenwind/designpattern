"""一种非常流行的设计模式，用于解耦处理用户界面的代码与处理（业务）逻辑
的代码，这种模式就是模型视图控制器模式"""

#模型— 视图— 控制器模式
#关注点分离（Separation of Concerns， SoC）原则是软件工程相关的设计原则之一。
#SoC原则背后的思想是将一个应用切分成不同的部分，每个部分解决一个单独的关注点。分层设计中的层
#次（数据访问层、业务逻辑层和表示层等）即是关注点的例子。使用SoC原则能简化软件应用的
#开发和维护


#模型—视图—控制器（Model-View-Controller， MVC）模式是应用到面向对象编程的Soc原则。

#MVC被认为是一种架构模式而不是一种设计模式。架构模式与设计模式之间的区别在于前者比后者的范畴更广。

"""模型是核心的部分，代表着应用的信息本源，包含和管理（业务）逻辑、数据、状态以及应
用的规则。视图是模型的可视化表现。视图的例子有，计算机图形用户界面、计算机终端的文本
输出、智能手机的应用图形界面、 PDF文档、饼图和柱状图等。视图只是展示数据，并不处理数
据。控制器是模型与视图之间的链接/粘附。模型与视图之间的所有通信都通过控制器进行。"""

"""对于将初始屏幕渲染给用户之后使用MVC的应用，其典型使用方式如下所示。
用户通过单击（键入、触摸等）某个按钮触发一个视图
视图把用户操作告知控制器
控制器处理用户输入，并与模型交互
模型执行所有必要的校验和状态改变，并通知控制器应该做什么
控制器按照模型给出的指令，指导视图适当地更新和显示输出"""

#为了实现模型与其表现之间的解耦，每个视图通常都需要属于它的控制器
#Django使用名称模型—模板—视图（Model-Template-View， MTV）来替代MVC (控制器被称为视
#图，视图被称为模板)
#其变种包括模式—
#视图—适配器（Model-View-Adapter， MVA）、 模型—视图—演示者（Model-View-Presenter， MVP）

quotes = ('A man is not complete until he is married. Then he is finished.',
		  'As I said before, I never repeat myself.',
		  'Behind a successful man is an exhausted woman.',
		  'Black holes really suck...', 'Facts are stubborn things.')

#模型负责访问数据，管理应用的状态
class QuoteModel:
	#模型
	"""使其变得像一个创建、 读取、 更新、 删除（Create, Read, Update,
	   Delete， CURD）应用"""
	"""为了让索引校验的代码被所有控制/视图复
	   用，将索引校验移到模型中进行，"""
	def get_quote(self, n):
		try:
			value = quotes[n]
		except IndexError as error:
			value = 'Not found!'
		return value
		
#视图是模型的外在表现
class QuoteTerminalView:
	#视图
	def show(self, quote):
		print('And the quote is :{}'.format(quote))

	def error(self, msg):
		print('Error: {}'.format(msg))

	def select_quote(self):
		return input('which quote number would you like to see?')

class QuoteTerminalController:
	#控制
	def __init__(self):
		self.model = QuoteModel()
		self.view = QuoteTerminalView()

	def run(self):
		valid_input = False
		while not valid_input:
			try:
				n = self.view.select_quote()
				n = int(n)
				valid_input = True
			except ValueError as error:
				self.view.error("Incorrect index '{}'".format(n))

		quote = self.model.get_quote(n)
		self.view.show(quote)

def main():
	controller = QuoteTerminalController()
	while True:
		controller.run()

if __name__ == '__main__':
	main()



