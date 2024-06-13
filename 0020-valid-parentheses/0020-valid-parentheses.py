class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        
        stack = [None]
        
        for i in s:
            if i in ("(", "[", "{"):
                stack.append(i)
            elif i==')' and stack[-1]!='(':
                return False
            elif i=='}' and stack[-1]!='{':
                return False
            elif i==']' and stack[-1]!='[':
                return False
            else:
                stack.pop()
        
        if stack!=[None]:
            return False
        return True