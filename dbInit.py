import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '.', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'models'))

from peewee import *
import config

import base
from chunks import Chunks
from comments import Comments
from descriptions import Descriptions
from features import Features
from frequencies import Frequencies
from merchants import Merchants
from ues import UEs

def create_tables():
	base.db.connect()
	base.db.create_tables([Merchants, Comments, Chunks, Features, \
		Descriptions, Frequencies, UEs])

create_tables()
