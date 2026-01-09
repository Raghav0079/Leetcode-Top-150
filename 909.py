"""A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
"""

from collections import deque

# 909. Snakes and Ladders
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        # BFS
        length = len(board)  
        board.reverse()

        # Convert integer to board position
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2 == 1:
                c = length - 1 - c
            return [r, c]
        # BFS
        q = deque()
        q.append([1, 0])
        visit = set()
        # visit.add(1)
        while q:    # while queue is not empty
            square, moves = q.popleft()
            # Try all the 6 possible moves
            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1
# @lc code=end

# time complexity: O(N^2)
# space complexity: O(N^2)

