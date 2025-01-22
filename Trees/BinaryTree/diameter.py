class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    # time: O(n), n: number of nodes
    # space: O(n)
    # Using recursive dfs
    def diameter_of_binary_tree(self, root):
        diameter = 0

        # return the height
        def dfs(root):
            if not root:
                return 0
            
            left_depth =   dfs(root.left)
            right_depth = dfs(root.right)

            nonlocal diameter
            diameter = max(diameter, left_depth + right_depth)
            

            return 1 + max(left_depth, right_depth)
        
        dfs(root)
        return diameter

if __name__ == '__main__':
    soln = Solution()
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.left.left = TreeNode(4)
    tree1.right = TreeNode(3)
    print(soln.diameter_of_binary_tree(tree1)) # 3
    

        
    