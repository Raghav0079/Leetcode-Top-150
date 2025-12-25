'''Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        min_distance = float('inf')
        prev = [None]
        
        def dfs(node):
            nonlocal min_distance
            if node is None:
                return
            
            dfs(node.left)
            
            if prev[0] is not None:
                min_distance = min(min_distance, node.val - prev[0])
            
            prev[0] = node.val
        
            dfs(node.right)
        dfs(root)
        return min_distance
    
# Time Complexity: O(N) where N is the number of nodes in the BST.
# Space Complexity: O(H) where H is the height of the BST due to the recursion stack.
