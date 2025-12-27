'''Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        n=0
        stack=[]
        cur = root
        while cur or stack :
            while cur :
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            n += 1
            if n == k :
                return cur.val
            cur = cur.right

# time complexity is O(H + k) where H is the height of the tree
# space complexity is O(H)


                
