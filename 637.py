'''Given the root of a binary tree, 
return the average value of the nodes on each level in the form of an array. 
Answers within 10 ^(-5) of the actual answer will be accepted.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if not root :
            return []
        res=[]
        
        q=deque()
        q.append(root)
        while q:
            size=len(q)
            level_sum=0
            for _ in range(size):
                node=q.popleft()
                level_sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_sum/size)
        return res
    