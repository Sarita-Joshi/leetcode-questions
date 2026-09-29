class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)
        window = defaultdict(int)
        for c in t:
            count[c]+=1

        l = 0
        have, need = 0, len(count)
        res, resLen = [-1,-1], len(s)+1
        
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            
            #check have and need
            if c in count and window[c] == count[c]:
                have += 1

            #update left pointer
            while have==need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                    
                window[s[l]]-=1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1

                
            #update res

        return s[res[0]:res[1]+1] if resLen <= len(s) else ""

