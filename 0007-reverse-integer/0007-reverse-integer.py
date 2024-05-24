class Solution:
    def reverse(self, x: int) -> int:
        change_sign = False
        if x < 0:
            change_sign = True
            x = -1*x
        
        res = int(str(x)[::-1])
        # res = 0
        # while x !=0:
        #     res = res * 10 + x%10
        #     x = x//10
            
        
        if res > 2**31-1:
            return 0
        
        if change_sign:
            res = res * -1
        
        return res
        