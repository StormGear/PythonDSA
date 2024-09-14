
def add(a, b) -> float:
    try:
        a = float(a)
        b = float(b)
        return a + b
    except:
        return None


a: str = input('Enter the value of a: ')
b: str = input('Enter the value of b: ')
result: float = add(a, b)
if (type(result) == float):
    print(f'The sum of {a} and {b} is {result}')
else:
    print('Invalid input')
    



