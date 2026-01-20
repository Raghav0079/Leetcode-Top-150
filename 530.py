"""Given the root of a Binary Search Tree (BST),
return the minimum absolute difference between the values of any two different nodes in the tree.

"""


# Definition for a binary tree node.
# solving approach: inorder traversal
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# defining the solution class
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # defining variables to store minimum distance and previous node value
        min_dist = [float("inf")]
        prev = [None]
# defining the dfs function for inorder traversal
        def dfs(node):
            if not node:
                return
# defining inorder traversal
            dfs(node.left)

            if prev[0] is not None:
                min_dist[0] = min(min_dist[0], abs(node.val - prev[0]))

            prev[0] = node.val

            dfs(node.right)


# example usage:
# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# solution = Solution()
# print(solution.getMinimumDifference(root))  # Output: 1

#  time complexity: O(N)
# space complexity: O(H) where H is the height of the tree



