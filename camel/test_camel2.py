# coding: utf-8
import unittest
import jinja2
from camel2 import *

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
