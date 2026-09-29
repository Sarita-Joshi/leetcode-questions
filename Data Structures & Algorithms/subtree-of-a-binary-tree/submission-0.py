# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(p, q):
            queue = deque([[p,q]])

            while queue:
                for i in range(len(queue)):
                    np,nq = queue.popleft()
                    if np==nq==None:
                        continue
                    if np==None or nq==None or np.val!=nq.val:
                        return False
                    queue.append([np.left, nq.left])
                    queue.append([np.right, nq.right])
            return True
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.val==subRoot.val and isSame(node, subRoot):
                    return True
                if node.left:
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
        return False
        

