class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        current_num = 0
        operator = 1
        
        for i, t in enumerate(s):
            # print([s[:i+1]], current_num, res, operator, stack)
            if t.isdigit():
                current_num = current_num*10 + int(t)
                 
            if t in "+-()" or i == len(s)-1:
                
                if operator == 1:
                    res += current_num
                elif operator == -1:
                    res -= current_num
                
                if t == '(':
                    stack.append(res)
                    stack.append(operator)
                    res = 0
                    operator = 1
                    
                elif t==')':
                    sign = stack.pop()
                    num1 = stack.pop()
                    res = num1 + res * sign

                current_num = 0
                if t=='+':
                    operator = 1
                elif t=='-':
                    operator = -1
                
                
        return res
        