# We will write our test cases here

import unittest
import os
import sys

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Dictionary.two_integer_sum import Solution
from Dynamic_Programming import power_of_cards


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = Solution().twoSum([3,4,5,6], 7)
        self.assertTrue(len(output) == 2)
        self.assertTrue(0 in output)
        self.assertTrue(1 in output)

    def test_case_2(self):
        res1 = power_of_cards.max_cards_dp([5,2,-3,-1,5])
        res2 = power_of_cards.max_cards_dp([-1,0,-1,2,0])
        res3 = power_of_cards.max_cards_dp([])
        self.assertTrue(res3 == 0)
        self.assertTrue(res1 == 5)
        self.assertTrue(res2 == 3)

if __name__ == "__main__":
    unittest.main()