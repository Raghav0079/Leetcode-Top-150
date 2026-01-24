'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''

# defining the Solution class
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Finding the leftmost and rightmost indices of the target
        left = self.binsearch (nums,target,True)
        right = self.binsearch (nums,target,False)
        # Returning the result
        return [left,right]
        # Binary search helper function
    def binsearch(self,nums,target,leftbias):
        l,r= 0,len(nums)-1
        i = -1
        # Binary search loop
        while l <= r:
            m= (l+r) //2
            if target > nums[m]:
                l = m+1
                # Move right
            elif target < nums[m]:
                r = m-1 
                # Move left
            else:
                i = m
                if leftbias:
                    r= m-1 
                else:
                    l= m+ 1
        return i # Return the found index or -1 if not found
    
                
# Example usage
# sol = Solution()
# print(sol.searchRange([5,7,7,8,8,10], 8))  # Output: [3, 4]
# print(sol.searchRange([5,7,7,8,8,10], 6))  # Output: [-1, -1]

