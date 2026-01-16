from collections import defaultdict
import heapq

class Djikstra:
    def __init__(self, edges:list[list[int]], n: int, src: int) -> dict[int, int]:
        self.edges = edges # edges(u,v,w)
        self.n = n # number of vertices
        self.src = src # starting node to every other node

    def shortestPath(self):
        graph = defaultdict(list)

        for u,v, w in self.edges:
            graph[u].append((v, w))

        res = {}
        minHeap = [(0, self.src)] # (shortest_dist, node)
        while minHeap:
            dist, u = heapq.heappop(minHeap)
            if u in res: # if u has been visited previously
                continue
            
            res[u] = dist

            for v, w in graph[u]:
                if v not in res:
                    heapq.heappush(minHeap, (dist+w, v))


        for i in range(self.n):
            if i not in res:
                res[i] = -1

        return res
    
if __name__=="__main__":
    edges = [
        [0,1,4],
        [0,2,2],
        [1,2,3],
        [1,4,3],
        [1,3,2],
        [2,1,1],
        [2,3,4],
        [2,3,4],
        [2,4,5]
    ]
    algo = Djikstra(edges, 5, 0)
    print(algo.shortestPath())