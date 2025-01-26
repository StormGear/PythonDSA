class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    # is t a subtree of s
    def is_subtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t: return True
        if not s: return False

        if self.is_sametree(s, t):
            return True
        
        return (self.is_subtree(s.left, t) or self.is_sametree(s.right, t))

    def is_sametree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p and q and p.value == q.value:
            return True
        
        return (self.is_sametree(p.left, q.left) and self.is_sametree(p.right, q.right))
    
if __name__ == '__main__':
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.left.left = TreeNode(4)
    tree1.right = TreeNode(3)
    sub1 = TreeNode(2)
    sub1.left = TreeNode(4)
    sub1.right = TreeNode(5)
    soln = Solution()
    print(soln.is_subtree(tree1, sub1))
    


        
        