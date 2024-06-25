class Solution:
    def canFinish(self, cnum: int, pre: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for c, p in pre:
            adj[c].append(p)
        
        taken = set()
        def dfs(course):
            if course in taken: return False
            if adj[course] == []: return True
            
            taken.add(course)
            for p in adj[course]:
                if not dfs(p): return False
            
            adj[course] = []
            taken.remove(course)
            
            return True
        
        for c, p in pre:
            if not dfs(c): return False
            
        return True
            