#!/usr/bin/env python


from chardet.universaldetector import UniversalDetector

def decode(string):
    """ detects string encoding and returns decoded string"""
    u = UniversalDetector()
    u.feed(string)
    u.close()
    result = u.result
    return string.decode(result['encoding'])
