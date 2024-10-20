
# maxiumum number of vowels in a string of size k problem
# s: string
# k: window size

# time: O(n)
def max_vowel(s: str, k: int) -> int:
    if (len(s)) < k:
        return 0
    
    def is_vowel(c: str) -> bool:
        import re
        vowel_match = re.compile(r'[aeiou]', re.IGNORECASE)
        if vowel_match.match(c):
            return True
        return False
    
    totalvowel = 0
    maxvowel = 0
    for i in s[:k]:
        if is_vowel(i):
            totalvowel += 1
    maxvowel = totalvowel

    for i in range(len(s)-k):
        totalvowel = 0
        for j in s[i+1:i+1+k]:
            if is_vowel(j):
                totalvowel += 1        
        maxvowel = max(maxvowel, totalvowel)

    return maxvowel


if __name__ == '__main__':
    s = "acacbefaobeacfe"
    k = 5
    print(f'Maximum number of vowels in window of size {k} is ' + str(max_vowel(s, k)))

