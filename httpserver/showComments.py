from __future__ import unicode_literals, print_function
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import base
from comments import Comments
import config
import re

def showComments():
    base.db.connect()

    for c in Comments:
        # if c.id > 600:
        #     c.delete_instance()
        print(c.id)
        print(c.raw)
        # if c.raw == '.':
        #     c.delete_instance()
        # print("s")
        print(c.segmented)
        # print("p")
        print(c.posed)
        # if c.id > 10:
        #     c.delete_instance()

    base.db.close()
