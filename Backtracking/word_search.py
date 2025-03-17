class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        Given an `m x n` board and a word, return `True` if the word exists in the grid.

        The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

        :param board: A 2D list of characters
        :param word: A string
        :return: A boolean value
        """
        rows, cols = len(board), len(board[0])
        path = set()
        def dfs(r, c, i):
            """
            `dfs` recursively explores a tree structure and returns `True` if the word exists in the grid.

            :param i: The row index of the current cell
            :param j: The column index of the current cell
            :param k: The index of the current character in the word
            :return: A boolean value
            """
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i] or (r, c) in path:
                return False
            if i == len(word) - 1:
                return True

            path.add((r, c))
            found = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            path.remove((r, c))
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False