class NQueens:
    def __init__(self, n: int):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def print_queens(self):
        for r in range(self.n):
            for c in range(self.n):
                if self.board[r][c]:
                    print(" Q ", end="")
                else:
                    print(" - ", end="")
            print()

    def is_safe(self, row: int, col: int) -> bool:
        # Check if there is a queen in the same row
        for c in range(self.n):
            if self.board[row][c]:
                return False

        # Check if there is a queen in the same diagonal (bottom-right to top-left) (leading diagonal)
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[r][c]:
                return False

        # Check if there is a queen in the same diagonal  (bottom-left to top-right) (trailing diagonal)
        for r, c in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[r][c]:
                return False

        return True

    def solve(self, col):
        if col == self.n:
            return True
        
        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve(col + 1):
                    return True
                self.board[row][col] = 0

        return False
    
    def solve_nqueens(self):
        if not self.solve(0):
            print("No solution exists")
            return False
        self.print_queens()
        return True


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        # define sets to keep track of used cols, positive and negative diagonal
        col = set()
        pos_diag = set()
        neg_diag = set()

        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (row+c) in pos_diag or (row-c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(row+c)
                neg_diag.add(row-c)
                board[row][c] = "Q"
                backtrack(row+1)

                col.remove(c)
                pos_diag.remove(row+c)
                neg_diag.remove(row-c)
                board[row][c] = "."
                
        backtrack(0)
        return res

    def print_board(self, board):
        for row in board:
            for col in row:
                for char in col:
                    if char == "Q":
                        print("Q ", end="")
                    else:
                        print("- ", end="")
                print()
            print()

        
        
    
    

if __name__ == '__main__':
    # nqueen = NQueens(4)
    # nqueen.solve_nqueens()
    soln = Solution()
    solved_board = soln.solveNQueens(4)
    soln.print_board(solved_board)
    
        