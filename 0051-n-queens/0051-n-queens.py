class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        
        # Sets to track columns and diagonals under attack
        cols = set()      # Columns
        diag1 = set()     # Row - Col (main diagonal)
        diag2 = set()     # Row + Col (anti-diagonal)
        
        def backtrack(row, board):
            if row == n:
                res.append(board[:])
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                # Place queen
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board.append('.' * col + 'Q' + '.' * (n - col - 1))
                
                backtrack(row + 1, board)
                
                # Remove queen
                board.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        backtrack(0, [])
        return res

# Example usage:
sol = Solution()
for solution in sol.solveNQueens(4):
    for row in solution:
        print(row)
    print()
