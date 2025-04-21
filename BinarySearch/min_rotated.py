# Problem minimum rotated sorted array
class Solution:
    """
    Problem: [link](https://neetcode.io/problems/find-minimum-in-rotated-sorted-array)
    """
    def min_rotated_brute(self, nums: list[int]) -> int:
        res = nums[0]

        for num in nums:
            res = min(res, num)

        return res
    
    def min_rotated_binary(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            # there is no pivot/break, it's infact increasing
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = l + ((r-l)//2)
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res
    
    def min_rotated_binary2(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            # let's find the pivot
            m = l + ((r-l)//2)
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 
        print('pivot:', l, 'value:', nums[l], 'r:', r, 'value:', nums[r], 'm:', m)
        return nums[l]
    
if __name__ == '__main__':
    soln = Solution()
    # print(soln.min_rotated_brute([3,4,5,6,1,2]))
    # print(soln.min_rotated_binary([3,4,5,6,1,2]))
    print(soln.min_rotated_binary2([3,4,5,6,1,2]))

