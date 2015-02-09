# -*- coding: utf-8 -*-

import sys
from HTMLParser import HTMLParser

class HTMLParserForComment(HTMLParser):

    def __init__(self):
        
        HTMLParser.__init__(self)

        self.inCommentContent = False
        self.isCommentContent = False
        self.isCommentContentDD = False
        self.maybeCommentContent = False
        self.commentContents = []
        
        self.commentCount = -1
        self.inCommentCount = False
        self.isCommentCount = False

    def handle_starttag(self, tag, attrs):

        # set inCommentContent tag
        if tag == 'div':
            for key, value in attrs:
                if key == 'class' and value == 'comment-content':
                    self.inCommentContent = True
            return

        # count dl tag
        if tag == 'dl' and self.inCommentContent == True:
            self.maybeCommentContent = True
            return

        if tag == 'dd' and self.isCommentContent == True:
            self.isCommentContentDD = True
            return

        # if tag == 'dt' and self.maybeCommentContent == True:
        #     print 'ddddddddddddddddddd'
        #     self.isCommentContent = True
        #     return

        # if tag == 'span' and self.isCommentContent == True:
        #     self.isCommentContent = False
        #     self.maybeCommentContent = False
        #     return
        
        if tag == 'li':
            for key, value in attrs:
                if key == 'clstag' and value.find('allpingjia') >= 0:
                    self.inCommentCount = True
            return

        if tag == 'em' and self.inCommentCount == True:
            self.isCommentCount = True
            return
    
    def handle_endtag(self, tag):
        pass
    
    def handle_data(self, data):

        if data.decode('gbk').find('心　　得') >= 0 and self.maybeCommentContent:
            self.isCommentContent = True
            return
        
        if len(data) != 0 and self.isCommentContentDD == True:
            self.commentContents.append(data.replace('\n', '.').decode('gbk'))
            self.commentCount -= 1
            self.isCommentContent = False
            self.inCommentContent = False
            self.isCommentContentDD = False
            self.maybeCommentContent = False
            return

        if len(data) != 0 and self.isCommentCount == True:
            self.commentCount = int(data[1:-1])
            self.isCommentCount = False
            self.inCommentCount = False
            return
