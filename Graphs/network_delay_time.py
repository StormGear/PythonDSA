from collections import defaultdict
from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        minHeap = [(0,k)]
        visited = set()
        min_t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue

            visited.add(n1)
            min_t = max(min_t, w1)

            for n2,w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, n2))

        return min_t if len(visited) == n else -1

    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))

        dist = defaultdict(lambda: float('inf'))
        dist[k] = 0
        visited = set([k])

        print(graph.items())

        # for u, (v, w) in graph.items():
        #     if dist[u] != float('inf') and dist[u] + w < dist[v]:
        #         dist[v] = dist[u] + w

        # print(dist)

if __name__ == "__main__":
    soln = Solution()
    times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]]
    n = 4
    k = 1
    val = soln.networkDelayTime(times, n, k)
    print(val)