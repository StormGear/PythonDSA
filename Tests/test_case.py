# We will write our test cases here

import unittest
import os
import sys

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Dictionary.two_integer_sum import Solution


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = Solution().twoSum([3,4,5,6], 7)
        self.assertTrue(len(output) == 2)
        self.assertTrue(0 in output)
        self.assertTrue(1 in output)

if __name__ == "__main__":
    unittest.main()