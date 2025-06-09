# Number of one bits (hamming weight)

def hamming_weight(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

def hamming_weight2(n):
    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res

print(hamming_weight(11))
print(hamming_weight2(11))
