# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
	#Enter Your Code Here
    visited = set()
    result = ''
    index = 0
    def dfs(root, i):
        nonlocal result
        stack = [root]
        visited.add(root)
        while stack:
            node = stack.pop()
            if node:
                if i in range(len(s)) and s[i] == "1" and node.right:
                    if node.right not in visited:
                        stack.append(node.right)
                        visited.add(node.right)
                        i += 1
                elif i in range(len(s)) and s[i] == "0" and node.left:
                    if node.left not in visited:
                        stack.append(node.left)
                        visited.add(node.left)
                        i += 1
                else:
                    result += node.data
                    visited.clear()
                    return i
      
    while index < len(s):
        # print(index)
        index = dfs(root, index)
        
                     
    print(result)