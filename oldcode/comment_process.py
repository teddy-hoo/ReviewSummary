#!/bin/env python
#coding=utf8

import sys

def process_comment(filename):

    print
    print 'processing the comment for tagging!.......'
    print
    comment = open(filename, 'r')
    processed = open(filename + '_for_tag', 'w')

    for line in comment:
        line = line[0:len(line)-1] + ' .\n'
        # line = line[:-5] + '\n'
        # print line,
        processed.write(line)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Please input the filename'
        exit()
    process_comment(sys.argv[1])
