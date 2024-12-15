# This problem was asked by Google.
# Daily Coding Problem: Problem #86 [Medium]
# Time complexity: O(n)
# Space complexity: O(1)
def min_removals_to_make_valid(s):
    open_count = 0  # Number of unmatched open parentheses '('
    remove_count = 0  # Number of parentheses to be removed

    # Traverse the string
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                # There's an unmatched open parenthesis to match with
                open_count -= 1
            else:
                # No matching open parenthesis, so this ')' is invalid
                remove_count += 1

    # Unmatched open parentheses are also invalid
    remove_count += open_count
    
    return remove_count

# Example usage:
print(min_removals_to_make_valid("()())()"))  # Output: 1
print(min_removals_to_make_valid(")("))       # Output: 2
