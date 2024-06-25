class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(grid), len(grid[0])
        visited = set()
        
        def bfs(row, col):
            neighbors = ((-1,0), (0,-1), (1,0), (0,1))
            q = deque([(row,col)])
            region = {(row,col)}
            edge = False
            while q:
                r,c = q.popleft()
                if r in (0,m-1) or c in (0,n-1):
                    edge = True
                for i,j in neighbors:
                    i +=r
                    j +=c
                    if 0<=i<m and 0<=j<n and grid[i][j]=="O" and (i,j) not in visited:
                        region.add((i,j))
                        visited.add((i,j))
                        q.append((i,j))
                        
            if not edge:
                for i,j in region:
                    grid[i][j] = "X"
                
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 'O' and (r,c) not in visited:
                    visited.add((r,c))
                    bfs(r,c)
                    