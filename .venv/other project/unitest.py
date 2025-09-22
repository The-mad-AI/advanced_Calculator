import unittest
class testmyFunction(unittest.TestCase):
    def test_case_1(self):
        result = my_function(2)
        self.assertEqual(result, 4)
        
if __name__ == "__main__":
    unittest.main()