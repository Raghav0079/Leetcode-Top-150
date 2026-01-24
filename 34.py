'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binsearch (nums,target,True)
        right = self.binsearch (nums,target,False)
        
        return [left,right]
        
    def binsearch(self,nums,target,leftbias):
        l,r= 0,len(nums)-1
        i = -1
        while l <= r:
            m= (l+r) //2
            if target > nums[m]:
                l = m+1
                
            elif target < nums[m]:
                r = m-1 
                
            else:
                i = m
                if leftbias:
                    r= m-1 
                else:
                    l= m+ 1
        return i
    
                