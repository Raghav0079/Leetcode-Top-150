"""You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

# approach : two pointers
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # edge case
        block = []
        i = 0

        # main logic
        while i < len(nums):
            start = nums[i]
            # move i to the end of the current range
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            # add the range to the block
            if start != nums[i]:
                block.append("{}->{}".format(start, nums[i]))
            else:  # single number
                block.append(str(start))
            i += 1
        return block  # return the list of ranges


# time complexity: O(n)
# space complexity: O(1)
# n is the length of nums
