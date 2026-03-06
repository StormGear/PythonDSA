# Given an array of integers, find the maximum XOR of any two elements.

from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = {num & mask for num in nums}
            tentative_max_xor = max_xor | (1 << i)
            for p in prefixes:
                if (tentative_max_xor ^ p) in prefixes:
                    max_xor = tentative_max_xor
                    break
        return max_xor