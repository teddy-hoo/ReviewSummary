#!/bin/env python
#conding=utf8

def get_word_table():
    sentence_segmented_file = open('../iphone/comment_yhd_iphone_format_segmented', 'r')
    word_table_file = open('../iphone/comment_yhd_iphone_word_table', 'w')

    word_table = ''
    word_count = 0
    for line in sentence_segmented_file:
        words = line.split()
        for word in words:
            if word_table.find(word) < 0:
                word_table += word + '\t'
                word_count += 1

    print 'There are ', word_count, ' words in comment!'
    word_table += '\n'
    word_table_file.write(word_table)

    sentence_segmented_file.close()
    word_table_file.close()

if __name__ == '__main__':
    get_word_table()
