#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import config
from stopword import StopWord

# static the word frequency

# nouns(NN)
# 手机#NN
# 苹果#NN
# 东西#NN
# 速度#NN 467
# 屏幕#NN 422

# predicative adjective(VA)
# 不错#VA 2407
# 快#VA 1174
# 大#VA 556
# 满意#VA 366
# 好用#VA 362


def wordCount(mid = 1):

	words    = {}
	s        = StopWord()
	comments = open('../data/%s.%s.merged.utf-8' % (config.PREFIX, mid))

	print('counting words...')
	for c in comments:
		ws = c.strip().split(' ')
		for w in ws:
			word = w.split('#')[0]
			if not s.isStopWord(word):
				if words.has_key(w):
					words[w] += 1
				else:
					words[w]  = 1
	print('done...')
	comments.close()

	nouns         = open('../data/%s.%s.frequent.nouns.utf-8' % (config.PREFIX_WORD, mid), 'w')
	allNouns      = open('../data/%s.%s.all.nouns.utf-8' % (config.PREFIX_WORD, mid), 'w')
	adjectives    = open('../data/%s.%s.frequent.adjectives.utf-8' % (config.PREFIX_WORD, mid), 'w')
	allAdjectives = open('../data/%s.%s.all.adjectives.utf-8' % (config.PREFIX_WORD, mid), 'w')

	sortedWords = sorted(words.iteritems(), key = lambda k:k[1], reverse = True)

	# ouput nouns
	# for s in sortedWords:
	# 	word = s[0].split('#')[0]
	# 	pos  = s[0].split('#')[1]
	# 	f    = s[1]
	# 	if pos == 'NN':
	# 		print word, f
	
	print('writing nouns...')
	count = 0
	length = len(sortedWords)

	for i in range(length):
		word = sortedWords[i][0].split('#')[0]
		pos  = sortedWords[i][0].split('#')[1]
		# if count < 5:
		# 	if pos == 'NN':
		# 		nouns.write(sortedWords[i][0] + '\n')
		# 		count += 1
		# else:
		if pos == 'NN':
			allNouns.write('%s %s\n' % (sortedWords[i][0], sortedWords[i][1]))

	nouns.close()
	allNouns.close()
	print('done...')

	print('writing adjectives...')
	count = 0

	for i in range(length):
		word = sortedWords[i][0].split('#')[0]
		pos  = sortedWords[i][0].split('#')[1]
		if count < 5:
			if pos == 'VA':
				adjectives.write(sortedWords[i][0] + '\n')
				count += 1
		else:
			break

	adjectives.close()
	allAdjectives.close()
	print('done...')
