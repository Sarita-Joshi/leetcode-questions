class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==1:
            return ['()']
        
        # count_open = 1
        res = set()
        
        def backtrack(curstr, count):
            
            # print("cur str -", curstr)
            
            if len(curstr)==2*n-1:
                if count==1:
                    res.add(curstr+ ')')
                return

            if count == 0:
                backtrack(curstr + '(', count + 1)
            
            elif count < n:
                backtrack(curstr + '(', count + 1)
                backtrack(curstr + ')', count - 1)
            elif count == n:
                backtrack(curstr + ')', count - 1)
                
                
        backtrack("(", 1)
        return res
                