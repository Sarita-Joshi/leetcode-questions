class Solution:
    def numIslands(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0

        for i in range(m):
            for j in range(n):
                var = matrix[i][j]
                if var =='0' or var =='.':
                    continue
                res+=1
                q = deque([[i,j]])
                while q:
                    r,c = q.popleft()
                    if matrix[r][c] =='1':
                        matrix[r][c] = '.'
                        if r-1>=0: q.append([r-1, c])
                        if c-1>=0: q.append([r,c-1])
                        if r+1<m: q.append([r+1,c])
                        if c+1<n: q.append([r,c+1])
        return res

                        

