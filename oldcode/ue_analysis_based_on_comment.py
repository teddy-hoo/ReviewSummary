#!/bin/env python
#coding=utf8

import sys
import datetime
import word_extend
from inverted_list import get_inverted_list
from statistics import word_statistics
from high_frequency_word import pre_process_high_frequency_word
from ue_evaluation import sentiment_about_ue_evaluation
from remove_disturb import remove_disturb_comment

def ue_analysis_based_on_comment(filename,file_seed_ue = None, file_seed_sentiment = None):
    starttime = datetime.datetime.now()
    print '------BEGIN ue_analysis------' + '\n'

    starttime_step = datetime.datetime.now()
    print '------BEGIN remove_disturb_comment------' + '\n'
    readfile = open(filename, 'r')
    comment_without_disturb = filename + '_without_disturb'
    writefile = open(comment_without_disturb, 'w')
    remove_disturb_comment(readfile, writefile)
    writefile.close()
    readfile.close()
    print '------END remove_disturb_comment------' + '\n'
    endtime_step = datetime.datetime.now()
    print '------USED TIME remove_disturb_comment ', (endtime_step - starttime_step).seconds, 'seconds!------' + '\n'

    starttime_step = datetime.datetime.now()
    print '------BEGIN word_statistics------' + '\n'
    readfile = open(comment_without_disturb, 'r')
    comment_word_statistics = filename + '_word_statistics'
    writefile = open(comment_word_statistics, 'w')
    word_statistics(readfile, writefile)
    writefile.close()
    readfile.close()
    print '------END word_statistics------' + '\n'
    endtime_step = datetime.datetime.now()
    print '------USED TIME word_statistics ', (endtime_step - starttime_step).seconds, 'seconds!------' + '\n'

    starttime_step = datetime.datetime.now()
    print '------BEGIN pre_process_high_frequency_word------' + '\n'
    readfile = open(comment_word_statistics, 'r')
    comment_high_frequency_word = filename + '_high_frequency'
    writefile = open(comment_high_frequency_word, 'w')
    pre_process_high_frequency_word(readfile, writefile)
    writefile.close()
    readfile.close()
    print '------END pre_process_high_frequency_word------' + '\n'
    endtime_step = datetime.datetime.now()
    print '------USED TIME pre_process_high_frequency_word ', (endtime_step - starttime_step).seconds, 'seconds!------' + '\n'

    starttime_step = datetime.datetime.now()
    print '------BEGIN get_inverted_list------' + '\n'
    readfile = open(comment_without_disturb, 'r')
    comment_inverted_list = filename + '_inverted_list'
    writefile = open(comment_inverted_list, 'w')
    get_inverted_list(readfile, writefile)
    readfile.close()
    writefile.close()
    print '------END get_inverted_list------' + '\n'
    endtime_step = datetime.datetime.now()
    print '------USED TIME get_inverted_list ', (endtime_step - starttime_step).seconds, 'seconds!------' + '\n'

    starttime_step = datetime.datetime.now()
    print '------BEGIN find_word_about_ue------' + '\n'
    readfile_inverted_list = open(comment_inverted_list, 'r')
    readfile_frequency_word = open(comment_high_frequency_word, 'r')
    readfile_seed = open(file_seed_ue, 'r')
    comment_word_about_ue = filename + '_word_about_ue'
    writefile = open(comment_word_about_ue, 'w')
    word_extend.find_word_about_ue(readfile_inverted_list, readfile_frequency_word, readfile_seed, writefile)
    readfile_inverted_list.close()
    readfile_frequency_word.close()
    writefile.close()
    print '------END find_word_about_ue------' + '\n'
    endtime_step = datetime.datetime.now()
    print '------USED TIME find_word_about_ue ', (endtime_step - starttime_step).seconds, 'seconds!------' + '\n'

    starttime_step = datetime.datetime.now()
    print '------BEGIN find_word_about_sentiment------' + '\n'
    readfile_inverted_list = open(comment_inverted_list, 'r')
    readfile_frequency_word = open(comment_high_frequency_word, 'r')
    readfile_seed = open(file_seed_sentiment, 'r')
    comment_word_about_sentiment = filename + '_word_about_sentiment'
    writefile = open(comment_word_about_sentiment, 'w')
    word_extend.find_word_about_sentiment(readfile_inverted_list, readfile_frequency_word, readfile_seed, writefile)
    readfile_inverted_list.close()
    readfile_frequency_word.close()
    writefile.close()
    print '------END find_word_about_sentiment------' + '\n'
    endtime_step = datetime.datetime.now()
    print '------USED TIME find_word_about_sentiment ', (endtime_step - starttime_step).seconds, 'seconds!------' + '\n'

    starttime_step = datetime.datetime.now()
    print '------BEGIN sentiment_about_ue_evaluation------' + '\n'
    readfile_inverted_list = open(comment_inverted_list, 'r')
    readfile_sentiment_word = open(comment_word_about_sentiment, 'r')
    readfile_ue_word = open(comment_word_about_ue, 'r')
    comment_evaluation = filename + '_ue_evaluation'
    writefile = open(comment_evaluation, 'w')
    sentiment_about_ue_evaluation(readfile_sentiment_word, readfile_ue_word, readfile_inverted_list, writefile)
    print '------END sentiment_about_ue_evaluation------' + '\n'
    endtime_step = datetime.datetime.now()
    print '------USED TIME sentiment_about_ue_evaluation ', (endtime_step - starttime_step).seconds, 'seconds!------' + '\n'

    endtime = datetime.datetime.now()
    print '------END ue_analysis------' + '\n'
    print '------USED TIME ue_analysis ', (endtime - starttime).seconds, ' seconds!------'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Please input a file name!'
        exit()
    ue_analysis_based_on_comment(sys.argv[1], sys.argv[2], sys.argv[3])