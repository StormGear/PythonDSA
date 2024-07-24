# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class GuessGame:
    @classmethod
    def guess(cls, guess: int, pick: int) -> int:
        pick = pick
        if guess == pick:
            return 0
        elif guess > pick:
            return -1
        else:
            return 1
        
        

class Solution:
    @classmethod
    def guessNumber(cls, n: int) -> int:
        low = 1
        high = n
		
        while low<=high:
		
            mid = (high+low)//2
            num = GuessGame.guess(mid, 6)
			
            if num == 0:
                return mid
            elif num == -1:
                high = mid-1
            else:
                low = mid+1

        return 'out of range'
            
print(Solution.guessNumber(10))
                
