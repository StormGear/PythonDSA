class Solution:
    def is_perfect_square(self, i: int) -> bool:
        l = 1
        r = i

        while l <= r:
            m = l + ((r-l)//2)
            if  m * m == i:
                return True
            elif m * m < i:
                l = m + 1
            else:
                r = m - 1

        return False
    
if __name__=='__main__':
    soln = Solution()
    print(soln.is_perfect_square(4))
    print(soln.is_perfect_square(9))
    print(soln.is_perfect_square(16))
    print(soln.is_perfect_square(25))
    print(soln.is_perfect_square(36))
    print(soln.is_perfect_square(49))
    print(soln.is_perfect_square(64))
    print(soln.is_perfect_square(65))
    
