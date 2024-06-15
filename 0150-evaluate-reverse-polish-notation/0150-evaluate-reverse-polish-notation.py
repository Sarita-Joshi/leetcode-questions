class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                num1 = stack.pop()
                num2 = stack.pop()
                res = 0
                if t == '+':
                    res = num1+num2
                elif t == '*':
                    res = num1*num2
                elif t == '-':
                    res = num2-num1
                elif t == '/':
                    if num1 * num2 <= 0:
                        res = -1* (abs(num2) // abs(num1))
                    else:
                        res = num2//num1
                stack.append(res)
            else:
                stack.append(int(t))
        
        return stack.pop()
                
            