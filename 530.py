class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        min_dist = [float("inf")]
        prev = [None]

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            if prev[0] is not None:
                min_dist[0] = min(min_dist[0], abs(node.val - prev[0]))

            prev[0] = node.val

            dfs(node.right)

        dfs(root)
        return min_dist[0]
