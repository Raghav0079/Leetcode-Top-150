'''
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.
'''


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows,cols=len(board),len(board[0])
        
        def capture (r,c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] !="O":
                return 
            board[r][c]="T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
            
        # 1. capture unsurrounded regions (O -> T)
        for r in range(rows):
            for c in range(cols):
                if ( board[r][c] == "O" and (r in [0,rows-1] or c in [0,cols-1]) ):
                    capture(r,c)
                    
        
        # 2. capture surrounded regions (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c]="X"
        
        # 3. uncapture unsurrounded regions (T -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"