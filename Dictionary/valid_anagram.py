from collections import Counter

class Solution():
    # Time: O(nlogn) 
    # Space: O(n) 
    def isAnagram1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
            
        print(countS)
        print(countT)
            
        return countS == countT
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def isAnagram3(self, s:str, t: str) -> bool:
        # implement using Counter
        return Counter(s) == Counter(t)
        
    
    
# s = "racecar", t = "carrace"
soln = Solution()
s = "racecar"
t = "carrace"
# print(sorted(s))
# print(sorted(t))
# print(soln.isAnagram3(s, t))

res = [1, 2, 3, 4, 5]
reversed_res = res[3:0:-1]
print(reversed_res)