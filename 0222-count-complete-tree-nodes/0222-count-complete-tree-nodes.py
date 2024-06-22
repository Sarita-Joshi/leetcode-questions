# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def lheight(self, root):
        h = 1
        while root:
            h+=1
            root = root.left
        return h
        
    def rheight(self, root):
        h = 1
        while root:
            h+=1
            root = root.right
        return h
        
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        h = 0
        lh = self.lheight(root.left)
        rh = self.rheight(root.right)
        print(root.val, lh,rh)
        if lh==rh:
            return 2 ** lh - 1
            
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
            
            
        