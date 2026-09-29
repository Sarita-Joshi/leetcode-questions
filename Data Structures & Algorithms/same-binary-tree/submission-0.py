# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        q = deque([[p,q]])

        while q:
            for i in range(len(q)):
                np, nq = q.popleft()
                if np==nq==None:
                    continue
                if np==None or nq==None or np.val!=nq.val:
                    return False
                q.append([np.left if np else None, nq.left if nq else None])
                q.append([np.right if np else None, nq.right if nq else None])

        return True  
            
            