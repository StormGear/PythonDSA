class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def search(node: Node, target: int) -> Node | None:
    if node is None:
        return None 
    elif node.data == target:
        return node
    elif target < node.data:
        return search(node.left, target) # search left subtree
    else:
        return search(node.right, target) # search right subtree
    
def insert(node: Node, data: int):
    if node is None:
        return Node(data)
    else:
        if data < node.data:
            node.left = insert(node.left, data)
        elif data > node.data:
            node.right = insert(node.right, data)
    return node # return the same node if data == current_node.data

def minValueNode(node: Node):
    # move as far left as possible to find the minimum number
    current = node
    while current.left is not None:
        current = current.left
    return current

def preOrder(root):
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