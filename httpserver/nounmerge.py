import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import config
from topthree import topThree

# 398
# PU
# 105
# VV
# 50
# NR
# 19
# AD
# 107
# PU
# 97
# VV
# 52

# 3417
# PU
# 920
# VV
# 466
# AD
# 138
# AD
# 981
# VV
# 435
# CD
# 58

# merge nouns when the after pos is AD VV VA

# statis pre pos and post pos of compound nouns
class Statis:

    def __init__(self):

        self.prePos  = {}
        self.postPos = {}
        self.total   = 0

    def parseSentence(self, sentence):

        nounCount = 0
        words  = sentence.strip().split(' ')
        length = len(words)

        for i in range(length):
            pos = words[i].split('#')[1]
            if pos == 'NN':
                nounCount += 1
                if nounCount == 2:
                    self.total += 1
                    pre = i - 2
                    if pre >= 0:
                        p = words[pre].split('#')[1]
                        if not self.prePos.has_key(p):
                            self.prePos[p] = 1
                        else:
                            self.prePos[p] += 1
            else:
                if nounCount > 1:
                    if not self.postPos.has_key(pos):
                        self.postPos[pos] = 1
                    else:
                        self.postPos[pos] += 1
                nounCount = 0

def merge(sentence):

    nounCount   = 0
    words       = sentence.strip().split(' ')
    length      = len(words)
    newSentence = ''
    mergedNoun  = ''

    for i in range(length):
        pos  = words[i].split('#')[1]
        if pos == 'NN':
            
            nounCount += 1
        
        else:
            
            if nounCount == 1:                
                newSentence += words[i - 1] + ' '
            elif nounCount > 1:
                if pos == 'VA' or pos == 'AD' or pos == 'VV':
                    for j in range(i - nounCount, i):
                        word = words[j].split('#')[0]
                        mergedNoun += word
                    mergedNoun  += '#NN '
                    newSentence += mergedNoun
                    print mergedNoun
                else:
                    for j in range(i - nounCount, i):
                        newSentence += words[j] + ' '
            
            nounCount = 0
            newSentence += words[i] + ' '

    return newSentence[:-1]


def nounMerge(mid = 1):

    comments = open('../data/%s.%s.postagged.utf-8' % (config.PREFIX, mid))
    results   = open('../data/%s.%s.merged.utf-8' % (config.PREFIX, mid), 'w')
    s = Statis()

    print('noun merging...')

    # for c in comments:
    #     s.parseSentence(c)

    # f, se, t = topThree(s.prePos)
    # print f, se, t
    # f, se, t = topThree(s.postPos)
    # print f, se, t

    for c in comments:
        results.write(merge(c) + '\n')

    comments.close()
    results.close()
