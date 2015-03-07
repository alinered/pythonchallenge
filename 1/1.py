#!/usr/bin/env python
__author__ = 'alinered'

import string

def trans():
    s1 = 'abcdefghijklmnopqrstuvwxyz'
    s2 = 'cdefghijklmnopqrstuvwxyzab'
    transmap = string.maketrans(s1, s2)
    s = """
        g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
        """
    return s.translate(transmap)

if __name__ == '__main__':
    print trans()
