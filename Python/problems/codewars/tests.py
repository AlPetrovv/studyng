import unittest
from solutions import narcissistic


class TestNarcissistic(unittest.TestCase):
    def test_narcissistic(self):
        self.assertEqual(narcissistic(153), True)
        self.assertEqual(narcissistic(370), True)
        self.assertEqual(narcissistic(371), False)
        self.assertEqual(narcissistic(407), True)
        self.assertEqual(narcissistic(1634), False)
        self.assertEqual(narcissistic(8208), True)
