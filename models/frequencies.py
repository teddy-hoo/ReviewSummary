import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

from base import BaseModel
from peewee import *

class Frequencies(BaseModel):
	id = PrimaryKeyField()
	type = CharField()
	word = CharField()
	frequecny = IntegerField()
