class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix), len(matrix[0])
        if m==1:
            return matrix[0]
        if n==1:
            return [m[0] for m in matrix]
        
        
        
        directions = ((0, 1),(1, 0), (0, -1), (-1, 0))
        curdir = 0
        m, n = len(matrix), len(matrix[0])
        i,j=0,0
        res = []
        for k in range(m*n):
            res.append(matrix[i][j])
            matrix[i][j] = -101
            new_i = i + directions[curdir][0]
            new_j = j + directions[curdir][1]
            
            if new_i>=m or new_j>=n or new_i<0 or new_j<0 or matrix[new_i][new_j] == -101:
                
                curdir = (curdir + 1) % 4
                new_i = i + directions[curdir][0]
                new_j = j + directions[curdir][1]
                
            i,j = new_i, new_j
            
            if matrix[i][j]==-101:
                break
                
        return res
            
            
            
            
            
            
        
        