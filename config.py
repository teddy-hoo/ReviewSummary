#!/usr/bin/env python
# -*- coding: utf-8 -*-

# configurations

# encode type
ENCODE_TYPE = 'utf-8'

# data file name prefix
PREFIX               = 'comments'
PREFIX_WORD          = 'words'
PREFIX_CONTEXT       = 'context'
PREFIX_FEATURE       = 'feature'
PREFIX_DESCRIPTION_P = 'positive.description'
PREFIX_DESCRIPTION_N = 'negtive.description'

# java path
JAVA_PATH = 'java'

# comments URL
COMMENTSURL = 'http://club.jd.com/review/'

# database path
# for ubuntu
# DATABASE = '/home/teddy/Documents/github/ReviewSummary/data/commentSummary.db'
# for windows
DATABASE = 'C:/Users/eway/Documents/GitHub/ReviewSummary/data/commentSummary.db'

# stanford nlp software path
# for ubuntu
# STANFORD_PATH = '/home/teddy/stanford_software'
# SEGMENT       = '/stanford-segmenter-2015-01-30'
# POSTAG        = '/stanford-postagger-full-2015-01-30'
# for windows
STANFORD_PATH = 'C:/stanford'
SEGMENT       = '/segmenter'
POSTAG        = '/postagger'

# jar name
SEGMENT_JN = 'stanford-segmenter-3.5.1.jar'
POSTAG_JN  = 'stanford-postagger-3.5.1.jar'

# class name
SEGMENT_CN = 'edu.stanford.nlp.ie.crf.CRFClassifier'
POSTAG_CN  = 'edu.stanford.nlp.tagger.maxent.MaxentTagger'

# factors
WORD_COUNT_FACTOR   = 0.85
PRE_CONTEXT_FACTOR  = 0.05
POST_CONTEXT_FACTOR = 0.1

# positive and nagtive words file
# for ubuntu
# POSITIVE_WORDS = '/home/teddy/Documents/github/ReviewSummary/data/sentiment_positive'
# NEGTIVE_WORDS  = '/home/teddy/Documents/github/ReviewSummary/data/sentiment_negtive'
# for windows
POSITIVE_WORDS = 'C:/Users/eway/Documents/GitHub/ReviewSummary/data/sentiment_positive'
NEGTIVE_WORDS  = 'C:/Users/eway/Documents/GitHub/ReviewSummary/data/sentiment_negtive'
