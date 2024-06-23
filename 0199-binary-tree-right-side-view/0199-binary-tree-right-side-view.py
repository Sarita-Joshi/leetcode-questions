# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            res.append(q[0].val)
            l = len(q)
            for i in range(l):
                curr = q.pop(0)
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
        return res   