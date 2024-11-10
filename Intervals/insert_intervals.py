class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def insert_intervals(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        if not intervals:
            return [new_interval]
        
        merged = []
        
        # left part of the merged intervals
        i = 0
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            merged.append(intervals[i])
            i += 1
        
        # middle part of the merged intervals, possibly overlapping with new_interval
        while i < len(intervals) and intervals[i][0] <= new_interval[1]:
            new_interval = [min(intervals[i][0], new_interval[0]), max(intervals[i][1], new_interval[1])]
            i += 1
        
        merged.append(new_interval)
        
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        
        return merged
    
if __name__ == '__main__':
    soln = Solution()

    test_cases = [
        ([], [5, 7], [[5, 7]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[3, 5], [7, 9]], [1, 2], [[1, 2], [3, 5], [7, 9]]),
        ([[1, 2], [3, 5]], [6, 7], [[1, 2], [3, 5], [6, 7]]),
        ([[1, 2], [3, 5], [6, 7]], [0, 8], [[0, 8]]),
        ([[1, 3], [6, 9], [12, 15]], [4, 13], [[1, 3], [4, 15]]),
        ([[1, 3], [6, 9]], [6, 9], [[1, 3], [6, 9]]),
        ([[1, 3], [6, 9]], [8, 10], [[1, 3], [6, 10]]),
        ([[1, 3], [6, 9]], [7, 10], [[1, 3], [6, 10]])
    ]
    
    for intervals, new_interval, expected in test_cases:
        result = soln.insert_intervals(intervals, new_interval)
        print(f"Intervals: {intervals}, New Interval: {new_interval}, Expected: {expected}, Result: {result}")
    