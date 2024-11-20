

class Solution:
    # Time complexity: O(nlogn)
    # Space complexity: O(1)
    def remove_overlap_intervals(self,intervals: list[int]) -> int:
        if len(intervals) <= 1:
            return 0
        
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        count = 0 # number of intervals to remove

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]

        return count
    
if __name__ == '__main__':
    soln = Solution()
    test_cases = [
        ([[1, 2], [3, 4], [5, 6]], 0),
        ([[1,8], [2,4], [6,7]], 2),
        ([[1, 4], [2, 5], [3, 6]], 2),
        ([[1, 3], [2, 4], [5, 7], [6, 8]], 2),
        ([[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]], 0),
        ([[1, 2]], 0),
        ([], 0),
        ([[1, 3], [3, 5], [5, 7], [2, 6]], 1),
        ([[1, 100], [101, 200], [201, 300], [50, 150], [150, 250]], 2),
        ([[1, 3], [2, 3], [3, 4], [4, 5]], 1),
        ([[1, 3], [1, 4], [1, 5], [1, 6]], 3)
    ]
    
    for intervals, expected in test_cases:
        result = soln.remove_overlap_intervals(intervals)
        print(f"Intervals: {intervals}, Expected: {expected}, Result: {result}")