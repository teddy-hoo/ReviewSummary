#!/bin/env python
#coding=utf8

import sys

def raw_to_format(filename):
    raw = open(filename, 'r')
    format = open(filename + '_format', 'w')

    for line in raw:
#        line = remove_punctuation(line)
        line = line.strip() + '\n'
        print line,
        format.write(line)

def remove_punctuation(format_line):

    print format_line

    pos = format_line.find('，')
    while pos >= 0:
        format_line = format_line[:pos] + ' ' + format_line[pos + 3:]
        pos = format_line.find('，')

    pos = format_line.find('。')
    while pos >= 0:
        format_line = format_line[:pos] + ' ' + format_line[pos + 3:]
        pos = format_line.find('。')

    pos = format_line.find('！')
    while pos >= 0:
        format_line = format_line[:pos] + ' ' + format_line[pos + 3:]
        pos = format_line.find('！')

    pos = format_line.find('~')
    while pos >= 0:
        format_line = format_line[:pos] + ' ' + format_line[pos + 1:]
        pos = format_line.find('~')

    pos = format_line.find(',')
    while pos >= 0:
        format_line = format_line[:pos] + ' ' + format_line[pos + 1:]
        pos = format_line.find(',')

    pos = format_line.find('!')
    while pos >= 0:
        format_line = format_line[:pos] + ' ' + format_line[pos + 1:]
        pos = format_line.find('!')

    print format_line
    return format_line

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Please input filename!'
        exit()
    raw_to_format(sys.argv[1])
