# In DFS there are 3 different ways to traverse preorder, inorder and postorder. Each traversal can be solved in both Iterative and Recursive methods. It is very important to know both methods.
import collections

class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BinaryTree:
    def __init__(self, root: BinaryTreeNode):
        self.root = root


    # dfs recursive approach
    def preorder(self, root: BinaryTreeNode):
        if not root:
            return []
    
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)
    
    def inorder(self, root: BinaryTreeNode):
        if not root:
            return []
        
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    

    def postorder(self, root: BinaryTreeNode):
        if not root:
            return []
    
        return self.postorder(root.left) + self.postorder(root.right) + [root.val]
    
    # dfs iterative approach
    def preorder_iterative(self, root: BinaryTreeNode):
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push right first so left is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result
    
    def inorder_iterative(self, root: BinaryTreeNode):
        stack = []
        result = []
        current = root

        while stack or current:
            # move as far left as possible
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
    

    def postorder_iterative(self, root:BinaryTreeNode):
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push left first so right is processed first
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]  # Reverse to get left → right → root
    
    def bfs_iterative(self, root):
        if not root:
            return []

        queue = collections.deque([root])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result
    

if __name__== "__main__":
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    print(root.left)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right = BinaryTreeNode(3)
    root.right.right = BinaryTreeNode(7)
    root.right.left = BinaryTreeNode(6)
    tree = BinaryTree(root)
    print(tree.bfs_iterative(root))
    print(tree.inorder_iterative(root))
    print(tree.preorder_iterative(root))

