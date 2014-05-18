#!/bin/env python
#coding=utf8

import sys

def caculate_frequency_terms(readfile_comment, readfile_terms, writefile):
	if str(type(readfile_comment)).find('str') >= 0:
		comment_segmented = open(readfile_comment, 'r')
		term_file = open(readfile_terms, 'r')
		result_statistics = open(writefile, 'w')
	else:
		comment_segmented = readfile
		term_file = readfile_terms
		result_statistics = writefile

	terms = read_terms(term_file)
	comments = read_comment(comment_segmented)

	result = {}
	for index0 in range(len(terms)):
		include_comment = [0]
		for index1 in range(len(comments)):
			if decision(terms[index0], comments[index1]):
				include_comment[0] += 1
				include_comment.append(index1)
		result[index0] = include_comment

	for term_frequency in sorted(result.iteritems(), key = lambda k:k[1][0], reverse = True):
		line = ''
		for word in terms[term_frequency[0]]:
			line += word
		for number in term_frequency[1]:
			line += '\t' + str(number)
		line += '\n'
		print line,
		result_statistics.write(line)

def read_terms(file):
	terms = []
	for line in file:
		terms.append(line.split())
	return terms

def read_comment(file):
	comments = []
	for line in file:
		comments.append(line.split())
	return comments
	
def decision(term, comment):
	for word_term in term:
		is_include = 0
		for word_comment in comment:
			if word_term == word_comment:
				is_include += 1

	if is_include > len(term):
		return True
	return False


if __name__ == '__main__':
	if len(sys.argv) < 4:
		print 'Please input filename!'
		exit()
	caculate_frequency_terms(sys.argv[1], sys.argv[2], sys.argv[3])