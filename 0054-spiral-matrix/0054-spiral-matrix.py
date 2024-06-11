class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m, n = len(matrix), len(matrix[0])
        if m==1:
            return matrix[0]
        if n==1:
            return [m[0] for m in matrix]
        
        res = []
        directions = ((0, 1),(1, 0), (0, -1), (-1, 0))
        i, j, curdir = 0, 0, 0
        
        
        for _ in range(m*n):
            if i>=m or j>=n or i<0 or j<0 or matrix[i][j] == -101:
                break
                
            res.append(matrix[i][j])
            matrix[i][j] = -101
            new_i = i + directions[curdir][0]
            new_j = j + directions[curdir][1]
            
            if new_i>=m or new_j>=n or new_i<0 or new_j<0 or matrix[new_i][new_j] == -101:

                curdir = (curdir + 1) % 4
                new_i = i + directions[curdir][0]
                new_j = j + directions[curdir][1]
                
            i,j = new_i, new_j
                
        return res
            
            
            
            
            
            
        
        