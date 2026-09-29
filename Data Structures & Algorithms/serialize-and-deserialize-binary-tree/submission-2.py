# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        pre = []
        def preorder(node):
            nonlocal pre
            if not node:
                pre.append('N')
                return
            pre.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return "#".join(pre)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        pre = data.split('#')
        def dfs():
            nonlocal pre
            if not len(pre) or pre[0]=='N':
                pre.pop(0)
                return None
            root = TreeNode(int(pre.pop(0)))
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

            

