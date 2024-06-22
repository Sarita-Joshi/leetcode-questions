# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.i = []
        def dfs(root):
            # print(self.i)
            if not root:
                return root
            if root.left:
                dfs(root.left)
            self.i.append(root.val)
            if root.right:
                dfs(root.right)
            
            
        dfs(root)

    def next(self) -> int:
        return self.i.pop(0)
        

    def hasNext(self) -> bool:
        return len(self.i)>0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()