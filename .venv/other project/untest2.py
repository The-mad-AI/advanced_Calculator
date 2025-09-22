import unittest

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("sen bayad add sahih bashad")
    if age < 0 or age > 120:
        raise ValueError("sen gheir mojaz ast")
    return True


class TestValidataeAge(unittest.TestCase):
    def test_valid_age(self):
        self.assertTrue(validate_age(30))
        
    def test_negative_age(self):
        with self.assertRaises(ValueError):
            validate_age(-5)
            
    def test_too_high_age(self):
        with self.assertRaises(ValueError):
            validate_age(150)
            
    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            validate_age("thirty")
            
if __name__ == "__main__":
    unittest.main()