class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word: str):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

# Time Complexity: O(n*m*k) where n is the number of rows, m is the number of columns and k is the number of words
# Space Complexity: O(n*m + k) where n is the number of rows, m is the number of columns and k is the number of words
class WordSearchII:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # build the trie
        trie = TrieNode()
        for word in words:
            trie.add_word(word)

        # dfs
        rows, cols = len(board), len(board[0])
        result, visited = set(), set()

        def dfs(r, c, node, word):
            if (r not in range(rows)) or (c not in range(cols)) or (board[r][c] not in node.children) or ((r, c) in visited):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                result.add(word)

            # explore all directions
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, node, word)

            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie, "")

        return list(result)