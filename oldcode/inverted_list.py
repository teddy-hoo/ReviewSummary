#!/bin/env python
#coding=utf8

def get_inverted_list(readfile, writefile):
    if str(type(readfile)).find('str') >= 0:
        comment_segmented = open(readfile, 'r')
        inverted_list = open(writefile, 'w')
    else:
        comment_segmented = readfile
        inverted_list = writefile

    word_list = {}
    line_count = 0
    for lines in comment_segmented:
        line_count += 1
        for line in lines.split('\t'):
            words = line.split()
            for index in range(len(words)):
                word_info = []
                pos_info = []
                context_info = []
                tag2 = True

                if (index - 2) >= 0 and words[index - 1] != '，' and words[index - 1] != '！' and words[index - 1] != '。':
                    context_info.append(words[index - 1])
                else:
                    context_info.append('---')

                if (index - 1) >= 0 and words[index - 2] != '，' and words[index - 2] != '！' and words[index - 2] != '。':
                    context_info.append(words[index - 2])
                else:
                    context_info.append('---')

                if (index + 1) < len(words) and words[index + 1] != '，' and words[index + 1] != '！' and words[index + 1] != '。':
                    context_info.append(words[index + 1])
                else:
                    tag2 = False
                    context_info.append('---')

                if tag2 and (index + 2) < len(words) and words[index + 2] != '，' and words[index + 2] != '！' and words[index + 2] != '。':
                    context_info.append(words[index + 2])
                else:
                    context_info.append('---')

                pos_info.append(line_count)
                pos_info.append(index)

                word_info.append(context_info)
                word_info.append(pos_info)

                if word_list.has_key(words[index][:words[index].find('/')]):
                    word_list[words[index][:words[index].find('/')]].append(word_info)
                else:
                    word_list[words[index][:words[index].find('/')]] = []
                    word_list[words[index][:words[index].find('/')]].append(word_info)

    for word in word_list:
        line = word
        for index in range(len(word_list[word])):
            line += '\t' + word_list[word][index][0][0] + '\t' + word_list[word][index][0][1] + '\t' + word_list[word][index][0][2] + '\t' + word_list[word][index][0][3] + '\t' + str(word_list[word][index][1][0]) + '\t' + str(word_list[word][index][1][1])
        line += '\n'
#        print line,
        inverted_list.write(line)

    comment_segmented.close()
    inverted_list.close()
if __name__ == '__main__':
    get_inverted_list()
