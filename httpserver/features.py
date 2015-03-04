#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a wrapper for stanford nlp segment software

from __future__ import unicode_literals, print_function
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import config
from fptree import FPNode, FPTree

'''
pre1 pre2 pivot post1 post2
pre3 pre4 pivot post3 post4
'''

# based fp tree
class Featrues:

    def __init__(self, mid = 1):

        self.mid       = mid
        self.contexts  = open('../data/%s.%s.all.nouns.contexts.utf-8' % \
                              (config.PREFIX_CONTEXT, mid))
        self.features  = open('../data/%s.%s.all.features.utf-8' % \
                              (config.PREFIX_FEATURE, mid), 'w')

        self.results   = open('../data/%s.%s.frequent.features.utf-8' % \
                              (config.PREFIX_FEATURE, mid), 'w')

        self.scores    = {}

        self.preTree   = FPTree()
        self.postTree  = FPTree()

        self.wordCount = self._genWordCount()

    def _genWordCount(self):

        nouns = open('../data/%s.%s.all.nouns.utf-8' % (config.PREFIX_WORD, self.mid))
        wc    = {}

        for n in nouns:
            w = n.strip().split(' ')[0]
            c = n.strip().split(' ')[1]
            wc[w.split('#')[0]] = c

        nouns.close()

        return wc

    def save(self):

        self.contexts.close()
        self.features.close()
        self.results.close()

    def outputFeatures(self):

        sortedFeatures = sorted(self.scores.iteritems(), key = lambda k:k[1], reverse = True)

        for f in sortedFeatures:
            if f[1] > 200:
                self.results.write(f[0] + '\n')

    def outputAllFeatures(self):

        preFP  = self.preTree.getFP()
        postFP = self.postTree.getFP()

        preFrequence  = self._toOneWord(preFP)
        postFrequence = self._toOneWord(postFP)
        # self.preTree.printTree()
        # self.postTree.printTree()

        sortedPre  = sorted(preFrequence.iteritems(), key = lambda k:k[1][0], reverse = True)

        for s in sortedPre:
            key = s[0]
            if postFrequence.has_key(key) and \
               preFrequence[key][1].strip() != 'empty' and \
               postFrequence[key][1].strip() != 'empty':

                if self.scores.has_key(key):
                    self.scores[key] += config.WORD_COUNT_FACTOR * float(self.wordCount[key]) + \
                                        config.PRE_CONTEXT_FACTOR * float(s[1][0]) + \
                                        config.POST_CONTEXT_FACTOR * float(postFrequence[key][0])
                else:
                    self.scores[key]  = config.WORD_COUNT_FACTOR * float(self.wordCount[key]) + \
                                        config.PRE_CONTEXT_FACTOR * float(s[1][0]) + \
                                        config.POST_CONTEXT_FACTOR * float(postFrequence[key][0])

                self.features.write('%s %s %s %s %s %s\n' % \
                                    (s[1][0], \
                                     postFrequence[key][0], \
                                     self.wordCount[key], \
                                     preFrequence[key][1], \
                                     postFrequence[key][1], \
                                     key))

    def _toOneWord(self, fp):

        f = {}

        for key in fp:
            for k in key.split(' '):
                f[k]  = fp[key]

        return f


    def genFeatrues(self):

        for c in self.contexts:
            
            if c.find('>>>') < 0:
                continue

            word = c.strip().split('>>>')[0].split('#')[0]
            cs   = c.strip().split('>>>')[1].split('&&&')
            for c in cs:
                pre         = c.split('---')[0].split(' ')
                post        = c.split('---')[1].split(' ')

                pre.reverse()
                
                transaction = self._genTransaction(word, pre)
                self.preTree.insertTransaction(transaction)
                
                transaction = self._genTransaction(word, post)
                self.postTree.insertTransaction(transaction)

    def _genTransaction(self, word, contexts):

        transaction = []
        length      = len(contexts)

        for i in range(length):
            c = contexts[length - i - 1]
            if c.find('#') < 0:
                transaction.append(c)
            else:
                transaction.append(c.split('#')[1])

        transaction.append(word)
        return transaction


# based on seeds and similarity of context
class FeatruesExtraction:

    def __init__(self, mid = 1):

        self.preSeeds  = []
        self.postSeeds = []
        self.mid       = mid

        self.contexts  = open('../data/%s.%s.all.nouns.contexts.utf-8' % \
                              (config.PREFIX_CONTEXT, mid))

        self.features  = open('../data/%s.%s.features.utf-8' % \
                              (config.PREFIX_FEATURE, mid), 'w')

        self.results   = {}


    def save(self):

        self.contexts.close()
        self.features.close()


    def genSeeds(self):

        seeds = open('../data/%s.%s.frequent.nouns.contexts.utf-8' % \
                        (config.PREFIX_CONTEXT, self.mid))

        for s in seeds:
            
            cs = s.strip().split('>>>')[1].split('&&&')
            
            for c in cs:
                self.preSeeds.append(c.split('---')[0])
                self.postSeeds.append(c.split('---')[1])

        seeds.close()


    def extractFeatures():

        for c in contexts:
        
            word  = c.strip().split('>>>')[0]
            cs    = c.strip().split('>>>')[1].split('&&&')

            score = 0

            for c in cs:
                pre   = c.split('---')[0]
                post  = c.split('---')[1]

                score += self._similarityOf(pre, post)

            self.results[word]

def extractFeatures(mid = 1):

    print('extracting features...')

    f = Featrues(mid)
    f.genFeatrues()
    f.outputAllFeatures()
    f.outputFeatures()
    f.save()

    print('done...')