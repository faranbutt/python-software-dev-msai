import unittest
from aoc1 import compute_manhattan, process_input
import os

class ManhattanTest(unittest.TestCase):
    def setUp(self):
        self.lst1 = [3,4]
        self.lst2 = [4,5]

    def test_negative(self):
        expected_manhattan = 2
        actual_manhattan = compute_manhattan(self.lst1, self.lst2)
        self.assertEqual(expected_manhattan, actual_manhattan)

    def test_positive(self):
        expected_manhattan = 2
        actual_manhattan = compute_manhattan(self.lst2, self.lst1)
        self.assertEqual(expected_manhattan, actual_manhattan)

class ProcessInputTest(unittest.TestCase):

    def setUp(self):
        self.inputs = [
            "3   4\n4   3\n2   5\n1   3\n3   9\n3   3\n",
            "33   44\n44   33\n22   55\n11   33\n33   99\n33   33\n",
        ]
        self.expected_lsts = [
            ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]),
            ([33, 44, 22, 11, 33, 33], [44, 33, 55, 33, 99, 33])
        ]

    def test_both_single_multiple_digits(self):
        for i, (input, expected_lists) in enumerate(zip(self.inputs, self.expected_lsts)):
            with self.subTest(i = i):
                with open("input.txt", "w") as f:
                    f.write(input)

                actual_lists = process_input()

                self.assertEqual(expected_lists, actual_lists)

    def tearDown(self):
        os.remove("input.txt")

if __name__ == '__main__':
    unittest.main()
