class Solution:
    # Time complexity: O(nlogn)
    # Space complexity: O(1)
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        
        intervals.sort(key=lambda x: (x[0], -x[1]))

        
        result = 0
        end = 0
        
        for interval in intervals:
            # if current interval end time is greater than the previous interval end time
            # then the current interval is not covered by the previous interval
            if interval[1] > end:
                result += 1
                end = interval[1]
        
        return result
    
if __name__ == '__main__':
    soln = Solution()
    intervals = [[1,4],[3,6],[2,8], [2,5]]
    # intervals = [[1,4],[2,3]]
    # intervals = [[0,10],[5,12]]
    print(soln.removeCoveredIntervals(intervals))
    
    