# This problem was asked by Google.
# Daily Coding Problem: Problem #80 [Easy]
# time: O(n) and space: O(n)
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deepest_node(root: TreeNode):
    if not root:
        return None
    
    queue = deque([root])
    node = None
    
    while queue:
        node = queue.popleft()
        
        # Add left and right children to the queue if they exist
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    # The last node processed is the deepest node
    return node

# Example tree
#     a
#    / \
#   b   c
#  /
# d

root = TreeNode('a')
root.left = TreeNode('b')
root.right = TreeNode('c')
root.left.left = TreeNode('d')

result = deepest_node(root)
print(result.val)  # Output: d
