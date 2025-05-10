class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.sum_squares(n)

            if n == 1:
                return True

        return False

    def sum_squares(self, n: int) -> int:
        output = 0
        for i in str(n):
            output += int(i) ** 2

        return output


    def sum_of_squares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit 
            n = n // 10
        return output
    

if __name__ == "__main__":
    soln = Solution()
    print(soln.isHappy(19))
    print(soln.isHappy(100))
    print(soln.isHappy(2))