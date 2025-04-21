from math import ceil

class Solution:
    """
    Problem: [link](https://neetcode.io/problems/eating-bananas)
    """
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        high = max(piles)
        res = 0

        for k in range(1, high+1):
            time = 0
            for i in piles:
                if time > h:
                    break
                time_taken = ceil(i/k)
                time += time_taken
            if time <= h:
                res = k
                break

        return res
    

    def minEatingSpeed2(self, piles: list[int], h: int) -> int:
        high = max(piles)
        res = high

        k = list(range(1,high+1))

        l, r = 0, len(k)-1
        while l <= r:
            m = l + ((r-l)//2)
            # calculate the total time to eat all piles with rate k[m]
            time = 0
            for i in piles:
                if time > h:
                    break
                time_taken = ceil(i/k[m])
                time += time_taken

            # move to the right or left of m depending on the total time 
            if time > h:
                l = m + 1
            else:
                res = min(res, k[m])
                r = m - 1
            
        return res
    
    def minEatingSpeed3(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = l + ((r-l)//2)
            hours = 0
            for p in piles:
                hours += ceil(p/k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res
    
    

if __name__ == '__main__':
    soln = Solution()
    print(soln.minEatingSpeed3([3,6,7,11], 8))  # 4