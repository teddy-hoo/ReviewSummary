#!/bin/env python
#coding=utf8

import sys
import string

def f_stat(readfile):
	read_file = open(readfile, 'r')
	write_file = open(readfile + '_stat', 'w')

	title = read_file.readline()
	write_file.write(title)

	jd = read_file.readline()
	jd_data = jd.split()
	jd_total = string.atof(jd_data[1])
	jd_correct = string.atof(jd_data[2])

	me = read_file.readline()
	me_data = me.split()
	me_total = string.atof(me_data[1])
	me_correct = string.atof(me_data[2])

	jd_wrong = jd_total - jd_correct
	me_wrong = me_total - me_correct

	jd_precision = jd_correct / jd_total
	me_precision = me_correct / me_total

	jd_recall = jd_correct / (jd_correct + me_correct)
	me_recall = me_correct / (jd_correct + me_correct)

	jd_f = 2 * jd_precision * jd_recall / (jd_precision + jd_recall)
	me_f = 2 * me_precision * me_recall / (me_precision + me_recall)

	jd_line = 'JD' + '\t' + str(jd_total) + '\t' + str(jd_correct) + '\t' + str(jd_wrong) + '\t' + str(jd_precision) + '\t' + str(jd_recall) + '\t' + str(jd_f) + '\n'
	me_line = 'ME' + '\t' + str(me_total) + '\t' + str(me_correct) + '\t' + str(me_wrong) + '\t' + str(me_precision) + '\t' + str(me_recall) + '\t' + str(me_f) + '\n'

	write_file.write(jd_line)
	write_file.write(me_line)

	read_file.close()
	write_file.close()

if __name__ == '__main__':
	f_stat(sys.argv[1])