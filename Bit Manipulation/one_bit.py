# Number of one bit

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n % 2
            n = n >> 1

        return res
    

    def hamming_weight(self, n: int) -> int:
        res = 0
        count = 0
        while n:
            count += 1
            n &= n - 1
            res += 1
        print(f'count: {count}')
        return res
    

if __name__ == "__main__":
    soln = Solution()
    print(soln.hammingWeight(44))