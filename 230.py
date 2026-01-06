'''Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Solution class to find kth smallest element in BST
        
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        n=0
        stack=[]
        curr=root
        # inorder traversal        
        while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                # process node
                curr = stack.pop()
                n += 1
                if n==k:
                    return curr.val
                curr = curr.right

        
# time complexity is O(H + k) where H is the height of the tree
# space complexity is O(H)
