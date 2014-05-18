#!/bin/env python
#coding=utf8

import remove_stop_word
import sys

def word_statistics(readfile, writefile):
    if str(type(readfile)).find('str') >= 0:
        comment = open(readfile, 'r')
        frequency = open(writefile, 'w')
    else:
        comment = readfile
        frequency = writefile

    word_frequency = {}
    line_count = 0.0
    for line in comment:
        sentence = line.split()
        for word in sentence:
            w = word[:word.find('/')]
            t = word[word.find('/') + 1:]
            if t == 'PU' or not(remove_stop_word.remove_stop_words(w)):
                continue
            if word_frequency.has_key(word):
                word_frequency[word] += 1.0
            else:
                word_frequency[word] = 0.0
#            print word + '\t', word_frequency[word]
        line_count += 1.0

    for word in sorted(word_frequency.iteritems(), key = lambda k:k[1], reverse = True):
        line = str(word[1]) + '\t' + word[0] + '\t' + str(word[1]/line_count) + '\n'
#        print line,
        frequency.write(line)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'please input the filename'
        exit()
    word_statistics(sys.argv[1], sys.argv[2])
