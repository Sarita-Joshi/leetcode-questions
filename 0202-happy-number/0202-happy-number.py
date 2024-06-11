class Solution:
    def isHappy(self, n: int) -> bool:
        
        while n != 1:
            temp = 0
            while n!=0:
                temp += (n % 10) ** 2
                n //= 10
            if temp in (1,7):
                return True
            if temp in (2,3,4,5,6,8,9):
                return False
            n = temp
        
        return n==1