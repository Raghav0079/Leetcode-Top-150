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
        # BFS
        if not root :
            return []
        res=[]
        
        # queue for BFS
        q=deque()
        q.append(root)
        # traverse the tree level by level
        while q:
            size=len(q)
            level_sum=0
            # process all nodes at the current level
            for _ in range(size):
                node=q.popleft()
                level_sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    # calculate the average for the current level
            res.append(level_sum/size)
        # return the list of averages    
        return res


    
# Time Complexity: O(N) where N is the number of nodes in the tree.
# Space Complexity: O(M) where M is the maximum number of nodes at any level in
# example test case 
# the tree (the width of the tree).
# Example:
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
# and on level 2 is 11.
# Hence return [3, 14.5, 11].

