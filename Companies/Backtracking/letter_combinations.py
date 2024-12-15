
# Daily Coding Problem: Problem #81 [Easy]
# This problem was asked by Yelp.
def letter_combinations(digits):
    if not digits:
        return []
    
    # Mapping of digits to letters like a phone keypad
    digit_to_letters = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    
    result = []
    
    # Helper function to perform backtracking
    def backtrack(index, current_combination):
        if index == len(digits):
            # If the current combination is the same length as digits, we found a valid combination
            result.append(current_combination)
            return
        
        # Get the letters corresponding to the current digit
        current_digit = digits[index]
        possible_letters = digit_to_letters[current_digit]
        
        # Recursively try each letter for the current digit
        for letter in possible_letters:
            backtrack(index + 1, current_combination + letter)
    
    # Start the backtracking process from the first digit
    backtrack(0, "")
    
    return result

# Test case
digits = "23"
combinations = letter_combinations(digits)
print(combinations)
