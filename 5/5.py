#!/usr/bin/env python
__author__ = ‘alinered’

import pickle
import urllib2

def peak():
    webpage = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
    result = pickle.loads(webpage)
    s = ''
    for i in result:
        for j in i:
            s += j[0] * j[1]
        s += '\n'
    return s

if __name__ == '__main__':
    print peak()
