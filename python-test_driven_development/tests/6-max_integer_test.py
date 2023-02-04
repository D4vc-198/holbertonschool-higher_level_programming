#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_list_order(self):
        list_ord = [1,2,3,4,5]
        self.assertEqual(max_integer(list_ord), 5)

    def test_not_order(self):
        list_not_ord = [2,5,3,4]
        self.assertEqual(max_integer(list_not_ord), 5)

if __name__ == '__main__':
    unittest.main()

