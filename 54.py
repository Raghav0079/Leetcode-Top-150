''' given a m*n matrix return all the elements of the matrix in spiral order '''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []
        
        left,right = 0, len(matrix[0])
        top,bottom = 0, len(matrix)
        
        while left < right and top < bottom :
            # get every value in the top row 
            for i in range (left,right):
                output.append(matrix [top][i])
            top += 1
            
            # get every value in the right column
            for i in range (top,bottom):
                output.append(matrix [i][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            
            # get every value in the bottom row
            for i in range (right-1,left-1,-1):
                output.append(matrix [bottom-1][i])
            bottom -= 1
            
            # get every value in the left column
            for i in range (bottom-1,top-1,-1):
                output.append(matrix [i][left])
            left += 1
            
        return output 
            
# Time Complexity: O(m*n) where m is the number of rows and n is the number of columns
# Space Complexity: O(1) ignoring the output list
