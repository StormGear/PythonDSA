class NQueens:
    def __init__(self, n: int):
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.res = []

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

        # Check if there is a queen in the same diagonal (bottom-right to top-left)
        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[r][c]:
                return False

        # Check if there is a queen in the same diagonal  (bottom-left to top-right)
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
        
    
    

if __name__ == '__main__':
    nqueen = NQueens(4)
    nqueen.solve_nqueens()
        