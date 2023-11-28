import unittest
from alpha import Alpha
import bravo

class MyTestCase(unittest.TestCase):
    def test_bravo(self):
        bravo

    def test_alpha(self):
        my_alpha = Alpha()
        self.assertEqual(my_alpha.greet(), 'Hello World!')

    def test_default(self):
        firstValue = "a"
        secondValue = "a"
        message = "First value and second value are not equal !"
        self.assertEqual(firstValue, secondValue, message)

if __name__ == '__main__':
    unittest.main()