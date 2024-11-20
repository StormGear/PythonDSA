import heapq
from collections import defaultdict
class Solution:
    # Time Complexity: O(ElogV)
    # Space Complexity: O(V + E)
    def shortestPath(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:
        adj_list = defaultdict(list)

        for u, v, w in edges:
            adj_list[u].append((v, w))

        shortest_path = {}
        min_heap = [(0, src)]
        while min_heap:
            w1, node = heapq.heappop(min_heap)
            if node in shortest_path:
                continue
            shortest_path[node] = w1
            for neighbor, weight in adj_list[node]:
                if neighbor not in shortest_path:
                    heapq.heappush(min_heap, (w1 + weight, neighbor))

        for i in range(n):
            if i not in shortest_path:
                shortest_path[i] = -1

        return shortest_path


if __name__ == "__main__":
    n = 5
    edges = [[0,1,10], [0,2,3], [2,1,4], [2,3,8], [2,4,2], [1,3,2], [3,4,5]]
    src = 0
    s = Solution()
    print(s.shortestPath(n, edges, src))