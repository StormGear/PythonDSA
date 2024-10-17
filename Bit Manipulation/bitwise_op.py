# bitwise_op.py

def demonstrate_bitwise_operators(a, b):
    print(f"Operands: a = {a}, b = {b}")
    print(f"a & b  (AND): {a & b}")
    print(f"a | b  (OR): {a | b}")
    print(f"a ^ b  (XOR): {a ^ b}")
    print(f"~a     (NOT): {~a}")
    print(f"a << 1 (LEFT SHIFT): {a << 1}")
    print(f"a >> 1 (RIGHT SHIFT): {a >> 1}")

if __name__ == "__main__":
    a = 60  # 60 = 0011 1100
    b = 13  # 13 = 0000 1101
    demonstrate_bitwise_operators(a, b)