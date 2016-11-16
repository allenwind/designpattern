import xml.etree.ElementTree as etree
import json
import sqlite3

#factory method

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
	def __init__(self.filepath):
		pass

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
