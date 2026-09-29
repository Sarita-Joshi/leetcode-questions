"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node : return node

        newnode = Node(node.val)
        q = deque([[node, newnode]])
        visited ={}
        while q:
            nn, newn = q.popleft()
            for nei in nn.neighbors:
                if nei not in visited:
                    newn.neighbors.append(Node(nei.val))
                    visited[nei] = newn.neighbors[-1]
                    q.append([nei, visited[nei]])
                else:
                    newn.neighbors.append(visited[nei])
        return newnode
