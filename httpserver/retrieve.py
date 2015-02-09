# -*- coding: utf-8 -*-

import httplib2
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
from htmlParserForComment import HTMLParserForComment
from htmlParser import HtmlParser

# set default str encoding type
reload(sys)
sys.setdefaultencoding('utf-8')

# constants
rawCommentsFile = open('../data/rawComments.utf-8', 'w')
path            = 'http://club.jd.com/review/'

def outputComment(output, comments):

    for c in comments:
        output.write(c + '\n')

httplib2.RETRIES = 10
h = httplib2.Http('.cache')

parser = HTMLParserForComment()

# first time
response, content = h.request(path + '1217524-3-1-0.html')
parser.feed(content)
parser.close()
commentCount = parser.commentCount
outputComment(rawCommentsFile, parser.commentContents)

print "There are", commentCount, "comments in total."
pageCount = commentCount / 30 if commentCount % 30 == 0 else commentCount / 30 + 1

# iteration
for p in xrange(1, pageCount + 1):

    print "Retrieving", str(30 * (p - 1)), " -- ", str(30 * p - 1), "comments..."
    
    try:
        response, content = h.request(path + '1217524-3-' + str(p) + '-0.html')
        parser.feed(content)
        parser.close()
        commentCount = parser.commentCount
        outputComment(rawCommentsFile, parser.commentContents)
    except(httplib2.ServerNotFoundError):
        p -= 1
        print "Page", str(p), "failed, try it again..."

rawCommentsFile.close()
