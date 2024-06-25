class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        for c, p in pre:
            adj[c].append(p)
            
        taken = set()
        order = []
        
        def dfs(course):
            if course in taken:
                return False
            if adj[course]== []:
                if course not in order:
                    order.append(course)
                return True
            
            taken.add(course)
            for p in adj[course]:
                if not dfs(p):
                    return False
            
            taken.remove(course)
            adj[course] = []
            if course not in order:
                order.append(course)
            
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                 return []
                
        return order