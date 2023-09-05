#!/usr/bin/python3
""" unittests for max_integer([..]) """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ unittest for max_integer """

    def test_Error(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
        self.assertEqual(max_integer([1, 2, 3, -10]), 3)
        self.assertEqual(max_integer([1000, 33, 200, -10]), 1000)
