from collections import defaultdict, deque
from typing import List
import heapq
from disjoint_set import DisjointSet


class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build the edges
        edges = []
        n = len(points)
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append((dist,i,j)) # sort by weight, if tie, i, if tie j

        edges.sort()
        dsu = DisjointSet.from_iterable(list(range(n+1)))
        res = 0
        for dist, i, j in edges:
            if dsu.union(i, j):
                res += dist

        return res
            

if __name__=="__main__":
    points = [[0,0],[2,2],[3,3],[2,4],[4,2]]
    print(Solution().minCostConnectPoints(points))