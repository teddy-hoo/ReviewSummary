#!/bin/env python
#coding=utf8

import sys
import get_context
import threading
import string

def find_word_about_sentiment(readfile_inverted_list, readfile_word_statistics, writefile):
    if str(type(readfile_inverted_list)).find('str') >= 0:
        word_about_sentiment_file = open(writefile, 'w')
        inverted_list = open(readfile_inverted_list, 'r')
        word_statistics = open(readfile_word_statistics, 'r')
    else:
        word_about_sentiment_file = writefile
        inverted_list = readfile_inverted_list
        word_statistics = readfile_word_statistics

    line_number_of_word, max_line_number = get_line_number(inverted_list)
    word_priori_probability, sentiment_word = get_word_priori_probability(word_statistics)

    word_about_sentiment = {}
    for word in word_priori_probability:
        if word == '\\':
            continue
        score = decision_sentiment(word, word_priori_probability, line_number_of_word, max_line_number, sentiment_word)
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
    stop_word = '真的 足够 绝对 超级 相当 非常'
    word_count = 0
    sentiment_word = []
    print 'SEEDS OF SENTIMENT:'
    for line in word_statistics:
        info = line.split()
        word = info[1][:info[1].find('/')]
        tag = info[1][info[1].find('/') + 1:]
        if tag == 'VA' and word_count < 5:
            print word
            sentiment_word.append(word)
            word_count += 1
        if len(word) < 3 or tag == 'AD' or tag == 'NN' or tag == 'VV' or stop_word.find(word) >= 0:
            continue
        word_priori_probability[word] = string.atof(info[2])

    return word_priori_probability, sentiment_word

def decision_sentiment(word, word_priori_probability, line_number_of_word, line_count, sentiment_word):
    score = 0.0
    times_of_concurrent = 0
    for s_word in sentiment_word:
        try:
            line_number = line_number_of_word[word]
        except:
            continue
        for line_pre in line_number:
            for line_beh in line_number_of_word[s_word]:
                if line_pre == line_beh:
                    times_of_concurrent += 1
    probability_of_concurrent = string.atof(times_of_concurrent)/line_count;
    try:
        score += probability_of_concurrent - (word_priori_probability[word] + word_priori_probability[s_word])
    except:
        score += 0

    return score

def find_word_about_ue(readfile_inverted_list, readfile_high_frequency_word, writefile):
    if str(type(writefile)).find('str') >= 0:
        word_about_ue = open(writefile, 'w')
        word_high_frequency = open(readfile_high_frequency_word, 'r')
    else:
        word_about_ue = writefile
        word_high_frequency = readfile_high_frequency_word

    context_list = get_context.get_context_info(readfile_inverted_list)
    word_list,seeds = read_word(word_high_frequency)
    context_of_seed = find_context(context_list, seeds)    
    word_maybe_about_ue = {}

    '''for candidate_word in word_list:
        try:
            context_of_candidate = context_list[candidate_word]
        except:
            continue
        score = decision_ue(context_of_candidate, context_of_seed)
        # print candidate_word + '\t' + str(score)
        if score > 12.0:
            word_maybe_about_ue[word_list[candidate_word]] = score'''

    split_pos = len(word_list)/4
    for index in range(1, 5):
        th = thread_of_ue_extend(word_list[split_pos * (index - 1):split_pos * index], context_list, context_of_seed)
        word_about_ue_dic = th.run()
        for word in word_about_ue_dic:
            if not word_maybe_about_ue.has_key(word):
                word_maybe_about_ue[word] = word_about_ue_dic[word]

    for word in sorted(word_maybe_about_ue.iteritems(), key = lambda k:k[1], reverse = True):
        line = str(word[1]) + ' ' + word[0] + '\n'
        # print line
        word_about_ue.write(line)

def find_context(context_list, seeds):

    context_of_seed = []
    for seed in seeds:
        try:
            for context in context_list[seed]:
                context_of_seed.append(context)
        except:
            continue

    return context_of_seed

def read_word(word_high_frequency):
    #word_list = {}
    word_list = []
    seeds = []
    word_count = 0
    stop_word = '号店 别人 老妈 妈妈 同事 朋友 比较 老爸'
    print 'SEEDS OF UE:'
    for line in word_high_frequency:
        elements = line.split()
        word = elements[1][:elements[1].find('/')]
        pos_tag = elements[1][elements[1].find('/') + 1:]
        if pos_tag == 'NN' and stop_word.find(word) < 0: #or pos_tag == 'VA' or pos_tag == 'VV' 
            if word_count < 5 and len(word) > 3:
                print word
                seeds.append(word)
                word_count += 1
            #word_list[word] = line[:-1]
            word_list.append(word)

    return word_list, seeds

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

class thread_of_ue_extend(threading.Thread):  
    def __init__(self, word_list, context_list, context_of_seed):  
        threading.Thread.__init__(self) 
        self.word_list = word_list
        self.context_list = context_list
        self.context_of_seed = context_of_seed
        self.word_maybe_about_ue = {}
        self.score = 0.0
    def run(self):  
        for candidate_word in self.word_list:
            try:
                context_of_candidate = self.context_list[candidate_word]
            except:
                continue
            self.score = decision_ue(context_of_candidate, self.context_of_seed)
            if self.score > 12.0:
                self.word_maybe_about_ue[candidate_word] = self.score
        return self.word_maybe_about_ue

if __name__ == '__main__':
    if len(sys.argv) < 5:
        print 'please input filename'
        exit()
    find_word_about_sentiment(sys.argv[1], sys.argv[2], sys.argv[3])
    find_word_about_ue(sys.argv[1], sys.argv[2], sys.argv[4])
