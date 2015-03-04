#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import config


class Descriptions:

    def __init__(self, mid = 1):

        self.mid       = mid

        self.positives = self._readWords(config.POSITIVE_WORDS)
        self.negtives  = self._readWords(config.NEGTIVE_WORDS)

        self.features  = self._genFeatures()
        self.contexts  = self._genContexts()


    def save(self):
        pass

    def getDescriptions(self):

        pResults = []
        nResults = []

        for w in self.contexts:
            cs = self.contexts[w]
            
            # pre contexts
            for c in cs[0]:
                try:
                    p = self.positives.index(c)
                    pResults.append(c + w)
                except:
                    pass
                try:
                    n = self.negtives.index(c)
                    nResults.append(c + w)
                except:
                    pass

            # post contexts
            for c in cs[1]:
                try:
                    p = self.positives.index(c)
                    pResults.append(w + c)
                except:
                    pass
                try:
                    n = self.negtives.index(c)
                    nResults.append(w + c)
                except:
                    pass

        return pResults, nResults


    def _readWords(self, filepath):

        f  = open(filepath)
        ws = []

        for w in f:
            ws.append(w.strip())

        return ws

    def _genFeatures(self):

        ff = open('../data/%s.%s.frequent.features.utf-8' % \
                              (config.PREFIX_FEATURE, self.mid))
        fs = ''

        for f in ff:
            fs += f.strip() + ' '

        ff.close()

        return fs[:-1]


    def _genContexts(self):

        fs = open('../data/%s.%s.all.nouns.contexts.utf-8' % (config.PREFIX_CONTEXT, self.mid))
        cs = {}

        for f in fs:
            
            f = f.strip()
            if f.find('>>>') < 0:
                continue

            word = f.strip().split('>>>')[0].split('#')[0]
            c    = f.strip().split('>>>')[1]

            if self.features.find(word) < 0:
                continue

            cs[word] = []

            cc   = c.split('&&&')
            for ccc in cc:
                cccc = []
                pre  = ccc.split('---')[0]
                post = ccc.split('---')[1]
                pres = []
                poss = []
                if pre == 'empty':
                    pres.append(pre)
                else:
                    if pre.find(' ') < 0:
                        pres.append(pre.split('#')[0])
                    else:
                        ps = pre.split(' ')
                        pres.append(ps[0].split('#')[0])
                        pres.append(ps[1].split('#')[0])
                if post == 'empty':
                    poss.append(post)
                else:
                    if post.find(' ') < 0:
                        poss.append(post.split('#')[0])
                    else:
                        ps = post.split(' ')
                        poss.append(ps[0].split('#')[0])
                        poss.append(ps[1].split('#')[0])

                cccc.append(pres)
                cccc.append(poss)
                cs[word] = cccc

        fs.close()

        return cs

def extractDescriptions(mid = 1):

    d    = Descriptions(mid)
    ps, ns = d.getDescriptions()

    p = open('../data/%s.%s.utf-8' % (config.PREFIX_DESCRIPTION_P, mid), 'w')
    n = open('../data/%s.%s.utf-8' % (config.PREFIX_DESCRIPTION_N, mid), 'w')

    for pp in ps:
        p.write(pp + '\n')

    for nn in ns:
        n.write(nn + '\n')

    p.close()
    n.close()
