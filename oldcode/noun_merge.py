#!/bin/env python
#coding=utf8

import sys

def merge(readfile, writefile):
	if str(type(readfile)).find('str') >= 0:
		tagged_sentences = open(readfile, 'r')
		merge_result = open(writefile, 'w')
	else:
		tagged_sentences = readfile
		merge_result = writefile

	for sentence in tagged_sentences:
		word_tags = sentence.split()
		new_sentence = ''
		pre_word = ''
		pre_tag = ''
		merged = False
		for word_tag in word_tags:
			word = word_tag[:word_tag.find('#')]
			tag = word_tag[word_tag.find('#') + 1:]
			if pre_tag == 'NN' and tag == 'NN':
				pre_word += word
				print pre_word
				merged = True
			if merged and tag == 'NN':
				continue
			merged = False
			if pre_word != '':
				new_sentence += (pre_word + '/' + pre_tag + ' ')
			pre_word = word
			pre_tag = tag
		new_sentence += (pre_word + '/' + pre_tag + '\n')
		merge_result.write(new_sentence)

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'please input filename'
		exit()
	merge(sys.argv[1], sys.argv[2])
