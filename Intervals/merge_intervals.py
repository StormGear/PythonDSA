class Solution:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) <= 1:
            return intervals
        
        result = []
        intervals.sort(key=lambda x: x[0])
        print(intervals)


        include : list[int] = intervals[0]
        i = 1

        while (i < len(intervals)):
            if (include[1] < intervals[i][0]):
                result.append(include)
                include = intervals[i]
            else:
                include[1] = max(include[1], intervals[i][1])
            i += 1

        result.append(include)
        return result

if __name__ == '__main__':
    soln = Solution()
    intervals = [[1,3],[2,6], [15,18], [8,10]]
    print(soln.merge(intervals))