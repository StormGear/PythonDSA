class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        
        if not p or not q or p.value != q.value:
            return False
        
        return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)