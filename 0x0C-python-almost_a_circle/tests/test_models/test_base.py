#!/usr/bin/python3
""" base class tests module """
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ test cases fo base class """

    def test_id(self):
        """ test for id cases """
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 10)

    def test_to_json(self):
        """ tests for converting objects to json striing """
        dictionaryl = [{'hello': 3, 'python': 6}, {'extra': 4}]
        result = "[{\"hello\": 3, \"python\": 6}, {\"extra\": 4}]"
        self.assertEqual(Base.to_json_string(dictionaryl), result)

    def test_from_json(self):
        """ tests for converting json string to object """
        string = "[{\"hello\": 3, \"python\": 6}, {\"extra\": 4}]"
        result = [{'hello': 3, 'python': 6}, {'extra': 4}]
        self.assertEqual(Base.from_json_string(string), result)
