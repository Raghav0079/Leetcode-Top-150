''' Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.'''

class Solution(object):
    def twoSum(self,num,target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r= 0 , len(num)-1
        
        while l<r:
            cursum=num[l]+num[r]
            
            if cursum > target :
                r -= 1
            elif cursum < target :
                l +=1 
            else:
                return [l+1,r+1]
        return []
        
        
# time complexity is O(n)
# space complexity is O(1)

            
    
            
