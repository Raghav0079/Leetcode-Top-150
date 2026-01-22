class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows, col = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1

            elif target < matrix[row][0]:
                bottom = row - 1

            else:
                break

        if not (top <= bottom):
            return False

        left, right = 0, col - 1
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
