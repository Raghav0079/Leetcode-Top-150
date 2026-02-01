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
        
