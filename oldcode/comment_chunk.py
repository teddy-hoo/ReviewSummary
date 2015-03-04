#!/bin/env python
#coding=utf8

import sys
from nltk import chunk
from nltk import Tree

# An earlier pattern may introduce a chunk boundary that prevents a later later pattern form executing.
# Sometimes an individual pattern will match on multiple, overlapping extents of the input.

#    价格/NN 也/AD 划算/VV 
#    包装/NN 很/AD 好/JJ
#    味道/NN 很/AD 喜欢/VV
#    价格/NN 实惠/VA
#    送货/VV 快捷/VA
#    物流/NN 很差/VV
#    气味/NN 就/AD 很/AD 冲/VV
#    快递/NN 超级/AD 慢/VA
#    蜂蜜/NN 太/AD 差/VA

def chunker(readfile, writefile):
    if str(type(readfile)).find('str') >= 0:
        sentences_file = open(readfile, 'r')
        chunks_file = open(writefile, 'w')
    else:
        sentences_file = readfile
        chunks_file = writefile

    count = 0
    for sentence in sentences_file:
        count += 1
        print '$$$$$$$$$$$$This is the ', count, 'th sentence $$$$$$$$$$'
        word_tag = sentence.split()
        tokens = []
        for item in word_tag:
            token = (item[:item.find('/')], item[item.find('/') + 1:])
            tokens.append(token)
        chunks = ''

        grammar = r"""
                 NP:
                  {<NN>+<AD>?<VV>}
                """
        chunk_parser = chunk.RegexpParser(grammar)
        result = chunk_parser.parse(Tree('S', tokens), trace=2)
        string_of_tree = str(result)
        for element in string_of_tree.split('\n'):
            element = element.strip()
            if element[0] == '(' and element[-1] == ')' and element[1] != 'S':
                chunks += ('\t' + element[4:-1])

        grammar = r"""
                 NP:
                  {<NN>+<AD>?<JJ>}      
                """
        chunk_parser = chunk.RegexpParser(grammar)
        result = chunk_parser.parse(Tree('S', tokens), trace=2)
        string_of_tree = str(result)
        for element in string_of_tree.split('\n'):
            element = element.strip()
            if element[0] == '(' and element[-1] == ')' and element[1] != 'S':
                chunks += ('\t' + element[4:-1])

        grammar = r"""
                 NP:    
                  {<NN>+<AD>?<VA>}
                """
        chunk_parser = chunk.RegexpParser(grammar)
        result = chunk_parser.parse(Tree('S', tokens), trace=2)
        string_of_tree = str(result)
        for element in string_of_tree.split('\n'):
            element = element.strip()
            if element[0] == '(' and element[-1] == ')' and element[1] != 'S':
                chunks += ('\t' + element[4:-1])       

        grammar = r"""
                 NP:    
                  {<VV>+<AD>?<VA>}
                """
        chunk_parser = chunk.RegexpParser(grammar)
        result = chunk_parser.parse(Tree('S', tokens), trace=2)
        string_of_tree = str(result)
        for element in string_of_tree.split('\n'):
            element = element.strip()
            if element[0] == '(' and element[-1] == ')' and element[1] != 'S':
                chunks += ('\t' + element[4:-1])   

        if len(chunks) > 0:
            chunks_file.write(chunks[1:] + '\n')

    chunks_file.close()
    sentences_file.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'please input sentence'
        exit()
    chunker(sys.argv[1], sys.argv[2])
