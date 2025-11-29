'''Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        q=collections.deque([root])
        
        while q:
            rightSide=None
            qlen=len(q)
            
            for i in range(qlen):
                node = q.popleft()
                if node :
                    rightSide=node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)         
              
            
        return res

# time complexity is O(N)
# space complexity is O(D) where D is the max width of the tree
