import unittest
from app.utils import sanitize_input

class TestUtils(unittest.TestCase):
    def test_sanitize_input(self):
        input_str = "test; rm -rf /"
        sanitized_input = sanitize_input(input_str)
        self.assertNotIn(';', sanitized_input)
        self.assertNotIn('&', sanitized_input)
        self.assertEqual(sanitized_input, "test rm -rf /")

if __name__ == '__main__':
    unittest.main()
