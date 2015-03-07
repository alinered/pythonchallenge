#!/usr/bin/env python
__author__ = ‘alienred’

def power(num):
    n = 1
    for i in range(38):
        n *= 2
    return n

if __name__ == '__main__':
    print power(38)
