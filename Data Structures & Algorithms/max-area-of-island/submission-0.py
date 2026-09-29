class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]!=1:
                    continue
                area = 0
                q = deque([[i,j]])
                while q:
                    r,c = q.popleft()
                    if grid[r][c]==1:
                        area+=1
                        grid[r][c]=0
                        if r-1>=0: q.append([r-1,c])
                        if c-1>=0: q.append([r,c-1])
                        if r+1<m: q.append([r+1,c])
                        if c+1<n: q.append([r,c+1])
                res = max(area, res)
        return res
