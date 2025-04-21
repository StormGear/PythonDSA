class Solution:
    """
    Problems: [link](https://codesignal.com/blog/interview-prep/example-codesignal-questions/)
    """

    def array_prob(a):
        b = []
        for i in range(len(a)):
            first = a[i-1] if i > 0 else 0
            last = a[i+1] if i+1 < len(a) else 0
            res = first + a[i] + last
            b.append(res)
        return b
    
    def pattern_matching(pattern, source):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        lpattern = len(pattern)
        lsource = len(source)
        matches = 0

        for i in range(lsource - lpattern + 1):
            sub_str = source[i:i+lpattern]
            for j in range(lpattern):
                if pattern[j] == "0" and sub_str[j] in vowels:
                    if j == lpattern - 1:
                        matches += 1
                elif pattern[j] == "1" and sub_str[j] not in vowels:
                    if j == lpattern - 1:
                        matches += 1
                else:
                    break
  
        return matches

            


if __name__ == "__main__":
    a = [4, 0, 1, -2, 3]
    source = "amazing"
    pattern = "010"
    print(Solution.array_prob(a))
    print(Solution.pattern_matching(pattern, source))