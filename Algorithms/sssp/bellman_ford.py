## Single Path Shortest Algorithm Problems
from collections import defaultdict
import heapq

class Graph:
    def __init__(self, nodes: int) -> None:
        self.nodes = nodes
        self.graph = []

    def add_edge(self, u, v, w) -> None:
        self.graph.append([u,v,w])

class Solution:
    def bellman_ford(self, n: int, edges: list[list[int]], src: int = 0) -> dict[int, int]:
        dist = [float('inf')] * n
        shortest = {}

        dist[src] = 0

        for _ in range(n-1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print('Graph contains negative cycles')

        for node, distance in enumerate(dist):
            shortest[node] = distance

        return shortest

    def bellman_ford2(self, graph: Graph, src: int = 0) -> dict[int, int]:
        dist = [float('inf')] * graph.nodes
        shortest = {}

        dist[src] = 0

        for _ in range(n-1):
            for u, v, w in graph.graph:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for u, v, w in graph.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print('Graph contains negative cycles')

        for node, distance in enumerate(dist):
            shortest[node] = distance

        return shortest


if __name__ == "__main__":
    n = 5
    edges = [[0,1,10], [0,2,3], [2,1,4], [2,3,8], [2,4,2], [1,3,2], [3,4,5]]
    graph = Graph(5)
    graph.add_edge(*[0,1,-10])
    graph.add_edge(*[0,2,3])
    graph.add_edge(*[2,1,4])
    graph.add_edge(*[2,3,8])
    graph.add_edge(*[2,4,2])
    graph.add_edge(*[1,3,2])
    graph.add_edge(*[3,4,5])
    src = 0
    s = Solution()
    print(s.bellman_ford(n, edges, src))
    print(s.bellman_ford2(graph, src))