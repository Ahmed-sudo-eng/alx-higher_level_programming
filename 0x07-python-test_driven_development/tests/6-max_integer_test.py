#!/usr/bin/python3
"""
Unittest for max_integer([])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This class is for testing max_integer"""
    def test_list(self):
        """Testing normal lists"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([9, 2, 6]), 9)
        self.assertEqual(max_integer([2, 7, 5]), 7)

    def test_empty_list(self):
        """Testing empty lists"""
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
