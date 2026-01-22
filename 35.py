class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left,right = 0 ,len(nums )- 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid 
            
            elif nums[mid] < target:
                left = mid +1 
                
            else :
                right = mid -1
        return left

# Example usage:
# sol = Solution()
# print(sol.searchInsert([1,3,5,6], 5))  # Output: 2
# print(sol.searchInsert([1,3,5,6], 2))  # Output: 1
# print(sol.searchInsert([1,3,5,6], 7))  # Output: 4

# time complexity : O(log n)
# space complexity: O(1)
