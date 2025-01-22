class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root):
        if root is None:
            return None
        root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
        return root
    
    def print_tree(self, root):
        if root is None:
            return
        self.print_tree(root.left)
        print(root.value, end=' ')
        self.print_tree(root.right)

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    s = Solution()
    s.print_tree(root)
    print()
    s.print_tree(s.invert_tree(root))