import pymysql
import pymongo
import redis

def dbconnect(dbtype, *args, **kwargs):
	dbdict = {'mongo': pymongo.MongoClient(),
			  'mysql': pymysql.connect(),
			  'reids': redis.Redis()}
	return dbdict[dbtype]

