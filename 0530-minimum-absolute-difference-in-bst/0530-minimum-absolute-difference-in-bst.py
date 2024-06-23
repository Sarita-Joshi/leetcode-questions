# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        best = 100000
        prev = -100000
        
        def inorder(root):
            nonlocal best, prev
            if not root:
                return
            inorder(root.left)
            best = min(best, root.val - prev)
            prev = root.val
            inorder(root.right)
        inorder(root)    
        return best