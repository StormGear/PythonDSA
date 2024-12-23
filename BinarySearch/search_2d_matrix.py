class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        for row in range(len(matrix)):
            curr = matrix[row]
            l, r = 0, len(matrix[row]) - 1

            while l <= r:
                m = l + ((r-l)//2)
                if curr[m] < target:
                    l = m + 1
                elif curr[m] > target:
                    r = m - 1
                else:
                    return True

        return False
    
if __name__ == '__main__':
    soln = Solution()
    print(soln.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # True