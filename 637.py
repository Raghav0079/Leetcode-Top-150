'''Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.'''

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
        from collections import deque
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        avgs=[]
        q=deque()
        q.append(root)

        while q:
            avg=0
            n=len(q)
            for _ in range(n):
                node = q.popleft()
                avg += node.val

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            avg /= n 
            avgs.append(avg)

        return avgs
    
# Time Complexity: O(N)
# Space Complexity: O(M) where M is the maximum number of nodes at any level