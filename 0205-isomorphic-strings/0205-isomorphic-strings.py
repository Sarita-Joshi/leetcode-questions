class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        su = {}
        tu = {}
        for i in range(len(s)):
            if s[i] not in su:
                su[s[i]] = t[i]
                

            if t[i] not in tu:
                tu[t[i]] = s[i]
                
            if su[s[i]] != t[i] or tu[t[i]] != s[i]:
                return False
                            
        
        return True
        