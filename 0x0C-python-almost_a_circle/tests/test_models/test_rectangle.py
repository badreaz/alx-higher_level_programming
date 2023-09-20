#!/usr/bin/python3
""" rectangle class tests module """
import unittest
import os
import io
from models.rectangle import Rectangle
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """ test cases for the rectangle class """

    def test_init(self):
        """ tests for instnce attribute """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 4, 12)
        self.assertEqual(r1.id, 9)
        self.assertEqual(r2.id, 10)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r3.y, 4)
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_str(self):
        """ tests for the str method """
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1, 0, 10)
        r1_str = "[Rectangle] (12) 2/1 - 4/6"
        r2_str = "[Rectangle] (10) 1/0 - 5/5"
        self.assertEqual(str(r1), r1_str)
        self.assertEqual(str(r2), r2_str)

    def test_display(self):
        """ tests display mmethod """
        r1 = Rectangle(2, 3, 0, 0 ,5)
        r2 = Rectangle(2, 3, 1, 0 ,5)
        r3 = Rectangle(2, 3, 1, 1 ,5)
        r1_d = "##\n##\n##\n"
        r2_d = " ##\n ##\n ##\n"
        r3_d = "\n ##\n ##\n ##\n"
        with patch('sys.stdout', new_callable=io.StringIO) as out:
            r1.display()
            display = out.getvalue()
        self.assertEqual(r1_d, display)
        with patch('sys.stdout', new_callable=io.StringIO) as out:
            r2.display()
            display = out.getvalue()
        self.assertEqual(r2_d, display)
        with patch('sys.stdout', new_callable=io.StringIO) as out:
            r3.display()
            display = out.getvalue()
        self.assertEqual(r3_d, display)

    def test_update(self):
        """ tests for update method """
        r = Rectangle(10, 10, 10, 10, 8)
        r1_str = "[Rectangle] (8) 10/10 - 10/10"
        self.assertEqual(str(r), r1_str)
        r.update(height=1)
        r2_str = "[Rectangle] (8) 10/10 - 10/1"
        self.assertEqual(str(r), r2_str)
        r.update(width=1, x=2)
        r3_str = "[Rectangle] (8) 2/10 - 1/1"
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

    def test_create(self):
        """ tests for create base class method """
        r1 = Rectangle.create(**{ 'id': 89 })
        self.assertEqual(str(r1), str(Rectangle(1, 1, 0, 0, 89)))
        r2 = Rectangle.create(**{ 'id': 89, 'width': 1 })
        self.assertEqual(str(r2), str(Rectangle(1, 1, 0, 0, 89)))
        r3 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        self.assertEqual(str(r3), str(Rectangle(1, 2, 0, 0, 89)))
        r4 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        self.assertEqual(str(r4), str(Rectangle(1, 2, 3, 0, 89)))
        r5 = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(str(r5), str(Rectangle(1, 2, 3, 4, 89)))

    def test_from_to_file(self):
        """ tests for save_to_file, load_from_file methods """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())
        os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())
        os.remove("Rectangle.json")
        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 6)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(f.read()), 52)
        load = Rectangle.load_from_file()
        self.assertTrue(type(load[0]) == Rectangle)
        os.remove("Rectangle.json")
        load = Rectangle.load_from_file()
        self.assertEqual(load, [])

    def test_to_dictionary(self):
        """ tests for dictionary method """
        r1 = Rectangle(10, 2, 1, 9, 11)
        r1_dictionary = {'x': 1, 'y': 9, 'id': 11, 'height': 2, 'width': 10}
        self.assertEqual(r1.to_dictionary(), r1_dictionary)
        self.assertEqual(type(r1.to_dictionary()), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1 == r2, False)
