
# Given a string, find the longest palindromic subsequence (LPS) in it.
# A palindromic subsequence is a sequence that reads the same forwards and backwards.
def findLPS(s, start_index, end_index):
    if start_index > end_index:
        return 0
    elif start_index == end_index:
        return 1
    elif s[start_index] == s[end_index]:
        return 2 + findLPS(s, start_index+1, end_index-1)
    else:
        option1 = findLPS(s, start_index+1, end_index)
        option2 = findLPS(s, start_index, end_index-1)
        return max(option1, option2)
    
if __name__=='__main__':
    s = 'elephant'
    s = 'elrmenmet'
    print(findLPS(s, 0, len(s)-1))
    print(''.join(list))
    