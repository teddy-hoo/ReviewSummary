import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

from base import BaseModel
from merchants import Merchants
from peewee import *

class Comments(BaseModel):
	id = PrimaryKeyField()
	merchantId = ForeignKeyField(Merchants)
	raw = TextField()
	clean = TextField(null = True)
	segmented = TextField(null = True)
	posed = TextField(null = True)
	mergedNouns = TextField(null = True)
