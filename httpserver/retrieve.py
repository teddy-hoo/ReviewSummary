# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', ''))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'helpers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

import httplib2
import config
import base
from htmlParserForComment import HTMLParserForComment
import HTMLParser
from comments import Comments
from merchants import Merchants
from extractMerchantId import extractId

class Retrieve:

    def __init__(self):

        # set httplib2 retry time
        httplib2.RETRIES = 10

        self.http = httplib2.Http()
        self.parser = HTMLParserForComment()

        self.commentCount = 0
        self.comments = []

    # save comment to db
    def saveComments(self, m):

        data = open('../data/%s.%s.raw.utf-8' % (config.PREFIX, m.id), 'w')

        for c in self.comments:
            clean = c.strip()
            data.write(clean + '\n')

        data.close()

        # connect db
        # base.db.connect()

        # print "There are", len(self.comments), "comments in total."

        # print('writing comments to db...')

        # for c in self.comments:
        #     clean = c.strip()
        #     if len(clean) > 0:
        #         Comments.create(raw = clean, merchantId = m)

        # print('done...')

        # base.db.close()

    def retrieveComments(self, id):

        # first time
        response, content = self.http.request(config.COMMENTSURL + \
                            id + '-3-1-0.html')
        self.parser.feed(content)
        self.parser.close()

        self.commentCount = self.parser.total
        self.parser.commentContents = []

        pageCount = self.commentCount / 30 if self.commentCount % 30 == 0 else self.commentCount / 30 + 1

        # iteration
        for p in xrange(1, pageCount + 1):

            print "Retrieving", len(self.comments), " -- ", len(self.comments) + 29, \
                  "comments..."
            try:
                response, content = self.http.request(config.COMMENTSURL + \
                                    id + '-3-' + str(p) + '-0.html')
                self.parser.feed(content)
                self.parser.close()
                for c in self.parser.commentContents:
                    self.comments.append(c)
                self.parser.commentContents = []
            except(httplib2.ServerNotFoundError):
                p -= 1
                print "Page", str(p), "failed, try it again..."

def saveMerchant(id, name):

    base.db.connect()

    m = Merchants.create(mid = id, name = name)

    base.db.close()

    return m


def retrieve(url, name = 'unknown'):

    id = extractId(url)
    if id == 'none':
        print "Merchant id is invalid!"
        exit()

    m = saveMerchant(id, name)

    r = Retrieve()
    r.retrieveComments(id)
    r.saveComments(m)

    return m.id


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print 'Please input the url of the merchant'
        exit()

    url = sys.argv[1]
    name = 'unknown'
    if len(sys.argv) > 2:
        name = sys.argv[2]
    retrieve(url, name)
