from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for w in strs:
            w_sorted = sorted(w)
            key = "".join(w_sorted)
            groups[key].append(w)

        return groups.values()

if __name__ == '__main__':
    soln = Solution()
    res = soln.groupAnagrams(["act","pots","tops","cat","stop","hat"])
    print(list(res))

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]