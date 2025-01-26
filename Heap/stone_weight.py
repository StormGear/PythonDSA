import heapq

# Use a minHeap to simulate a maxHeap by making negating non-negative integers
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        self.maxHeap = []
        heapq.heapify(self.maxHeap)

        for i in stones:
            heapq.heappush(self.maxHeap,-i)

        while len(self.maxHeap) > 1:
            y = heapq.heappop(self.maxHeap)
            x = heapq.heappop(self.maxHeap)

            if y < x:
                heapq.heappush(self.maxHeap, (y - x))

        return -(self.maxHeap[0]) if len(self.maxHeap) == 1 else 0