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


# This is the second question
'''
Given an array, take consecutive pairs in the array and sort them
Return an array of the sorted pairs
In case an array is odd in length, keep the last element intact
'''
def solution2(nums: list[int]) -> list[int]:
    last = float('inf')
    res = []
    final =  []

    def sort_nums(nums: list[int]) -> list[list[int]]:
        i = 0
        while i < len(nums) - 1:
            res.append([nums[i], nums[i+1]])
            i += 2
        for j in res:
            j.sort()
        return res

    if len(nums) % 2 == 0:
        # handle even len
        res = sort_nums(nums)
    else:
       last = nums[-1]
       res = sort_nums(nums)

    for i in res:
        final.extend(i)
    if last < float('inf'):
        final.append(last)


    return final

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
    nums = [10,10,11,8,5,2,8, 1, 12]
    print('Result ', solution2(nums))


