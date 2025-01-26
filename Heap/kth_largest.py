import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        self.res = []
        heapq.heapify(self.res)

        for num in nums:
            heapq.heappush(self.res, num)
            if len(self.res) > k:
                heapq.heappop(self.res)

        return self.res[0]