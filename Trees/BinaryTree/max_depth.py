class TreeNode:
    def __init__(self, value=0):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    # time: O(n), n: number of nodes
    # space: O(n)
    # Using recursive dfs
    def max_depth1(self, root):
        if not root:
            return 0
        
        left_depth = self.max_depth1(root.left)
        right_depth = self.max_depth1(root.right)

        return 1 + max(left_depth, right_depth)
    
    # Using bfs
    def max_depth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = 0
        q = [root]
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level
    
    # Using iterative dfs
    def max_depth3(self, root: TreeNode) -> int:
        res = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                if node.left:
                    stack.append((node.left, depth+1))
                if node.right:
                    stack.append((node.right, depth+1))

        return res
    
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
    print(s.max_depth3(root))