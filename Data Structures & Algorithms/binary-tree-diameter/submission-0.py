# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def diameter(root):
            if not root:
                return 0
            hl = diameter(root.left)
            hr = diameter(root.right)
            self.res = max(self.res, hl+hr)
            return max(hl,hr)+1
        diameter(root)
        return self.res