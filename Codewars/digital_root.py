# Online Python - IDE, Editor, Compiler, Interpreter
def digital_root(n: int) -> int:
    total = 0
    for i in str(n):
        total += int(i)
    if len(str(total)) > 1:
        total = digital_root(int(total))
    return total

def digital_root2(n: int) -> int:
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n
        
# print(digital_root(942))
# print(digital_root(16))
print(digital_root2(132189))