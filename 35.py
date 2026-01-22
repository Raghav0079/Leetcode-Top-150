"""Given a sorted array of distinct integers and a target value,
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""

# define the Solution class
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Initialize left and right pointers
        left,right = 0 ,len(nums )- 1
        # Binary search algorithm
        while left <= right:
            mid = (left + right) // 2
            # Check if the mid element is the target
            if nums[mid] == target:
                return mid 
            # Adjust search range based on comparison
            elif nums[mid] < target:
                left = mid +1 
            # If target is smaller, search in the left half   
            else :
                right = mid -1
        return left  # Return the insertion index if target is not found
    
    
# Example usage:
# sol = Solution()
# print(sol.searchInsert([1,3,5,6], 5))  # Output: 2
# print(sol.searchInsert([1,3,5,6], 2))  # Output: 1
# print(sol.searchInsert([1,3,5,6], 7))  # Output: 4

# time complexity : O(log n)
# space complexity: O(1)
   
