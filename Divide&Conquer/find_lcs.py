# Longest Common Subsequence
# Given two strings, find the longest common subsequence (LCS).

def findLCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    elif s1[index1] == s2[index2]:
        return 1 + findLCS(s1, s2, index1+1, index2+1)
    else:
        option1 = findLCS(s1, s2, index1+1, index2)
        option2 = findLCS(s1, s2, index1, index2+1)
        return max(option1, option2)

if __name__=='__main__':
    print(findLCS('elephant', 'eretpat', 0, 0))