''''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l ,r = 0, len(nums) - 1
        
        while l <= r:
            m = (l+r) //2
            
            if nums[m] == target:
                return m 
            
            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] :
                    l = m + 1
                elif target < nums[l]:
                    l = m + 1
                else:
                    r= m -1 
                    
            # right sorted portion
            else:
                if target < nums[m]:
                    r= m - 1
                elif target > nums[r]:
                    r= m -1 
                    
                else:
                    l = m +1
                    

        return -1


# Example usage:
# sol = Solution()
# print(sol.search([4,5,6,7,0,1,2], 0))  # Output: 4
# print(sol.search([4,5,6,7,0,1,2], 3))  # Output: -1
# print(sol.search([1], 0))                # Output: -1
# print(sol.search([1], 1))                # Output: 0

# time complexity: O(log n)
# space complexity: O(1)
