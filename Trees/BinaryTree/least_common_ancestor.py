class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    # time: O(n)
    def least_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            if p.value > curr.value and q.value > curr.value:
                curr = curr.right
            elif p.value < curr.value and q.value < curr.value:
                curr = curr.left
            else:
                return curr
            

if __name__=='__main__':
    soln = Solution()
            # 10
           # / \
          # 6   11
        #  /
        # 5
    tree1 = TreeNode(10)
    tree1.left = TreeNode(6)
    tree1.left.left = TreeNode(5)
    tree1.right = TreeNode(11)
    print(soln.least_common_ancestor(tree1, TreeNode(6), TreeNode(11)).value)
        