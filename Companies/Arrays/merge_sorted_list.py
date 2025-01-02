class Solution:
    def merge_sorted_list(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        if i < len(nums1):
            res.extend(nums1[i:])
        else:
            res.extend(nums2[j:])

        return res
    
if __name__ == '__main__':
    soln = Solution()
    print(soln.merge_sorted_list([1,2,4], [1,3,4]))