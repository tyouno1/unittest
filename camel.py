#!/usr/bin/python
# coding=utf-8
import unittest
import pdb

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

# 测试用例 
class TestCameltoUnderline(unittest.TestCase):
    def test_upper_num(self):
        camel = "aaaC4321#A@ab1_"
        underLine = "aaa_c4321#_a@ab1_"
        self.assertEqual(camel_to_underline(camel), underLine)
    def test_upper(self):
        camel = "aaaBbbCccc"
        underLine = "aaa_bbb_cccc"
        self.assertEqual(camel_to_underline(camel), underLine)


if __name__ == '__main__':
    unittest.main()
