"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = [root]
        while q:
            l = len(q)
            x = Node()
            for _ in range(l):
                print([a.val for a in q])
                curr = q.pop(0)
                x.next = curr
                x = x.next
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
        return root
            
                
        
        
        
        
        