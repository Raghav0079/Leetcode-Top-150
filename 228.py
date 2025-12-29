''' You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        i =0 
        
        while i < len(nums):
            start = nums[i]
            
            while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
                i += 1
                
            if start != nums[i]:
                ans.append(str(start) + "->" + str(nums[i]))
            else:
                ans.append(str(start))
            i +=1
            
        return ans
# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [0,1,2,4,5,7]
    print("Input:", nums1)
    print("Output:", solution.summaryRanges(nums1))  # Expected: ["0->2","4->5","7"]
    
    # Test case 2
    nums2 = [0,2,3,4,6,8,9]
    print("\nInput:", nums2)
    print("Output:", solution.summaryRanges(nums2))  # Expected: ["0","2->4","6","8->9"]
    
    # Test case 3
    nums3 = []
    print("\nInput:", nums3)
    print("Output:", solution.summaryRanges(nums3))  # Expected: []
    
    # Test case 4
    nums4 = [-1]
    print("\nInput:", nums4)
    print("Output:", solution.summaryRanges(nums4))  # Expected: ["-1"]
    
    # Test case 5
    nums5 = [0]
    print("\nInput:", nums5)
    print("Output:", solution.summaryRanges(nums5))  # Expected: ["0"]
    
# time complexity: O(n)
# space complexity: O(1) excluding output list

             
