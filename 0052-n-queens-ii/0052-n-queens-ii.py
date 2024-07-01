class Solution:
    def totalNQueens(self, n: int) -> int:
        if n==1:
            return 1
        res = 0
        cols=set()
        posdia=set()
        negdia=set()
        def backtrack(r):
            if r == n:
                nonlocal res 
                res += 1
                return
            for c in range(n):
                if c in cols or (r+c) in posdia or (r-c) in negdia:
                    continue
                cols.add(c)
                posdia.add(r+c)
                negdia.add(r-c)
                backtrack(r+1)
                cols.remove(c)
                posdia.remove(r+c)
                negdia.remove(r-c)
                
        backtrack(0)
        return res