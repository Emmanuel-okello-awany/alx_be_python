import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(4,5),9)
        # Add more assertions to thoroughly test the add method.
        
    def test_subtraction(self):
        """Test subtraction method"""
        self.assertEqual(self.calc.subtract(5,2),3)
        self.assertEqual(self.calc.subtract(7,3),4)
        self.assertEqual(self.calc.subtract(2,0),2)
        
    def test_multiplication(self):
        """Test for multiplication"""
        self.assertEqual(self.calc.multiply(2,3),6)
        self.assertEqual(self.calc.multiply(4,2),8)
        self.assertEqual(self.calc.multiply(5,5),25)
        
    def test_division(self):
        """Test for division"""
        self.assertEqual(self.calc.divide(4,2),2)
        self.assertEqual(self.calc.divide(10,2),5)
        self.assertEqual(self.calc.divide(4,2),2)
        
        
        
if __name__ == "__main__":
   unittest.main()


        

# Remember to write additional test methods for subtract, multiply, and divide.