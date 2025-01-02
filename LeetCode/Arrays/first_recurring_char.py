# Time complexity: O(n^2). This problem was asked by Google.
def first_recurring_char1(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return string[i]
    return None

# Time complexity: O(n^2).
def first_nonrecurring1(string):
    for i in range(len(string)):
        if string[i] not in string[i+1:]:
            return string[i]
    return None

# Time complexity: O(n)
def first_nonrecurring2(string):
    seen = set()
    for char in string:
        if char in seen:
            seen.remove(char)
        else:
            seen.add(char)
    return next(iter(seen), None)
    


# Time complexity: O(n)
def first_recurring_char2(string):
    seen = set()
    for char in string:
        if char in seen:
            return char
        seen.add(char)
    return None

string1 = "ABCAB"
string2 = "BCABA"
# print(first_recurring_char1(string1))
# print(first_recurring_char1(string2))

# print(first_recurring_char2(string1))

# print(first_recurring_char2(string2))

# print(first_nonrecurring1(string1))
# print(first_nonrecurring1(string2))

# print(first_nonrecurring2(string1))
print(first_nonrecurring2(string2))
print(first_recurring_char2("DBCABA"))
