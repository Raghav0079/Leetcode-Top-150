'''Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # apply dfs to check symmetry
        def dfs(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            # check on the values and continue dfs on the children
            return (left.val == right.val and 
                    dfs(left.left,right.right) and
                    dfs(left.right,right.left))
            
        # initiate dfs on root's left and right
        return dfs(root.left,root.right)

# time complexity: O(n)
# space complexity: O(h) where h is the height of the tree
