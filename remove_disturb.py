#!/bin/env python
#coding=utf8

import sys

def remove_disturb_comment(readfile, writefile):
    if str(type(writefile)).find('str') >= 0:
        comment_without_disturb = open(writefile, 'w')
        comment_with_disturb = open(readfile, 'r')
    else:
        comment_without_disturb = writefile
        comment_with_disturb = readfile

    for line in comment_with_disturb:
        word_list = line.split()
        word_repetition = 0
        for index in range(0, len(word_list)):
            word_list[index] = word_list[index][0:word_list[index].find('/')]
        for index0 in range(1, len(word_list)):
            for index1 in range(0, index0 - 1):
                if word_list[index0] == word_list[index1]:
                    word_repetition += 1
                    break
        if float(word_repetition)/float(len(word_list)) < 0.4:
            comment_without_disturb.write(line)
#        else:
#            print line,

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Please input the filename!'
        exit()
    remove_disturb_comment(sys.argv[1], sys.argv[2])
