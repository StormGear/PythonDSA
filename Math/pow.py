def power(x, n):
    result = 1
    negative = n < 0
    n = abs(n)
    
    for _ in range(n):
        result *= x

    if negative:
        return 1 / result
    return result

# Example usage
print(power(2, 3))   # Output: 8
print(power(5, -2))  # Output: 0.04
