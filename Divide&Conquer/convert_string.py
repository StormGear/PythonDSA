# Convert s2 to s1 using insert, delete or replace with minimum  operations (i.e trying to make s1 the same as s2, making manipulations on s1)

def convert_string(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2 # delete all remaining characters from s2
    if index2 == len(s2):
        return len(s1) - index1 # insert all remaining characters from s1
    if s1[index1] == s2[index2]:
        return convert_string(s1, s2, index1 + 1, index2 + 1) # skip current characters
    else:
        insert = 1 + convert_string(s1, s2, index1+1, index2 ) # insert character from s1
        delete = 1 + convert_string(s1, s2, index1, index2+1) # delete character from s2
        replace = 1 + convert_string(s1, s2, index1 + 1, index2 + 1) # replace character from s1 with character from s2
        return min(insert, delete, replace)
    

if __name__ == "__main__":
    # print(convert_string("table", "tbrles", 0, 0)) # 3
    print(convert_string("table", "tubrle", 0, 0)) # 2