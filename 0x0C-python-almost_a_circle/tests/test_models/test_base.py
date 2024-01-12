#!/usr/bin/python3
""" module for Base unit tests """

import unittest
module = __import__('models.base', fromlist=['Base'])
Base = module.Base

class TestBase(unittest.TestCase):
    def test_id_incrementation(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        b4 = Base(12)
        b5 = Base()

        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

if __name__ == '__main__':
    unittest.main()
