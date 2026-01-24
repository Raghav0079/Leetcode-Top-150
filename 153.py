"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time
"""
# defining the Solution class
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Finding the minimum element using binary search
        res = nums[0]
        l,r = 0,len(nums)-1
        # Binary search loop
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break 
            # Finding the mid index
            m = (l+r) //2
            res = min(res,nums[m])
            # Deciding which side to search next
            if nums[m] >= nums[l]:
                l = m +1
                # Move right
            else:
                r= m-1 # Move left
        return res # Return the minimum element
    

# Example usage
# sol = Solution()
# print(sol.findMin([3,4,5,1,2]))  # Output: 1
# print(sol.findMin([4,5,6,7,0,1,2]))  # Output: 0

# time complexity: O(log n)
# space complexity: O(1)    


