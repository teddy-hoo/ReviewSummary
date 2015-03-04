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
    word_sentiment = get_word_sentiment(word_about_sentiment_file)
    context_info = get_context.get_context_info(inverted_list_file)

    total_count = 0
    for word in word_about_ue:
        score, related_word = sentiment_evaluation(word, word_sentiment, context_info[word])

        if score <= 1.0:
            continue
        line = word + '\t' + str(score)
        count = 0
        for word in sorted(related_word.iteritems(), key = lambda k:k[1], reverse = True):
            if word[1] <= 1.0:
                continue
            line += '\t' + word[0] + str(word[1])
            count += 1
            total_count += 1
            if count > 11:
                break
        line += '\n'

        print line
        sentiment_about_ue_evaluation_file.write(line)
    sentiment_about_ue_evaluation_file.write('total_count ' + str(total_count) + '\n')

def get_word_about_ue(word_about_ue_file):
    word_count = 0
    word_about_ue = []
    word_count = 0
    for line in word_about_ue_file:
        elements = line.split()
        #word = elements[2][:elements[2].find('/')]
        word = elements[1]
        stop_word = '号店 东西 别人 老妈 妈妈 同事 朋友'
        if stop_word.find(word) >= 0 or len(word) <= 3:
            continue
        word_count += 1
        word_about_ue.append(word)
        if word_count > 20:
            break

    return word_about_ue

def get_word_sentiment(file):
    word_sentiment = []
    word_count = 0
    for line in file:
        elements = line.split()
        word = elements[0]
        if len(word) <= 3:
            continue
        word_count += 1
        word_sentiment.append(word)
        if word_count >= 50:
            break

    return word_sentiment

def sentiment_evaluation(word, sentiment_words, context_infos):
    related_word = {}
    score_sum = 0.0
    for sentiment_word in sentiment_words:
        score = 0.0
        if sentiment_word == word:
            continue
        for context_info in context_infos:
            for context in context_info:
                if context.find(sentiment_word) >= 0:
                    score += 1.0
        related_word[sentiment_word] = score
        if score <= 1.0:
            continue
        score_sum += score

    return score_sum, related_word

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print 'Please input filename!'
        exit()
    sentiment_about_ue_evaluation(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
