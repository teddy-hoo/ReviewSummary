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
from merchants import Merchants
from extractMerchantId import extractId

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
    def saveComments(self, m):

        # connect db
        base.db.connect()

        for c in self.parser.commentContents:
            Comments.create(raw = c, merchantId = m)

        base.db.close()

    def retrieveComments(self, id):
        
        # first time
        response, content = self.http.request(config.COMMENTSURL + \
                            id + '-3-1-0.html')
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
                                    id + '-3-' + str(p) + '-0.html')
                self.parser.feed(content)
                self.parser.close()
            except(httplib2.ServerNotFoundError):
                p -= 1
                print "Page", str(p), "failed, try it again..."

def saveMerchant(id, name):

    base.db.connect()

    m = Merchants.create(mid = id, name = name)

    base.db.close()

    return m


def retrieve(arguments):
    url = arguments[1]
    name = 'unknown'
    
    if len(arguments) > 2:
        name = arguments[2]
    
    id = extractId(url)
    if id == 'none':
        print "Merchant id is invalid!"
        exit()

    m = saveMerchant(id, name)

    r = Retrieve()
    r.retrieveComments(id)
    r.saveComments(m)


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print 'Please input the url of the merchant'
        exit()
    
    retrieve(sys.argv)
