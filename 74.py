"""You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

"""

# define the Solution class
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Get the number of rows and columns
        rows, col = len(matrix), len(matrix[0])
# Binary search to find the correct row
        top, bottom = 0, rows - 1
        # Search for the row that may contain the target
        while top <= bottom:
            row = (top + bottom) // 2
# Check the first and last elements of the row
            if target > matrix[row][-1]:
                top = row + 1
# If target is greater than the last element, search in the lower rows
            elif target < matrix[row][0]:
                bottom = row - 1
# If target is smaller than the first element, search in the upper rows
            else:
                break
# If no valid row is found, return False
        if not (top <= bottom):
            return False
# Binary search within the identified row
        left, right = 0, col - 1
        # Search for the target in the identified row
        while left <= right:
            mid = (left + right) // 2
            # Check if the mid element is the target
            if target == matrix[row][mid]:
                return True
            # Adjust search range based on comparison
            elif target < matrix[row][mid]:
                right = mid - 1
                # If target is smaller, search in the left half
            else:
                left = mid + 1
        return False  # Return False if target is not found
# Example usage:
# sol = Solution()
# print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # Output: True
# print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # Output: False


# time complexity : O(log(m*n))
# space complexity: O(1)
