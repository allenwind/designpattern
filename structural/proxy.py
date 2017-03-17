"""
访问敏感信息——在允许用户访问敏感信息之前，我们希望确保用户具备足够的权限。


延迟初始化:
是另一个案例：我们想要把一个计算成本较高的对象的创建过程延迟到用户
首次真正使用它时才进行


远程代理：实际存在于不同地址空间（例如，某个网络服务器）的对象在本地的代理者。

虚拟代理：用于懒初始化，将一个大计算量对象的创建延迟到真正需要的时候进行。

保护/防护代理：控制对敏感对象的访问。

智能（引用）代理：在对象被访问时执行额外的动作。此类代理的例子包括引用计数和线程安全检查

Python的weakref模块包含一个proxy()方法，该方法接受一个输入对象并将一个智能代理
返回给该对象。弱引用是为对象添加引用计数支持的一种推荐方式
"""

import time

#use descriptor
class descriptor:
	pass

#property, variable, attribute
class LazyProperty:
	#虚拟代理：用于懒初始化，将一个大计算量对象的创建延迟到真正需要的时候进行
	def __init__(self, method):
		self.method = method
		self.method_name = method.__name__

	def __get__(self, obj, cls):
		if not obj:
			return None
		value = self.method(obj)
		setattr(obj, self.method_name, value)
		return value

"""
在OOP中有两种基本的、不同类型的懒初始化，如下所示。
在实例级：这意味着会一个对象的特性进行懒初始化，但该特性有一个对象作用域。同
一个类的每个实例（对象）都有自己的（不同的）特性副本。

在类级或模块级：在这种情况下，我们不希望每个实例都有一个不同的特性副本，而是
所有实例共享同一个特性，而特性是懒初始化的。这一情况在本章不涉及。如果你觉得
有意思，可以将其作为练习。
"""

class Test:
	def __init__(self):
		self.x = 'x'
		self.y = 'y'
		self._resource = None

	@LazyProperty
	def resource(self):
		#LazyProperty惰性地（首次使用时）加载特性
		print('initializing self._resource which is: {}'.format(self._resource))
		self._resource = tuple(range(5))
		time.sleep(2)
		return self._resource

#SensitiveInfo类包含我们希望保护的信息
class SensitiveInfo:
	def __init__(self):
		self.users = ['nick', 'tom', 'ben', 'mike']

	def read(self):
		print('there are {} users: {}'.format(len(self.users), ''.join(self.users)))

	def add(self, user):
		self.users.append(user)
		print('Added user {}'.format(user))

#Info类是SensitiveInfo的一个保护代理
class Info:
	def __init__(self):
		self.protected = SensitiveInfo()
		self.secret = 'hello'

	def read(self):
		self.protected.read()

	def add(self, user):
		sec = input('What is the secret?')
		self.protected.add(user) if sec == self.secret else print('it" wrong')

class SimpleRedisProxy(object):
	#build a simple redis server proxy from instance of Proxy Design Pattern

	def __init__(self):
		self.r = redis.Redis(password='redisroot')

	def set(self, key, value):
		if isinstance(value, (int, float)):
			raise TyepError("typeError")
		self.r.set(key, value)

	def get(self, *keys):
		for item in keys:
			if isinstance(item, (int, float)):
				raise TypeError("typeError")
			yield self.r.get(item)





def main():
	t = Test()
	print(t.x)
	print(t.resource)
	print(t.resource) #第二次访问不用创建了

if __name__ == '__main__':
	main()