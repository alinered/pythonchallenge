#!/usr/bin/env python
__author__ = ‘alinered’

import urllib2

def chain():
    #num = '12345', first while: result is "going.", then next nothing is 6711
    #num = '6711', first while: result is 'peak.html', then next nothing is 6711
    num = '6711'
    while num.isdigit():
        req = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + num)
        response = urllib2.urlopen(req)
        the_page = response.read()
        num = the_page.split()
        num = num[-1]
        print num
    return num

if __name__ == '__main__':
    print chain()
