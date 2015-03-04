#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import config

def genList(nouns):

    nounList       = []
    nounCount      = 0
    contextsOfNoun = {}

    for n in nouns:
        nn = n.strip().split(' ')[0]
        nounCount += 1
        nounList.append(nn)
        contextsOfNoun[nn] = nn + '>>>'

    return nounList, nounCount, contextsOfNoun

def genContext(comments, nounList, nounCount, contextsOfNoun):

    for c in comments:
        words  = c.strip().split(' ')
        length = len(words)
        for i in range(length):
            for j in range(nounCount):
                if words[i] == nounList[j]:

                    ctx = ''
                    if i > 1:
                        ctx += words[i - 2] + ' ' + words[i - 1]
                    elif i > 0:
                        ctx += words[i - 1]

                    if len(ctx) == 0:
                        ctx = 'empty'
                    ctx += '---'

                    if i < length - 2:
                        ctx += words[i + 1] + ' ' + words[i + 2]
                    elif i < length - 1:
                        ctx += words[i + 1]
                    else:
                        ctx += 'empty'
                
                    contextsOfNoun[nounList[j]] += ctx + '&&&'


# 送货速度#NN >>> .#PU --- 快#VA &&&  --- 比#P 预计#VV
def getContext(mid):

    comments = open('../data/%s.%s.postagged.utf-8' % (config.PREFIX, mid))

    nouns    = open('../data/%s.%s.frequent.nouns.utf-8' % (config.PREFIX_WORD, mid))
    contexts = open('../data/%s.%s.frequent.nouns.contexts.utf-8' % (config.PREFIX_CONTEXT, mid), 'w')

    print('getting context of frequent nouns...')
    
    nounList, nounCount, contextsOfNoun = genList(nouns)

    genContext(comments, nounList, nounCount, contextsOfNoun)

    for k in contextsOfNoun:
        print k, contextsOfNoun[k]
        contexts.write(contextsOfNoun[k][:-3] + '\n')

    print('done...')

    nouns.close()
    contexts.close()

    comments.close()


def getAllContext(mid = 1):

    comments = open('../data/%s.%s.postagged.utf-8' % (config.PREFIX, mid))

    nouns    = open('../data/%s.%s.all.nouns.utf-8' % (config.PREFIX_WORD, mid))
    contexts = open('../data/%s.%s.all.nouns.contexts.utf-8' % (config.PREFIX_CONTEXT, mid), 'w')

    print('getting context of all nouns...')
        
    nounList, nounCount, contextsOfNoun = genList(nouns)
    
    genContext(comments, nounList, nounCount, contextsOfNoun)

    for k in contextsOfNoun:
        print k, contextsOfNoun[k]
        contexts.write(contextsOfNoun[k][:-3] + '\n')

    print('done...')

    comments.close()
    nouns.close()
    contexts.close()
