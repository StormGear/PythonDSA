class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def preOrder(root):
    #Write your code here
    res = []
    def _preOrder(root):
        if root:
            res.append(str(root.info))
        else:
            return
        _preOrder(root.left)
        _preOrder(root.right)
    _preOrder(root)
    print(" ".join(res))

def preOrder2(root):
    if not root:
        return []
    return [root.info] + preOrder2(root.left) + preOrder2(root.right)

def preOrder3(root):
    res = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            res.append(node.info)
            stack.append(node.right) # right child is pushed first since left child is processed first
            stack.append(node.left)
    return res


def inOrder(root):
    if not root:
        return []
    return inOrder(root.left) + [root.info] + inOrder(root.right)

def postOrder(root):
    if not root:
        return []
    return postOrder(root.left) + postOrder(root.right) + [root.info]

def preOrder(root):
    if not root:
        return []
    return [root.info] + preOrder(root.left) + preOrder(root.right)


if __name__=="__main__":
    bst = BinarySearchTree()
    bst.create(10)
    bst.create(5)
    bst.create(15)
    bst.create(2)
    bst.create(6)
    bst.create(12)
    bst.create(16)
    preOrder(bst.root)