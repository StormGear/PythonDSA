# This problem was asked by Amazon.

# Given n numbers, find the greatest common denominator between them.

# For example, given the numbers [42, 56, 14], return 14.

from math import gcd
from functools import reduce

def find_gcd_of_list1(numbers):
    return gcd(*numbers)

def find_gcd_of_list2(numbers):
    return reduce(euclidean_gcd_recursive, numbers )

def euclidean_gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return euclidean_gcd_recursive(b, a % b)

# Example usage:
numbers = [42, 56, 14]
result = find_gcd_of_list2(numbers)
print(result)  # Output: 14