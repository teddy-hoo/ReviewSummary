#!/bin/env python
#coding=utf8

import sys
import remove_stop_word

def pre_process_high_frequency_word(readfile, writefile):
    if str(type(readfile)).find('str') >= 0:
        raw_words = open(readfile, 'r')
        selected_words = open(writefile, 'w')
    else:
        raw_words = readfile
        selected_words = writefile

    for line in raw_words:
        word = line.split()[1]
        pos_tag = word[word.find('/') + 1:]
        # print 'tag:'+'\t'+pos_tag
        word = word[:word.find('/')]
        # print 'word:'+'\t'+word
        if not(remove_stop_word.remove_stop_words(word)) or pos_tag == 'OD' or pos_tag == 'NT' or pos_tag == 'CD' or pos_tag == 'DT' or pos_tag == 'M' or pos_tag == 'AD':
            continue
        # print line,
        selected_words.write(line)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Please input filename!'
        exit()
    pre_process_high_frequency_word(sys.argv[1], sys.argv[2])