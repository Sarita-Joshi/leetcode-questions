# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        prev = -10 ** 10
        def inorder(root):
            if not root:
                return True
            res = inorder(root.left)  
            if res==False:
                return False
            nonlocal prev
            if prev >= root.val:
                return False
            prev = root.val
            res = inorder(root.right)
            return res
            
        return inorder(root)
