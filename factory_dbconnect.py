import pymysql
import pymongo
import redis

"""pymysql.connections
host, user, port, password"""




def dbconnect(dbtype, host, user, port, password):
	dbdict = {'mongo': pymongo.MongoClient(host=host, user=user, port=port, password=password),
			  'mysql': pymysql.connect(host=host, user=user, port=port, password=password),
			  'reids': redis.Redis(host=host, user=user, port=port, password=password)}
	return dbdict[dbtype]

