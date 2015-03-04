#!/bin/env python
#coding=utf8

import get_context
import sys

def sentiment_about_ue_evaluation(readfile_sentiment_word, readfile_ue_word, readfile_inverted_list, writefile):
    
    if str(type(readfile_sentiment_word)).find('str') >= 0:
        word_about_sentiment_file = open(readfile_sentiment_word, 'r')
        sentiment_about_ue_evaluation_file = open(writefile, 'w')
        word_about_ue_file = open(readfile_ue_word, 'r')
        inverted_list_file = open(readfile_inverted_list, 'r')
    else:
        word_about_sentiment_file = readfile_sentiment_word
        sentiment_about_ue_evaluation_file = writefile
        word_about_ue_file = readfile_ue_word
        inverted_list_file = readfile_inverted_list

    word_about_ue = get_word_about_ue(word_about_ue_file)
    word_positive = get_word_positive(word_about_sentiment_file)
    word_negtive = get_word_negtive(word_about_sentiment_file)
    context_info = get_context.get_context_info(inverted_list_file)

    for word in word_about_ue:
        score_of_positive, related_positive_word = sentiment_evaluation(word, word_positive, context_info[word])
        score_of_negtive, related_negtive_word = sentiment_evaluation(word, word_negtive, context_info[word])

        line = word + '\t' + str(score_of_positive)
        count = 0
        for word_p in sorted(related_positive_word.iteritems(), key = lambda k:k[1], reverse = True):
            line += '\t' + word_p[0] + str(word_p[1])
            count += 1
            if count > 6:
                break

        line += '\n' + '    \t' + str(score_of_negtive)
        count = 0
        for word_n in sorted(related_negtive_word.iteritems(), key = lambda k:k[1], reverse = True):
            line += '\t' + word_n[0] + str(word_n[1])
            count += 1
            if count > 6:
                break
        line += '\n'

        print line
        sentiment_about_ue_evaluation_file.write(line)

def get_word_about_ue(word_about_ue_file):
    word_count = 0
    word_about_ue = []
    word_count = 0
    for line in word_about_ue_file:
        elements = line.split()
        word = elements[2][:elements[2].find('/')]
        if word == '号' or word == '店' or len(word) <= 3:
            continue
        word_count += 1
        word_about_ue.append(word)
        if word_count > 10:
            break

    return word_about_ue

def get_word_positive(file):
    word_positive = []
    word_count = 0
    for line in file:
        elements = line.split()
        word = elements[0]
        if len(word) <= 3:
            continue
        word_count += 1
        word_positive.append(word)
        if word_count >= 30:
            break

    return word_positive

def get_word_negtive(file):
    word_negtive = []
    all_words = []
    for line in file:
        elements = line.split()
        all_words.append(elements[0])
    for index in range(len(all_words) - 30, len(all_words)):
        word_negtive.append(all_words[index])
    '''for index in range(30):
        elements = file.readline().split()
        word = elements[2]
        if index > 29:
            word_negtive.append(word[:word.find('/')])'''
    return word_negtive

def sentiment_evaluation(word, sentiment_words, context_infos):
    related_word = {}
    score_sum = 0.0
    for sentiment_word in sentiment_words:
        score = 0.0
        for context_info in context_infos:
            for context in context_info:
                if context.find(sentiment_word) >= 0:
                    score += 1.0
        related_word[sentiment_word] = score
        score_sum += score

    return score_sum, related_word

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print 'Please input filename!'
        exit()
    sentiment_about_ue_evaluation(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
