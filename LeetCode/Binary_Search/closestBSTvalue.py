# Closest Binary Search Tree value problem

# Definition for a binary tree node.
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self) -> str:
        return 'Definition for a Binary Tree Node'
        
class Solution:
    def closestValue(self, root: [TreeNode], target: float) -> int:
        ans, mi = root.val, inf
        while root:
            t = abs(root.val - target)
            if t < mi:
                mi = t
                ans = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return ans
    
# root = [4,2,5,1,3], target = 3.714286
root = TreeNode(val=4, left=2, right=5)
root.left = TreeNode(val=2, left=1, right=3)
root.left.left = TreeNode(val=1)
root.left.right = TreeNode(val=3)
root.right = TreeNode(5)

target = 3.714286

print(Solution().closestValue(root, target)) # result = 4

# root = [1], target = 4.428571
root = TreeNode(val=1)
target = 4.428571
print(Solution().closestValue(root, target)) # result = 1



