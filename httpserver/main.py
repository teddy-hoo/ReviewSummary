import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

from retrieve import *
from poser import poser

# set default str encoding type
reload(sys)
sys.setdefaultencoding('utf-8')

URL = 'http://item.jd.com/1253301.html'

# retrieve comments from jingdong
# retrieve(URL)

# segment the comments


# tag part of speach for the comments
poser()

# remove disturb comments


# extract chunk from comments


# extract feed words


# extract feature and description


# extract ue evaluation

