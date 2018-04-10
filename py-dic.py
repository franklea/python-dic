#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup as bs4
import urllib2

promot = '''
 ___  _  _  ___  __  __ 
(  ,\( \/ )(   \(  )/ _)
 ) _/ \  /  ) ) ))(( (_ 
(_)  (__/  (___/(__)\__)
'''

def query():
    word = raw_input('\> ')
    if word == '88':
        print 'Have a good day ~ \nbye~'
        exit(0)
    
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

    # get pronunciation
    try:
        ls_pr = soup.body.div.div.div.find_all('span')
        print '[O] en: ' + ls_pr[1].bdo.string + '; ' + 'us: ' + ls_pr[2].bdo.string
    except:
        print 'get pronounciation failed...'
    
    try:
        ls = soup.body.div.div.div.ul.find_all('li')
        for child in ls[:-1]:
            print '[*] ' + child.span.string + ' ' + child.strong.string
    except:
        print 'Qeury failed...\nPlease check your spelling...'

if __name__ == '__main__':
    print promot

    while True:
        query()
