class Solution:
    def min_ballons(self, points: list[list[int]]) -> int:
        if not points or not points[0]:
            return 0
        
        points.sort(key=lambda x: x[1])
        
        count = 1
        end = points[0][1]
        
        for i in range(1, len(points)):
            if points[i][0] > end:
                count += 1
                end = points[i][1]
        
        return count
    
if __name__ == '__main__':
    # Test cases from LeetCode
    soln = Solution()
    test_cases = [
        ([[]], 0),
        ([[1,8], [2,4], [6,7]], 2),
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]], 3),
        ([[1, 2], [1, 2], [1, 2], [1, 2]], 1),
        ([[2, 3], [2, 3], [2, 3], [2, 3]], 1),
        ([[1, 2], [2, 3]], 1),
        ([[2, 3], [1, 2]], 1),
        ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], 3),
        ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]], 3),
        ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]], 5)
    ]

    for points, expected in test_cases:
        result = soln.min_ballons(points)
        print(f"Points: {points}, Expected: {expected}, Result: {result}")