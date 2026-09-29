# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def height(root):
            nonlocal flag
            if not root:
                return 0
            hl = height(root.left)
            hr = height(root.right)
            flag = flag and (abs(hl-hr) <=1)
            print(root.val, hl, hr, flag)
            return max(hl,hr)+1
        height(root)
        return flag

        