import unittest
from alpha import Alpha
import charlie

class MyTestCase(unittest.TestCase):
    def test_alpha(self):
        my_alpha = Alpha()
        error_message = "I don't say: Hello World!"
        self.assertEqual(my_alpha.greet(), 'Hello World!', error_message)

    def test_default(self):
        firstValue = "a"
        secondValue = "a"
        error_message = "First value and second value are not equal !"
        self.assertEqual(first_value, second_value, error_message)

    def test_charlie(self):
        # See charlie for test
        # to output information to the console
        charlie.test_add_1_to_function()

if __name__ == '__main__':
    unittest.main()