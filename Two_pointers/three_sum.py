class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        nums.sort()
    
        # Time Complexity: O(n^3) where n is the number of elements in the list
        # Space Complexity: O(m) where m is the number of unique triplets
        # Brute force approach
        for i in range(len(nums)-1):
            j = i + 1
            for j in range(i+1, len(nums)):
                k = j + 1
                while k < len(nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        print('i:', i, 'j:', j, 'k:', k)
                        res.add((nums[i], nums[j], nums[k]))
                    k += 1

        return [list(triplet) for triplet in res]
    
    # Time Complexity: O(n^2) where n is the number of elements in the list
    # Space Complexity: O(1) or O(n) depending on the sorting algorithm used
    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
 

        for index, ele in enumerate(nums):
           
            # If the current element is positive, any triplet including it will have a positive sum
            if ele > 0:
                break
            
            # avoid duplicates for the first element in the three sum
            if index > 0 and ele == nums[index - 1]:
                continue
       

            l, r = index + 1, len(nums) - 1
            while l < r:
                threeSum = ele + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([ele, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # avoid duplicates
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1  
        return res
    
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum2(nums))