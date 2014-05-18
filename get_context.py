#!/bin/env python
#coding=utf8

def get_context_info(readfile):
    if str(type(readfile)).find('str') >= 0:
        inverted_list = open(readfile, 'r')
    else:
        inverted_list = readfile

    context_list = {}

    for line in inverted_list:
        elements = line.split()
        word = elements[0]
        context_sum = []
        flag1 = 0
        flag2 = 0
        for index in range(1, len(elements)):
            if flag1 == flag2:
                context = []
            remainder = index % 6
            if remainder >= 1 and remainder <= 4:
                context.append(elements[index])
                flag1 += 1
            if remainder == 0:
                flag2 += 4
                context_sum.append(context)
        context_list[word] = context_sum

    return context_list
