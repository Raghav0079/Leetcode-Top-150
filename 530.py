'''Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.min_distance = float('inf')
        self.prev = None
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            
            if self.prev is not None:
                self.min_distance = min(self.min_distance, node.val - self.prev)
            
            self.prev = node.val
        
            dfs(node.right)
        dfs(root)
        return self.min_distance
    
# Time Complexity: O(N) where N is the number of nodes in the BST.
# Space Complexity: O(H) where H is the height of the BST due to the recursion stack.
