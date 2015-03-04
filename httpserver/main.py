#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

from cleaner import cleaner
from postagger import postagger
from retrieve import *
from segmenter import segmenter
from showComments import showComments
from nounmerge import nounMerge
from wordcount import wordCount
from context import *
from features import extractFeatures
from descriptions import extractDescriptions

# set default str encoding typeu
reload(sys)
sys.setdefaultencoding('utf-8')

URL = 'http://item.jd.com/1217524.html'

# showComments()

# retrieve comments from jingdong
# MID = retrieve(URL)

# segment the comments
# segmenter(MID)

# remove disturb comments
# cleaner(MID)

# tag part of speach for the comments
# postagger(MID)

# merge compound nouns
# nounMerge(2)

# conunt words and extract feed words
# wordCount(2)

# get context of features and generate new features
# getContext(2)
# getAllContext(2)

# extract feature and description
# extractFeatures(2)
extractDescriptions(2)

# extract ue evaluation

