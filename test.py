"""
    python -m unittest test.py
    python -m unittest test.TestSequenceFunctions
    python -m unittest test.TestSequenceFunctions.test_getTaxRate
    python -m unittest test.TestSequenceFunctions.test_getDiscountRate

"""
from ececlass import ececlass
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.ece = ececlass()

    def tearDown(self):
        pass
    
    def test_getTaxRate(self):
        self.assertEqual(self.ece.getTaxRate('UT'), 6.85)
        self.assertEqual(self.ece.getTaxRate('NV'), 8.00)
        self.assertEqual(self.ece.getTaxRate('TX'), 6.25)
        self.assertEqual(self.ece.getTaxRate('AL'), 4.00)
        self.assertEqual(self.ece.getTaxRate('CA'), 8.25)

    def test_getDiscountRate(self):
        self.assertEqual(self.ece.getDiscountRate(50000.01), 15.0)
        self.assertEqual(self.ece.getDiscountRate(10000.01), 10.0)
        self.assertEqual(self.ece.getDiscountRate( 7000.01),  7.0)
        self.assertEqual(self.ece.getDiscountRate( 5000.01),  5.0)
        self.assertEqual(self.ece.getDiscountRate( 1000.01),  3.0)
        self.assertEqual(self.ece.getDiscountRate( 1000.00),  0.0)

if __name__ == '__main__':
    unittest.main()
