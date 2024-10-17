def select_value(x, y, b):
    return (x * b) | (y * (1 - b))

# Example usage:
x = 5  # example value for x
y = 10 # example value for y
b = 0  # change between 0 and 1 to test

print(select_value(x, y, b))  # This will return x when b=1 and y when b=0
