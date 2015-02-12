# -*- coding: utf-8 -*-

import re

def extractId(url):

	regex = '/([0-9]*)\.'

	found = re.search(regex, url)

	if found:
		return found.group(1)
	else:
		return "none"