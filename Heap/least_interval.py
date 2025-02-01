
import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count = Counter(tasks) # count the occurrence of each task
        maxHeap = [-cnt for cnt in count.values()] # highest occurring task is processed first
        heapq.heapify(maxHeap)

        time = 0 # track total time
        q = [] # track remaining tasks to process [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # we just processed one task
                if cnt: # if there are more tasks
                    q.append([cnt, time + n]) # track idle time, the next time we can process this task

            # it now time to process another task
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.pop(0)[0])

        return time