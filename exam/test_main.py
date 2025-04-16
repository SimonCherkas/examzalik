import unittest
from main import contains_a

class TestContainsA(unittest.TestCase):
    def test_contains_a(self):
        self.assertTrue(contains_a("apple"))

    def test_no_a(self):
        self.assertFalse(contains_a("hello"))

if __name__ == '__main__':
    unittest.main()
