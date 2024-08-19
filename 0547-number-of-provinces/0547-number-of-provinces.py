class Solution:
    def findCircleNum(self, mat: List[List[int]]) -> int:
        visited= []
        prov = 0
        ncities = len(mat)
        
        def dfs(i):
            for c in range(ncities):
                if c != i:
                    if mat[i][c]==1 and c not in visited:
                        visited.append(c)
                        dfs(c)

            print(prov)

        for i in range(ncities):
            if i not in visited:
                visited.append(i)
                dfs(i)
                prov+=1
        return prov
                
                            
            
            