class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new node with the given key
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    # Helper method to recursively insert a node
    def _insert(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(current_node.left, data)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(current_node.right, data)

    # Search for a node with a given data
    def search(self, data):
        return self._search(self.root, data)

    # Helper method to recursively search for a data
    def _search(self, current_node, data):
        if current_node is None or current_node.data == data:
            return current_node

        if data < current_node.data:
            return self._search(current_node.left, data)
        return self._search(current_node.right, data)

    # In-order traversal (left, root, right)
    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, current_node, traversal):
        if current_node:
            self._inorder_traversal(current_node.left, traversal)
            traversal.append(current_node.data)
            self._inorder_traversal(current_node.right, traversal)
        return traversal

    # Pre-order traversal (root, left, right)
    def preorder_traversal(self):
        return self._preorder_traversal(self.root, [])

    def _preorder_traversal(self, current_node, traversal):
        if current_node:
            traversal.append(current_node.data)
            self._preorder_traversal(current_node.left, traversal)
            self._preorder_traversal(current_node.right, traversal)
        return traversal

    # Post-order traversal (left, right, root)
    def postorder_traversal(self):
        return self._postorder_traversal(self.root, [])

    def _postorder_traversal(self, current_node, traversal):
        if current_node:
            self._postorder_traversal(current_node.left, traversal)
            self._postorder_traversal(current_node.right, traversal)
            traversal.append(current_node.data)
        return traversal

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(25)
    bst.insert(21)
    bst.insert(30)

    print("In-order Traversal:", bst.inorder_traversal())
    print("Pre-order Traversal:", bst.preorder_traversal())
    print("Post-order Traversal:", bst.postorder_traversal())

    search_key = 30
    result = bst.search(search_key)
    if result:
        print(f"Node with key {search_key} found!")
    else:
        print(f"Node with key {search_key} not found.")
