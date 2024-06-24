class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        if m==n==1:
            return 1 if grid[0][0] == "1" else 0
        
        def bfs(row, col):
            neighbors = ((-1,0), (0,-1,), (1,0), (0,1))
            q = [(row,col)]
            while q:
                row,col = q.pop(0)
                for i,j in neighbors:
                    if 0 <= row+i < m and 0 <= col+j < n and grid[row+i][col+j] == "1":
                        grid[row+i][col+j] = -1
                        q.append((row+i, col+j))
        
        islands = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = -1
                    bfs(i,j)
                    islands += 1
        return islands
                