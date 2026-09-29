# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')

        def findpath(node):
            nonlocal res
            if not node:
                return 0
            l = max(findpath(node.left),0)
            r = max(findpath(node.right),0)
            res = max(res, node.val+l+r)
            return max(node.val, node.val+max(l,r))
        findpath(root)
        return res


