'''Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

# BFS approach 
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        res =[]
        # queue for BFS
        q= deque([root] if root else [])
        while q :
            level =[]
            length = len(q)
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level=list(reversed(level)) if len(res)%2 else level
            res.append(level)
        # return the list of zigzag levels
        return res


# Time Complexity: O(N) where N is the number of nodes in the tree.
# Space Complexity: O(M) where M is the maximum number of nodes at any level in
# example test case
# the tree (the width of the tree).
# Example:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
# Explanation: The zigzag level order traversal of the binary tree is as follows:
# Level 0: [3]
# Level 1: [20,9]
# Level 2: [15,7]
# Hence return [[3],[20,9],[15,7]].
