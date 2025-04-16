# Breadth First Search

from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.adjacency_list = []
        self.visited = False

class BreadthFirstSearch:
    # O(V+E), V:vertices/nodes and E:edges
    # space: O(n)
    def bfs(self, startNode):
        queue = deque([startNode])
        startNode.visited = True

        while queue:
            actual_node = queue.popleft()
            # process this node
            print(actual_node.data, end=" ")

            for node in actual_node.adjacency_list:
                if not node.visited:
                    queue.append(node)
                    node.visited = True

if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # node1.adjacency_list.append(node2)
    # node1.adjacency_list.append(node3)
    # node2.adjacency_list.append(node4)
    # node4.adjacency_list.append(node5)

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)

    bfs = BreadthFirstSearch()
    bfs.bfs(node1)
                    