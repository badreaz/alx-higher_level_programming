#!/usr/bin/python3
""" square class tests module """
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ test cases for square class """

    def test_init(self):
        """ tests for the instance attribute """

        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s1), "[Square] (9) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        self.assertEqual(str(s2), "[Square] (10) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        self.assertEqual(str(s3), "[Square] (11) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_update(self):
        """ tests for update method """

        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (14) 0/0 - 5")
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_to_dictionary(self):
        """ tests for to_dictionary method """

        s1 = Square(10, 2, 1)
        self.assertEqual(str(s1), "[Square] (12) 2/1 - 10")
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 12, 'x': 2, 'size': 10, 'y': 1})
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        self.assertEqual(str(s2), "[Square] (13) 1/0 - 1")
        s2.update(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (12) 2/1 - 10")
        self.assertFalse(s1 == s2)
