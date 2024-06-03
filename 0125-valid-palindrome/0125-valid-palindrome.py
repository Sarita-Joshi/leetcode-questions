import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-z0-9]", "", s.lower())
        n = len(s)
        mid = n // 2
        if n % 2 == 1:
            for i in range(mid+1):
                print(s[mid-i] , s[mid+i])
                if s[mid-i] != s[mid+i]:
                    return False
        else:
            for i in range(mid):
                if s[mid-1-i] != s[mid+i]:
                    return False
        
        return True