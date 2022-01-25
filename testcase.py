#!/usr/bin/env python3
import unittest
from app import CurryHandler


class TestCases(unittest.TestCase):
    def test1(self):
        with open("./test/test_input.txt", "r") as f:
            orders = f.readlines()
        with open("./test/test_output.txt", "r") as g:
            check = g.readlines()
        check = check.pop(0)
        ch = CurryHandler(orders)
        output = ch.select_curry()
        self.assertEqual(output, check)


if __name__ == '__main__':
    unittest.main()
# python -m unittest testcase.py