def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime
    if n % 2 == 0:
        return False  # eliminate other even numbers
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(2))   # True
print(is_prime(17))  # True
print(is_prime(18))  # False
