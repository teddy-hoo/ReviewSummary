# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import httplib2
import config
import base
from htmlParserForComment import HTMLParserForComment
from htmlParser import HtmlParser
from comments import Comments

class Retrieve:

    def __init__(self):

        # set default str encoding type
        reload(sys)
        sys.setdefaultencoding('utf-8')

        # set httplib2 retry time
        httplib2.RETRIES = 10

        self.http = httplib2.Http()
        self.parser = HTMLParserForComment()

        self.commentCount = 0

    # save comment to db
    def saveComments(self):

        # connect db
        base.db.connect()

        for c in self.parser.commentContents:
            Comments.create(raw = c)

    def retrieveComments(self):
        
        # first time
        response, content = self.http.request(config.COMMENTSURL + \
                            '1452957314-3-1-0.html')
        self.parser.feed(content)
        self.parser.close()

        c = self.parser.commentCount

        print "There are", c, "comments in total."
        pageCount = c / 30 if c % 30 == 0 else c / 30 + 1

        # iteration
        for p in xrange(1, pageCount + 1):
            print "Retrieving", str(30 * (p - 1)), " -- ", str(30 * p - 1), \
                  "comments..."
            try:
                response, content = self.http.request(config.COMMENTSURL + \
                                    '1452957314-3-' + str(p) + '-0.html')
                self.parser.feed(content)
                self.parser.close()
            except(httplib2.ServerNotFoundError):
                p -= 1
                print "Page", str(p), "failed, try it again..."


r = Retrieve()
r.retrieveComments()
r.saveComments()