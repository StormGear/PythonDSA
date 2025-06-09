# Reverse a 32-bit number
def reversebits(n):
    """
    Reverses the digits of a 32-bit signed integer.

    Args:
        x (int): The input integer to be reversed.

    Returns:
        int: The reversed integer if it falls within the range of a 32-bit signed integer.
             Otherwise, returns 0.
    """
    res = 0
    for i in range(32):
        bit = (n >> i) & 1 # Get the i-th bit
        res = res | (bit << (31 - i)) # Move bit to its reversed position
    return res 
    


# Original number in binary
n = 11
print(f"Original: {n} in binary is {bin(n)}")

# Reversed number
reversed_n = reversebits(n)
print(f"Reversed: {reversed_n} in binary is {bin(reversed_n)}")