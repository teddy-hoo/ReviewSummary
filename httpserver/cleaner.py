#!/usr/bin/env python
# -*- coding: utf-8 -*-
# remove disturbing comments

# repeated comments
# comments with many repeated words

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import base
from comments import Comments
import config

class Cleaner:

    def __init__(self):
        
        self.uniqueComments = {}


    def isDisturbingComment(self, sentence):

        if self.uniqueComments.has_key(sentence):
            return True

        self.uniqueComments[sentence] = 1

        words = sentence.split(' ')
        counts = {}
        for w in words:
            if counts.has_key(w):
                counts[w] += 1
            else:
                counts[w] = 1

        for k in counts:
            if counts[k] >= len(words) / 2:
                return True

        return False


def cleaner(mid = 1):

    cl = Cleaner()

    # base.db.connect()

    print('cleaning...')
    comments = open('../data/%s.%s.segmented.utf-8' % (config.PREFIX, mid))
    results = open('../data/%s.%s.segmented.clean.utf-8' % (config.PREFIX, mid), 'w')
    
    for c in comments:
        if not cl.isDisturbingComment(c):
            results.write(c)

    comments.close()
    results.close()

    print('done...')
    # base.db.close()
