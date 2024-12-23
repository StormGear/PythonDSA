def jaden_casing(string: str):
    str_list = string.split(" ")
    print(str_list)

    for i in range(len(str_list)):
        str_list[i] = str_list[i].capitalize()

    return " ".join(str_list)

print(jaden_casing("How can mirrors be real if our eyes aren't real"))