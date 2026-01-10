'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

# BFS approach
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # queue for BFS
        q = []
        res = []
        if not root:
            return res
        
        # start BFS
        q.append(root)
        while q:
            size =len (q)
            level =[]
            # process all nodes at the current level
            for _ in range(size):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        # return the list of levels
        return res

    
# Time Complexity: O(N) where N is the number of nodes in the tree.
# Space Complexity: O(M) where M is the maximum number of nodes at any level in
# example test case
# the tree (the width of the tree).
# Example:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Explanation: The level order traversal of the binary tree is as follows:
# Level 0: [3]
# Level 1: [9,20]
# Level 2: [15,7]
# Hence return [[3],[9,20],[15,7]].

