class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        change_sign = False
        if x < 0:
            change_sign = True
            x = abs(x)
        
        digits = []
        while x !=0:
            digits.append(x%10)
            x = x//10
            
        res = 0
        for n in digits:
            res = res * 10 + n
        
        if res > 2**31-1:
            return 0
        
        if change_sign:
            res = res * -1
        
        
        
        return res
        