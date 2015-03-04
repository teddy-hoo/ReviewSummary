#!/bin/env python
#coding=utf8

import sys

def remove_stop_words(word):
    stop_word = open('stop_word_list', 'r')

    stop_words = ''
    for line in stop_word:
        stop_words += line[:-1] + ' '
    stop_word.close()

    if stop_words.find(word) < 0:
        return True
    else:
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'please input word'
        exit()
    remove_stop_words(sys.argv[1])
