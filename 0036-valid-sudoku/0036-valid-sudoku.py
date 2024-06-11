class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for row in board:
            numbers = collections.defaultdict(int)
            for cell in row:
                if cell != ".":
                    numbers[cell] += 1
                if numbers[cell] > 1:
                    return False
        # print('Rows checks')
        # check columns
        for i in range(9):
            numbers = collections.defaultdict(int)
            for j in range(9):
                cell = board[j][i]
                if cell != ".":
                    numbers[cell] += 1
                if numbers[cell] > 1:
                    return False
                
        # print('Cols checks')
        
        for i in range(9):
            if i % 3 ==0:
                # print('3 box checking')
                numbers1 = collections.defaultdict(int)
                numbers2 = collections.defaultdict(int)
                numbers3 = collections.defaultdict(int)
            
            for j in range(0,3):
                cell = board[j][i]
                if cell != ".":
                    numbers1[cell] += 1
                if numbers1[cell] > 1:
                    return False
            
            for j in range(3,6):
                cell = board[j][i]
                if cell != ".":
                    numbers2[cell] += 1
                if numbers2[cell] > 1:
                    return False
            
            for j in range(6,9):
                cell = board[j][i]
                if cell != ".":
                    numbers3[cell] += 1
                if numbers3[cell] > 1:
                    return False

        return True