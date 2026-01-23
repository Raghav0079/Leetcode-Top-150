"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.


"""


class Solution:

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left

# time complexity: O(log n)
# space complexity: O(1)

# Example usage:
# sol = Solution()
# print(sol.findPeakElement([1,2,3,1]))  # Output: 2
# print(sol.findPeakElement([1,2,1,3,5,6,4]))  # Output: 5
# print(sol.findPeakElement([1]))  # Output: 0
