#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_list_order(self):
        list_ord = [1,2,3,4,5]
        self.assertEqual(max_integer(list_ord), 5)

    def test_not_order(self):
        list_not_ord = [5,1,3,4,2]
        self.assertEqual(max_integer(list_not_ord), 5)

    def test_negative_num(self):
        list_n = [1, -2, 3, -4,]
        self.assertEqual(max_integer(list_n), 3)

    def test_only_negative_num(self):
        list_n = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(list_n), -1)

    def test_one_element(self):
        list_n = [1]
        self.assertEqual(max_integer(list_n), 1)

    def test_empty(self):
        list_n = []
        self.assertEqual(max_integer(list_n), None)

if __name__ == '__main__':
    unittest.main()

