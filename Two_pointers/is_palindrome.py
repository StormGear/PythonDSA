
# check if a string is a palindrome
# time complexity: O(n)
# space complexity: O(1)
def is_palindrome(s: str) -> bool:
    if not s:
        return False

    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalnum(): # to skip non-alphanumeric characters on the left
            left += 1
        elif not s[right].isalnum(): # to skip non-alphanumeric characters on the right
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True

s = "Was it a car or a cat I saw?"
print(is_palindrome(s))  # True