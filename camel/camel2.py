#!/usr/bin/python
# coding=utf-8
#import pdb

def camel_to_underline(camel_format):
    '''
    驼峰命名格式->下划线命名格式
    '''
    underline_format=''
    if isinstance(camel_format, str):
        for _s_ in camel_format:
	    #pdb.set_trace()
            underline_format += '_'+_s_.lower() if _s_.isupper() and  _s_.isalpha() else _s_
    return underline_format

