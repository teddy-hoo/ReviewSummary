#!/bin/python
#coding=utf8

import httplib
import string

import sys

def main(product_id, filename):

    host = 'e.yhd.com'
    url = '/front-pe/productExperience/proExperience!loadProductExperience.do?'
    parameters = ['product.id', 'pagenationVO.currentPage', 'merchantId', 'orderType', 'pagenationVO.rownumperpage', 'currSiteId', 'currSiteType', 'commentFlag', 'tt', 'callback']
    # id = [44802, 16825, 44801, 1623094, 1413583]
    id = product_id
    parameter_value = (id, 1, '1', 'newest', '5', '1', '1', 'total', 'tt=Mon%20Nov%2004%202013%2017:22:12%20GMT+0800%20(CST)', 'checkItemDataHandler')

    get_data(host, url, parameters, parameter_value, filename)

def get_data(host, url, parameters, parameter_value, filename):
    global exist_comment, is_or_not_firsttime, count
    count = 0

    connection = httplib.HTTPConnection(host)

    sub_parameter = ''
    for index in range(2, len(parameter_value)):
        sub_parameter += '&' + parameters[index] + '=' + parameter_value[index]


    exist_comment = 11
    is_or_not_firsttime = True
    page_number = 1
    while exist_comment > 10:
        print '---------There are ' + str(exist_comment) + ' comments remain--------'
        parameter = parameters[0] + '='+ str(parameter_value[0])
        parameter += '&' + parameters[1] + '=' + str(page_number)
        parameter += sub_parameter
        connection.request('GET', url + parameter)
        response = connection.getresponse()
        data = response.read()
        #print data
        process_data(data, filename)
        page_number += 1

    connection.close()

def process_data(data, filename):
    global exist_comment, is_or_not_firsttime, count

    file = open(filename, "a")

    if is_or_not_firsttime:
        pos_number_of_comment = data.find('productExperienceTotalCount') + 38
        data = data[pos_number_of_comment:len(data)]
        pos_number_of_comment_end = data.find('\\')
        exist_comment = string.atoi(data[0:pos_number_of_comment_end])
        is_or_not_firsttime = False

    pos_begin = data.find("内容：")
    while pos_begin > 0:
        count += 1
        exist_comment -= 1
        pos_begin += 53
        data = data[pos_begin:len(data)]
        pos_end = data.find('<')
        comment = data[0:pos_end]
        data = data[pos_end:len(data)]
        comment_list = comment + "\n"
        print str(count) + comment_list,
        file.write(comment_list)
        pos_begin = data.find("内容：")

    file.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print 'Please input the product ID and file name'
        exit()
    main(sys.argv[1], sys.argv[2])
