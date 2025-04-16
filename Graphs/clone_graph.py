
# Definition for a Node.
from typing import  Optional
from collections import deque


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # Time Complexity: O(V+E), V:vertices/nodes and E:edges
    # Space Complexity: O(V) for the hashmap
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        oldToNew = {}

        def dfs(old_node):
            if not old_node:
                return None

            if old_node in oldToNew:
                return oldToNew[old_node]
            
            copy = Node(old_node.val)
            oldToNew[old_node] = copy
            for neighbor in old_node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
    
    def bfs(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        
        queue = deque([node])
        visited = set([node])
        
        while queue:
            actual_node = queue.popleft()
            print(actual_node.val, end=" ")

            for neighbor in actual_node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        print()
        

    
if __name__ == '__main__':
    soln = Solution()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors.append(node2)
    node1.neighbors.append(node3)
    node2.neighbors.append(node1)
    node2.neighbors.append(node4)
    node3.neighbors.append(node1)
    node3.neighbors.append(node4)
    node4.neighbors.append(node3)
    node4.neighbors.append(node2)
    # Cloning the graph
    clone = soln.cloneGraph(node1)
    # BFS traversal of the original graph
    soln.bfs(node1)
    # BFS traversal of the cloned graph
    soln.bfs(clone)
    
    
        