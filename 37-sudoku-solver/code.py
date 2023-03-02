class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Define a function to check if a given value can be placed in a given cell
        def canPlace(num, row, col):
            # Check row
            for i in range(9):
                if board[row][i] == num:
                    return False
            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False
            # Check sub-box
            startRow = (row // 3) * 3
            startCol = (col // 3) * 3
            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == num:
                        return False
            # All checks passed
            return True
        
        # Define a function to solve the puzzle recursively
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in range(1, 10):
                            if canPlace(str(num), i, j):
                                board[i][j] = str(num)
                                if solve():
                                    return True
                                else:
                                    board[i][j] = '.'
                        return False
            return True
        
        # Call the recursive function to solve the puzzle
        solve()
