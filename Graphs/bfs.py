# Breadth First Search

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.adjacency_list = []
        self.visited = False

class BreadthFirstSearch:
    # O(V+E), V:vertices/nodes and E:edges
    # space: O(n)
    def bfs(self, startNode):
        queue = [startNode]
        startNode.visited = True

        while queue:
            actualNode = queue.pop(0)
            print(actualNode.data, end=" ")

            for n in actualNode.adjacency_list:
                if not n.visited:
                    queue.append(n)
                    n.visited = True

if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node4)
    node4.adjacency_list.append(node5)

    bfs = BreadthFirstSearch()
    bfs.bfs(node1)
                    