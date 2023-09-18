#!/usr/bin/python3
""" rectangle class tests module """
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ test cases for the rectangle class """

    def test_init(self):
        """ tests for instnce attribute """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 4, 12)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r2.id, 6)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r3.y, 4)

    def test_display(self):
        """ tests for the method display """
        r1 = Rectangle(4, 6)
        r2 = Rectangle(4, 6, 2, 3)
        r1_display = "\n####\n####\n####\n####\n####\n####\n"
        r2_display = "\n\n   ####\n   ####\n   ####\n   ####\n   ####\n   ####\n"
        self.assertEqual(r1.display(), r1_display)
        self.assertEqual(r2.display(), r2_display)

    def test_str(self):
        """ tests for the str method """
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        r1_str = "[Rectangle] (12) 2/1 - 4/6"
        r2_str = "[Rectangle] (7) 1/0 - 5/5"
        self.assertEqual(str(r1), r1_str)
        self.assertEqual(str(r2), r2_str)

    def test_update(self):
        """ tests for update method """
        r = Rectangle(10, 10, 10, 10)
        r1_str = "[Rectangle] (10) 10/10 - 10/10"
        self.assertEqual(str(r), r1_str)
        r.update(height=1)
        r2_str = "[Rectangle] (10) 10/10 - 10/1"
        self.assertEqual(str(r), r2_str)
        r.update(width=1, x=2)
        r3_str = "[Rectangle] (10) 2/10 - 1/1"
        self.assertEqual(str(r), r3_str)
        r.update(y=1, width=2, x=3, id=98)
        r4_str = "[Rectangle] (98) 3/1 - 2/1"
        self.assertEqual(str(r), r4_str)
        r.update(x=1, height=2, y=3, width=4)
        r5_str = "[Rectangle] (98) 1/3 - 4/2"
        self.assertEqual(str(r), r5_str)
        r.update(6)
        r6_str = "[Rectangle] (6) 1/3 - 4/2"
        self.assertEqual(str(r), r6_str)
        r.update(6, 2, 3, 4, 5)
        r7_str = "[Rectangle] (6) 4/5 - 2/3"
        self.assertEqual(str(r), r7_str)

    def test_to_dictionary(self):
        """ tests for dictionary method """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = {'x': 1, 'y': 9, 'id': 8, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), r1_dictionary)
        self.assertEqual(type(r1.to_dictionary()), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1 == r2, False)
