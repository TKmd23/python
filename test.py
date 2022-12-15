# import unittest
# from less_7_tests import *
#
#
# class Tester(unittest.TestCase):
#
#     def test_args(self):
#         self.assertEqual(adder(2, 2), 5)
#
#
# if __name__ == "__main__":
#     unittest.main()
# --------------------------------------------
import unittest
from less_7_tests import *


class Tester(unittest.TestCase):

    def test_args(self):
        self.assertEqual(adder(a=10, b=11), 21)

    def test_mix(self):
        self.assertEqual(adder(1, a=2), 4)

    def test_diff(self):
        x = 10
        y = 0
        self.assertEqual(adder(0, -5, y, a=x), 5)

    def test_wrongdata(self):
        self.assertEqual(adder("5", "abd", 10), 15)


if __name__ == "__main__":
    unittest.main()
