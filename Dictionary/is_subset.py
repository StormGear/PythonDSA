# Function to check if a list is a subset of another list
def is_subset(list1, list2):
    larger_list = list1 if len(list1) > len(list2) else list2
    smaller_list = list1 if len(list1) < len(list2) else list2

    for item in smaller_list:
        if item not in larger_list:
            return False

    return True

# Using a hash table or set
def is_subset2(list1, list2):
    larger_list = list1 if len(list1) > len(list2) else list2
    smaller_list = list1 if len(list1) < len(list2) else list2

    seen = set()
    for item in larger_list:
        seen.add(item)

    for item in smaller_list:
        if item not in seen:
            return False

    return True

# Using a dictionary
def is_subset3(list1, list2):
    larger_list = list1 if len(list1) > len(list2) else list2
    smaller_list = list1 if len(list1) < len(list2) else list2

    hashTable = {}
    for item in larger_list:
        hashTable[item] = True

    for item in smaller_list:
        if item not in hashTable:
            return False

    print(hashTable)

    return True


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3,]
# print(is_subset(list1, list2))
print(is_subset3(list1, list2))

