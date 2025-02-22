

# Number factor problem
# Given a number ‘n’, implement a method to count how many possible ways to express ‘n’ as the sum of 1, 3, or 4.
# solution in simple words: Form base cases and recursively compute sum for n-1, n-3, n-4
def number_factor(n):
    if n < 0:
        return 0
    elif n in [0, 1, 2]:
        return 1
    elif n == 3:
        return 2
    else:
        sub1 = number_factor(n-1)
        sub2 = number_factor(n-3)
        sub3 = number_factor(n-4)
        return sub1 + sub2 + sub3
    

if __name__ == "__main__":
    print(number_factor(5)) # 6