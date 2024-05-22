class Solution:
    def unique(self, subs):
        if len(subs)==1:
            return True

        for i in range(len(subs)-1):
            if subs[i] in subs[i+1:]:
                return False
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0: return 0
        if len(s)==1: return 1
        if len(s)==2: return 2 if s[0]!=s[1] else 1
        
        maxlen = 1

        for i in range(len(s)-1):
            for j in range(i+2, len(s)+1):
                if j-i > maxlen:
                    if self.unique(s[i:j]):
                        maxlen = max(maxlen, j-i)
                    else:
                        break
        return maxlen