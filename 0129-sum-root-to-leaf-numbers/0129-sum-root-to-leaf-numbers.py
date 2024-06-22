# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        self.res = 0
        
        def addnum(root, number):
            number = number*10 + root.val
            
            if root.left==None and root.right==None:
                self.res +=  number 
            else:
                if root.left:
                    addnum(root.left, number)
                if root.right:
                    addnum(root.right, number)
        
        addnum(root,0)
        return self.res