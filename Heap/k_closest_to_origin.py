import heapq

# negate distance values effectively making larger distances smaller, pop larger(more negative) until we have K elements
# left in the max heap
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        self.res = []
        heapq.heapify(self.res)

        for x, y in points:
            d = (x)**2 + (y)**2
            heapq.heappush(self.res, [-d, x, y])    

        while len(self.res) > k:
            heapq.heappop(self.res)

        return [[point[0], point[1]] for point in self.res]
       

    
    def kClosest2(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]