class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(node):
    if not node:
        return -1
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1

def depth(node, root):
    if root is None:
        return -1
    if root == node:
        return 0
    left_depth = depth(node, root.left)
    if left_depth != -1:
        return left_depth + 1
    right_depth = depth(node, root.right)
    if right_depth != -1:
        return right_depth + 1
    return -1

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(f"Height of the tree: {height(root)}")  # Output: 2
print(f"Depth of node 4: {depth(root.left.left, root)}")  # Output: 2