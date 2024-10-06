import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_add(self):
        result = self.calc.add(4, 7)
        self.assertEqual(result, 11)
    
    def test_subtract(self):
        result = self.calc.subtract(8, 3)
        self.assertEqual(result, 5)
    
    def test_multiply(self):
        result = self.calc.multiply(5, 5)
        self.assertEqual(result, 25)
    
    def test_divide(self):
            result = self.calc.divide(6, 0)
            

