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
        cache = {}
        while q:
            curr = q.popleft()
            cache[curr.val] = (curr, Node(curr.val, []))
            visited.append(curr.val)

            for n in curr.neighbors:
                if n.val not in visited:    
                    q.append(n)
                    visited.append(n.val)
                    
        for v in visited:
            node, newnode = cache[v][0], cache[v][1]
            newnode.neighbors = [cache[n.val][1]  for n in node.neighbors]
        return cache[visited[0]][1]
                
                
            
            
            
        
        
        