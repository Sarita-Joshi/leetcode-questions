# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, p: List[int], i: List[int]) -> Optional[TreeNode]:    
        
        def build(left, right):
            root = TreeNode(p.pop(0))
            if len(left)>1:
                #divide
                pos = left.index(p[0])
                l = left[:pos]
                r = left[pos+1:]
                root.left = build(l, r)
                
            elif len(left)==1:
                root.left = TreeNode(p.pop(0))
            
            if len(right)>1:
                pos = right.index(p[0])
                l = right[:pos]
                r = right[pos+1:]
                root.right = build(l, r)
            elif len(right)==1:
                root.right = TreeNode(p.pop(0))
            
            return root
        
        
        pos = i.index(p[0])
        left = i[:pos]
        right = i[pos+1:]
        return build(left, right)
        
        
        