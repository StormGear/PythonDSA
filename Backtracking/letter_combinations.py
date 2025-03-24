class Solution:
    def letter_combinations(self, digits: str) -> list[str]:
        res = []
          

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, curr_str):
            if i == len(digits):
                res.append(curr_str)
                return

            for char in phone[digits[i]]:
                backtrack(i + 1, curr_str + char)

        if digits:
            backtrack(0, '')
        return res
        
                