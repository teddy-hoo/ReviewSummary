#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import config

def select(mid):

	allComments = open('../data/%s.%s.raw.utf-8' % (config.PREFIX, mid))
	selected    = open('../data/%s.%s.200.utf-8' % (config.PREFIX, mid), 'w')
	count       = 0

	for a in allComments:
		selected.write(a)
		count += 1
		if count >= 200:
			break

	allComments.close()
	selected.close()
