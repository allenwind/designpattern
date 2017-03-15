import xml.etree.ElementTree as etree
import json
import sqlite3

"""
工厂模式:
通过对输入内容的特征进行判断，创建具体的合适的对象
下面以文件连接器为例
"""

class JSONConnector:
	def __init__(self, filepath):
		self.data = dict()
		with open(filepath, 'r', encoding='utf-8') as f:
			self.data = json.load(f)

	@property
	def parsed_data(self):
		return self.data

class XMLConnector:
	def __init__(self, filepath):
		self.tree = etree.parse(filepath)

	@property 
	def parsed_data(self):
		return self.tree

class SQLConnector:
	def __init__(self, filepath):
		self.cursor = sqlite3.connect(filepath)

	@property
	def parsed_data(self):
		return self.cursor.execute("SELECT * FROM db")
	

def factory(filepath):
	if filepath.endswith('json'):
		connector = JSONConnector
	elif filepath.endswith('xml'):
		connector = XMLConnector
	elif filepath.endswith('sql'):
		connector = SQLConnector
	else:
		raise ValueError('Cannot connect to {}'.format(filepath))
	return connector(filepath)

def connection(filepath):
	factory = None
	try:
		factory = factory(filepath)
	except ValueError as error:
		print(error)
	return factory

"""
类似的例子，根据数据库连接类型的不同，创建不同的连接实例
根据用户输入的类型，创建不同的数据库连接

"""

def dbconnect(db, host, user, port, password):
	
	import pymysql
    import pymongo
	import redis

	type_ = {'mongo': pymongo.MongoClient(host=host, user=user, 
		                                   port=port, password=password),
			  'mysql': pymysql.connect(host=host, user=user, 
			  	                       port=port, password=password),
			  'reids': redis.Redis(host=host, user=user, 
			  	                   port=port, password=password)}
	return type_[db]

