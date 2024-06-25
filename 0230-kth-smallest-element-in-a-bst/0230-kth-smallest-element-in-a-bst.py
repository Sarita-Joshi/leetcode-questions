# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        nlist = []
        def inorder(root):
            nonlocal nlist
            if root==None or len(nlist)==k:
                return
            inorder(root.left)
            nlist.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return nlist[k-1]