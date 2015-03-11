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
from select import select

# set default str encoding typeu
reload(sys)
sys.setdefaultencoding('utf-8')

# URL = 'http://item.jd.com/1162187.html'
# URL = 'http://item.jd.com/1217501.html'
# URL = 'http://item.jd.com/1303463.html'
# URL = 'http://item.jd.com/1042512394.html'
# URL = 'http://item.jd.com/1348962168.html'
# URL = 'http://item.jd.com/1266468631.html'
# URL = 'http://item.jd.com/1093680.html'
# URL = 'http://item.jd.com/1052415111.html'
# URL = 'http://item.jd.com/1216351.html'
# URL = 'http://item.jd.com/326321.html'





# showComments()

# retrieve comments from jingdong
# MID = retrieve(URL)

# select 200 from comments
# for i in range(1, 11):
# 	select(i)

# segment the comments
# segmenter(MID)
# for i in range(1, 11):
# 	segmenter(i)

# remove disturb comments
# cleaner(MID)
# for i in range(1, 11):
# 	cleaner(i)

# tag part of speach for the comments
# postagger(MID)
# for i in range(1, 11):
# 	postagger(i)

# merge compound nouns
# nounMerge(MID)
# for i in range(1, 11):
# 	nounMerge(i)

# conunt words and extract feed words
# wordCount(MID)
# for i in range(1, 11):
# 	wordCount(i)

# get context of features and generate new features
# getContext(MID)
# getAllContext(MID)
# for i in range(1, 11):
# 	getContext(i)
# 	getAllContext(i)

# extract feature and description
# extractFeatures(7)
# extractDescriptions(MID)
# for i in range(1, 11):
# 	extractFeatures(i)
# for i in range(1, 11):
# 	extractDescriptions(i)

# extract ue evaluation

