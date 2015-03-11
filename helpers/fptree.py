# FP-Tree

from collections import deque

class FPNode:

    def __init__(self):

        self.content   = ''
        self.frequence = 0
        self.children  = []


class FPTree:

    def __init__(self):

        self.root = FPNode()

    
    def insertTransaction(self, transaction):

        if len(transaction) != 3:
            return

        self._insertTransaction(self.root, transaction, 0)


    def _insertTransaction(self, root, transaction, index):

        if index == len(transaction):
            return

        existed = False

        for c in root.children:

            if index == len(transaction) - 1:
                c.frequence += 1
                if c.content.find(transaction[index]) < 0:
                    c.content += ' ' + transaction[index]
                existed = True
                break
            elif c.content == transaction[index]:
                c.frequence += 1
                root.children.append(c)
                self._insertTransaction(c, transaction, index + 1)
                existed = True
                break

        if not existed:
            newNode = FPNode()
            newNode.content = transaction[index]
            newNode.frequence = 1
            root.children.append(newNode)
            self._insertTransaction(newNode, transaction, index + 1)


    def getFP(self):

        FPs = {}

        self._getFP(self.root, FPs, '')

        return FPs


    def _getFP(self, root, FPs, path):

        length = len(root.children)

        if length == 0:
            return

        for c in root.children:
            if len(c.children) == 0:
                # print(root.children[s[0]].content)
                FPs[c.content] = (c.frequence, path + ' ' + root.content)
            else:
                self._getFP(c, FPs, path + ' ' + root.content)


    def printTree(self):

        flag         = FPNode()
        flag.content = 'levelFlag'

        q            = deque()
        q.append(self.root)

        while len(q) > 0:
            n = q[0]
            q.popleft()
            if n.content == 'levelFlag':
                if len(q) <= 0:
                    break
                q.append(flag)
                print(' ')
            else:
                print n.content,
                for c in n.children:
                    q.append(c)
