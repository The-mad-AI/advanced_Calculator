import unittest
import os
import math
from unittest.mock import patch
from io import StringIO
from calculator import Calculator

class TestAdvancedCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        
    def test_add(self):
        self.assertEqual(self.calc.add(5, 2), 7)
        self.assertEqual(self.calc.add(-1, 6), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6, 10), -4)
        self.assertEqual(self.calc.subtract(5, 15), -10)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(-5, 2), -10)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-100, 50), -2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        
    def test_divide_by_zero(self):
        self.assertEqual(self.calc.divide(5, 0), "Error: Division by zero is not allowed")
        
    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        
        
    def test_square_root(self):
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertEqual(self.calc.square_root(0), 0)
        self.assertEqual(self.calc.square_root(2), math.sqrt(2))
    
    def test_square_root_negative(self):
        self.assertEqual(self.calc.square_root(-10), "square root of negative numbers is undefined")
     
    def test_percentage(self):
        self.assertEqual(self.calc.percentage(10, 100), 10)
        self.assertEqual(self.calc.percentage(0, 50), 0)
        
    def test_memory_add(self):
        self.calc.memory_add(10)
        self.assertEqual(self.calc.memory_recall(), 10)
        self.calc.memory_add(7)
        self.assertEqual(self.calc.memory_recall(), 17)
        
    def test_memory_subtract(self):
        self.calc.memory_add(10)
        self.calc.memory_subtract(5)
        self.assertEqual(self.calc.memory_recall(), 5)
        self.calc.memory_subtract(2)
        self.assertEqual(self.calc.memory_recall(), 3)
        
        
    def test_memory_clear(self):
        self.calc.memory_add(20)
        self.calc.memory_clear()
        self.assertEqual(self.calc.memory_recall(), 0)
        
    def test_hstory_tracking(self):
        self.calc.add(2, 5)
        self.calc.subtract(10 , 5)
        self.calc.multiply(5, 2)
        
        self.assertEqual(len(self.calc.history), 3)
        self.assertIn("2 + 5 = 7", self.calc.history[0])
        self.assertIn("10 - 5 = 5", self.calc.history[1])
        self.assertIn("5 × 2 = 10", self.calc.history[2])
        
    
    def test_history_after_division_by_zero(self):
        self.calc.divide(5, 0)
        self.assertEqual(len(self.calc.history), 1)
        self.assertIn("5 ÷ 0 = Error: Division by zero is not allowed", self.calc.history[0])
        
    def test_clear_screen(self):
        try:
            self.calc.clear_screen()
            success = True
        except:
            success = False
        self.assertTrue(success)
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_history_empty(self, mock_stdout):
        self.calc.show_history()
        output = mock_stdout.getvalue()
        self.assertIn("history is empty", output)
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_history_with_items(self, mock_stdout):
        self.calc.add(2, 5)
        self.calc.multiply(2, 5)
        self.calc.show_history()
        output = mock_stdout.getvalue()
        self.assertIn("2 + 5 = 7", output)
        self.assertIn("2 × 5 = 10", output)
        
        
        
if __name__ == '__main__':
    unittest.main()