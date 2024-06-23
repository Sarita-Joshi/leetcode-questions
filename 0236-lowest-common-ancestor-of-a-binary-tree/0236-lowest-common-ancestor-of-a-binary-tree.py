# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
            
        def getpath(root,node):
            if not root:
                return None
            
            if root==node: 
                return [node]
            l = getpath(root.left, node)
            if l!=None and len(l)>0:
                l.append(root)
                return l
            r = getpath(root.right, node)
            if r!=None and len(r)>0:
                r.append(root)
                return r
            return None
        
        ppath = getpath(root, p)
        qpath = getpath(root, q)
        print([i.val for i in ppath], [i.val for i in qpath])
        
        if len(ppath) < len(qpath):
            for i in range(len(ppath)):
                if ppath[i] in qpath:
                    return ppath[i]
        else:
            for i in range(len(qpath)):
                if qpath[i] in ppath:
                    return qpath[i]
            
        
        
        
            
            
            
            
            
            