#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup as bs4
import urllib2

def query():
    word = raw_input('\> ')
    print '---------- %s ----------' %(word)
    qurl = 'http://dict.cn/' + word
    #print qurl
    try:
        request = urllib2.Request(qurl)
        response = urllib2.urlopen(request,timeout=500)
        content = response.read()
    except expression as identifier:
        print 'query error'
        exit
    

    soup = bs4(content, 'html.parser')
    ls = soup.body.div.div.div.ul.find_all('li')
    for child in ls[:-1]:
        print child.span.string + ' ' + child.strong.string

if __name__ == '__main__':
    while True:
        query()