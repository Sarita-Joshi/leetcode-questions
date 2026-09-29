class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        visited = set()
        l = r = 0
        maxl = 0

        while r < len(s):
            if s[r] in visited:
                maxl = max(maxl, r-l)
                while s[r] in visited:
                    visited.remove(s[l])
                    l+=1
            visited.add(s[r])
            r+=1
        return max(maxl, r-l)