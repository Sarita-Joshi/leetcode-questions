class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {"}": "{", ']':'[', ")": "("}
        
        for char in s:
            if char in mapper.values():
                stack.append(char)
            elif not stack or stack.pop() != mapper[char]:
                return False
            
        if stack:
            return False
        return True
            
            
