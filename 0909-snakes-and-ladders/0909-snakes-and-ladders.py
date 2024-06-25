class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        if n**2 <= 6:
            return 1
    
        board.reverse()
        
        def intToPos(square):
            r = (square-1) // n
            c = (square-1) % n
            if r % 2:
                c = n - 1 - c
            # print('int to pos', (r,c), square)
            return r,c
        
        q = deque([[1,0]]) ## square, move
        visited = set()
        
        while q:
            square, moves = q.popleft()
            # print(square, moves)
            for i in range(1,7):
                newSquare = square + i
                r,c = intToPos(newSquare)
                # print(square, newSquare, (r,c), board[r][c])
                if board[r][c] != -1:
                    newSquare = board[r][c]  ## if there is a jump
                if newSquare >= n ** 2: ## If target reached
                    return moves + 1
                
                if newSquare not in visited:
                    visited.add(newSquare)
                    q.append([newSquare, moves+1])
                # print(q)
                # print('Next=============')
        return -1
        
        