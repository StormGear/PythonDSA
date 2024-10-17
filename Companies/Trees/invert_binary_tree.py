
# This problem was asked by Google.
# Daily Coding Problem: Problem #83 [Medium]
# 
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invert_tree(root):
    if root is None:
        return None
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    
    # Recursively invert the left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root

# Helper function to print the tree (in order traversal)
def print_tree(node, level=0, label='root'):
    if node is not None:
        print(' ' * (level*2) + label + ':', node.value)
        print_tree(node.left, level + 1, 'L')
        print_tree(node.right, level + 1, 'R')

# Example tree:
root = TreeNode('a')
root.left = TreeNode('b')
root.right = TreeNode('c')
root.left.left = TreeNode('d')
root.left.right = TreeNode('e')
root.right.left = TreeNode('f')

print("Original tree:")
print_tree(root)

# Invert the binary tree
invert_tree(root)

print("\nInverted tree:")
print_tree(root)
