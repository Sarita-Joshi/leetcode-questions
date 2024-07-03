class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word)==1:
            if any([word in row for row in board]):
                return True
            return False
        m,n = len(board), len(board[0])
        
        if m*n < len(word):
            return False
        
        def dfs(row, col, i):
            if i == len(word):
                return True
            
            if not 0 <=row < m or not 0 <= col < n or board[row][col] != word[i]:
                return False

            
            temp = board[row][col]
            board[row][col] = ''
                    
            if dfs(row,col+1,i+1) or dfs(row,col-1,i+1) or dfs(row+1,col,i+1) or dfs(row-1,col,i+1):
                return True

            board[row][col]=temp

            return False
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False
    
    
    
#         def backtrack(i, j, k):
#             if k == len(word):
#                 return True
#             if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
#                 return False
            
#             temp = board[i][j]
#             board[i][j] = ''
            
#             if backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1):
#                 return True
            
#             board[i][j] = temp
#             return False
        
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if backtrack(i, j, 0):
#                     return True
#         return False
    
        
    