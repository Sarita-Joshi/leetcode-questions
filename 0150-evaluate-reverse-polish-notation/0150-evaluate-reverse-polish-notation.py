class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv
        }
        
        stack = []
        
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(ops[t](num1, num2)))
            else:
                stack.append(int(t))
        
        return stack.pop()
                
            