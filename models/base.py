import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))

from peewee import *
import config

db = SqliteDatabase(config.DATABASE)

class BaseModel(Model):
	class Meta:
		database = db
