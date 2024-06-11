class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # s = s.split()
        # pairings = set(zip(pattern, s))
        # # print(pairings)
        # return len(pairings)==len(set(pattern))==len(set(s)) and len(pattern) == len(s)
        
        
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        su = {}
        pu = {}
        
        for i in range(len(s)):
            if s[i] not in su:
                su[s[i]] = pattern[i]
            
            if pattern[i] not in pu:
                pu[pattern[i]] = s[i]
            
            if su[s[i]]!=pattern[i] or pu[pattern[i]] != s[i]:
                return False
            
        return True
                
        
        
        
        