
class two_d_lists:
    def __init__(self, matrix):
        self.matrix = matrix

    # time complexity: O(n * m)
    # space complexity: O(1)
    def row_traversal(self):
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])
        for r in range(nrows):
            for c in range(ncols):
                print(self.matrix[r][c], end=' ')
            print()

    # time complexity: O(n * m)
    # space complexity: O(1)
    def column_traversal(self):
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])
        for c in range(ncols):
            for r in range(nrows):
                print(self.matrix[r][c], end=' ')
            print()

    # time complexity: O(min(n, m))
    # space complexity: O(1)
    def diagonal_traversal(self):
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])
        for r in range(min(nrows, ncols)):           
            print(self.matrix[r][r], end=' ')
        print()

    # time complexity: O(n * m)
    # space complexity: O(1)
    def reverse_diagonal_traversal(self):
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])
        for r in range(nrows):
            for c in range(ncols):
                if r + c == ncols - 1:
                    print(self.matrix[r][c], end=' ')
        print()

if __name__ == '__main__':
    matrix = [[1, 2], [3, 4], [5, 6]]
    obj = two_d_lists(matrix)
    print('Row Traversal:')
    obj.row_traversal()
    print('Column Traversal:')
    obj.column_traversal()
    print('Diagonal Traversal:')
    obj.diagonal_traversal()
    print('Reverse Diagonal Traversal:')
    obj.reverse_diagonal_traversal()
