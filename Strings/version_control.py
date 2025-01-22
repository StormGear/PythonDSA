# This question was asked in my Amalitech CodeSignal Interview

'''
Design lightweight version control
- switch changes branches
- files cannot be duplicated
- push adds files to a branch
- return the name of the branch with the maximum number of files
'''
from collections import defaultdict

def switch(s: str):
    res = s.split()
    if res[0] == 'switch':
        return [True, res[1]]
    return [False, ""]

def push(s: str):
    res = s.split()
    if res[0] == 'push':
        return [True, res[1]]
    return [False, ""]

def solution(logs: list[str]):
    branches = defaultdict(int) # keep track of each branch(branch) and the number of files(value)

    curr_branch = ""
    seen = set()
    for log in logs:
        is_switch = switch(log)
        is_push = push(log)

        if is_switch[0]:
            curr_branch = is_switch[1]
            branches[curr_branch] = 0
            seen = set()

        if is_push[0]:
            seen.add(is_push[1])
            branches[curr_branch] =  len(seen)
            

    print(list(branches.items()))
    return max(branches, key=branches.get)

if __name__=='__main__':
    logs = [
        'switch branch1',
        'push file1',
        'push file2',
        'push file1',
        'switch branch2',
        'switch issue1',
        'push file1',
        'push file2',
        'push file3',
        'push file2',
        'switch issue3',
        'push file1',
        'push file2',
        'push file3'
    ]
    print('The branch with the max number of files is :' + solution(logs))


