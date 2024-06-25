class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(grid), len(grid[0])
        q = deque()
        
        for r in range(m):
            if grid[r][0] == "O":
                q.append((r,0))
            if grid[r][n-1] == "O":
                q.append((r,n-1))
                
        for c in range(n):
            if grid[0][c] == "O":
                q.append((0,c))
            if grid[m-1][c] == "O":
                q.append((m-1,c))

        def bfs(row, col):
            neighbors = ((-1,0), (0,-1), (1,0), (0,1))
            q = deque([(row,col)])
            while q:
                r,c = q.popleft()
                for i,j in neighbors:
                    i +=r
                    j +=c
                    if 0<=i<m and 0<=j<n and grid[i][j]=="O":
                        grid[i][j] = '#'
                        q.append((i,j))

        while q:
            r,c = q.popleft()
            grid[r][c] = '#'
            bfs(r,c)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='O':
                    grid[i][j] = 'X'
                elif grid[i][j]=='#':
                    grid[i][j] = 'O'
        
        
        
        
                    