# DepthFirst First Search

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.adjacency_list = []
        self.visited = False

class DepthFirstSearch:
    # time: O(V+E), V:vertices/nodes and E:edges
    # space: O(logn)
    # it seems that this implementation starts with the right neighbor nodes first
    def dfs_iteration(self, start_node):
        # LIFO structure
        stack = [start_node]
        start_node.visited = True

        while stack:
            actual_node = stack.pop()
            actual_node.visited = True
            print(actual_node.data, end=" ")

            for node in actual_node.adjacency_list:
                # if the node has not been visited
                if not node.visited:
                    stack.append(node)
                    node.visited = True

    # it seems that this implementation starts with the left neighbor nodes first
    def dfs_recursion(self, start_node):
        start_node.visited = True
        print(start_node.data, end=" ")

        for node in start_node.adjacency_list:
            if not node.visited:
                self.dfs_recursion(node)



if __name__ == '__main__':
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    H = Node("H")

    A.adjacency_list.append(B)
    A.adjacency_list.append(F)
    A.adjacency_list.append(G)
    B.adjacency_list.append(C)
    B.adjacency_list.append(D)
    D.adjacency_list.append(E)
    G.adjacency_list.append(H)

    dfs = DepthFirstSearch()
    # dfs.dfs_recursion(A)
    dfs.dfs_iteration(A)