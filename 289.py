'''The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.'''

from typing import List

class Solution(object):
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows,cols=len(board),len(board[0])
        
        def countNeighbors(board: List[List[int]], r: int, c: int) -> int:
            nei =0 
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if (i==r and j==c) or i<0 or j<0 or i>=rows or j>=cols:
                        continue
                    if board[i][j] in [1,3]:
                        nei+=1
            return nei
        
        for r in range(rows):
            for c in range(cols):
                nei = countNeighbors(board, r, c)
                if board[r][c] == 1 and nei in [2,3]:
                    board[r][c] = 3  # live -> live
                elif board[r][c] == 0 and nei == 3:
                    board[r][c] = 2  # dead -> live
                    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 1:
                    board[r][c] = 0
                elif board[r][c] in [2,3]:
                    board[r][c] = 1

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Blinker pattern
    board1 = [[0,1,0],[0,1,0],[0,1,0]]
    print("Original board:")
    for row in board1:
        print(row)
    
    solution.gameOfLife(board1)
    print("\nAfter one generation:")
    for row in board1:
        print(row)
    
    # Test case 2: Block pattern (should remain stable)
    board2 = [[1,1],[1,1]]
    print("\n\nBlock pattern original:")
    for row in board2:
        print(row)
    
    solution.gameOfLife(board2)
    print("Block pattern after one generation:")
    for row in board2:
        print(row)
        
# time complexity: O(m*n)
# space complexity: O(1)
