from collections import deque


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


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    # Write your code here
    res = []
    map = {}

    def _topView(root):
        if not root:
            return res

        q = deque([(root, 0)])

        while q:
            node, line = q.popleft()

            # if vertical position not in map already
            if line not in map:
                map[line] = node.info

            if node.left:
                q.append((node.left, line-1))

            if node.right:
                q.append((node.right, line+1))

        for value in sorted(map.items()):
            res.append(str(value[1]))

        print(" ".join(res))
    _topView(root)
