'''Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # Base case
        if not preorder or not inorder:
            return None
        
        # Create the root node
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder[1:mid + 1 ],inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:],inorder[mid + 1:])
        
        # Return the root node
        return root


# time complexity: O(n^2) in the worst case due to index() call inside recursion
# space complexity: O(n) for the recursion stack and the tree nodes


