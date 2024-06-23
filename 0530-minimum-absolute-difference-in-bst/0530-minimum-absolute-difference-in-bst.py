# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy as np
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        curr, stack,  prev, best = root, [], -10**5, 10**5
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            best = min(best, node.val - prev)
            curr = node.right
            prev = node.val
        
        return best
            
            
            