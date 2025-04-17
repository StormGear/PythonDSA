def calculate_sqrt(number, tolerance=1e-10):
    if number < 0:
        return "Square root of a negative number is not real"
    if number == 0:
        return 0
    guess = number / 2.0
    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2.0
    return guess

# Example usage
print(calculate_sqrt(25))   # Output: ~5.0
print(calculate_sqrt(2))    # Output: ~1.4142
print(calculate_sqrt(-9))   # Output: Square root of a negative number is not real
