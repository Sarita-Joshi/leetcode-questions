class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n = len(needle)
        for i, s in enumerate(haystack):
            
            if s == needle[0]:
                if haystack[i : i + n] == needle:
                    return i
        
        return -1
                
        
            