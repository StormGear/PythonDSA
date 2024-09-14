# sentence = "The quick brown fox jumps over the lazy dog"
# print(sentence.split())

# numbers = input('Enter some numbers').split()
# print(numbers)

for i in range(0, 3):
    print('Hello World')

n = int(input('Enter the number of elements: '))
numbers = input('Enter the numbers: ').split()

for i in range(0, n):
    numbers[i] = int(numbers[i])

print(numbers)