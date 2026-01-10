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
    
