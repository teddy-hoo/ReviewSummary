#!/bin/env python
#coding=utf8

import sys
import get_context

import string

def find_word_about_sentiment(readfile_inverted_list, readfile_word_statistics, readfile_seed, writefile):
    if str(type(readfile_inverted_list)).find('str') >= 0:
        word_about_sentiment_file = open(writefile, 'w')
        inverted_list = open(readfile_inverted_list, 'r')
        word_statistics = open(readfile_word_statistics, 'r')
        seed_file = open(readfile_seed, 'r')
    else:
        word_about_sentiment_file = writefile
        inverted_list = readfile_inverted_list
        word_statistics = readfile_word_statistics
        seed_file = readfile_seed

    flag = True
    positive_words = []
    negtive_words = []
    for line in seed_file:
        words = line.split()
        if flag:
            for word in words:
                positive_words.append(word)
            flag = False
        else:
            for word in words:
                negtive_words.append(word)

    line_number_of_word, max_line_number = get_line_number(inverted_list)
    word_priori_probability = get_word_priori_probability(word_statistics)

    word_about_sentiment = {}
    for word in word_priori_probability:
        if word == '\\':
            continue
        score = decision_sentiment(word, word_priori_probability, line_number_of_word, max_line_number, positive_words, negtive_words)
        word_about_sentiment[word] = score

    for word in sorted(word_about_sentiment.iteritems(), key = lambda k:k[1], reverse = True):
        line = word[0] + '\t' + str(word[1]) + '\n'
        word_about_sentiment_file.write(line)

def get_line_number(inverted_list):
    line_number_of_word = {}

    max_line_number = 0
    for line in inverted_list:
        elements = line.split()
        word = elements[0]
        line_number = []
        for index in range(1, len(elements)):
            if index % 6 == 5:
                line_number.append(elements[index])
                if string.atof(elements[index]) > max_line_number:
                    max_line_number = string.atof(elements[index])
        line_number_of_word[word] = line_number

    return line_number_of_word, max_line_number

def get_word_priori_probability(word_statistics):
    word_priori_probability = {}

    for line in word_statistics:
        info = line.split()
        word = info[1][:info[1].find('/')]
        #tag = info[1][info[1].find('/') + 1:]
        if len(word) <= 3:
            continue
        word_priori_probability[word] = string.atof(info[2])

    return word_priori_probability

def decision_sentiment(word, word_priori_probability, line_number_of_word, line_count, positive_words, negtive_words):
    # positive_words = ['赞', '好', '不错', '便宜', '满意', '棒']
    # negtive_words = ['慢', '黑屏', '坏', '问题', '失望', '慎重']

    score_of_positive = 0.0
    times_of_concurrent = 0
    for p_word in positive_words:
        try:
            line_number = line_number_of_word[word]
        except:
            continue
        for line_pre in line_number:
            for line_beh in line_number_of_word[p_word]:
                if line_pre == line_beh:
                    times_of_concurrent += 1
    probability_of_concurrent = string.atof(times_of_concurrent)/line_count;
    try:
        score_of_positive += probability_of_concurrent - (word_priori_probability[word] + word_priori_probability[p_word])
    except:
        score_of_positive += 0

    score_of_negtive = 0.0
    times_of_concurrent = 0
    for p_word in negtive_words:
        try:
            line_number = line_number_of_word[word]
        except:
            continue
        for line_pre in line_number:
            try:
                lines = line_number_of_word[p_word]
            except:
                continue
            for line_beh in lines:
                if line_pre == line_beh:
                    times_of_concurrent += 1
    probability_of_concurrent = string.atof(times_of_concurrent)/line_count;
    try:
        score_of_negtive += probability_of_concurrent - (word_priori_probability[word] + word_priori_probability[p_word])
    except:
        score_of_negtive += 0

    score = score_of_positive - score_of_negtive
    # print word + '\t', score
    return score

def find_word_about_ue(readfile_inverted_list, readfile_high_frequency_word, readfile_seed, writefile):
    if str(type(writefile)).find('str') >= 0:
        word_about_ue = open(writefile, 'w')
        word_high_frequency = open(readfile_high_frequency_word, 'r')
        seed_file = open(readfile_seed, 'r')
    else:
        word_about_ue = writefile
        word_high_frequency = readfile_high_frequency_word
        seed_file = readfile_seed

    seeds = []
    for line in seed_file:
        words = line.split()
        for word in words:
            seeds.append(word)

    context_list = get_context.get_context_info(readfile_inverted_list)
    context_of_seed = find_context(context_list, seeds)
    word_list = read_word(word_high_frequency)
    word_maybe_about_ue = {}

    for candidate_word in word_list:
        try:
            context_of_candidate = context_list[candidate_word]
        except:
            continue
        score = decision_ue(context_of_candidate, context_of_seed)
        # print candidate_word + '\t' + str(score)
        if score > 12.0:
            word_maybe_about_ue[word_list[candidate_word]] = score

    for word in sorted(word_maybe_about_ue.iteritems(), key = lambda k:k[1], reverse = True):
        line = str(word[1]) + ' ' + word[0] + '\n'
        # print line
        word_about_ue.write(line)

def find_context(context_list, seeds):
 #   seeds = ['价格', '速度', '快递', '质量', '性价比', '外观']

    context_of_seed = []
    for seed in seeds:
        try:
            for context in context_list[seed]:
                context_of_seed.append(context)
        except:
            continue

    return context_of_seed

def read_word(word_high_frequency):
    word_list = {}

    for line in word_high_frequency:
        elements = line.split()
        word = elements[1][:elements[1].find('/')]
        pos_tag = elements[1][elements[1].find('/') + 1:]
        if pos_tag == 'NN': #or pos_tag == 'VA' or pos_tag == 'VV' 
            word_list[word] = line[:-1]

    return word_list

def decision_ue(context_of_candidate, context_of_seed):
    score = 0.0
    for context in context_of_candidate:
        for context_pool in context_of_seed:
            for index in range(4):
                context_w = context[index][:context[index].find('/')]
                context_t = context[index][context[index].find('/') + 1:]
                context_pool_w = context_pool[index][:context_pool[index].find('/')]
                context_pool_t = context_pool[index][context_pool[index].find('/') + 1:]

                if context_w == context_pool_w:
                    if index == 2 or index == 3:
                        score += 3.0
                    else:
                        score += 1.0
                elif context_t == context_pool_t:
                    if index == 2 or index == 3:
                        score += 1.5
                    else:
                        score += 0.5

    return score

if __name__ == '__main__':
    if len(sys.argv) < 7:
        print 'please input filename'
        exit()
    find_word_about_sentiment(sys.argv[1], sys.argv[2], sys.argv[4], sys.argv[6])
    find_word_about_ue(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[5])
