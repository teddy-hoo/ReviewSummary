#!/bin/env python
#coding=utf8

import httplib
import urllib
import string
import sys

def main(product_id, par1, par2, filename1, filename2):

    host = 'club.jd.com'
    url = '/productpage/p-' + product_id + '-s-0-t-3-p-'
    referer = 'http://item.jd.com/' + product_id + '.html'

    get_data(host, url, par1, par2, referer, filename1, filename2)

def get_data(host, url, par1, par2, referer, filename1, filename2):
    global exist_comment, is_firsttime, pages
    headers = {'Referer':referer, 'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/30.0.1599.114 Chrome/30.0.1599.114 Safari/537.36', 'Accept-Language':'en-US,en;q=0.5'}

    connection = httplib.HTTPConnection(host)
    parameters = urllib.urlencode({'@callback':par1, '@_':par2})
    exist_comment = 11
    is_firsttime = True
    pages = 1
    page_number = 0
    while page_number <= pages:
        print '---------There are ' + str(pages - page_number) + ' pages of  comments remain--------'
        urls = url + str(page_number) + '.html?'
        connection.request('GET', urls, parameters, headers)
        response = connection.getresponse()
        data = response.read()
        #print data
        process_data(data, filename1, filename2)
        page_number += 1

    connection.close()

def process_data(data, filename1, filename2):
    global exist_comment, is_firsttime, pages

    file1 = open(filename1, "a")

    hot_comment = {}
    if is_firsttime:
        file2 = open(filename2, 'w')
        pos = data.find('commentCount') + 14
        data = data[pos:]
        pages = string.atoi(data[:data.find(',')])/10
        data = data[data.find('hotCommentTagStatistics'):]
        hot_comment_statistics = data[:data.find(']')]
        while hot_comment_statistics.find('name') >= 0:
            hot_comment_statistics = hot_comment_statistics[hot_comment_statistics.find('name') + 7:]
            comment = hot_comment_statistics[:hot_comment_statistics.find('"')]
            comment = comment.decode('GBK').encode('UTF-8')
            print comment
            hot_comment_statistics = hot_comment_statistics[hot_comment_statistics.find('count') + 7:]
            count = hot_comment_statistics[:hot_comment_statistics.find(',')]
            hot_comment[comment] = count
        for comment in hot_comment:
            file2.write(comment + '\t' + hot_comment[comment] + '\n')
        file2.close()
        is_firsttime = False

    pos_begin = data.find('content')
    while pos_begin > 0:
        pos_begin += 10
        if data[:pos_begin].find('commentId') >= 0:
            data = data[pos_begin:]
            pos_begin = data.find('content') + 10
            continue
        else:
            data = data[pos_begin:]
            pos_end = data.find('"')
            comment = data[:pos_end]
            try:
                comment = comment.decode('GBK').encode('UTF-8')
            except:
                continue
            if comment.find('div') >= 0:
                comment = comment[:comment.find('<div')]
            print comment
            file1.write(comment + '\n')
        pos_begin = data.find('content')

    file1.close()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
