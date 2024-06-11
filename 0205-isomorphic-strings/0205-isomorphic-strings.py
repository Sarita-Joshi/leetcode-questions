class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        su = {}
        tu = {}

        scount = 0
        tcount = 0
        for i in range(len(s)):
            if s[i] not in su:
                su[s[i]] = scount
                scount += 1

            if t[i] not in tu:
                tu[t[i]] = tcount
                tcount += 1
                
            if su[s[i]] != tu[t[i]]:
                return False
                            
        
        return True
        