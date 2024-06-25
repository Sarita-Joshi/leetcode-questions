"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        visited = []
        q = deque([node])
        cache = {node.val: Node(node.val, [])}
        while q:
            curr = q.popleft()
            
            curr_clone = cache[curr.val]

            for n in curr.neighbors:
                if n.val not in cache.keys():    
                    cache[n.val] = Node(n.val, [])
                    q.append(n)
                curr_clone.neighbors.append(cache[n.val])
                
        return cache[node.val]
                
                
            
            
            
        
        
        