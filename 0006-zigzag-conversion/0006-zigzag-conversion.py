class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s)<3 or len(s) <= numRows:
            return s
        
        rows = [""] * numRows
        
        add = 0
        inc = 1
        
        for i in s:
            rows[add] += i
            if add == 0:
                inc = 1
            elif add == numRows -1:
                inc =-1
                
            add += inc
            
            
        return ''.join(rows)
        
        
        
             
        
        