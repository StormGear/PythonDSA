from typing import List

class Solution:
    def smaller_elements(self, arr: List[int])-> List[int]:
        # Brute-force O(n^2)
        res = [0 for _ in range(len(arr))]

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] < arr[i]:
                    res[i] += 1

        return res



if __name__ == "__main__":
    soln = Solution()
    arr = [5, 4, 3, 2, 1]
    arr2 = [1, 2, 0]
    print(soln.smaller_elements(arr))
    print(soln.smaller_elements(arr2))
