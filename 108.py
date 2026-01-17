''' Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# define solution class
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # helper function to build BST
        def helper(l,r):
            if l > r:
                return None 
        # find mid element
            mid = (l+r)//2
            # create root node
            root = TreeNode(nums[mid])
            root.left = helper(l,mid-1)
            root.right = helper(mid+1,r)
            return root
        # call helper function
        return helper(0,len(nums)-1)
    


# time complexity: O(n)
# space complexity: O(log n)

