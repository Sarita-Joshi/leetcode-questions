# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return [0]
        
        q = [root]
        res = []
        s = root.val
        while q:
            l = len(q)
            res.append(s / l)
            s = 0
            for _ in range(l):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                    s += curr.left.val
                if curr.right:
                    q.append(curr.right)
                    s += curr.right.val
                    
        return res
        
        