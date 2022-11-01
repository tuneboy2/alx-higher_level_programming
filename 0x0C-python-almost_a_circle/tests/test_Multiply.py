#!/usr/bin/python3
""" A module that defines a Unit test class """


import Multiply
import unittest


class TestMultiply(unittest.TestCase):
    """ A Unit test testcase """
    def test_multiply(self):
        """ Test the result of multiplication """
        self.assertEqual(Multiply.multiply(5, 10), 50)
