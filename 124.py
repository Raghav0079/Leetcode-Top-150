'''A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res=[root.val]
        
        def dfs(root):
            if not root:
                return 0
            
            leftmax=dfs(root.left)
            rightmax=dfs(root.right)
            leftmax=max(0,leftmax)
            rightmax=max(0,rightmax)
            # compute max path sum with split 
            res[0] = max(res[0], root.val + leftmax + rightmax)
            
            return root.val + max(leftmax, rightmax)
        
        dfs(root)
        return res[0]
    
# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of the tree due to recursion stack

