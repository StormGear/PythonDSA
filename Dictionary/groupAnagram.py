from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for w in strs:
            w_sorted = sorted(w)
            key = "".join(w_sorted)
            groups[key].append(w)

        return list(groups.values())

if __name__ == '__main__':
    soln = Solution()
    res = soln.groupAnagrams(["act","pots","tops","cat","stop","hat"])
    print(res)

# Output: [["act", "cat"],["stop", "pots", "tops"], ["hat"]]
