class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mn, mx = min(strs), max(strs)
        i=0
        for i in range(len(mn)):
            if mn[i]!=mx[i]:
                return mn[:i]
        
        return mn