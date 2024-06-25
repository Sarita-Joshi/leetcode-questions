class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(list) ## Map a -> (b, a/b)
        
        for i, eq in enumerate(equations):
            n, d = eq
            adj[n].append((d, values[i]))
            adj[d].append((n, 1 / values[i]))
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            
            q = deque([[src,1]])
            visited = []
            while q:
                node, w = q.popleft()
                if node == target:
                    return w
                for n, val in adj[node]:
                    if n not in visited:
                        q.append([n, val * w])
                        visited.append(n)
                
            return -1
                
                
        return [bfs(n,d) for n, d in queries]
        
        
        