"""由于对象创建的开销，面向对象的系统可能会面临性能问题。性能问题通常在资源受限的嵌
入式系统中出现，

大型复杂系统中也可能会出现同样的问题，因为要
在其中创建大量对象（也可能是用户），这些对象需要同时并存

除内存使用之外，计算性能也是一个考虑点

享元设计模式通过为相似对象引入数据共享来最小化内存使用，提升性能

一个享元（Flyweight）就是一个包含状态独立的不可变（又称固有的）数据的
共享对象。依赖状态的可变（又称非固有的）数据不应是享元的一部分，因为每个对象的这种信
息都不同，无法共享。如果享元需要非固有的数据，应该由客户端代码显式地提供

享元模式是一个用于优化的设计模式

Peppy是一个用Python语言实现的类XEmacs编辑器

#应用场合
应用需要使用大量的对象。
对象太多，存储/渲染它们的代价太大。一旦移除对象中的可变状态（因为在需要之时，应
该由客户端代码显式地传递给享元），多组不同的对象可被相对更少的共享对象所替代。
对象ID对于应用不重要。对象共享会造成ID比较的失败，所以不能依赖对象ID（那些在
客户端代码看来不同的对象，最终具有相同的ID）。"""

"""解释一下memoization与享元模式之间的区别。 memoization是一
种优化技术，使用一个缓存来避免重复计算那些在更早的执行步骤中已经计算好的结果。
memoization并不是只能应用于某种特定的编程方式，比如面向对象编程（Object-Oriented
Programming， OOP）
享元则是一种特定于面向对象编程优化的设计模式，关注的是共享对象数据。"""

import random

from enum import Enum 

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')

class Tree:
	"""该类根据类型创建实例，如果已经创建了，则返回，对客户端来说，renderer是独立的。
	本质上这种创建方法和客户端渲染是互相独立的"""

	pool = dict() #缓存同一个享元家族

	def __new__(cls, tree_type):  #真正的构造器
		obj = cls.pool.get(tree_type, None) #返回之前创建的对象
		if not obj:
			obj = object.__new__(cls)
			cls.pool[tree_type] = obj
			obj.tree_type = tree_type

		return obj

	def render(self, age, x, y):  #客户端上的表现
		print('render a tree of type {} and age {} at ({}, {}) id->{}'.
			format(self.tree_type, age, x, y, id(self)))

""" Python规范
并没有要求id()返回对象的内存地址，只是要求id()为每个对象返回一个唯一性ID，不过
CPython（Python的官方实现）正好使用对象的内存地址作为对象唯一性ID。"""



def main():
	rnd = random.Random()
	age_min, age_max = 1, 30
	min_point, max_point = 0, 100
	tree_counter = 0

	for _ in range(10):
		t1 = Tree(TreeType.apple_tree)
		t1.render(rnd.randint(age_min, age_max), 
				  rnd.randint(min_point, max_point),
				  rnd.randint(min_point, max_point))
		tree_counter += 1

	for _ in range(3):
		t2 = Tree(TreeType.cherry_tree)
		t2.render(rnd.randint(age_min, age_max), 
				  rnd.randint(min_point, max_point),
				  rnd.randint(min_point, max_point))
		tree_counter += 1

	for _ in range(5):
		t3 = Tree(TreeType.peach_tree)
		t3.render(rnd.randint(age_min, age_max), 
				  rnd.randint(min_point, max_point),
				  rnd.randint(min_point, max_point))
		tree_counter += 1

	print('trees rendered: {}'.format(tree_counter))
	print('trees actualy created: {}'.format(len(Tree.pool)))

if __name__ == '__main__':
	main()




