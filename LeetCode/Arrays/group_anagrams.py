from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for w in strs:
            w_sorted = sorted(w)
            key = "".join(w_sorted)
            groups[key].append(w)
        return list(groups.values())
    

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
result = solution.groupAnagrams(strs)
print(result)  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]